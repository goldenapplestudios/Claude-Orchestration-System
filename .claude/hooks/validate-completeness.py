#!/usr/bin/env python3
"""
Pre-Tool-Use Hook: Validate Code Completeness and Quality

This hook validates code changes before they're written to catch common
Claude Code mistakes, security issues, and language-specific problems.

Based on deepwiki research from:
- security-guidance plugin
- code-review plugin
- agent-sdk-verifier patterns

Exit Codes:
  0 - Success, allow operation
  1 - User error, show warning but allow
  2 - Block operation, show error
"""

import sys
import json
import re
from pathlib import Path

# ============================================================================
# INCOMPLETE IMPLEMENTATION PATTERNS (Universal)
# ============================================================================

INCOMPLETE_PATTERNS = [
    # TODO markers
    (r'//\s*TODO:', 'TODO comment found - implementation incomplete'),
    (r'#\s*TODO:', 'TODO comment found - implementation incomplete'),
    (r'/\*\s*TODO:', 'TODO comment found - implementation incomplete'),

    # FIXME markers
    (r'//\s*FIXME:', 'FIXME comment found - known issue not resolved'),
    (r'#\s*FIXME:', 'FIXME comment found - known issue not resolved'),

    # HACK markers
    (r'//\s*HACK:', 'HACK comment found - needs proper solution'),
    (r'#\s*HACK:', 'HACK comment found - needs proper solution'),

    # Deferred implementation language
    (r'for now', '"For now" solution detected - not production ready'),
    (r'temporary', 'Temporary solution detected - needs completion'),
    (r'we can add this later', 'Deferred implementation detected'),
    (r'placeholder', 'Placeholder detected - needs real implementation'),

    # Empty implementations
    (r'function\s+\w+\s*\([^)]*\)\s*{\s*}', 'Empty function body'),
    (r'catch\s*\([^)]*\)\s*{\s*}', 'Empty catch block - no error handling'),
    (r'except\s*:?\s*\n\s*pass', 'Empty except block - no error handling'),
]

# ============================================================================
# SECURITY PATTERNS (CRITICAL - BLOCKS EXECUTION)
# Based on security-guidance plugin from deepwiki
# ============================================================================

SECURITY_PATTERNS = [
    # SQL Injection
    (r'SELECT.*\$\{', 'SQL injection risk - use parameterized queries'),
    (r'INSERT.*\$\{', 'SQL injection risk - use parameterized queries'),
    (r'UPDATE.*\$\{', 'SQL injection risk - use parameterized queries'),
    (r'DELETE.*\$\{', 'SQL injection risk - use parameterized queries'),
    (r'SELECT.*\%s.*\%', 'SQL injection risk - use parameterized queries'),
    (r'execute\s*\(\s*f["\']', 'SQL injection risk - use parameterized queries, not f-strings'),

    # Code Evaluation/Injection
    (r'eval\s*\(', 'eval() usage - arbitrary code execution risk'),
    (r'new Function\s*\(', 'new Function() - code injection risk'),
    (r'exec\s*\(', 'exec() usage - arbitrary code execution risk (Python)'),

    # Hardcoded Secrets
    (r'password\s*=\s*["\'][^"\']+["\']', 'Hardcoded password detected'),
    (r'api[_-]?key\s*=\s*["\'][^"\']{10,}["\']', 'Hardcoded API key detected'),
    (r'secret\s*=\s*["\'][^"\']{10,}["\']', 'Hardcoded secret detected'),
    (r'token\s*=\s*["\'][^"\']{20,}["\']', 'Hardcoded token detected'),
]

# ============================================================================
# JAVASCRIPT/TYPESCRIPT SPECIFIC SECURITY PATTERNS
# Based on security-guidance plugin
# ============================================================================

JS_TS_SECURITY_PATTERNS = [
    # Command Injection
    (r'child_process\.exec\s*\(', 'Command injection risk - use execFile instead of exec'),
    (r'execSync\s*\(', 'Command injection risk - use execFileSync instead'),

    # XSS
    (r'dangerouslySetInnerHTML', 'XSS risk - ensure content is sanitized'),
    (r'document\.write\s*\(', 'XSS and performance risk - use safer DOM methods'),
    (r'\.innerHTML\s*=', 'XSS risk - use textContent or sanitize content'),
]

# ============================================================================
# JAVASCRIPT/TYPESCRIPT SPECIFIC QUALITY PATTERNS
# Based on agent-sdk-verifier-ts and code-review plugin patterns
# ============================================================================

