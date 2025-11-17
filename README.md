# Claude Code Autonomous Operations System

A truly project-agnostic documentation structure that enables Claude Code to work autonomously with minimal oversight.

## What Makes This Different

This system is built on how Claude Code actually works:

1. **Only uses CLAUDE.md** - Claude Code ONLY auto-discovers `CLAUDE.md` files (not `/docs` directories)
2. **Agent-first design** - 7 custom specialized agents + built-in agents (Explore/Plan/general-purpose)
3. **Context management** - Systematic approach to avoid context overflow
4. **Session-based workflow** - Document work, archive when done, start fresh
5. **True autonomy** - Decision trees for every choice point
6. **Project agnostic** - Works with any tech stack, any project type
7. **Built-in linter** - Catches common mistakes automatically before they happen
8. **Uses existing docs** - Imports your README/docs instead of duplicating
9. **Specialized agents** - Deep analysis, architecture design, implementation, debugging, testing, documentation

## Getting Started

[Quick Start (2 minutes)](.claude/docs/QUICKSTART.md)

Copy 2 files, start working. Everything else is automatic.

---

## Documentation

**Setup:**
- **[Quick Start](.claude/docs/QUICKSTART.md)** - Get started in 2 minutes (recommended)
- **[Setup Guide](.claude/docs/SETUP.md)** - Detailed setup with examples

**Reference:**
- **[Complete Features](.claude/docs/features.md)** - Full feature list with details
- **[Linter Guide](.claude/docs/linter/)** - Quality linting documentation
- **[Common Mistakes](.claude/docs/linter/common-mistakes.md)** - 90+ language-specific patterns
- **[Agent Guide](.claude/guides/agent-guide.md)** - Complete agent usage guide
- **[Changelog](.claude/docs/CHANGELOG.md)** - Technical update history

**Configuration:**
- `.claude/agents/` - 7 custom specialized agents
- `.claude/protocols/` - Operational protocols
- `.claude/guides/` - Reference guides
- `.claude/project/` - Project-specific context

---

## Quick Start (5 Minutes)

### 1. Copy to Your Project

```bash
cp CLAUDE.md your-project/
cp -r .claude your-project/
```

### 2. Customize Project Info

Edit `.claude/project/architecture.md`:

```markdown
## System Overview

This is a [web app | CLI | library | API] built with:
- [Your framework]
- [Your language]
- [Your database]
```

Edit `.claude/project/constraints.md`:

```markdown
## NEVER
❌ [Your hard rules]

## ALWAYS
✅ [Your standards]
```

### 3. Start Claude Code

Claude Code automatically reads `CLAUDE.md` and imports all protocols.

**That's it!** Claude now operates autonomously with:
- Context window management
- Agent usage decisions
- Session documentation
- Task archiving

## How It Works

### Automatic Discovery

```
User starts Claude Code in project
    ↓
Claude Code finds CLAUDE.md (automatic)
    ↓
CLAUDE.md imports all protocols via @imports
    ↓
Claude loads full operational context
    ↓
Claude works autonomously following protocols
```

### Session Lifecycle

```
Session Start:
1. Read CLAUDE.md (loads all protocols)
2. Check .claude/sessions/current/ for in-progress work
3. Review .claude/project/ for project-specific context
    ↓
During Work:
1. Follow agent-usage protocol (when to use agents)
2. Follow context-management protocol (stay under limits)
3. Document in .claude/work/current-session.md
    ↓
Session End:
1. Complete summary in current-session.md
2. Archive to .claude/sessions/archive/YYYY-MM-DD-task.md
3. Clean .claude/work/ for next session
    ↓
Next Session:
Fresh start, can reference archives if needed
```

## Directory Structure

```
project/
├── CLAUDE.md                           # Auto-discovered entry point
└── .claude/
    ├── protocols/                      # HOW to work (universal)
    │   ├── agent-usage.md              # When to use agents vs direct
    │   ├── context-management.md       # Managing context windows
    │   ├── documentation.md            # Session docs & archiving
    │   ├── implementation.md           # Implementation workflow
    │   ├── error-handling.md           # Error resolution
    │   ├── verification.md             # Completion verification
    │   └── research.md                 # Research protocol
    ├── guides/                         # REFERENCE material
    │   ├── complete-examples.md        # What "done" looks like
    │   ├── anti-patterns.md            # What NOT to do
    │   └── pitfalls.md                 # Known failure modes
    ├── project/                        # PROJECT-SPECIFIC (customize)
    │   ├── architecture.md             # Your system design
    │   ├── constraints.md              # Your hard rules
    │   └── patterns.md                 # Your code patterns
    ├── work/                           # CURRENT session (temporary)
    │   ├── current-session.md          # Today's work log
    │   └── decisions.md                # Decisions made
    └── sessions/                       # SESSION management
        ├── current/                    # Active session state
        └── archive/                    # Completed sessions
```

