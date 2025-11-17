# Complete Agent Usage Guide

A comprehensive guide to all available agents for autonomous operation in Claude Code.

## Agent Overview

We have **7 specialized custom agents** plus **3 built-in agents** for different aspects of development.

### Custom Agents (Specialized)

1. **code-explorer** - Deep codebase analysis
2. **code-architect** - Architecture design
3. **implementation-helper** - Step-by-step implementation
4. **error-resolver** - Debug and fix errors
5. **test-writer** - Write comprehensive tests
6. **doc-writer** - Write documentation
7. **quality-checker** - Code quality review

### Built-in Agents (General Purpose)

1. **Explore** - Fast codebase searching (Haiku-powered)
2. **Plan** - Strategic planning (Haiku-powered)
3. **general-purpose** - Multi-step autonomous tasks

---

## When to Use Which Agent

### Decision Tree

```
What do you need to do?
│
├─ Understand existing code
│  ├─ Quick search for pattern → Use built-in **Explore** agent
│  └─ Deep analysis of feature → Use **code-explorer** agent
│
├─ Design new feature
│  ├─ Simple addition (<30 lines) → Work directly
│  ├─ Need high-level plan → Use built-in **Plan** agent
│  └─ Need detailed blueprint → Use **code-architect** agent
│
├─ Implement new feature
│  ├─ Simple, clear path → Work directly
│  ├─ Complex, multi-phase → Use **implementation-helper** agent
│  └─ Complex, uncertain approach → Use **code-architect** first
│
├─ Debug error
│  ├─ Obvious fix → Fix directly
│  ├─ Same error 2+ times → Use **error-resolver** agent
│  └─ Complex multi-file error → Use **error-resolver** agent
│
├─ Write tests
│  ├─ Simple function → Write directly
│  └─ Comprehensive suite needed → Use **test-writer** agent
│
├─ Write documentation
│  ├─ Simple docstring → Write directly
│  └─ Full API/feature docs → Use **doc-writer** agent
│
└─ Review code quality
   ├─ Quick check → Run /quality-check command
   └─ Deep analysis → Use **quality-checker** agent
```

---

## Agent Details

### 1. code-explorer (Deep Analysis)

**Purpose**: Deeply analyze existing codebase features

**Use when:**
- Exploring unfamiliar codebase
- Looking for similar feature implementations
- Understanding how existing features work
- Tracing execution paths for debugging
- Need to understand patterns before implementing
- Context window >70% and need to search

**Capabilities:**
- Trace execution flows
- Map architecture layers
- Identify patterns and conventions
- Document dependencies
- Find integration points
- Research via deepwiki (never websearch)

**Tools**: Glob, Grep, Read, TodoWrite, mcp__deepwiki__ask_question
**Model**: Sonnet

**Research Protocol**: Always use deepwiki for research. Never use websearch.
**Output**: Comprehensive exploration report

**Example invocation:**
```
"Launch code-explorer to trace how authentication works"
"Explore how the payment processing feature is implemented"
```

**When NOT to use:**
- Quick keyword search → Use built-in Explore instead
- Already know where code is → Read directly
- Simple file location → Use Glob/Grep directly

---

### 2. code-architect (Design & Blueprint)

**Purpose**: Design feature architectures with complete implementation blueprints

**Use when:**
- Designing complex new features (>50 lines)
- Unclear implementation approach
- Need architectural decisions
- Multiple ways to implement something
- Building significant new functionality
- Need structured plan before coding

**Capabilities:**
- Analyze existing patterns
- Make architectural decisions
- Design component interfaces
- Map data flows
- Create build sequences
- List all files to create/modify
- Research via deepwiki (never websearch)

**Tools**: Glob, Grep, Read, TodoWrite, mcp__deepwiki__ask_question
**Model**: Sonnet

**Research Protocol**: Always use deepwiki for research. Never use websearch.
**Output**: Complete architecture blueprint

