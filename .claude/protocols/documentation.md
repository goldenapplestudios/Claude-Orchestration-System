# Documentation & Archiving Protocol

**Critical for autonomous operation:** Document work as you go, archive when complete, start fresh for next task.

## Core Principle

**Every session creates documentation. When task completes, archive everything. Next task starts with clean context.**

## Documentation Workflow

### During Every Session

**You MUST maintain these files:**

1. **`.claude/work/current-session.md`** - Work log
2. **`.claude/work/decisions.md`** - Key decisions made
3. **Task-specific docs** - As needed for the task

### 1. Session Start

**Create `.claude/work/current-session.md`:**

```markdown
# Session: [Task Name]

**Date Started:** 2024-01-15
**Status:** In Progress

## Task Description
[What you're working on]

## Approach
- [ ] Step 1
- [ ] Step 2
- [ ] Step 3

## Progress Log

### [Time] - Session Start
- Read CLAUDE.md
- Loaded project context
- Reviewed architecture.md and constraints.md
- Ready to begin

```

### 2. During Work

**Update current-session.md AS YOU GO:**

```markdown
### [Time] - Exploration
- Used Explore agent to find auth code
- Found key files: src/auth/login.ts, src/middleware/auth.ts
- Auth uses JWT tokens, stored in localStorage
- Context: 25%

### [Time] - Planning
- Decided to add refresh token alongside access token
- Will modify generateToken() in src/auth/login.ts
- Will add refreshToken() endpoint
- Context: 35%

### [Time] - Implementation Started
- Reading src/auth/login.ts
- Adding refreshToken field to JWT payload
- Context: 45%

### [Time] - Issue Encountered
- Tests failing - tokens now different structure
- Need to update test fixtures
- Fixing in tests/auth.test.ts
- Context: 55%

### [Time] - Completed
- Refresh tokens implemented
- All tests passing
- Documentation updated
- Context: 60%
```

### 3. Document Decisions

**Create `.claude/work/decisions.md` for important choices:**

```markdown
# Decisions Made

## Refresh Token Storage

**Decision:** Store refresh tokens in httpOnly cookies, not localStorage

**Reasoning:**
- More secure (can't be accessed by JavaScript)
- Prevents XSS attacks
- Standard practice found in codebase (see src/auth/sessions.ts)

**Alternatives Considered:**
- localStorage: Less secure, vulnerable to XSS
- sessionStorage: Would require re-login on tab close

**Trade-offs:**
- Cookies require CSRF protection (already implemented)
- Can't access from client-side JS (intentional for security)

**Date:** 2024-01-15
**Context:** Adding refresh token feature

---

## Token Expiration Times

**Decision:** Access token: 15min, Refresh token: 7 days

**Reasoning:**
- Matches existing session timeout in constraints.md
- Balances security (short access) with UX (longer refresh)
- Industry standard

**Alternatives Considered:**
- Longer access tokens: Less secure
- Shorter refresh tokens: Poor UX, frequent re-logins

**Date:** 2024-01-15
```

## Session Completion & Archiving

### When Task is Complete

**1. Final Update to current-session.md:**

```markdown
## Summary

**Status:** ✅ Completed

**What Was Accomplished:**
- Implemented refresh token functionality
- Added /api/auth/refresh endpoint
- Updated authentication middleware
- All tests passing (23/23)
- Documentation updated

**Files Modified:**
- src/auth/login.ts - Added refresh token generation
- src/middleware/auth.ts - Added refresh validation
- src/routes/auth.ts - Added /refresh endpoint
- tests/auth.test.ts - Updated test fixtures

**Files Created:**
- None

**Key Decisions:**
- Used httpOnly cookies for refresh tokens (see decisions.md)
- 15min access / 7day refresh expiration

**Follow-up Needed:**
- None - feature is complete

**Context Final:** 60%
```

**2. Archive the Session:**

```bash
# Move session doc to archive with descriptive name
DATE=$(date +%Y-%m-%d)
mv .claude/work/current-session.md .claude/sessions/archive/${DATE}-refresh-tokens.md

# Move decisions doc into archive
cat .claude/work/decisions.md >> .claude/sessions/archive/${DATE}-refresh-tokens.md
rm .claude/work/decisions.md

# Clean up work directory
# (ready for next task)
```

**3. Update Project Documentation if Patterns Emerged:**

If this task revealed new project patterns:

```markdown
# Add to .claude/project/patterns.md

## Authentication Pattern: Refresh Tokens

We use httpOnly cookies for refresh tokens:
- Access token: 15min lifetime
- Refresh token: 7day lifetime
- Stored in httpOnly cookie (not localStorage)
- CSRF protection required

Example: See src/auth/login.ts generateTokenPair()
```

### Archive File Structure

**Archived session should include:**

```markdown
# Session: Implement Refresh Tokens

**Date:** 2024-01-15
**Status:** ✅ Completed
**Context Used:** 60%

## Task
Add refresh token functionality to authentication system

## Approach Taken
1. Explored existing auth code (Explore agent)
2. Planned implementation (JWT with httpOnly cookies)
3. Implemented token generation
4. Added refresh endpoint
5. Updated tests
6. Verified security

## Progress Log
[... all the during-work updates ...]

## Final Summary
[... what was accomplished ...]

## Decisions Made

### Refresh Token Storage
**Decision:** Store in httpOnly cookies
**Reasoning:** [...]
[... all decisions from decisions.md ...]

## Files Modified
- src/auth/login.ts
- src/middleware/auth.ts
- src/routes/auth.ts
- tests/auth.test.ts

## Follow-up
None - feature complete

---
**Archived:** 2024-01-15
**Session Duration:** 2 hours
**Final Context:** 60%
```