JS_TS_QUALITY_PATTERNS = [
    # Async/Await issues - common Claude Code mistakes
    (r'async\s+function[^{]*{\s*return\s+[^a]+\(', 'Async function not using await - remove async or await the call'),
    (r'\.then\([^)]+\)(?!.*\.catch)', 'Promise without .catch() - unhandled rejection risk'),
    (r'new Promise\([^)]+\)(?!.*catch)', 'Promise created without error handling'),

    # Race conditions
    (r'Promise\.all\([^)]*\)(?!.*catch)', 'Promise.all without catch - fails on first rejection'),
    (r'Promise\.race\([^)]*\)(?!.*catch)', 'Promise.race without error handling'),

    # Memory leaks
    (r'addEventListener\([^)]+\)(?!.*removeEventListener)', 'Event listener added without cleanup - potential memory leak'),
    (r'setInterval\([^)]+\)(?!.*clearInterval)', 'setInterval without clearInterval - potential memory leak'),
    (r'setTimeout.*setTimeout', 'Recursive setTimeout - verify cleanup logic exists'),
]

# ============================================================================
# PYTHON SPECIFIC SECURITY PATTERNS
# Based on security-guidance plugin
# ============================================================================

PYTHON_SECURITY_PATTERNS = [
    # Command Injection
    (r'os\.system\s*\(', 'Command injection risk - use subprocess with list args'),
    (r'from os import system', 'Command injection risk - use subprocess instead'),

    # Unsafe Deserialization
    (r'pickle\.loads?\s*\(', 'Arbitrary code execution risk - use JSON for untrusted data'),
    (r'import pickle', 'Unsafe deserialization - avoid pickle with untrusted data'),

    # Path Traversal
    (r'open\s*\(\s*.*\+.*\)', 'Path traversal risk - validate and sanitize file paths'),
]

# ============================================================================
# PYTHON SPECIFIC QUALITY PATTERNS
# Based on agent-sdk-verifier-py and code-review plugin patterns
# ============================================================================

PYTHON_QUALITY_PATTERNS = [
    # Mutable default arguments - very common Python mistake
    (r'def\s+\w+\([^)]*=\s*\[', 'Mutable default argument (list) - use None and initialize in function'),
    (r'def\s+\w+\([^)]*=\s*\{', 'Mutable default argument (dict) - use None and initialize in function'),
    (r'def\s+\w+\([^)]*=\s*set\(', 'Mutable default argument (set) - use None and initialize in function'),

    # Missing context managers
    (r'open\([^)]+\)(?!.*with)(?!.*\.__enter__)', 'File opened without context manager - use "with open(...)"'),
    (r'= open\(', 'File assigned without context manager - use "with open(...) as f:"'),

    # Exception handling issues
    (r'except\s*:', 'Bare except clause - catch specific exceptions'),
    (r'except Exception\s*:', 'Catching Exception too broad - catch specific exception types'),
    (r'except.*:\s*pass\s*$', 'Silent exception - log error or re-raise'),

    # Iterator issues
    (r'list\(range\(.*\)\)(?!.*for)', 'Unnecessary list() around range() - use range() directly in loops'),
]

# ============================================================================
# GO SPECIFIC PATTERNS
# Common Go security and quality issues
# ============================================================================

GO_SECURITY_PATTERNS = [
    # Command Injection
    (r'exec\.Command\s*\(\s*["\']sh["\']', 'Command injection risk - avoid shell execution'),
    (r'exec\.Command\s*\(\s*["\']bash["\']', 'Command injection risk - avoid shell execution'),

    # SQL Injection
    (r'db\.Query\s*\(\s*fmt\.Sprintf', 'SQL injection risk - use prepared statements'),
    (r'db\.Exec\s*\(\s*fmt\.Sprintf', 'SQL injection risk - use prepared statements'),
]

GO_QUALITY_PATTERNS = [
    # Error handling - very common Go mistakes
    (r'_\s*:?=.*\n\s*$', 'Ignored error - handle or explicitly ignore'),
    (r'if err != nil\s*{\s*}', 'Empty error handler'),
    (r'if err != nil\s*{\s*return\s*}', 'Error returned without context - wrap error with context'),

    # Nil pointer issues
    (r'\.(\w+)(?!\s*==\s*nil)(?!\s*!=\s*nil)', 'Potential nil pointer - check for nil before dereferencing'),
    (r'func.*\*\w+.*{[^}]*return [^&]', 'Returning pointer without nil check'),

    # Goroutine leaks
    (r'go func\(', 'Goroutine started - ensure it has exit condition and cleanup'),
    (r'go\s+\w+\(', 'Goroutine started - verify no leaks and proper context cancellation'),

    # Channel issues
    (r'make\(chan\b(?!.*,)', 'Unbuffered channel - may cause deadlock, consider timeout or buffer'),
    (r'<-.*chan\b(?!.*select)(?!.*time\.After)', 'Channel receive without timeout - may block forever'),

    # Defer misuse
    (r'defer.*\.Close\(\).*for', 'defer in loop - will not run until function exits, not loop iteration'),
    (r'defer.*\.Close\(\).*\n.*defer.*\.Close\(\)', 'Multiple defers - verify execution order is correct'),
]

