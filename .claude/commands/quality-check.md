---
description: Run quality checks on code to catch common Claude Code mistakes
allowed-tools: Bash, Read, Grep, Glob, Task
---

# Quality Check Command

Run comprehensive quality checks on your code to catch common implementation mistakes.

## What This Checks

1. **Incomplete Implementations**
   - TODO/FIXME comments
   - Stub functions
   - "For now" solutions

2. **Type Safety**
   - TypeScript `any` usage
   - Missing type annotations
   - Type assertion abuse

3. **Error Handling**
   - Empty catch blocks
   - Unhandled promises
   - Missing error cases

4. **Security Issues**
   - SQL injection risks
   - XSS vulnerabilities
   - Hardcoded secrets

5. **Pattern Violations**
   - Project constraints
   - Architecture patterns
   - Code standards

## Usage

```bash
# Check all files
/quality-check

# Check specific directory
/quality-check src/components

# Check specific file
/quality-check src/services/auth.ts
```

## How It Works

1. **Launch Quality Checker Agent**
   - Specialized agent reviews code
   - Checks against common mistakes
   - Verifies project standards

2. **Generate Report**
   - Critical issues (must fix)
   - Warnings (should fix)
   - Verification checklist

3. **Provide Actionable Feedback**
   - Specific line numbers
   - Clear explanations
   - Suggested fixes

## Example Output

```markdown
# Quality Check Report

## Summary
- Files Reviewed: 12
- Critical Issues: 2
- Warnings: 5

## Critical Issues

### Incomplete Error Handling
**File:** src/services/api.ts:45
**Problem:** Empty catch block - errors are silently ignored
**Fix:** Add proper error handling and logging

### SQL Injection Risk
**File:** src/database/queries.ts:78
**Problem:** String concatenation in SQL query
**Fix:** Use parameterized queries

## Warnings

### Type Safety Concern
**File:** src/utils/helpers.ts:23
**Problem:** Using `any` type without justification
**Suggestion:** Define proper interface or use generics
```

## When to Run

**Before committing:**
```bash
/quality-check
# Fix any critical issues
# Review warnings
```

**During development:**
```bash
/quality-check src/new-feature
# Verify implementation quality
# Catch mistakes early
```

**After complex changes:**
```bash
/quality-check
# Ensure nothing was missed
# Verify completeness
```

## Integration with Workflow

This command works well with:
- **Pre-commit hooks**: Auto-run before commits
- **Code review**: Run before creating PR
- **Session end**: Final check before archiving

## Action

Let me run quality checks on your code now using the quality-checker agent.

What would you like me to check?
- All files (slower but thorough)
- Specific directory (focused check)
- Recent changes (quick check)
