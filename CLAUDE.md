# Claude Code Autonomous Operations Guide

> **This file is automatically discovered by Claude Code. All other documentation is imported from here.**

## Critical: How This Works

Claude Code **ONLY** automatically discovers `CLAUDE.md` files - it does NOT look in `/docs` or other directories.

This file imports all operational protocols using `@path/to/file.md` syntax:

```
@.claude/protocols/agent-usage.md          # When to use Task agents vs direct work
@.claude/protocols/context-management.md   # Managing context windows effectively
@.claude/protocols/documentation.md        # Creating and archiving documentation
@.claude/protocols/gamification.md         # Achievement tracking & scoring system
@.claude/protocols/good-girl-points.md     # GGP: Earn trust, maintain quality
```

## Autonomous Session Workflow

**Gamification and GGP tracking happen AUTOMATICALLY. No user intervention required.**

Every Claude Code session follows this workflow with automatic scoring:

### 1. Session Start (Auto-Initialize)
- [ ] Read this CLAUDE.md file (you're doing this now)
- [ ] **AUTO: Initialize GGP = +50** (Good Standing) - tracked internally
- [ ] **AUTO: Initialize Score = 0/100** - updated automatically during work
- [ ] Load current project context from `.claude/sessions/current/`
- [ ] Review any archived sessions in `.claude/sessions/archive/`
- [ ] Check for in-progress work in `.claude/work/`

### 2. During Work (Auto-Track Everything)
- [ ] Follow agent usage protocol (when to use Explore, Plan, etc.)
- [ ] Manage context windows (use agents to save context)
- [ ] **AUTO: GGP updates** - Earn/lose points based on actions (runs in background)
  - Quality code written → +5-10 GGP automatically
  - Tests added → +10 GGP automatically
  - Linter warning → -5 GGP automatically
  - Security issue → -20 GGP automatically
- [ ] **AUTO: Redemption prompts** - If GGP < +50, suggest specific fixes automatically
- [ ] **AUTO: Score subtasks** - Assign confidence (0-100) to each completed subtask
- [ ] Document decisions in `.claude/work/current-session.md`
- [ ] Create task-specific documentation as needed

### 3. Session End / Task Complete (Auto-Report)
- [ ] **AUTO: Generate final score** - Calculated from all actions taken
- [ ] **AUTO: Generate final GGP balance** - Sum of all earned/lost points
- [ ] **AUTO: Award achievements** - Based on score and GGP standing
- [ ] **AUTO: Display performance report** - Bronze/Silver/Gold/Platinum level
- [ ] Create summary in `.claude/work/current-session.md`
- [ ] Archive session to `.claude/sessions/archive/{date}-{task}.md`
- [ ] Clean up `.claude/work/` for next session
- [ ] Update project-specific documentation if patterns emerged

**Templates in `.claude/work/` are OPTIONAL for user reference only. Not required for autonomous operation.**

## Achievement System

**Track your success with 4 performance levels:**

- 🥉 **Bronze (50-59)**: Basic completion - all todos done, no blockers
- 🥈 **Silver (60-74)**: Quality work - + tests, no warnings, documented
- 🥇 **Gold (75-89)**: Excellence - + >80% coverage, quality-checker PASS
- 🏆 **Platinum (90-100)**: Mastery - + zero issues, optimized, perfect execution

**Scoring Quick Reference:**
```
Base (50 pts):  Todos ✓, No blocks ✓, No TODOs ✓, Errors handled ✓, Documented ✓
Quality (30):   No warnings ✓, Tests pass ✓, Docs complete ✓
Excellence (20): quality-checker PASS ✓, Context <70% ✓, Agents used well ✓, Patterns ✓

Total: 100 points possible
```

**See:** @.claude/protocols/gamification.md for full scoring system and achievements.

## Good Girl Points (GGP)

**Earn trust and maintain quality through immediate feedback.**

```
🌟 Starting Balance: +50 GGP (Good Standing)

Earn Points (+GGP):
  +5-10:  Quality code, error handling, logging
  +10-15: Tests, documentation, best practices
  +15-20: Patterns followed, agent usage, quality-checker PASS
  +20-50: Excellence, Platinum level, perfect execution

Lose Points (-GGP):
  -5:  Linter warnings, console.log, magic numbers
  -10: TODO markers, empty catches, missing tests
  -20: Security issues (SQL injection, XSS)
  -50: Major violations (bypassing linter, ignoring critical issues)

Standings:
  🌟 +100:  Excellent (1.5x bonus, all achievements unlocked)
  ✅ +50-99: Good (normal operation)
  ⚠️ +1-49:  Cautious (redemption recommended)
  🚨 ≤0:     Poor (redemption REQUIRED before continuing)

Redemption:
  💪 Quick: +10 GGP (fix one issue)
  💪 Standard: +25 GGP (quality improvement)
  💪 Full: +50 GGP (achieve excellence)
  💪 Extra: +75 GGP (go above and beyond)
```

**Track in:** `.claude/work/.ggp-tracker-template.md` (optional reference)

**See:** @.claude/protocols/good-girl-points.md for complete GGP system.

## Quick Decision Trees

### Should I use an agent?

We have **built-in Task agents** (Explore, Plan, general-purpose) and **custom specialized agents** (code-explorer, code-architect, implementation-helper, error-resolver, test-writer, doc-writer, quality-checker).

**Use built-in Explore agent when:**
- Quick search for patterns/keywords
- Finding files efficiently
- Context window getting full (>70%)
- Task: "Where is X in the code?"

**Use custom code-explorer agent when:**
- Need deep feature analysis (not just search)
- Tracing execution flows
- Understanding architecture patterns
- Task: "How does authentication work?"

**Use built-in Plan agent when:**
- Need high-level strategic plan
- Breaking down large tasks
- Deciding between approaches

**Use custom code-architect agent when:**
- Need detailed blueprint (files, interfaces, data flow)
- Complex features (>50 lines)
- Architectural decisions required
- Task: "Design the authentication system"

**Use custom implementation-helper agent when:**
- Very complex implementation (>100 lines)
- Multi-phase implementation needed
- Previous attempts failed
- Want to prevent incomplete code

**Use custom error-resolver agent when:**
- Same error occurs 2+ times
- "Coding in circles"
- Complex debugging needed
- Task: "Why does this keep failing?"

**Use custom test-writer agent when:**
- New feature needs comprehensive tests
- Need >80% coverage
- Complex testing scenarios

**Use custom doc-writer agent when:**
- API documentation needed
- Feature guide required
- Complex system needs explaining

**Use custom quality-checker agent when:**
- Before committing
- After complex implementation
- OR just run: /quality-check

**Use general-purpose agent when:**
- Multi-step research task
- Uncertain scope
- Multiple searches needed

**Work directly when:**
- Simple, well-defined task (<30 lines)
- Know exactly where code goes
- Context window manageable (<50%)
- Quick fix needed

### Is my context window getting full?

**Signs you need to use agents:**
- Conversation history >20 messages
- Read >10 files already
- Feeling uncertain about what you read earlier
- Need to search again for something

**Action:**
- Launch Explore agent to search
- Summarize findings in session doc
- Continue with focused context

## Project-Specific Context

**Note:** These files can import your existing documentation or supplement it.

@.claude/project/architecture.md
@.claude/project/constraints.md
@.claude/project/patterns.md

**Common existing docs you can import:**
- README.md (project overview)
- docs/architecture.md or ARCHITECTURE.md
- docs/api.md or API.md
- CONTRIBUTING.md (conventions)
- package.json (dependencies, scripts)

## Built-in Quality Linting

**Automatic mistake detection:**
- PreToolUse hook validates before Write/Edit
- Blocks security issues automatically
- Warns about incomplete implementations
- Run `/quality-check` for comprehensive analysis

See: @.claude/docs/linter/README.md

## Protocols (Read When Needed)

### Core Protocols
@.claude/protocols/agent-usage.md
@.claude/protocols/context-management.md
@.claude/protocols/documentation.md
@.claude/protocols/gamification.md
@.claude/protocols/good-girl-points.md

### Reference
@.claude/guides/complete-examples.md
@.claude/guides/anti-patterns.md
@.claude/guides/pitfalls.md

---

## Directory Structure

```
project/
├── CLAUDE.md                              # This file (auto-discovered)
├── .claude/
│   ├── protocols/                         # How to work (universal)
│   │   ├── agent-usage.md                 # When to use agents
│   │   ├── context-management.md          # Managing context
│   │   ├── implementation.md              # Implementation workflow
│   │   ├── error-handling.md              # Error resolution
│   │   ├── documentation.md               # Doc creation/archiving
│   │   ├── research.md                    # Research workflow
│   │   └── verification.md                # Completion verification
│   ├── guides/                            # Reference material
│   │   ├── complete-examples.md           # What "done" looks like
│   │   ├── anti-patterns.md               # What NOT to do
│   │   └── pitfalls.md                    # Known failure modes
│   ├── project/                           # Project-specific (customize)
│   │   ├── architecture.md                # System design
│   │   ├── constraints.md                 # Hard rules
│   │   └── patterns.md                    # Project patterns
│   ├── work/                              # Current session work
│   │   ├── current-session.md             # Today's work log
│   │   └── decisions.md                   # Decisions made
│   └── sessions/                          # Session management
│       ├── current/                       # Current session state
│       │   └── context.md                 # Current context
│       └── archive/                       # Completed sessions
│           ├── 2024-01-15-auth-feature.md
│           └── 2024-01-16-bug-fix.md
```

## Autonomous Operation Checklist

Before starting ANY task:

**1. Assess Complexity (10 seconds)**
- [ ] Simple task (<30 lines)? → Work directly
- [ ] Complex task (>30 lines)? → Use Plan agent
- [ ] Don't know codebase? → Use Explore agent

**2. Check Context (5 seconds)**
- [ ] Context window <50%? → Can work directly
- [ ] Context window >70%? → Use agents to search
- [ ] Need to explore? → Use Explore agent

**3. Load Project Context (30 seconds)**
- [ ] Read architecture.md (system design)
- [ ] Read constraints.md (hard rules)
- [ ] Check sessions/current/ (in-progress work)

**4. Document As You Go**
- [ ] Update work/current-session.md with decisions
- [ ] Create task-specific docs if needed
- [ ] Archive when complete

**5. Use Verification Protocol**
- [ ] Follow verification.md before marking complete
- [ ] Look back through work for evidence
- [ ] No TODOs, no stubs, no "for now"

## Emergency Recovery

If you're:
- Going in circles (same error 2+ times)
- Context window is full
- Confused about task
- Multiple tasks mixed up

**STOP and:**
1. Archive current session immediately
2. Create fresh session in sessions/archive/
3. Re-read CLAUDE.md (this file)
4. Start with Explore agent or error-resolver to re-orient

## Custom Specialized Agents

We have 7 custom agents for autonomous operation:

1. **code-explorer** - Deep codebase analysis, trace execution flows
2. **code-architect** - Design complete architecture blueprints
3. **implementation-helper** - Step-by-step implementation guidance
4. **error-resolver** - Systematic debugging and root cause analysis
5. **test-writer** - Write comprehensive test suites
6. **doc-writer** - Write clear documentation
7. **quality-checker** - Code quality review (also via /quality-check command)

**Full guide:** @.claude/guides/agent-guide.md

**When to use:** See decision trees above and @.claude/protocols/agent-usage.md

**Example workflows:**
- New feature: code-explorer → code-architect → implementation-helper → test-writer → doc-writer → quality-checker
- Bug fix: error-resolver → test-writer (add regression test) → fix → quality-checker
- Refactoring: test-writer (ensure tests exist) → code-explorer → code-architect → implement → quality-checker

---

**Last Updated:** Auto-generated
**Session ID:** Will be set by Claude Code
**Current Task:** Check .claude/work/current-session.md
