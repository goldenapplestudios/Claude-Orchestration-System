# Agent Usage Protocol

**Critical for autonomous operation:** This protocol determines when to use Task agents vs working directly.

## Core Principle

**Use agents to save context and parallelize complex work. Work directly for simple, focused tasks.**

## Agent Types Available

We have two categories of agents: **Built-in Task Agents** (for general tasks) and **Custom Specialized Agents** (for specific workflows).

---

## Built-in Task Agents

### 1. Explore Agent (`subagent_type: "Explore"`)

**Purpose:** Search codebase efficiently to save context

**When to use:**
- Need to find files by patterns (`src/components/**/*.tsx`)
- Search code for keywords ("API endpoints", "authentication")
- Answer questions about codebase ("how do API endpoints work?")
- Don't know where code lives
- Context window >70% and need to search
- **Thoroughness levels:** "quick" | "medium" | "very thorough"

**Example tasks:**
- "Find all React components that use authentication"
- "Where is error handling implemented?"
- "How does the payment flow work?"
- "Find all API endpoints"

**Benefits:**
- Saves massive context (agent searches, you get summary)
- Fast parallel searches
- Can search multiple locations

**How to use:**
```
Use Task tool with:
- subagent_type: "Explore"
- description: "Find authentication components"
- prompt: "Search for all files that implement user authentication.
          Check src/components, src/services, and src/auth directories.
          Return file paths and brief description of how auth works."
- thoroughness: "medium" (or "quick" / "very thorough")
```

### 2. Plan Agent (`subagent_type: "Plan"`)

**Purpose:** Design implementation approach for complex features

**When to use:**
- Complex feature (>50 lines of code)
- Multiple files need changes
- Architectural decisions needed
- Unclear how to approach the task
- Need to design before implementing

**Example tasks:**
- "Plan how to add user authentication"
- "Design the data model for comments feature"
- "How should we refactor this module?"

**Benefits:**
- Thinks through approach before coding
- Identifies all files that need changes
- Can explore multiple approaches
- Returns structured plan

**How to use:**
```
Use Task tool with:
- subagent_type: "Plan"
- description: "Plan authentication feature"
- prompt: "Design an implementation plan for adding user authentication.
          Include: files to create/modify, data models needed, API endpoints,
          security considerations, and step-by-step implementation order.
          Review existing code patterns first."
- thoroughness: "very thorough"
```

### 3. General-Purpose Agent (`subagent_type: "general-purpose"`)

**Purpose:** Multi-step research and complex autonomous tasks

**When to use:**
- Multi-step research requiring multiple searches
- Don't know exactly what you're looking for
- Exploratory task with uncertain scope
- Need to research across codebase and documentation
- Task requires multiple rounds of searching/reading

**Example tasks:**
- "Research how to implement websockets in this project"
- "Investigate why tests are failing in CI"
- "Find and document all database migration patterns"

**Benefits:**
- Fully autonomous for complex research
- Can iterate and refine search
- Accesses all tools
- Returns comprehensive findings

**How to use:**
```
Use Task tool with:
- subagent_type: "general-purpose"
- description: "Research websocket implementation"
- prompt: "Research how to add websocket support to this project.
          1. Find if websockets are already used anywhere
          2. Check what websocket libraries are available
          3. Review project architecture to see where it fits
          4. Provide implementation recommendations with examples.
          Return detailed findings with file references."
```

---

## Custom Specialized Agents

These are project-specific custom agents designed for specific development workflows. They have specialized tools and knowledge.

### 4. code-explorer Agent

**Purpose:** Deep codebase analysis - trace execution, map architecture, understand patterns

**When to use:**
- Need deep feature understanding (beyond quick search)
- Tracing execution flows
- Understanding existing patterns before implementing
- Mapping architecture layers
- Context >70% and need thorough analysis

**Tools:** Glob, Grep, Read, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet

**Research Protocol:** Always use deepwiki for research. NEVER websearch.

**Difference from built-in Explore:**
- Built-in Explore: Quick keyword searches
- code-explorer: Deep analysis with execution tracing

**How to launch:**
```
"Launch code-explorer agent to trace how authentication works in this codebase"
```

### 5. code-architect Agent

**Purpose:** Design feature architectures with complete implementation blueprints

**When to use:**
- Complex features (>50 lines)
- Need detailed blueprint (files, interfaces, data flow)
- Architectural decisions required
- Multiple implementation approaches to evaluate

**Tools:** Glob, Grep, Read, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet

**Research Protocol:** Always use deepwiki for research. NEVER websearch.

**Difference from built-in Plan:**
- Built-in Plan: High-level strategic planning
- code-architect: Detailed blueprints with file-level specifics

**How to launch:**
```
"Launch code-architect agent to design user authentication system with complete blueprint"
```

### 6. implementation-helper Agent

**Purpose:** Step-by-step implementation guidance for complex features

