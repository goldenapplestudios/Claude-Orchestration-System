# Claude Code Quality Linter

Automatic quality checks to catch common Claude Code mistakes before they become problems.

## What It Does

The linter catches common Claude Code mistakes based on deepwiki research from:
- security-guidance plugin
- code-review plugin
- agent-sdk-verifier patterns

**Detects:**
- ✅ Incomplete implementations (TODOs, stubs, placeholders)
- ✅ Missing error handling (empty catch/except blocks)
- ✅ Security vulnerabilities (SQL injection, XSS, command injection)
- ✅ Language-specific issues (TypeScript, JavaScript, Python, Go, Rust)
- ✅ Type safety issues (TypeScript `any` usage)
- ✅ Code quality problems (null handling, console logging)
- ✅ Pattern violations

## Three-Layer System

### 1. Automatic Hook (Prevents Mistakes)

**When:** Before every Write/Edit operation
**How:** PreToolUse hook validates code automatically
**Action:**
- **Blocks** security issues (exit code 2)
- **Warns** about incomplete implementations (exit code 1)
- **Informs** about type safety concerns

**File:** `.claude/hooks/validate-completeness.py`

**Example:**
```python
# You try to write this:
function validateUser(user) {
  // TODO: Add validation
  return true;
}

# Hook catches it:
⚠️  WARNING: Incomplete implementation detected
Line 2: TODO comment found - implementation incomplete
  > // TODO: Add validation

Consider completing implementation before committing.
```

### 2. Manual Command (On-Demand Checks)

**When:** You run `/quality-check`
**How:** Slash command triggers quality-checker agent
**Action:** Comprehensive analysis with detailed report

**File:** `.claude/commands/quality-check.md`

**Usage:**
```bash
/quality-check                    # Check all files
/quality-check src/components     # Check directory
/quality-check src/auth.ts        # Check file
```

**Example Output:**
```markdown
# Quality Check Report

## Summary
- Files Reviewed: 12
- Critical Issues: 2
- Warnings: 5

## Critical Issues

### Empty Error Handling
**File:** src/api.ts:45
**Problem:** catch (e) {} - errors silently ignored
**Fix:** Add proper error handling and logging

### SQL Injection Risk
**File:** src/db.ts:78
**Problem:** String interpolation in SQL query
**Fix:** Use parameterized queries
```

### 3. Quality Checker Agent (Deep Analysis)

**When:** Invoked by command or manually
**How:** Custom agent with specialized tools
**Action:** Thorough review with confidence scoring

**File:** `.claude/agents/quality-checker.md`

**Capabilities:**
- Searches entire codebase
- Cross-references project standards
- Provides fix suggestions
- Scores issues by confidence (0-100)

## What Gets Checked

### Universal Checks (All Languages)

#### Incomplete Implementations (WARNS - Exit 1)

