# Quick Start - 3 Steps

Get Claude Code autonomous operations running in under 2 minutes.

---

## Step 1: Copy Files (30 seconds)

Copy these files to your project:

```bash
# From this repo to your project:
cp CLAUDE.md /path/to/your-project/
cp -r .claude /path/to/your-project/
```

That's it. Two files copied.

---

## Step 2: Claude Code Discovers Automatically

When you open your project in Claude Code, it will automatically:

1. Find `CLAUDE.md` at your project root
2. Load all protocols from `.claude/protocols/`
3. Activate quality linter (hook system)
4. Discover all 7 custom agents
5. Enable autonomous gamification system

Claude Code auto-discovers `CLAUDE.md` files.

---

## Step 3: Start Working

Just start Claude Code in your project directory and give it a task:

```bash
cd your-project
# Start Claude Code (your usual method)
```

Then say something like:
- "Add a user authentication feature"
- "Fix the bug in the login flow"
- "Refactor the database layer"

**What happens automatically:**

1. **Quality Linter activates** → Blocks TODO markers, security issues, incomplete code
2. **Agents available** → Can use `/quality-check`, or agents like `code-explorer`, `quality-checker`
3. **Gamification runs** → Tracks score and GGP automatically in background
4. **Context management** → Uses agents when context gets high
5. **Session tracking** → Documents decisions as it works

**Final report generated automatically:**
```
Task Complete

Final Score: 88/100 (GOLD LEVEL)

GGP Balance: +75 (Good Standing)
  Started: +50
  Earned: +35 (quality code, tests, docs)
  Lost: -10 (2 linter warnings)

Achievements:
  Gold Excellence
  Test Champion (85% coverage)
```

---

## Optional: Customize for Your Project

Only do this if you want to reference your existing docs:

### If you have existing documentation:

Edit `.claude/project/architecture.md`:
```markdown
# Project Architecture

@../../README.md
@../../docs/architecture.md

## Additional Notes
[Only add what's NOT already in your docs]
```

Edit `.claude/project/constraints.md`:
```markdown
# Project Constraints

@../../CONTRIBUTING.md

## Additional Rules
[Only add what's NOT already documented]
```

### If you don't have documentation:

Fill in `.claude/project/architecture.md` with:
- Tech stack
- Directory structure
- Key patterns

Fill in `.claude/project/constraints.md` with:
- Hard rules (NEVER do X)
- Standards (ALWAYS do Y)

**That's optional.** The system works without this.

---

## What You Get

### Automatic Quality Checks

**Before (without system):**
```typescript
function authenticate(user: User) {
  // TODO: Add validation
  return true;
}
```
Committed (wrong)

**After (with system):**
```typescript
function authenticate(user: User) {
  // TODO: Add validation
  return true;
}
```
**BLOCKED by linter:**
```
⚠️  WARNING: Incomplete implementation detected
Line 2: TODO comment found - implementation incomplete
  > // TODO: Add validation

Consider completing implementation before committing.
```

---

### Custom Agents Available

Use specialized agents for complex tasks:

```bash
# Deep codebase exploration
"Use code-explorer to find all authentication code"

# Architecture design
"Use code-architect to design a new feature"

# Quality checking
/quality-check
```

---

### Autonomous Gamification

No manual tracking needed. System runs in background:

- Tracks quality automatically
- Updates GGP based on actions
- Generates final report
- Awards achievements

---

## Verification

Test that it's working:

### 1. Check CLAUDE.md is loaded

Ask: "What protocols are you using?"

Should mention: agent-usage, context-management, gamification, GGP, etc.

### 2. Check quality linter works

Try to write:
```javascript
function test() {
  // TODO: implement
}
```

Should get warning about incomplete implementation.

### 3. Check agents are available

Ask: "What custom agents are available?"

Should list: code-explorer, code-architect, implementation-helper, error-resolver, test-writer, doc-writer, quality-checker

---

## Summary

Setup: 30 seconds (copy 2 things)
Configuration: 0-5 minutes (optional)
Usage: Automatic

The system runs autonomously from this point forward.

---

## Troubleshooting

**Claude Code not finding CLAUDE.md?**
- Verify `CLAUDE.md` is at your project root
- Restart Claude Code

**Linter not working?**
- Check `.claude/settings.json` exists
- Verify `.claude/hooks/validate-completeness.py` is executable: `chmod +x .claude/hooks/validate-completeness.py`
- Ensure Python 3 is available: `python3 --version`

**Need more help?**
- See `SETUP.md` for detailed examples
- See `README.md` for complete overview
- See `.claude/docs/` for full documentation
