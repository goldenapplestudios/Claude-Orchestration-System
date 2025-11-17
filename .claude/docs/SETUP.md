# Setup Guide

Quick setup for Claude Code autonomous operations.

## For Projects With Existing Documentation

**If your project already has docs (README.md, /docs, CONTRIBUTING.md, etc.):**

### Step 1: Copy Structure (30 seconds)

```bash
cp CLAUDE.md your-project/
cp -r .claude your-project/
```

### Step 2: Point to Existing Docs (2 minutes)

Edit `.claude/project/architecture.md`:

```markdown
# Project Architecture

@../../README.md
@../../docs/architecture.md

## Additional Notes
- [Add only what's NOT in existing docs]
```

Edit `.claude/project/constraints.md`:

```markdown
# Project Constraints

@../../CONTRIBUTING.md
@../../docs/security.md

## Additional Constraints
- [Add only what's NOT in existing docs]
```

### Step 3: Done!

Claude Code will now read:
- Your existing README.md
- Your existing architecture docs
- Your existing contributing guidelines
- The autonomous operation protocols

**No duplication required.**

## For Projects Without Documentation

### Step 1: Copy Structure (30 seconds)

```bash
cp CLAUDE.md your-project/
cp -r .claude your-project/
```

### Step 2: Fill in Basics (3 minutes)

Edit `.claude/project/architecture.md`:

```markdown
# Project Architecture

## System Overview

This is a [web app | API | CLI | library] built with:
- [Framework/Language]
- [Database]
- [Key libraries]

## Directory Structure

\`\`\`
src/
├── [your structure]
\`\`\`
```

Edit `.claude/project/constraints.md`:

```markdown
# Project Constraints

## NEVER
❌ [Your hard rules]

## ALWAYS
✅ [Your standards]
```

### Step 3: Done!

## Examples by Project Type

### Web App (React) - Has Existing Docs

```bash
# Your existing docs:
README.md (setup, overview)
docs/architecture.md (system design)
CONTRIBUTING.md (code style)

# .claude/project/architecture.md:
@../../README.md
@../../docs/architecture.md

## Quick Reference
- Components: src/components/
- State: React Context
- Routing: React Router
```

### API - Has Existing Docs

```bash
# Your existing docs:
README.md
docs/api.md
docs/database-schema.md
CONTRIBUTING.md

# .claude/project/architecture.md:
@../../README.md
@../../docs/api.md
@../../docs/database-schema.md

## Quick Reference
- Controllers: src/controllers/
- Services: src/services/
- Models: Prisma schemas
```

### CLI Tool - Minimal Existing Docs

```bash
# Your existing docs:
README.md (basic usage)

# .claude/project/architecture.md:
@../../README.md

## Additional Context

### Command Structure
- Commands in src/commands/
- Each exports { name, description, action }

### Common Patterns
- Use Commander.js
- Config in .toolrc.json
```

### New Project - No Existing Docs

```bash
# .claude/project/architecture.md:

## System Overview

New TypeScript library for [purpose]

## Tech Stack
- TypeScript 5.0
- Vite (build)
- Vitest (tests)

## Structure
src/
├── index.ts (main export)
└── lib/ (implementation)
```

## Common Existing Documentation to Import

**Root level:**
- `@../../README.md` - Project overview
- `@../../CONTRIBUTING.md` - Guidelines
- `@../../ARCHITECTURE.md` - Design docs
- `@../../API.md` - API reference

**In /docs:**
- `@../../docs/architecture.md`
- `@../../docs/api.md`
- `@../../docs/database-schema.md`
- `@../../docs/security.md`
- `@../../docs/testing.md`

**Reference (don't import):**
- `package.json` - Dependencies, scripts
- `tsconfig.json` - TypeScript config
- `.eslintrc` - Code style

## Verification

After setup, test it:

```bash
# Start Claude Code in your project
cd your-project

# Claude Code will automatically:
1. Find CLAUDE.md
2. Import all protocols
3. Import your existing docs (via @imports)
4. Be ready for autonomous work
```

Ask Claude:
- "What's the architecture of this project?"
  → Should reference your existing docs

- "What are the constraints?"
  → Should reference CONTRIBUTING.md, etc.

- "How should I add a new feature?"
  → Should follow your patterns

## Tips

**DO:**
- Import existing docs with `@path/to/file.md`
- Reference files when appropriate
- Only add what's not already documented
- Keep it DRY (Don't Repeat Yourself)

**DON'T:**
- Duplicate existing documentation
- Recreate what's in README.md
- Copy-paste from other files
- Ignore existing docs

## Multi-Module Projects

For monorepos:

```
project/
├── CLAUDE.md                    # Root
├── .claude/                     # Shared protocols
├── frontend/
│   ├── CLAUDE.md                # Frontend-specific
│   │   └── @../CLAUDE.md        # Imports root
│   └── docs/                    # Frontend docs
├── backend/
│   ├── CLAUDE.md                # Backend-specific
│   │   └── @../CLAUDE.md        # Imports root
│   └── docs/                    # Backend docs
```

Each module's CLAUDE.md:
```markdown
# Frontend Module

@../CLAUDE.md
@./docs/frontend-architecture.md

## Frontend-Specific Notes
...
```

## Troubleshooting

**Claude not reading existing docs?**
- Check `@import` syntax: `@../../path/to/file.md`
- Verify file exists at that path
- Check file is markdown (.md)

**Getting duplicate information?**
- Remove duplicated sections from .claude/project/
- Use references instead of imports
- Only supplement, don't duplicate

**Existing docs not markdown?**
- Reference them instead of importing
- Add summary in .claude/project/ files
- Example: "See api-spec.yaml for full API"

## Next Steps

1. Setup complete? Start using Claude Code
2. As you work, refine .claude/project/ files
3. Add patterns as they emerge
4. Keep documentation updated

**The goal:** Claude Code uses YOUR existing docs + autonomous protocols = minimal setup, maximum effectiveness.