Catches:
- `TODO:` comments (all comment styles: //, #, /*)
- `FIXME:` comments
- `HACK:` comments
- "for now" solutions
- "temporary" solutions
- "placeholder" markers
- "we can add this later"
- Empty function bodies
- Empty catch/except blocks

**Example:**
```typescript
// ❌ Caught by linter
function processData(data: any) {
  // TODO: Implement validation
  return data;
}

// ✅ Passes linting
function processData(data: DataType): ProcessedData {
  if (!isValid(data)) {
    throw new Error('Invalid data');
  }
  return transform(data);
}
```

#### Security Issues (BLOCKS - Exit 2)

Based on security-guidance plugin from deepwiki.

**Universal Security Patterns:**
- SQL injection (SELECT/INSERT/UPDATE/DELETE with ${} or %s)
- SQL injection with f-strings (Python)
- eval() usage (JavaScript/Python)
- new Function() usage (JavaScript)
- exec() usage (Python)
- Hardcoded passwords
- Hardcoded API keys (10+ chars)
- Hardcoded secrets (10+ chars)
- Hardcoded tokens (20+ chars)

**Example:**
```typescript
// ❌ BLOCKED by linter - SQL injection
const query = `SELECT * FROM users WHERE id = ${userId}`;
const query2 = `INSERT INTO logs VALUES (${data})`;

// ❌ BLOCKED by linter - Code execution
eval(userInput);
new Function(code)();

// ❌ BLOCKED by linter - Hardcoded secrets
const apiKey = "sk_live_abc123def456";

// ✅ Passes linting
const query = 'SELECT * FROM users WHERE id = $1';
db.query(query, [userId]);

const apiKey = process.env.API_KEY;
```

---

### Language-Specific Checks

Based on deepwiki research from security-guidance and code-review plugins.

#### JavaScript/TypeScript

**Security (BLOCKS):**
- `child_process.exec()` - command injection risk (use execFile)
- `execSync()` - command injection risk (use execFileSync)
- `dangerouslySetInnerHTML` - XSS risk (sanitize content)
- `document.write()` - XSS and performance risk
- `.innerHTML =` - XSS risk (use textContent)

**Type Safety (INFORMS):**
- `: any` - reduces type safety
- `as any` - bypasses type checking
- `@ts-ignore` - suppresses errors
- `@ts-nocheck` - disables type checking
- `@ts-expect-error` - should document why

**Common Mistakes (INFORMS):**
- Async/await issues:
  - `async function` not using `await` - unnecessary async
  - `.then()` without `.catch()` - unhandled rejection risk
  - `new Promise()` without error handling
- Promise handling:
  - `Promise.all()` without catch - fails on first rejection
  - `Promise.race()` without error handling
- Memory leaks:
  - `addEventListener()` without `removeEventListener()` - memory leak
  - `setInterval()` without `clearInterval()` - memory leak
  - Recursive `setTimeout` - verify cleanup logic

**Code Quality (INFORMS):**
- `console.log()` - use proper logging in production
- `.length` without null check - potential undefined
- `[0]` without optional chaining - could be undefined

**Example:**
```typescript
// ❌ BLOCKED - Command injection
import { exec } from 'child_process';
exec(`git commit -m "${userMessage}"`);

// ❌ BLOCKED - XSS
element.innerHTML = userInput;
<div dangerouslySetInnerHTML={{__html: data}} />

// ⚠️ WARNING - Type safety
function process(data: any) { }
const x = data as any;

// ℹ️  INFO - Code quality
console.log('debug info');
const first = array[0]; // Could be undefined

// ✅ Passes linting
import { execFile } from 'child_process';
execFile('git', ['commit', '-m', userMessage]);

element.textContent = userInput;
// Or use sanitizer

function process(data: SpecificType): ReturnType { }
logger.info('user action', { data });
const first = array[0] ?? defaultValue;
```

#### Python

**Security (BLOCKS):**
- `os.system()` - command injection (use subprocess with list)
- `from os import system` - command injection
- `pickle.loads()` / `pickle.load()` - arbitrary code execution
- `import pickle` - unsafe deserialization warning
- `open()` with string concatenation - path traversal risk
- `execute(f"...")` - SQL injection with f-strings

**Common Mistakes (INFORMS):**
- Mutable default arguments:
  - `def func(x=[])` - mutable list default (use None)
  - `def func(x={})` - mutable dict default (use None)
  - `def func(x=set())` - mutable set default (use None)
- Missing context managers:
  - `open()` without `with` - resource leak risk
  - `f = open()` - file not properly closed
- Exception handling:
  - `except:` - bare except clause (catch specific exceptions)
  - `except Exception:` - too broad (catch specific types)
  - `except: pass` - silent exception (log or re-raise)
- Iterator issues:
  - `list(range())` - unnecessary list conversion

**Code Quality (INFORMS):**
- `print()` - use proper logging in production

**Example:**
```python
# ❌ BLOCKED - Command injection
os.system(f"rm -rf {user_path}")

# ❌ BLOCKED - Unsafe deserialization
data = pickle.loads(untrusted_data)

# ❌ BLOCKED - Path traversal
open(base_path + user_file)

# ❌ BLOCKED - SQL injection
cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")

# ℹ️  INFO - Code quality
print("Debug info")

# ✅ Passes linting
import subprocess
subprocess.run(['rm', '-rf', validated_path])

import json
data = json.loads(untrusted_data)

from pathlib import Path
safe_path = Path(base_path) / Path(user_file).name

cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))

import logging
logging.info("Debug info")
```

#### Go

**Security (BLOCKS):**
- `exec.Command("sh", ...)` - command injection
- `exec.Command("bash", ...)` - command injection
- `db.Query(fmt.Sprintf(...))` - SQL injection
- `db.Exec(fmt.Sprintf(...))` - SQL injection

**Common Mistakes (INFORMS):**
- Error handling:
  - `_ = ...` - ignored error (handle or explicitly ignore)
  - `if err != nil {}` - empty error handler
  - `if err != nil { return }` - error without context (wrap with context)
- Nil pointer issues:
  - Dereferencing without nil check - potential panic
  - Returning pointer without nil check
- Concurrency issues:
  - `go func()` - ensure exit condition and cleanup
  - `go funcName()` - verify no leaks and proper context cancellation
- Channel issues:
  - `make(chan ...)` unbuffered - may cause deadlock, consider timeout/buffer
  - Channel receive without timeout - may block forever
- Defer misuse:
  - `defer` in loop - runs at function exit, not loop iteration
  - Multiple defers - verify execution order

**Code Quality (INFORMS):**
- `fmt.Println()` - use structured logging

**Example:**
```go
// ❌ BLOCKED - Command injection
exec.Command("sh", "-c", userCmd).Run()

// ❌ BLOCKED - SQL injection
db.Query(fmt.Sprintf("SELECT * FROM users WHERE id = %s", userId))

// ℹ️  INFO - Error handling
_ = doSomething() // Ignored error

// ℹ️  INFO - Logging
fmt.Println("debug")

// ✅ Passes linting
exec.Command("program", arg1, arg2).Run()

db.Query("SELECT * FROM users WHERE id = $1", userId)

if err := doSomething(); err != nil {
    return err
}

log.Info("debug", "field", value)
```

#### Rust

**Common Mistakes (INFORMS):**
- Panic-inducing operations:
  - `.unwrap()` - can panic, use expect() or handle error
  - `.expect("")` - empty message, provide context
  - `.unwrap_or_default()` - verify default makes sense
  - `[index]` - direct index access, use .get() to avoid panics
  - `.get_unchecked()` - ensure bounds verified, document safety
- Ownership/borrowing issues:
  - Multiple `.clone()` - review ownership/borrowing
  - `.clone()` without comment - consider borrowing instead
- Lifetime issues:
  - `<'static>` - verify truly static, not just to satisfy compiler
  - Duplicate lifetime parameters - simplify or explain
- Error handling:
  - `?` at end of function - consider handling or documenting
  - Empty error match arm - handle or log error
- Unsafe code:
  - `unsafe { }` - ensure necessary, document why
- Borrow checker workarounds:
  - `Rc<RefCell<` - verify interior mutability is necessary
  - `Arc<Mutex<` - ensure synchronization actually needed
  - `.as_ref().unwrap()` - use if let or pattern matching

**Code Quality (INFORMS):**
- `println!()` - use proper logging

**Example:**
```rust
// ℹ️  INFO - Unsafe code
unsafe {
    // Needs documentation
}

// ℹ️  INFO - Can panic
let value = option.unwrap();
let x = result.expect("");

// ℹ️  INFO - Excessive cloning
let a = data.clone().process().clone();

// ℹ️  INFO - Debug output
println!("debug: {:?}", data);

// ✅ Passes linting
// SAFETY: Pointer is valid because...
unsafe {
    // Documented reason
}

let value = option.expect("Config must have value");
match result {
    Ok(v) => v,
    Err(e) => return Err(e),
}

// Use borrowing instead
let processed = data.process();

use log::info;
info!("processed data: {:?}", data);
```

## Configuration

### Hook Configuration

File: `.claude/settings.json`

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write",
        "hooks": [{
          "type": "command",
          "command": "python3 .claude/hooks/validate-completeness.py",
          "timeout": 5000
        }]
      },
      {
        "matcher": "Edit",
        "hooks": [{
          "type": "command",
          "command": "python3 .claude/hooks/validate-completeness.py",
          "timeout": 5000
        }]
      }
    ]
  }
}
```

### Customizing Patterns

Edit `.claude/hooks/validate-completeness.py`:

```python
# Add custom patterns
INCOMPLETE_PATTERNS = [
    (r'YOUR_PATTERN', 'Your message'),
]

