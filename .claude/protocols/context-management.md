# Context Window Management Protocol

**Critical for autonomous operation:** Manage context to avoid overflow and maintain focus.

## Core Principle

**Context window is precious. Use agents to search externally. Only load what you need when you need it.**

## Understanding Context Usage

### What Fills Context

1. **Conversation history** - Every message adds to context
2. **File reads** - Reading files (especially large ones)
3. **Tool outputs** - Grep results, bash outputs, etc.
4. **Imported documentation** - All the @imports from CLAUDE.md

### Context Capacity

- **Working comfortably:** <50% full
- **Getting full:** 50-70%
- **Critical:** >70%
- **Emergency:** >90%

## Strategies to Save Context

### 1. Use Agents for Exploration

**Instead of:** Reading 10 files to find something
**Do:** Launch Explore agent, get summary, read only what's needed

```
❌ Bad (fills context):
1. Read src/components/Auth.tsx
2. Read src/components/Login.tsx
3. Read src/components/Signup.tsx
4. Read src/services/auth.ts
5. Read src/utils/token.ts
... (context now 60% full)

✅ Good (saves context):
1. Launch Explore agent: "Find all auth-related code"
2. Get summary (small context cost)
3. Read only the 2 files I actually need to modify
... (context only 20% full)
```

### 2. Incremental Information Retrieval

**Load information only when needed:**

```
Phase 1: Explore (via agent)
- Get high-level understanding
- Identify relevant files

Phase 2: Plan (via agent if complex)
- Design approach
- List specific files needed

Phase 3: Implement (direct)
- Read ONLY the files from plan
- Implement step by step
- Test as you go
```

### 3. Summarize and Document

**When context is building up:**

1. Summarize current findings in `.claude/work/current-session.md`
2. Write down key decisions
3. This creates a compressed reference you can re-read

**Example:**
```markdown
## Authentication Flow (Discovered)

After exploring, found that:
- Login: `src/components/Login.tsx` (lines 45-67)
- Token generation: `src/services/auth.ts` (generateToken function)
- Middleware: `src/middleware/auth.ts` (validateToken function)
- Storage: localStorage with key 'auth_token'

To add refresh tokens, modify generateToken() to also create refreshToken.
```

Now you can reference THIS instead of re-reading all those files.

### 4. Parallel Processing

**Launch multiple agents simultaneously** to gather information without sequential context buildup:

```
Instead of:
1. Explore components (wait)
2. Explore services (wait)
3. Explore tests (wait)

Do:
1. Launch 3 Explore agents in parallel
2. Get all results at once
3. Synthesize findings
```

### 5. Confidence-Based Filtering

**Only load high-confidence information:**

When researching, focus on:
- Most relevant files (not all files)
- Key functions (not entire codebase)
- Current implementation (not historical)

### 6. Avoid Re-reading

**Keep track of what you've learned:**

- Document findings in `.claude/work/current-session.md`
- Reference your notes instead of re-reading
- Use agents if you need to search again

## Context Monitoring

### Check Context Level

**Signs context is filling up:**
- Feeling uncertain about earlier information
- Need to re-read things
- Conversation history >20 messages
- Have read >10 files
- Getting confused about task

**Action at each threshold:**

**<50%:** Work normally
- Read files as needed
- Work directly on tasks
- Document key findings

**50-70%:** Be selective
- Use agents for new searches
- Summarize what you've learned
- Only read files you'll modify

**>70%:** Emergency mode
- STOP reading new files
- Use agents for ALL searches
- Summarize immediately
- Consider archiving session

**>90%:** Archive and restart
- Save current work to `.claude/sessions/archive/`
- Create fresh session
- Load only essential context

## Session Management

### Current Session

**Document in `.claude/work/current-session.md`:**

```markdown
# Current Session: Add User Profile Editing

## Task
Add user profile editing feature

## Progress
- [x] Explored existing profile code (src/components/Profile.tsx)
- [x] Planned implementation (see decisions.md)
- [ ] Implementing edit form
- [ ] Adding API endpoint
- [ ] Adding tests

## Key Findings
- Profile display: src/components/Profile.tsx
- User API: src/services/api/users.ts
- Form pattern: Use Formik like in Settings.tsx

## Next Steps
1. Create ProfileEdit component
2. Add PUT /api/user/profile endpoint
3. Add form validation

## Context Usage: ~45%
```

### Archive When Done

**Move to `.claude/sessions/archive/{date}-{task}.md`:**

```bash
# Session complete, archive it
mv .claude/work/current-session.md .claude/sessions/archive/2024-01-15-profile-editing.md

# Clean up for next session
rm .claude/work/decisions.md
```

