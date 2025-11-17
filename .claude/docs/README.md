# Documentation Index

Complete documentation for the Claude Code Autonomous Operations System.

---

## Getting Started

- **[Main README](../../README.md)** - System overview and quick start
- **[Setup Guide](../../SETUP.md)** - Installation and configuration

---

## Features & Capabilities

- **[Complete Features](features.md)** - Full feature list with implementation details
  - 7 custom specialized agents
  - 90+ language-specific linter patterns
  - Context management protocols
  - Session-based workflows

---

## Quality Linting

Automatic code quality validation with 90+ patterns across 5 languages.

- **[Linter Guide](linter/README.md)** - Complete linter documentation
  - Three-layer validation system
  - Language-specific security patterns
  - Configuration and customization

- **[Common Mistakes](linter/common-mistakes.md)** - Language-specific patterns
  - JavaScript/TypeScript: 18 patterns (async/await, promises, memory leaks)
  - Python: 17 patterns (mutable defaults, context managers, exceptions)
  - Go: 18 patterns (error handling, goroutines, channels, defer)
  - Rust: 17 patterns (unwrap, lifetimes, borrowing, unsafe)
  - Examples and fixes for each pattern

---

## Guides & Protocols

### Agent Usage

- **[Agent Guide](../guides/agent-guide.md)** - Complete agent usage guide
  - 7 custom specialized agents
  - Decision matrices for when to use which agent
  - Multi-agent workflows
  - Tool access patterns

- **[Agent Usage Protocol](../protocols/agent-usage.md)** - Operational protocol
  - Built-in agents (Explore, Plan, general-purpose)
  - Custom agents (code-explorer, code-architect, etc.)
  - Decision trees and workflows

### Best Practices

- **[Complete Examples](../guides/complete-examples.md)** - What "done" looks like
- **[Anti-Patterns](../guides/anti-patterns.md)** - What NOT to do
- **[Pitfalls](../guides/pitfalls.md)** - Known failure modes (14+)

### Operational Protocols

- **[Context Management](../protocols/context-management.md)** - Managing context windows
- **[Documentation](../protocols/documentation.md)** - Session lifecycle and archiving
- **[Implementation](../protocols/implementation.md)** - Implementation workflow
- **[Error Handling](../protocols/error-handling.md)** - Error resolution protocol
- **[Verification](../protocols/verification.md)** - Completion verification
- **[Research](../protocols/research.md)** - Research protocol

---

## Changelog

Complete technical update history for the system.

- **[Technical Changelog](CHANGELOG.md)** - Comprehensive update history
  - 2025-11-16: System build and verification
  - Custom agents added (7 specialized agents)
  - DeepWiki integration (research protocol)
  - Linter enhancement (language-specific checks)
  - Gamification system implementation
  - Codebase audit and cleanup
  - Agent verification and tool additions
  - Documentation updates
  - Compatibility audit (100% Claude Code aligned)

---

## Configuration Files

### Custom Agents

Located in `.claude/agents/`:

- `code-explorer.md` - Deep codebase analysis, execution tracing
- `code-architect.md` - Architecture design, implementation blueprints
- `implementation-helper.md` - Step-by-step implementation guidance
- `error-resolver.md` - Systematic debugging, root cause analysis
- `test-writer.md` - Comprehensive test suite generation
- `doc-writer.md` - API and feature documentation
- `quality-checker.md` - Code quality review

### Slash Commands

Located in `.claude/commands/`:

- `quality-check.md` - Manual code quality checking

### Hooks

Located in `.claude/hooks/`:

- `validate-completeness.py` - PreToolUse validation (90+ patterns)

### Project Context

Located in `.claude/project/` (customize for your project):

- `architecture.md` - Your system design
- `constraints.md` - Your hard rules
- `patterns.md` - Your code patterns
- `README.md` - How to use existing docs

---

## Directory Structure

```
.claude/
├── docs/                          # THIS DIRECTORY
│   ├── README.md                  # Documentation index (you are here)
│   ├── features.md                # Complete feature list
│   ├── CHANGELOG.md               # Technical update history
│   ├── QUICKSTART.md              # Quick start guide
│   ├── SETUP.md                   # Detailed setup
│   └── linter/                    # Linter documentation
│       ├── README.md              # Main linter guide
│       └── common-mistakes.md     # 90+ language patterns
├── agents/                        # 7 custom agents
├── commands/                      # Slash commands
├── hooks/                         # PreToolUse hooks
├── protocols/                     # Operational protocols
├── guides/                        # Reference guides
└── project/                       # Project-specific context
```

---

## Quick Navigation

**I want to...**

- **Get started** → [Main README](../../README.md), [Setup Guide](../../SETUP.md)
- **Understand features** → [Complete Features](features.md)
- **Configure the linter** → [Linter Guide](linter/README.md)
- **Learn about language mistakes** → [Common Mistakes](linter/common-mistakes.md)
- **Use agents effectively** → [Agent Guide](../guides/agent-guide.md)
- **Avoid common pitfalls** → [Pitfalls](../guides/pitfalls.md)
- **See what's changed** → [Technical Changelog](CHANGELOG.md)
- **Customize for my project** → [Project Context](../project/)

---

**For questions or issues, refer to the main [README](../../README.md) troubleshooting section.**