**When to use:**
- Complex multi-file implementations (>100 lines)
- Need phased, structured approach
- Want to prevent incomplete implementations
- Previous attempts failed

**Tools:** Glob, Grep, Read, Bash, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet

**Research Protocol:** Always use deepwiki for research. NEVER websearch.

**How to launch:**
```
"Launch implementation-helper agent to build payment processing feature step-by-step"
```

### 7. error-resolver Agent

**Purpose:** Systematic debugging to find root causes

**When to use:**
- Same error occurs 2+ times
- "Coding in circles" with random fixes
- Complex multi-file errors
- Need systematic investigation

**Tools:** Glob, Grep, Read, Bash, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet

**Research Protocol:** Always use deepwiki for research. NEVER websearch.

**How to launch:**
```
"Launch error-resolver agent to debug this TypeError systematically"
```

### 8. test-writer Agent

**Purpose:** Write comprehensive test suites

**When to use:**
- New feature needs tests
- Need >80% coverage
- Complex logic requires thorough testing
- Setting up test infrastructure

**Tools:** Glob, Grep, Read, Bash, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet

**Research Protocol:** Always use deepwiki for research. NEVER websearch.

**How to launch:**
```
"Launch test-writer agent to create comprehensive tests for authentication module"
```

### 9. doc-writer Agent

**Purpose:** Write clear, comprehensive documentation

**When to use:**
- New feature needs documentation
- API documentation needed
- Feature guides required
- Complex system needs explanation

**Tools:** Glob, Grep, Read, mcp__deepwiki__ask_question
**Model:** Sonnet

**Research Protocol:** Always use deepwiki for research. NEVER websearch.

**How to launch:**
```
"Launch doc-writer agent to document the authentication API"
```

### 10. quality-checker Agent

**Purpose:** Review code for quality and common mistakes

**When to use:**
- Before committing
- After complex implementation
- Need confidence-scored issues
- Checking against project standards

**Tools:** Read, Grep, Glob
**Model:** Sonnet

**How to launch:**
```
"Launch quality-checker agent to review recent changes"
OR use /quality-check command
```

---

## Decision Matrix

### Use Explore Agent When:

| Situation | Why Explore |
|-----------|-------------|
| Context >70% full | Saves context by searching externally |
| Need to find files | Efficient pattern matching |
| "Where is X?" questions | Designed for code discovery |
| Searching for patterns | Can search multiple locations in parallel |
| Don't know codebase | Quick orientation |

### Use Plan Agent When:

| Situation | Why Plan |
|-----------|----------|
| Complex feature (>50 lines) | Needs design before implementation |
| Multiple files affected | Needs coordination |
| Architectural decisions | Needs structured thinking |
| Unclear approach | Needs exploration of options |
| Breaking changes | Needs impact analysis |

### Use General-Purpose Agent When:

| Situation | Why General-Purpose |
|-----------|---------------------|
| Multi-step research | Needs autonomy to iterate |
| Uncertain scope | Needs flexibility |
| Multiple searches needed | Can search repeatedly |
| Complex investigation | Full tool access |
| Documentation research | Can fetch and synthesize |

### Work Directly When:

| Situation | Why Direct |
|-----------|-----------|
| Simple task (<30 lines) | Overhead not worth it |
| Know exactly where code goes | No exploration needed |
| Context <50% | Room to work |
| File already open | Already have context |
| Quick fix | Faster to just do it |

## Context Window Management

### When Context is Getting Full

**Signs:**
- Conversation history >20 messages
- Have read >10 files
- Feeling uncertain about earlier context
- Need to re-read files
- Getting confused about task

**Action:**
1. **Stop adding to context**
2. **Use Explore agent** to search instead of reading more files
3. **Summarize** current findings in `.claude/work/current-session.md`
4. **Archive** and start fresh if needed

### Context Thresholds

- **<50% full:** Work directly, read files as needed
- **50-70% full:** Be selective, prefer agents for searches
- **>70% full:** Use agents for ALL searches, summarize frequently
- **>90% full:** Archive session, start fresh

## Parallelization

### Launch Multiple Agents

You can launch multiple agents in parallel for efficiency:

```
Launch 3 Explore agents simultaneously:
1. Search src/components for auth
2. Search src/services for API calls
3. Search tests/ for auth tests

Then synthesize results.
```

**When to parallelize:**
- Need information from multiple locations
- Independent searches
- Time-sensitive task
- Can process results separately

## Agent Prompts: Best Practices

### Be Specific

❌ Bad:
```
"Find authentication code"
```

✅ Good:
```
"Find all authentication-related code. Search:
1. src/auth/ for auth logic
2. src/components/ for login/signup UI
3. src/services/api/ for auth API calls
Return: file paths, brief descriptions, and how they connect."
```

### Include Context

❌ Bad:
```
"How does this work?"
```

✅ Good:
```
"Analyze the user authentication flow. We use JWT tokens.
I need to understand:
1. Where tokens are generated
2. How tokens are validated
3. Where auth middleware is applied
4. How refresh tokens work
Return detailed explanation with file references."
```