**Example invocation:**
```
"Launch code-architect to design user authentication system"
"Design architecture for real-time notifications"
"Create implementation blueprint for caching layer"
```

**When NOT to use:**
- Simple additions (<30 lines) → Work directly
- Implementation approach is obvious → Work directly
- Just need high-level plan → Use built-in Plan instead

---

### 3. implementation-helper (Step-by-Step)

**Purpose**: Guide through complex implementations step-by-step

**Use when:**
- Complex feature (>100 lines)
- Multiple files involved
- Unclear implementation path
- Need structured, phased approach
- Previous implementation attempts failed
- Want to ensure complete implementation (no TODOs)

**Capabilities:**
- Break down into phases
- Complete each step fully
- Verify each phase
- Prevent incomplete implementations
- Track progress through phases
- Ensure acceptance criteria met
- Research via deepwiki (never websearch)

**Tools**: Glob, Grep, Read, Bash, TodoWrite, mcp__deepwiki__ask_question
**Model**: Sonnet

**Research Protocol**: Always use deepwiki for research. Never use websearch.
**Output**: Phased implementation plan with verification

**Example invocation:**
```
"Launch implementation-helper to build payment processing feature"
"Help me implement authentication system step-by-step"
"Guide implementation of data migration feature"
```

**When NOT to use:**
- Simple task (<30 lines) → Work directly
- Clear straightforward implementation → Work directly
- Already have detailed blueprint → Follow it directly

---

### 4. error-resolver (Debugging)

**Purpose**: Debug errors systematically to find root causes

**Use when:**
- Same error occurs 2+ times
- Error message is confusing
- Multiple possible causes
- Need systematic investigation
- "Coding in circles" (trying random fixes)
- Complex multi-file errors

**Capabilities:**
- Analyze stack traces
- Check implementation completeness
- Verify dependencies
- Recognize error patterns
- Design complete fixes (not workarounds)
- Prevent circular debugging
- Research via deepwiki (never websearch)

**Tools**: Glob, Grep, Read, Bash, TodoWrite, mcp__deepwiki__ask_question
**Model**: Sonnet

**Research Protocol**: Always use deepwiki for research. Never use websearch.
**Output**: Root cause analysis with complete fix

**Example invocation:**
```
"Launch error-resolver to debug this TypeError"
"Investigate why authentication keeps failing"
"Debug module resolution error systematically"
```

**When NOT to use:**
- Error is obvious (typo) → Fix directly
- Simple missing import → Fix directly
- Error message is self-explanatory → Fix directly

---

### 5. test-writer (Testing)

**Purpose**: Write comprehensive test suites

**Use when:**
- New feature needs tests
- Existing code lacks test coverage
- Need comprehensive test suite
- Complex logic requires thorough testing
- Setting up testing infrastructure
- Want >80% coverage

**Capabilities:**
- Write unit tests
- Write integration tests
- Cover edge cases
- Cover error conditions
- Set up mocking
- Achieve high coverage
- Research via deepwiki (never websearch)

**Tools**: Glob, Grep, Read, Bash, TodoWrite, mcp__deepwiki__ask_question
**Model**: Sonnet

**Research Protocol**: Always use deepwiki for research. Never use websearch.
**Output**: Complete test suite with coverage

**Example invocation:**
```
"Launch test-writer to create tests for authentication module"
"Write comprehensive tests for user service"
"Add edge case tests for payment processing"
```

**When NOT to use:**
- Trivial code (<5 lines) → Skip or write simple test
- Tests already exist and comprehensive → Skip
- Quick prototype (though tests still recommended)

---

### 6. doc-writer (Documentation)

**Purpose**: Write clear, comprehensive documentation

**Use when:**
- New feature needs documentation
- API needs documenting
- Existing docs are outdated
- Documentation is missing
- Complex feature needs explanation
- Need user-facing documentation

