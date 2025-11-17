# Project Context Files

These files provide Claude Code with project-specific context.

## Philosophy: Don't Duplicate

**If your project already has documentation, USE IT.**

These files should:
1. **Import existing docs** using `@path/to/file.md`
2. **Supplement** with Claude Code-specific context
3. **Reference** existing files when appropriate

## How to Use Existing Documentation

### Option 1: Import Directly

```markdown
# architecture.md

@../../README.md
@../../docs/architecture.md

## Additional Context for Claude Code

Only add what's NOT in existing docs...
```

### Option 2: Reference and Supplement

```markdown
# architecture.md

See main project documentation:
- README.md - System overview
- docs/database.md - Data model
- CONTRIBUTING.md - Development setup

## Claude Code Specific Notes

- Use Explore agent to find component patterns
- State management is in src/store/
- API calls always go through src/services/api/
```

### Option 3: Start Fresh (No Existing Docs)

```markdown
# architecture.md

## System Overview

This is a [your project description]...
```

## Common Existing Documentation Locations

Your project might already have:

**Root level:**
- `README.md` - Project overview, setup, usage
- `CONTRIBUTING.md` - Contribution guidelines
- `ARCHITECTURE.md` - Architecture documentation
- `CHANGELOG.md` - Version history
- `API.md` - API documentation

**In /docs:**
- `docs/architecture.md` - System design
- `docs/database-schema.md` - Data model
- `docs/api.md` - API reference
- `docs/deployment.md` - Deployment guide
- `docs/testing.md` - Testing guide
- `docs/security.md` - Security requirements

**Configuration files (reference, don't import):**
- `package.json` - Dependencies, scripts
- `tsconfig.json` - TypeScript config
- `.eslintrc` - Linting rules
- `docker-compose.yml` - Service definitions

## Examples

### Web App with Existing Docs

```markdown
# architecture.md

## Existing Project Documentation

@../../README.md
@../../docs/architecture.md
@../../docs/api.md

## Additional Context for Claude Code

### Quick Reference
- Components: src/components/
- API layer: src/services/api/
- State: React Context (see README.md)
- Routing: React Router (see docs/architecture.md)

### Common Tasks
- New component: Use src/components/common/Button.tsx as template
- New API endpoint: Follow pattern in src/services/api/users.ts
- New route: Add to src/routes/index.tsx
```

### CLI Tool

```markdown
# architecture.md

## Existing Documentation

@../../README.md

See package.json for available commands.

## Additional Context

### Command Structure
All commands in src/commands/
Each command exports: { name, description, action }

### Adding New Command
1. Create src/commands/mycommand.ts
2. Export command object
3. Register in src/index.ts
```

### API with Comprehensive Docs

```markdown
# architecture.md

## Full Documentation Available

See existing documentation:
- README.md - Overview and setup
- docs/architecture.md - System design
- docs/database-schema.md - Data models
- docs/api.md - API reference
- CONTRIBUTING.md - Development guidelines

## Claude Code Quick Reference

When implementing:
- Controllers: src/controllers/ (see existing for patterns)
- Services: src/services/ (business logic)
- Models: src/models/ (Prisma schemas)
- Tests: Co-located with source files

All documented in CONTRIBUTING.md
```

## What to Add Here

**DO add:**
- Quick references for common tasks
- Patterns not documented elsewhere
- Claude Code-specific guidance
- Pointers to existing docs
- Shortcuts and decision trees

**DON'T duplicate:**
- System architecture (if in docs/)
- API documentation (if in docs/)
- Setup instructions (if in README.md)
- Contribution guidelines (if in CONTRIBUTING.md)

## Files in This Directory

### architecture.md
- Import or reference existing architecture docs
- Add Claude Code-specific architecture notes
- Quick reference for common patterns

### constraints.md
- Import CONTRIBUTING.md, security guidelines
- Add hard rules not documented elsewhere
- Never/Always lists

### patterns.md
- Import existing pattern documentation
- Add code patterns and examples
- Reference existing style guides

## Maintenance

**When to update:**
- New patterns emerge during development
- Existing docs change location
- New documentation is added to project
- Claude Code encounters missing context

**Keep it DRY:**
- Import existing docs when possible
- Reference rather than duplicate
- Only add what's unique to Claude Code