# Add project-specific security checks
SECURITY_PATTERNS = [
    (r'YOUR_SECURITY_PATTERN', 'Your warning'),
]
```

### Disabling Linter (Not Recommended)

Remove or comment out hooks in `.claude/settings.json`

## How It Works

### Automatic Validation Flow

```
Claude writes/edits code
    ↓
PreToolUse hook triggered
    ↓
validate-completeness.py runs
    ↓
Checks content against patterns
    ↓
┌─────────────────────┬──────────────────────┬─────────────────┐
│ Security issues?    │ Incomplete code?     │ Type issues?    │
│ Exit 2 (BLOCK)      │ Exit 1 (WARN)        │ Exit 0 (INFO)   │
└─────────────────────┴──────────────────────┴─────────────────┘
    ↓                      ↓                       ↓
Operation blocked     Warning shown          Info displayed
Code not written      Code written anyway    Code written
```

### Manual Check Flow

```
User runs /quality-check
    ↓
Command launches quality-checker agent
    ↓
Agent scans codebase with Grep/Glob
    ↓
Checks against:
- Project constraints
- Security patterns
- Completeness markers
    ↓
Generates comprehensive report
    ↓
Returns findings with line numbers and fixes
```

## Benefits

### Catches Mistakes Early

**Before:**
```
1. Write incomplete code
2. Mark task complete
3. Commit to git
4. Discover issues later
5. Fix and recommit
```

**With Linter:**
```
1. Try to write incomplete code
2. Linter catches it immediately
3. Fix it right away
4. Complete and correct code
```

### Prevents Common Failures

- **Incomplete implementations** → Caught by TODO detection
- **Security vulnerabilities** → Blocked by security checks
- **Type safety issues** → Warned about `any` usage
- **Pattern violations** → Verified against constraints

### Maintains Quality Standards

- Every Write/Edit is validated
- Automatic enforcement (can't bypass accidentally)
- Consistent standards across all code
- No manual review needed for basics

## Examples

### Example 1: TODO Detection

```typescript
// Claude writes:
function authenticate(user: User): boolean {
  // TODO: Implement JWT validation
  return true;
}