**Capabilities:**
- Write API documentation
- Write function/module docs
- Write feature guides
- Create examples
- Write troubleshooting guides
- Audience-appropriate content

**Tools**: Glob, Grep, Read, WebFetch, WebSearch
**Model**: Sonnet
**Output**: Complete documentation

**Example invocation:**
```
"Launch doc-writer to document the authentication API"
"Write documentation for user service"
"Create usage guide for new feature"
```

**When NOT to use:**
- Code is self-documenting → Skip
- Simple docstring needed → Write directly
- Documentation already good → Skip

---

### 7. quality-checker (Code Review)

**Purpose**: Review code for mistakes and quality issues

**Use when:**
- Before committing code
- After complex implementation
- Need comprehensive quality check
- Want confidence scoring
- Checking against project standards

**Capabilities:**
- Detect incomplete implementations (TODOs)
- Find security issues
- Check type safety
- Verify pattern compliance
- Score issues by confidence
- Suggest fixes

**Tools**: Read, Grep, Glob
**Model**: Sonnet
**Output**: Quality check report with confidence scores

**Example invocation:**
```
"Launch quality-checker to review recent changes"
"/quality-check" (via command)
"Review code quality in src/services"
```

**When NOT to use:**
- Simple code → PreToolUse hook handles it
- Need quick check → Use /quality-check command instead
- During active development → Wait until complete

---

## Built-in Agents

### Explore (Fast Search)

**Purpose**: Efficiently search through codebases

**Use when:**
- Need to find files quickly
- Searching for keywords
- Context window getting full (>70%)
- Quick exploration needed

**Powered by**: Haiku (fast, efficient)

**When to use custom code-explorer instead:**
- Need deep analysis
- Need to trace execution
- Need to understand patterns
- Need comprehensive report

### Plan (Strategic Planning)

**Purpose**: High-level planning before implementation

**Use when:**
- Need to strategize approach
- Breaking down large tasks
- Deciding between options

**Powered by**: Haiku switching to Sonnet for planning

**When to use custom code-architect instead:**
- Need detailed blueprint
- Need file-by-file plan
- Need complete interfaces
- Complex architectural decisions

### general-purpose (Multi-Step Tasks)

**Purpose**: Handle complex autonomous tasks

**Use when:**
- Multi-step research needed
- Uncertain scope
- Need autonomous execution
- Task doesn't fit other agents

---

## Multi-Agent Workflows

### Workflow 1: New Complex Feature

1. **code-explorer**: Understand existing patterns
2. **code-architect**: Design architecture
3. **implementation-helper**: Implement step-by-step
4. **test-writer**: Write comprehensive tests
5. **doc-writer**: Document feature
6. **quality-checker**: Final review

### Workflow 2: Debug Complex Error

1. **error-resolver**: Identify root cause
2. **test-writer**: Add test that reproduces bug
3. Fix implementation
4. **quality-checker**: Verify fix

### Workflow 3: Refactoring

1. **test-writer**: Ensure tests exist first
2. **code-explorer**: Understand current implementation
3. **code-architect**: Design better approach
4. **implementation-helper**: Refactor step-by-step
5. **quality-checker**: Verify quality maintained

---

## Parallel Agent Execution

Launch multiple agents in parallel when tasks are independent:

```typescript
// Example: Explore multiple features simultaneously
"Launch 3 code-explorer agents in parallel to analyze:
1. Authentication system
2. Payment processing
3. User management"
```

**When to use parallel agents:**
- Exploring multiple independent features
- Reviewing different parts of codebase
- Researching multiple approaches

**Based on deepwiki best practices:**
- feature-dev plugin runs 2-3 explorers in parallel
- code-review plugin runs 3 reviewers in parallel

---

## Agent Tool Access

Based on deepwiki research, here's what tools each agent type should have:

### Read-Only Analysis Agents
**Agents**: code-explorer, code-architect, quality-checker
**Tools**: Glob, Grep, Read, TodoWrite, mcp__deepwiki__ask_question
**No Write Access**: These analyze and recommend, don't modify code
**Research**: Use deepwiki, NEVER websearch

### Implementation Agents
**Agents**: implementation-helper, error-resolver, test-writer
**Tools**: Glob, Grep, Read, Bash, TodoWrite, mcp__deepwiki__ask_question
**Bash Access**: Can run tests, verify builds
**Research**: Use deepwiki, NEVER websearch

### Documentation Agents
**Agents**: doc-writer
**Tools**: Glob, Grep, Read, mcp__deepwiki__ask_question
**Limited Tools**: Just need to read and research
**Research**: Use deepwiki, NEVER websearch

---

## Research Protocol

**CRITICAL: All agents MUST use deepwiki for research, NEVER websearch.**

This is a documented failure mode: "We should always research with deepwiki before using websearch."

**Why deepwiki over websearch:**
- More accurate Claude Code-specific information
- Official documentation and examples
- Proven patterns from actual plugins
- No outdated or incorrect web results

**How agents use deepwiki:**
```
When agent needs to research:
1. Use mcp__deepwiki__ask_question tool
2. Ask specific questions about patterns, frameworks, best practices
3. Get accurate, up-to-date information
4. NEVER fall back to websearch
```

---

## Best Practices

### DO:

✅ **Use agents to save context** when window >70%
✅ **Use specific agents** for specialized tasks
✅ **Run agents in parallel** when tasks are independent
✅ **Let agents be autonomous** - provide clear task, let them work
✅ **Use multi-agent workflows** for complex features
✅ **Review agent output** before implementing
✅ **Launch error-resolver** after 2nd failed fix attempt

### DON'T:

❌ **Don't use agents for trivial tasks** - work directly instead
❌ **Don't micromanage agents** - let them be autonomous
❌ **Don't skip agents for complex tasks** - they prevent mistakes
❌ **Don't ignore agent recommendations** - they're specialized
❌ **Don't use wrong agent type** - use decision tree above

---

## Integration with Protocols

Agents work with our protocols:

- **agent-usage.md**: When to use agents vs direct work
- **context-management.md**: Use agents to save context
- **implementation.md**: Use implementation-helper for complex features
- **error-handling.md**: Use error-resolver for debugging
- **verification.md**: Use quality-checker before completion

---

## Measuring Agent Effectiveness

### Successful Agent Use:

- ✅ Task completed without circular debugging
- ✅ No incomplete implementations (no TODOs)
- ✅ Context window stayed manageable
- ✅ Quality standards maintained
- ✅ Time saved compared to manual work

### When to Improve Agent Use:

- ❌ Same error occurred 3+ times
- ❌ Implementation had TODOs
- ❌ Context window filled up
- ❌ Task took much longer than expected
- ❌ Quality issues in final code

---

## Quick Reference

| Task | Agent | Complexity | Time Saved |
|------|-------|-----------|------------|
| Deep code analysis | code-explorer | High | 30-60 min |
| Architecture design | code-architect | High | 45-90 min |
| Step-by-step impl | implementation-helper | High | 60-120 min |
| Debug complex error | error-resolver | Medium | 20-40 min |
| Write test suite | test-writer | Medium | 20-40 min |
| Write documentation | doc-writer | Medium | 15-30 min |
| Code quality review | quality-checker | Low | 5-15 min |

---

## Summary

**7 specialized custom agents** designed based on deepwiki best practices from the feature-dev and code-review plugins:

1. **code-explorer** - Understand existing code
2. **code-architect** - Design new features
3. **implementation-helper** - Implement step-by-step
4. **error-resolver** - Fix bugs systematically
5. **test-writer** - Ensure quality
6. **doc-writer** - Document features
7. **quality-checker** - Review quality

Use them autonomously to build better software faster with fewer mistakes.