## Multiple Tasks Management

### Switching Between Tasks

**NEVER work on multiple tasks in one session.**

**Instead:**

```
Task A (in progress):
1. Update current-session.md with current state
2. Archive to .claude/sessions/archive/2024-01-15-task-a-PARTIAL.md
3. Note: "Partial - In Progress"

Task B (new task):
1. Start fresh current-session.md
2. Clean context
3. Work on Task B
4. Complete and archive

Resume Task A:
1. Read archived partial session
2. Start new current-session.md
3. Reference previous session
4. Continue work
```

### Task Dependencies

**If Task B depends on Task A:**

```markdown
# Session: Task B

## Dependencies
- Task A must be complete first
- See: .claude/sessions/archive/2024-01-15-task-a.md
- Key finding from Task A: Auth uses httpOnly cookies

## Task Description
[...]
```

## Documentation Types

### 1. Session Documentation (Required)

**Where:** `.claude/work/current-session.md`
**When:** Every session
**Purpose:** Track progress, decisions, context
**Archive:** When task complete

### 2. Decision Documentation (As Needed)

**Where:** `.claude/work/decisions.md`
**When:** Making non-obvious choices
**Purpose:** Record reasoning for future reference
**Archive:** Append to session doc

### 3. Project Pattern Documentation (When Patterns Emerge)

**Where:** `.claude/project/patterns.md`
**When:** Discover new project patterns
**Purpose:** Guide future work
**Archive:** Never - living document

### 4. Investigation Documentation (For Research Tasks)

**Where:** `.claude/work/investigation-{topic}.md`
**When:** Research/exploration tasks
**Purpose:** Document findings
**Archive:** When research complete

## Session Templates

### Standard Feature Implementation

```markdown
# Session: [Feature Name]

**Date:** [YYYY-MM-DD]
**Status:** In Progress
**Type:** Feature Implementation

## Task
[Description]

## Exploration
- [ ] Understand existing code
- [ ] Identify files to modify
- [ ] Review similar implementations

## Design
- [ ] Design approach
- [ ] Identify files to create/modify
- [ ] Plan implementation steps

## Implementation
- [ ] Step 1
- [ ] Step 2
- [ ] Tests
- [ ] Documentation

## Progress Log
[Updates as you go]

## Summary
[When complete]
```

### Bug Fix Template

```markdown
# Session: Fix [Bug Description]

**Date:** [YYYY-MM-DD]
**Status:** In Progress
**Type:** Bug Fix

## Bug Description
[What's wrong]

## Investigation
- [ ] Reproduce bug
- [ ] Find root cause
- [ ] Identify affected files

## Fix
- [ ] Implement fix
- [ ] Add regression test
- [ ] Verify fix works

## Progress Log
[Updates]

## Summary
- Root cause: [...]
- Fix: [...]
- Files modified: [...]
```

### Research Template

```markdown
# Research: [Topic]

**Date:** [YYYY-MM-DD]
**Status:** In Progress
**Type:** Research

## Question
[What are you investigating]

## Approach
- [ ] Search codebase
- [ ] Review documentation
- [ ] Test hypotheses

## Findings
[Document as you discover]

## Conclusion
[Final answer to question]

## Recommendations
[If applicable]
```

## Best Practices

### DO:

✅ Update session doc after every major step
✅ Document WHY decisions were made
✅ Archive immediately when task complete
✅ Start fresh for each new task
✅ Reference previous sessions if needed
✅ Keep session docs concise but complete

### DON'T:

❌ Work without session documentation
❌ Mix multiple tasks in one session
❌ Forget to archive completed work
❌ Delete archives (keep for reference)
❌ Document obvious things (focus on decisions)
❌ Let session docs get stale

## Archiving Checklist

Before starting new task:

- [ ] Current task documented in current-session.md
- [ ] All decisions recorded
- [ ] Final summary written
- [ ] Status marked as complete
- [ ] Moved to archive with descriptive name
- [ ] Work directory cleaned
- [ ] Project patterns updated if needed
- [ ] Ready for fresh start

## Recovery from Confusion

**If you realize you're confused or mixing tasks:**

1. **STOP immediately**
2. **Review current-session.md** - what were you working on?
3. **Check context level** - is it too full?
4. **Archive current state** - even if incomplete
5. **Start fresh** - new session, clean context
6. **Reference archive** - if continuing same task

## Example Session Lifecycle

### Day 1: Start Feature

```
09:00 - Create current-session.md
09:05 - Use Explore agent to find relevant code
09:20 - Document findings in session
09:30 - Use Plan agent to design approach
10:00 - Start implementation
11:30 - Document progress (50% done)
12:00 - Archive session (partial - to continue tomorrow)
```

**Archive as:** `2024-01-15-user-profile-PARTIAL.md`

### Day 2: Continue Feature

```
09:00 - Create new current-session.md
09:05 - Read yesterday's archive
09:10 - Continue implementation
11:00 - Complete feature
11:30 - All tests passing
11:45 - Final summary
12:00 - Archive session (complete)
```

**Archive as:** `2024-01-16-user-profile-COMPLETE.md`

## Remember

**Documentation is about:**
1. **Tracking progress** - Know what you've done
2. **Recording decisions** - Remember why
3. **Managing context** - Compress information
4. **Enabling resumption** - Pick up where you left off
5. **Preventing confusion** - One task at a time

**The goal:** Clear documentation, clean archives, fresh starts for each task.