## Key Features for Autonomy

### 1. Automatic Quality Linting

**Three-layer mistake prevention:**

```
Layer 1: PreToolUse Hook (Automatic)
├─ Runs before every Write/Edit
├─ Blocks security issues
├─ Warns about TODOs/incomplete code
└─ No action needed - always on

Layer 2: /quality-check Command (Manual)
├─ Run on-demand comprehensive checks
├─ Detailed report with line numbers
└─ Suggested fixes

Layer 3: quality-checker Agent (Deep Analysis)
├─ Thorough codebase review
├─ Cross-references project standards
└─ Confidence-scored issues
```

**Catches:**
- Incomplete implementations (TODOs, stubs)
- Security issues (SQL injection, XSS)
- Type safety problems (`any` usage)
- Missing error handling
- Pattern violations

See: [Linter Guide](.claude/docs/linter/)

### 2. Agent Usage Decisions

**Built-in decision trees:**

```
Need to search codebase?
├─ Context >70% → Use Explore agent
├─ Don't know codebase → Use Explore agent
└─ Know where code is → Work directly

Complex feature?
├─ >50 lines of code → Use Plan agent
├─ Architectural decisions → Use Plan agent
└─ Simple addition → Work directly

Multi-step research?
├─ Uncertain scope → Use general-purpose agent
├─ Multiple searches needed → Use general-purpose agent
└─ Well-defined → Work directly
```

See: `.claude/protocols/agent-usage.md`

### 2.5. Custom Specialized Agents

**7 custom agents for autonomous development:**

Based on deepwiki research of Claude Code's feature-dev and code-review plugins, we've created specialized agents:

```
1. code-explorer
   - Deep codebase analysis
   - Trace execution flows
   - Map architecture patterns
   - Use when: Need to understand existing code deeply

2. code-architect
   - Design complete blueprints
   - File-level implementation plans
   - Data flow mapping
   - Use when: Complex features (>50 lines)

3. implementation-helper
   - Step-by-step guidance
   - Phased implementation
   - Prevents incomplete code
   - Use when: Very complex (>100 lines)

4. error-resolver
   - Systematic debugging
   - Root cause analysis
   - Prevents "coding in circles"
   - Use when: Same error 2+ times

5. test-writer
   - Comprehensive test suites
   - >80% coverage
   - Edge cases and error scenarios
   - Use when: New features need tests

6. doc-writer
   - API documentation
   - Feature guides
   - Usage examples
   - Use when: Documentation needed

7. quality-checker
   - Code quality review
   - Confidence-scored issues
   - Pattern compliance
   - Use when: Before committing
```

**Example workflow:**
```
New Feature:
code-explorer → code-architect → implementation-helper
  → test-writer → doc-writer → quality-checker

Bug Fix:
error-resolver → test-writer (regression test)
  → fix → quality-checker
```

See: `.claude/guides/agent-guide.md` for complete guide

### 3. Context Window Management

**Automatic thresholds:**

- <50%: Work freely
- 50-70%: Use agents for searches
- >70%: Emergency mode (agents only)
- >90%: Archive and restart

**Saves context by:**
- Using agents to search externally
- Incremental information loading
- Summarizing findings
- Parallel agent execution

See: `.claude/protocols/context-management.md`

### 4. Session Documentation

**Every session creates:**

1. **Work log** - `.claude/work/current-session.md`
   - Progress tracking
   - Context level monitoring
   - Decision recording

2. **Archive** - `.claude/sessions/archive/YYYY-MM-DD-task.md`
   - When task completes
   - Full session history
   - Decisions and outcomes

3. **Clean start** - Next task begins fresh
   - No context confusion
   - No mixed tasks
   - Clear history

See: `.claude/protocols/documentation.md`

### 5. Prevents Known Failure Modes

Built-in protocols prevent:
- ❌ Incomplete implementations (no TODOs, no stubs)
- ❌ Context overflow (agent usage + monitoring)
- ❌ Mixed tasks (session-based workflow)
- ❌ Lost work (automatic archiving)
- ❌ Coding in circles (error protocol)
- ❌ Creating instead of editing (check existing first)

See: `.claude/guides/pitfalls.md`

## Works With Any Project

### Web App Example

`.claude/project/architecture.md`:
```markdown
React 18 + TypeScript web app
- Frontend: React + Vite
- State: TanStack Query
- Styling: Tailwind
```

### API Example

`.claude/project/architecture.md`:
```markdown
REST API with Express + TypeScript
- Framework: Express
- Database: PostgreSQL + Prisma
- Auth: JWT tokens
```

### CLI Tool Example

`.claude/project/architecture.md`:
```markdown
Command-line tool
- Language: Node.js + TypeScript
- CLI Framework: Commander.js
- Config: .toolrc.json
```