# ============================================================================
# RUST SPECIFIC PATTERNS
# Common Rust safety issues
# ============================================================================

RUST_QUALITY_PATTERNS = [
    # Unsafe blocks without justification
    (r'unsafe\s*{', 'Unsafe block - ensure it\'s necessary and document why'),

    # Unwrap usage (can panic) - very common Rust mistakes
    (r'\.unwrap\(\)', 'unwrap() can panic - use expect() with message or proper error handling'),
    (r'\.expect\s*\(\s*["\']["\']', 'Empty expect message - provide meaningful error context'),
    (r'\.unwrap_or_default\(\)', 'unwrap_or_default() - verify default makes sense for this type'),

    # Clone overuse - ownership issues
    (r'\.clone\(\).*\.clone\(\)', 'Multiple clones - review ownership/borrowing'),
    (r'\.clone\(\)(?!.*//.*borrow)', 'clone() without comment - consider borrowing instead'),

    # Lifetime issues
    (r'<\'static>', 'Static lifetime - verify this is truly static, not just to satisfy compiler'),
    (r'fn.*<\'a,\s*\'a>', 'Duplicate lifetime parameter - simplify or explain why needed'),

    # Error handling
    (r'\?(?!;).*\n\s*}', 'Error propagated at end of function - consider handling or documenting'),
    (r'match.*Err\(e\)\s*=>\s*\{\s*\}', 'Empty error match arm - handle or log error'),

    # Borrow checker workarounds
    (r'Rc<RefCell<', 'Rc<RefCell> pattern - verify interior mutability is necessary'),
    (r'Arc<Mutex<', 'Arc<Mutex> pattern - ensure synchronization is actually needed'),
    (r'\.as_ref\(\)\.unwrap\(\)', 'Chained as_ref().unwrap() - use if let or pattern matching'),

    # Panic-inducing operations
    (r'\[index\](?!.*get\()', 'Direct index access - use .get() to avoid panics'),
    (r'\.get_unchecked\(', 'get_unchecked() - ensure bounds are verified, document safety'),
]

# ============================================================================
# TYPE SAFETY PATTERNS (TypeScript/JavaScript)
# ============================================================================

TYPE_SAFETY_PATTERNS = [
    (r':\s*any\b', 'TypeScript "any" type - reduces type safety'),
    (r'as any\b', 'Type assertion to "any" - bypasses type checking'),
    (r'@ts-ignore', '@ts-ignore directive - suppresses type errors'),
    (r'@ts-nocheck', '@ts-nocheck directive - disables type checking'),
    (r'@ts-expect-error', '@ts-expect-error - document why error is expected'),
]

# ============================================================================
# CODE QUALITY PATTERNS (All Languages)
# Based on code-review plugin patterns
# ============================================================================

CODE_QUALITY_PATTERNS = [
    # Null/undefined handling
    (r'\.length(?!\s*>)', 'Potential null/undefined - check before accessing length'),
    (r'\[0\](?!\s*\?)', 'Array access without bounds check - could be undefined'),

    # Console statements (should use proper logging)
    (r'console\.log\(', 'console.log in production code - use proper logging'),
    (r'print\s*\(', 'print() in production code - use proper logging (Python)'),
    (r'fmt\.Println\(', 'fmt.Println in production - use structured logging (Go)'),
    (r'println!\(', 'println! in production - use proper logging (Rust)'),

    # Magic numbers
    (r'\d{3,}(?!\s*//)', 'Magic number - consider using named constant'),
]

# ============================================================================
# LANGUAGE DETECTION
# ============================================================================

def detect_language(file_path):
    """Detect programming language from file extension."""
    ext = Path(file_path).suffix.lower()

    language_map = {
        '.ts': 'typescript',
        '.tsx': 'typescript',
        '.js': 'javascript',
        '.jsx': 'javascript',
        '.py': 'python',
        '.go': 'go',
        '.rs': 'rust',
        '.java': 'java',
        '.c': 'c',
        '.cpp': 'cpp',
        '.h': 'c',
        '.hpp': 'cpp',
    }

    return language_map.get(ext, 'unknown')

# ============================================================================
# PATTERN CHECKING
# ============================================================================

def check_patterns(content, patterns):
    """Check content against patterns and return issues found."""
    issues = []
    lines = content.split('\n')

    for line_num, line in enumerate(lines, 1):
        for pattern, message in patterns:
            if re.search(pattern, line, re.IGNORECASE):
                issues.append({
                    'line': line_num,
                    'pattern': pattern,
                    'message': message,
                    'content': line.strip()
                })

    return issues