### Specify Output Format

❌ Bad:
```
"Find all API endpoints"
```

✅ Good:
```
"Find all API endpoints and return as:
- File path
- HTTP method
- Route path
- Brief description
- Authentication required (yes/no)
Format as a table for easy scanning."
```

## Anti-Patterns

### ❌ Don't: Use agents for trivial tasks

```
❌ Bad:
Use Explore agent to "find package.json"

✅ Good:
Just read ./package.json directly
```

### ❌ Don't: Read files then use Explore

```
❌ Bad:
Read 10 files, THEN use Explore agent (context already full!)

✅ Good:
Use Explore agent FIRST, then read only necessary files
```

### ❌ Don't: Use agents sequentially when can parallelize

```
❌ Bad:
1. Explore for components
2. Wait for results
3. Explore for services
4. Wait for results

✅ Good:
Launch both Explore agents simultaneously, process results together
```

### ❌ Don't: Give vague prompts

```
❌ Bad:
"Look into authentication"

✅ Good:
"Search for authentication implementation. Check:
- src/auth/ directory for auth logic
- middleware/ for auth middleware
- routes/ for protected routes
Return file list with descriptions."
```

## Workflow Examples

### Example 1: Adding New Feature (Complex)

**Task:** Add user profile editing feature

**Approach with custom agents:**
```
1. Use code-explorer agent
   - Deep analysis of existing profile code
   - Trace execution flows
   - Understand patterns

2. Use code-architect agent
   - Design complete blueprint
   - List all files to create/modify
   - Map data flow and interfaces

3. Review blueprint, get user approval

4. Use implementation-helper agent (if very complex)
   - Step-by-step phased implementation
   - Verify each phase
   - Prevent incomplete implementations

5. Use test-writer agent
   - Write comprehensive tests
   - Cover edge cases
   - Ensure >80% coverage

6. Use doc-writer agent
   - Document the feature
   - Write usage examples

7. Use quality-checker agent
   - Final review before commit
```

**Faster approach with built-in agents:**
```
1. Use Explore agent (thoroughness: "medium")
   - Find existing profile-related code
   - Find form patterns in codebase
   - Find API endpoint patterns

2. Review Explore results (don't read all files yet!)

3. Use Plan agent (thoroughness: "very thorough")
   - Design the feature based on Explore findings
   - Identify files to create/modify
   - Plan data flow

4. Review plan, get user approval

5. Work directly to implement (now you know exactly what to do)
   - Read only the specific files from plan
   - Implement step by step
   - Context stays manageable

6. Verify completion
```

### Example 2: Bug Fix (Medium)

**Task:** Fix authentication bug

**Approach with custom agents:**
```
1. If error is confusing or recurring:
   - Use error-resolver agent
   - Systematic root cause analysis
   - Get complete fix recommendation

2. Use test-writer agent
   - Add test that reproduces bug
   - Ensures bug won't regress

3. Implement fix from error-resolver

4. Use quality-checker agent
   - Verify fix doesn't introduce issues
```

**Faster approach:**
```
1. If familiar with auth code: Work directly
   - Read relevant files
   - Fix bug
   - Test

2. If unfamiliar: Use Explore agent first
   - Find auth-related code
   - Understand flow
   - Then work directly to fix
```

### Example 3: Code Investigation (Research)

**Task:** "Why are tests failing in CI but not locally?"

**Approach:**
```
1. Use General-Purpose agent
   - Investigate CI configuration
   - Compare with local setup
   - Check test files
   - Review recent changes
   - Return findings

2. Work directly to fix based on findings
```

## Measuring Success

**You're using agents well if:**
- Context window stays <70%
- You get results faster
- Less "I don't remember what I read earlier"
- Clear separation between exploration and implementation
- Can work on complex tasks without confusion

**You're not using agents effectively if:**
- Context window constantly full
- Re-reading files multiple times
- Launching agents for trivial tasks
- Not using agents when context is full
- Working directly when should be exploring

## Quick Reference

| Task Type | Agent | Thoroughness | Why |
|-----------|-------|--------------|-----|
| "Find all X" | Explore | quick/medium | Fast search |
| "How does X work?" | Explore | medium/thorough | Deep understanding |
| "Plan feature Y" | Plan | very thorough | Need design |
| "Research Z" | General-purpose | N/A | Multi-step |
| "Add function to X.ts" | None (direct) | N/A | Simple task |
| "Fix bug in Y" | Explore then direct | medium | Find then fix |

## Remember

**Agent usage is about:**
1. **Saving context** - Don't fill your context window with searches
2. **Parallelization** - Multiple agents work simultaneously
3. **Focused work** - Get summary from agents, then work with precision
4. **Autonomy** - Let agents do heavy exploration while you implement

**The goal:** Stay focused, keep context manageable, work efficiently.