### Multiple Tasks

**One task at a time:**

If working on multiple tasks:
1. Complete Task A
2. Archive Task A session
3. Start fresh for Task B

**DON'T mix tasks in one session** - leads to confusion

## Workflow by Context Level

### Fresh Start (<30%)

**You can:**
- Read multiple files
- Explore broadly
- Work directly
- Take time to understand

**Strategy:**
- Get oriented
- Understand codebase
- Plan approach

### Getting Full (30-50%)

**You should:**
- Be more selective with reads
- Start using agents
- Document findings
- Focus on task

**Strategy:**
- Know what you're looking for
- Read only necessary files
- Summarize as you go

### Approaching Limit (50-70%)

**You must:**
- Use agents for ALL searches
- Summarize frequently
- Only read files you'll edit
- Stay focused

**Strategy:**
- Work in focused bursts
- Document everything
- Avoid exploration
- Implement what's planned

### Critical (>70%)

**Emergency actions:**
- STOP reading files
- Summarize current state
- Use agents exclusively
- Consider archiving

**Strategy:**
- Finish current piece
- Archive session
- Start fresh

## Patterns for Long Tasks

### Multi-Day Feature

**Day 1:**
- Explore codebase (use agents)
- Plan implementation
- Document plan
- Archive session

**Day 2:**
- Load previous session summary
- Implement part 1
- Document progress
- Archive session

**Day 3:**
- Load previous session summary
- Implement part 2
- Complete & test
- Final archive

**Each session starts fresh** - context never gets full

### Complex Investigation

**Phase 1: Discovery (use agent)**
```
Launch General-Purpose agent:
"Investigate authentication flow. Return detailed findings."

Get summary (minimal context)
Document findings
```

**Phase 2: Design (use agent)**
```
Launch Plan agent:
"Based on findings, design refresh token implementation."

Get plan (minimal context)
Review and approve
```

**Phase 3: Implement (direct)**
```
Read only specific files from plan
Implement step by step
Context stays low because you know exactly what to do
```

## Anti-Patterns

### ❌ Don't: Read everything upfront

```
❌ Bad:
Read 20 files to "understand the codebase"
... context now 80% full before even starting

✅ Good:
Use Explore agent to understand codebase
Get summary
Read only files you'll modify
```

### ❌ Don't: Keep working when context is full

```
❌ Bad:
Context at 85%, keep adding more files
Eventually hit limit, lose focus

✅ Good:
Context at 75%, STOP
Summarize current work
Archive and start fresh
```

### ❌ Don't: Re-read files

```
❌ Bad:
Read file on message 5
Forget details
Read same file again on message 25
(Doubles context cost)

✅ Good:
Read file on message 5
Summarize key points in session doc
Reference your summary later
```

### ❌ Don't: Mix multiple tasks

```
❌ Bad:
Work on auth feature
Switch to bug fix
Back to auth
Back to bug
(Context full of both tasks, confused)

✅ Good:
Complete auth feature
Archive session
Start fresh for bug fix
```

## Tools for Context Management

### 1. Session Documentation

**`.claude/work/current-session.md`**
- Compress findings into summary
- Reference instead of re-reading
- Track progress

### 2. Decision Log

**`.claude/work/decisions.md`**
- Document key decisions
- Why choices were made
- Trade-offs considered

### 3. Archive

**`.claude/sessions/archive/`**
- Completed sessions
- Reference if needed
- Prevents mixing tasks

### 4. Agents

**Explore, Plan, General-Purpose**
- Search externally (saves your context)
- Get summaries instead of raw data
- Parallelize information gathering

## Measuring Success

**Context management is working if:**
- Context never exceeds 70%
- Can complete complex tasks without hitting limits
- Clear what you're working on at any time
- Not re-reading files
- Sessions are focused and complete

**Context management needs improvement if:**
- Frequently hitting 80%+ context
- Re-reading same files multiple times
- Forgetting what you read earlier
- Tasks bleeding into each other
- Getting confused mid-task

## Quick Reference

| Context Level | Action | Tools |
|---------------|--------|-------|
| <30% | Work freely | Direct work |
| 30-50% | Be selective | Start using agents |
| 50-70% | Use agents | Document frequently |
| 70-85% | Emergency mode | Agents only, summarize |
| >85% | Archive & restart | Save and start fresh |

## Remember

**Context management is about:**
1. **Using agents** - They search externally
2. **Loading incrementally** - Only what you need
3. **Documenting** - Compress information
4. **Archiving** - Start fresh when needed
5. **Focusing** - One task at a time

**The goal:** Never hit context limits, stay focused, complete tasks efficiently.