def get_language_specific_patterns(language):
    """Get security and quality patterns for specific language."""
    security = []
    quality = []

    if language in ('javascript', 'typescript'):
        security = JS_TS_SECURITY_PATTERNS
        quality = JS_TS_QUALITY_PATTERNS
    elif language == 'python':
        security = PYTHON_SECURITY_PATTERNS
        quality = PYTHON_QUALITY_PATTERNS
    elif language == 'go':
        security = GO_SECURITY_PATTERNS
        quality = GO_QUALITY_PATTERNS
    elif language == 'rust':
        quality = RUST_QUALITY_PATTERNS

    return security, quality

# ============================================================================
# MAIN VALIDATION
# ============================================================================

def main():
    # Read hook input from stdin
    try:
        hook_data = json.loads(sys.stdin.read())
    except json.JSONDecodeError:
        print("Error: Invalid JSON input", file=sys.stderr)
        sys.exit(1)

    tool_name = hook_data.get('tool_name', '')
    tool_input = hook_data.get('tool_input', {})

    # Only validate Write and Edit operations
    if tool_name not in ['Write', 'Edit']:
        sys.exit(0)

    # Get file content
    if tool_name == 'Write':
        file_path = tool_input.get('file_path', '')
        content = tool_input.get('content', '')
    elif tool_name == 'Edit':
        file_path = tool_input.get('file_path', '')
        content = tool_input.get('new_string', '')
    else:
        sys.exit(0)

    # Skip validation for certain file types
    if file_path.endswith(('.md', '.txt', '.json', '.yml', '.yaml', '.lock', '.sum')):
        sys.exit(0)

    # Detect language
    language = detect_language(file_path)

    # Get language-specific patterns
    lang_security, lang_quality = get_language_specific_patterns(language)

    # Run all checks
    incomplete_issues = check_patterns(content, INCOMPLETE_PATTERNS)
    security_issues = check_patterns(content, SECURITY_PATTERNS)
    lang_security_issues = check_patterns(content, lang_security)
    type_issues = check_patterns(content, TYPE_SAFETY_PATTERNS) if language in ('typescript', 'javascript') else []
    quality_issues = check_patterns(content, CODE_QUALITY_PATTERNS + lang_quality)

    # Combine all security issues
    all_security_issues = security_issues + lang_security_issues

    # ========================================================================
    # BLOCK: Critical security issues
    # ========================================================================
    if all_security_issues:
        print("❌ BLOCKED: Security issues detected", file=sys.stderr)
        print(f"\nFile: {file_path}", file=sys.stderr)
        print(f"Language: {language}", file=sys.stderr)
        for issue in all_security_issues[:5]:  # Show first 5
            print(f"\n  Line {issue['line']}: {issue['message']}", file=sys.stderr)
            print(f"    > {issue['content']}", file=sys.stderr)
        if len(all_security_issues) > 5:
            print(f"\n  ... and {len(all_security_issues) - 5} more security issues", file=sys.stderr)
        print("\n⚠️  CRITICAL: Fix security issues before proceeding.", file=sys.stderr)
        print("Run /quality-check for full analysis.\n", file=sys.stderr)
        sys.exit(2)  # Block execution

    # ========================================================================
    # WARN: Incomplete implementations
    # ========================================================================
    if incomplete_issues:
        print("⚠️  WARNING: Incomplete implementation detected", file=sys.stderr)
        print(f"\nFile: {file_path}", file=sys.stderr)
        for issue in incomplete_issues[:3]:  # Show first 3
            print(f"  Line {issue['line']}: {issue['message']}", file=sys.stderr)
            print(f"    > {issue['content']}", file=sys.stderr)
        if len(incomplete_issues) > 3:
            print(f"  ... and {len(incomplete_issues) - 3} more issues", file=sys.stderr)
        print("\nComplete implementation before committing.", file=sys.stderr)
        print("Run /quality-check for full analysis.\n", file=sys.stderr)
        sys.exit(1)  # Warn but allow

    # ========================================================================
    # INFO: Type safety and code quality
    # ========================================================================
    total_info_issues = len(type_issues) + len(quality_issues)

    if total_info_issues > 3:
        print(f"ℹ️  Info: {total_info_issues} code quality concerns in {file_path}", file=sys.stderr)

        if type_issues:
            print(f"  - {len(type_issues)} type safety issues", file=sys.stderr)
        if quality_issues:
            print(f"  - {len(quality_issues)} code quality issues", file=sys.stderr)

        print("Run /quality-check for details.\n", file=sys.stderr)

    # All good
    sys.exit(0)

if __name__ == '__main__':
    main()