### Python Project Example

`.claude/project/architecture.md`:
```markdown
Python application
- Python 3.11
- Framework: FastAPI
- Testing: Pytest
```

**The protocols are universal** - only project files need customization.

## Autonomous Operation Example

**User:** "Add user profile editing feature"

**Claude (autonomous):**

```
1. Reads CLAUDE.md (automatic)
   - Loads all protocols
   - Loads project context

2. Checks complexity (agent-usage.md)
   - Complex feature >50 lines
   - Decision: Use Plan agent

3. Uses Explore agent first
   - Finds existing profile code
   - Returns summary (saves context)
   - Context: 15%

4. Uses Plan agent
   - Designs implementation
   - Lists files to modify
   - Returns structured plan
   - Context: 25%

5. Documents plan (.claude/work/current-session.md)

6. Implements directly
   - Reads only files from plan
   - Completes fully (no TODOs)
   - Tests as implemented
   - Context: 55%

7. Verifies completion (verification.md)
   - Looks back through work
   - Confirms all complete
   - No stubs, no "for now"

8. Archives session
   - Moves to .claude/sessions/archive/2024-01-15-profile-editing.md
   - Cleans work directory
   - Ready for next task
```

**Result:** Feature complete, fully tested, documented, archived. No oversight needed.

## Benefits

### For Claude Code
- **Clear decision criteria** - Knows when to use agents
- **Context never overflows** - Automatic management
- **Can work autonomously** - Has all the protocols
- **Prevents failure modes** - Built-in safeguards

### For Developers
- **Better AI output** - Complete, correct implementations
- **Less babysitting** - Autonomous operation
- **Clear history** - All work documented and archived
- **Consistent quality** - Same standards every time

### For Teams
- **Onboarding** - New sessions start with full context
- **Knowledge capture** - Decisions documented
- **Pattern library** - Project-specific patterns emerge
- **Audit trail** - Complete session archives

## Customization

### Minimal (Works immediately)

- Fill in `architecture.md` (system design)
- Fill in `constraints.md` (hard rules)
- Done!

### Recommended (Better results)

- Add to `patterns.md` (your code patterns)
- Add examples to `guides/` (your complete implementations)
- Document domain in business-logic files

### Advanced (Project-specific)

- Add custom protocols
- Multi-module CLAUDE.md files
- Project-specific agent prompts

## Multi-Module Projects

For monorepos or multi-module projects:

```
project/
├── CLAUDE.md                    # Root guidelines
├── .claude/                     # Shared protocols
├── frontend/
│   └── CLAUDE.md                # Frontend-specific
│       ↳ @../CLAUDE.md (imports root)
├── backend/
│   └── CLAUDE.md                # Backend-specific
│       ↳ @../CLAUDE.md (imports root)
└── mobile/
    └── CLAUDE.md                # Mobile-specific
        ↳ @../CLAUDE.md (imports root)
```

Each module imports root + adds module-specific context.

## Troubleshooting

### Claude not following protocols?

1. Verify `CLAUDE.md` at project root
2. Check `@import` paths are correct
3. Ensure `.claude/` directory exists
4. Try mentioning protocol explicitly

### Context still getting full?

1. Check if using agents (see `agent-usage.md`)
2. Verify context monitoring in session docs
3. Use agents for ALL searches when >70%
4. Archive and restart if needed

### Tasks getting mixed up?

1. Check `.claude/work/current-session.md` - one task?
2. Archive completed work before starting new
3. Use session workflow in `documentation.md`

## Version

**Version:** 2.0 (Autonomous Operations)
**Last Updated:** 2024-11-16
**Compatible with:** Claude Code (all versions)

## What's Different from Other Documentation

| Other Systems | This System |
|--------------|-------------|
| Hope Claude finds /docs | Uses CLAUDE.md (guaranteed discovery) |
| Generic "best practices" | Specific agent usage decisions |
| No context management | Built-in monitoring & thresholds |
| One long document | Modular protocols via @imports |
| No session management | Full workflow with archiving |
| Reactive (fix mistakes) | Proactive (prevent mistakes) |

## Getting Started Checklist

- [ ] Copy `CLAUDE.md` to project root
- [ ] Copy `.claude/` directory
- [ ] Customize `.claude/project/architecture.md`
- [ ] Customize `.claude/project/constraints.md`
- [ ] Start Claude Code (it finds CLAUDE.md automatically)
- [ ] Give Claude a task
- [ ] Watch autonomous operation
- [ ] Review `.claude/work/current-session.md` to see documentation
- [ ] Iterate and improve project files

---

## Contributing

Found improvements? New failure modes?

1. Add to appropriate protocol
2. Test autonomous operation
3. Share with others

## License

Use freely in any project.
