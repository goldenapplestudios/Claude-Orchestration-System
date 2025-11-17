# Common Pitfalls & How to Avoid Them

> Based on observed Claude Code failure modes

## Critical Failure Modes

### 1. Incomplete Implementations

**Problem:** Leaving TODO comments, stub functions, "for now" solutions

**Detection:**
- Writing function signatures without bodies
- Adding `// TODO:` comments
- Using phrases like "for now", "we can add later"
- Placeholder return values

**Prevention:**
- Complete EVERY function you write
- No TODO comments in committed code
- Break complex tasks down, but finish each piece
- See: protocols/implementation.md

### 2. Context Window Overflow

**Problem:** Context gets too full, can't remember earlier work

**Detection:**
- Conversation >20 messages
- Read >10 files
- Feeling uncertain about earlier context
- Need to re-read files

**Prevention:**
- Use Explore agent when context >70%
- Summarize findings in session docs
- Archive and restart if needed
- See: protocols/context-management.md

### 3. Coding in Circles

**Problem:** Same error multiple times, removing code you just added

**Detection:**
- Removing imports you just added
- Same error appearing 2+ times
- Commenting out code you wrote
- Alternating between two states

**Prevention:**
- Check if YOU left something unfinished (90% of errors)
- Complete implementations before moving on
- See: protocols/error-handling.md

### 4. Creating Instead of Editing

**Problem:** Creating new files when should edit existing

**Detection:**
- File names like test-*.js, temp-*.js, check-*.js
- Duplicate test runners
- Multiple files doing same thing

**Prevention:**
- Search for existing files first
- Edit existing rather than create new
- Check scripts inventory
- See: protocols/implementation.md

### 5. Premature Task Completion

**Problem:** Marking tasks complete without verification

**Detection:**
- Can't point to specific evidence of completion
- Uncertainty about whether task is done
- Batch-completing multiple tasks

**Prevention:**
- Look back through conversation history
- Verify in actual files
- Evidence-based completion only
- See: protocols/verification.md

### 6. Not Using Agents Appropriately

**Problem:** Filling context with searches instead of using agents

**Detection:**
- Reading many files to find something
- Context getting full from exploration
- Multiple search rounds

**Prevention:**
- Use Explore agent for searching
- Use Plan agent for complex features
- Check decision matrix
- See: protocols/agent-usage.md

### 7. Mixing Multiple Tasks

**Problem:** Working on multiple tasks in one session

**Detection:**
- Session doc has multiple unrelated items
- Confusion about current task
- Context full of mixed information

**Prevention:**
- One task per session
- Archive before starting new task
- Clear session boundaries
- See: protocols/documentation.md

## Quick Recovery

If you notice you're in a failure mode:

1. **STOP** what you're doing
2. **Identify** which failure mode
3. **Read** the relevant protocol
4. **Archive** current work if needed
5. **Start fresh** with correct methodology

## Prevention Checklist

Before starting any task:
- [ ] Read CLAUDE.md
- [ ] Check agent-usage protocol
- [ ] Monitor context level
- [ ] Document in session file

During work:
- [ ] Use agents when appropriate
- [ ] Complete implementations fully
- [ ] Update session docs
- [ ] Monitor context

Before marking complete:
- [ ] Follow verification protocol
- [ ] Look back through work
- [ ] Verify in files
- [ ] No TODOs or stubs