// Linter responds:
⚠️  WARNING: Incomplete implementation detected
File: src/auth.ts
  Line 2: TODO comment found - implementation incomplete
    > // TODO: Implement JWT validation

Consider completing implementation before committing.
Run /quality-check for full analysis.

// Claude fixes:
function authenticate(user: User): boolean {
  const token = user.token;
  if (!token) return false;

  try {
    const decoded = jwt.verify(token, SECRET_KEY);
    return decoded.userId === user.id;
  } catch (error) {
    console.error('Auth failed:', error);
    return false;
  }
}

// ✅ Linter passes
```

### Example 2: Security Block

```typescript
// Claude writes:
function getUser(userId: string) {
  return db.query(`SELECT * FROM users WHERE id = ${userId}`);
}

// Linter BLOCKS:
❌ BLOCKED: Security issues detected
File: src/database.ts
  Line 2: Potential SQL injection - use parameterized queries
    > return db.query(`SELECT * FROM users WHERE id = ${userId}`);

Please fix security issues before proceeding.

// Operation blocked - file not written

// Claude fixes:
function getUser(userId: string) {
  return db.query('SELECT * FROM users WHERE id = $1', [userId]);
}

// ✅ Linter allows
```

### Example 3: Comprehensive Check

```bash
$ /quality-check src/

# Quality Check Report

## Summary
- Files Reviewed: 8
- Critical Issues: 1
- Warnings: 3

## Critical Issues

### Missing Error Handling
**File:** src/services/api.ts:34
**Problem:** Empty catch block silently ignores errors
**Fix:** Add error logging and proper error handling
**Confidence:** 95%

## Warnings

### Type Safety
**File:** src/utils/helpers.ts:12
**Problem:** Using `any` type without justification
**Suggestion:** Define proper interface
**Confidence:** 75%

### Potential Issue
**File:** src/components/Form.tsx:89
**Problem:** "for now" comment suggests incomplete implementation
**Suggestion:** Complete implementation or create follow-up task
**Confidence:** 70%
```

## Troubleshooting

### Linter Not Running

**Check:**
1. `.claude/settings.json` exists and is valid JSON
2. Hook script is executable: `chmod +x .claude/hooks/validate-completeness.py`
3. Python 3 is available: `python3 --version`

### False Positives

**Adjust patterns** in `.claude/hooks/validate-completeness.py`:
```python
# Skip certain files
if file_path.endswith(('.test.ts', '.spec.ts')):
    sys.exit(0)  # Allow test files
```

### Hook Timeout

**Increase timeout** in `.claude/settings.json`:
```json
{
  "timeout": 10000  // 10 seconds instead of 5
}
```

## Best Practices

### DO:

- ✅ Keep linter enabled during development
- ✅ Run `/quality-check` before committing
- ✅ Fix warnings, not just blockers
- ✅ Update patterns for project-specific issues
- ✅ Use linter as learning tool

### DON'T:

- ❌ Disable linter to "save time"
- ❌ Ignore warnings consistently
- ❌ Commit code with TODOs
- ❌ Work around linter instead of fixing issues

## Integration with Workflow

### During Development

1. Write code as normal
2. Linter validates automatically
3. Fix any issues immediately
4. Continue with quality code

### Before Session End

```bash
/quality-check
# Review any warnings
# Fix critical issues
# Archive clean code
```

### In CI/CD

```bash
# Add to pre-commit hook or CI
python3 .claude/hooks/validate-completeness.py < changes.json
```

## Summary

The linter provides:
- **Automatic validation** via PreToolUse hooks
- **Manual checking** via /quality-check command
- **Deep analysis** via quality-checker agent
- **Immediate feedback** before mistakes persist
- **Consistent quality** across all code

**The goal:** Catch common Claude Code mistakes automatically so you can focus on building features, not fixing quality issues.
