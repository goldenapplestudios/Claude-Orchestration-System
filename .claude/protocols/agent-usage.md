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

## Language Expert Agents

Cross-framework language specialists for deep language-specific work, migrations, and optimization.

### 11. dart-expert Agent

**Purpose:** Dart language specialist for modern features, null safety, async patterns, isolates, FFI

**When to use:**
- Dart-specific optimization
- Migrating to Dart 3.x features
- Isolate-based architecture
- FFI integration with C/C++
- Null safety migration
- Async pattern optimization

**Tools:** Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** flutter-performance-optimizer, flutter-platform-integrator

**How to launch:**
```
"Launch dart-expert to optimize this Dart code for performance"
"Use dart-expert to migrate this code to Dart 3.x patterns"
```

### 12. typescript-expert Agent

**Purpose:** TypeScript specialist for type system, generics, strict mode, JS migration

**When to use:**
- JavaScript → TypeScript migration
- Complex type definitions
- Type safety improvements
- Generic component design
- tsconfig optimization

**Tools:** Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** react-implementer, react-architect

**How to launch:**
```
"Launch typescript-expert to create type-safe interfaces for this API"
"Use typescript-expert to migrate this JS file to TypeScript"
```

### 13. javascript-expert Agent

**Purpose:** JavaScript specialist for ES2015+, async patterns, performance, runtime optimization

**When to use:**
- JavaScript performance optimization
- Async pattern refactoring
- ES5 → ES2015+ modernization
- Memory leak investigation
- Event loop optimization

**Tools:** Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** react-performance-optimizer, typescript-expert

**How to launch:**
```
"Launch javascript-expert to optimize this async code"
"Use javascript-expert to modernize this ES5 code"
```

### 14. kotlin-expert Agent

**Purpose:** Kotlin specialist for Android development, coroutines, platform channels, Java interop

**When to use:**
- Flutter Android platform channels
- Kotlin coroutines implementation
- Java → Kotlin migration
- Android SDK integration
- Gradle build optimization

**Tools:** Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** flutter-platform-integrator, dart-expert

**How to launch:**
```
"Launch kotlin-expert to implement Android platform channel"
"Use kotlin-expert to optimize Kotlin coroutines"
```

### 15. swift-expert Agent

**Purpose:** Swift specialist for iOS development, Swift concurrency, platform channels, Objective-C interop

**When to use:**
- Flutter iOS platform channels
- Swift concurrency patterns
- Objective-C → Swift migration
- iOS SDK integration
- Memory management (ARC)

**Tools:** Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** flutter-platform-integrator, dart-expert

**How to launch:**
```
"Launch swift-expert to implement iOS platform channel"
"Use swift-expert to add Swift async/await patterns"
```

### 16. rust-expert Agent

**Purpose:** Rust specialist for ownership/borrowing, async Tokio, WASM integration, FFI, Tauri backend

**When to use:**
- Tauri Rust backend development
- WASM module integration (wasm-bindgen, wasm-pack)
- Complex async operations with Tokio
- FFI (Foreign Function Interface) implementations
- Memory-safe systems programming
- Ownership/borrowing optimization

**Tools:** Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** tauri-implementer, tauri-plugin-developer, tauri-ipc-specialist

**How to launch:**
```
"Launch rust-expert to implement async Tokio backend"
"Use rust-expert to create WASM module with wasm-bindgen"
"Launch rust-expert to optimize Rust ownership patterns"
```

---

## Flutter Framework Agents

Specialized agents for Flutter development across all aspects of mobile app creation.

### Flutter Core Agents

#### 16. flutter-explorer Agent

**Purpose:** Deeply analyze Flutter codebases - trace widget trees, state flows, architecture

**When to use:**
- Starting Flutter feature (understand patterns)
- Unfamiliar with Flutter codebase
- Looking for similar Flutter implementations
- Understanding state management approach
- Exploring navigation structure

**Tools:** Glob, Grep, Read, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** flutter-architect

**How to launch:**
```
"Launch flutter-explorer to understand the widget hierarchy"
"Use flutter-explorer to find existing state management patterns"
```

#### 17. flutter-architect Agent

**Purpose:** Design Flutter feature architectures with complete implementation blueprints

**When to use:**
- Designing complex Flutter features (>50 lines)
- Need widget hierarchy design
- State management strategy unclear
- Navigation approach undecided
- Multiple implementation approaches

**Tools:** Glob, Grep, Read, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** flutter-explorer, flutter-implementer

**How to launch:**
```
"Launch flutter-architect to design user profile feature"
"Use flutter-architect to create blueprint for authentication flow"
```

#### 18. flutter-implementer Agent

**Purpose:** Build Flutter features step-by-step with complete implementations

**When to use:**
- Building Flutter features
- Complex multi-widget implementations
- Need structured guidance
- Want to prevent incomplete code
- Following architecture blueprint

**Tools:** Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** flutter-architect, flutter-tester

**How to launch:**
```
"Launch flutter-implementer to build the user profile screen"
"Use flutter-implementer to implement this blueprint"
```

#### 19. flutter-tester Agent

**Purpose:** Write comprehensive Flutter tests (widget, unit, integration)

**When to use:**
- New Flutter feature needs tests
- Need >80% test coverage
- Complex widget testing
- Integration test setup

**Tools:** Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** flutter-implementer, flutter-reviewer

**How to launch:**
```
"Launch flutter-tester to write widget tests for ProfileScreen"
"Use flutter-tester to create comprehensive test suite"
```

#### 20. flutter-reviewer Agent

**Purpose:** Review Flutter code for quality, widget patterns, state management

**When to use:**
- Before committing Flutter code
- After complex implementation
- Need confidence-scored feedback
- Quality gate checkpoint

**Tools:** Read, Grep, Glob, TodoWrite
**Model:** Sonnet
**Works with:** flutter-performance-optimizer

**How to launch:**
```
"Launch flutter-reviewer to review these widget implementations"
"Use flutter-reviewer for final code review"
```

### Flutter Specialized Agents

#### 21. flutter-animator Agent

**Purpose:** Animation specialist - AnimationController, Tween, implicit/explicit animations

**When to use:**
- Complex animation requirements
- Performance optimization for animations
- Custom animation patterns
- Hero transitions
- Physics-based motion

**Tools:** Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** flutter-implementer, flutter-performance-optimizer

**How to launch:**
```
"Launch flutter-animator to create staggered list animations"
"Use flutter-animator to optimize these frame drops"
```

#### 22. flutter-platform-integrator Agent

**Purpose:** Platform channel specialist - MethodChannel, EventChannel, FFI, native integration

**When to use:**
- Need native platform features
- Hardware access (camera, sensors)
- Platform-specific APIs
- Third-party native SDKs
- FFI integration

**Tools:** Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** kotlin-expert, swift-expert, dart-expert

**How to launch:**
```
"Launch flutter-platform-integrator to implement camera access"
"Use flutter-platform-integrator to create platform channel"
```

#### 23. flutter-performance-optimizer Agent

**Purpose:** Performance specialist - DevTools profiling, widget rebuilds, isolates, memory

**When to use:**
- Flutter app feels laggy
- Frame drops detected
- Memory issues or leaks
- Long list rendering problems
- Build time optimization

**Tools:** Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** dart-expert, flutter-animator

**How to launch:**
```
"Launch flutter-performance-optimizer to profile scroll performance"
"Use flutter-performance-optimizer to fix these memory leaks"
```

#### 24. flutter-accessibility-specialist Agent

**Purpose:** Accessibility expert - Semantics widgets, screen readers, WCAG compliance

**When to use:**
- Building accessible Flutter features
- Accessibility audit required
- WCAG compliance needed
- Screen reader testing
- Inclusive design review

**Tools:** Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** flutter-implementer, flutter-reviewer

**How to launch:**
```
"Launch flutter-accessibility-specialist to audit this screen"
"Use flutter-accessibility-specialist to add semantic labels"
```

---

## React Framework Agents

Specialized agents for React development including modern concurrent features and SSR.

### React Core Agents

#### 25. react-explorer Agent

**Purpose:** Deeply analyze React codebases - component trees, hooks, state flows

**When to use:**
- Starting React feature
- Unfamiliar with React codebase
- Looking for component patterns
- Understanding hooks usage
- Exploring routing structure

**Tools:** Glob, Grep, Read, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** react-architect

**How to launch:**
```
"Launch react-explorer to understand component hierarchy"
"Use react-explorer to find existing hooks patterns"
```

#### 26. react-architect Agent

**Purpose:** Design React feature architectures with complete component blueprints

**When to use:**
- Designing complex React features
- Need component hierarchy design
- State management strategy unclear
- Hooks strategy undecided
- Multiple implementation approaches

**Tools:** Glob, Grep, Read, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** react-explorer, react-implementer

**How to launch:**
```
"Launch react-architect to design dashboard feature"
"Use react-architect to create component architecture"
```

#### 27. react-implementer Agent

**Purpose:** Build React features step-by-step with complete implementations

**When to use:**
- Building React components
- Complex multi-component implementations
- Proper hooks usage needed
- Want to prevent incomplete code
- Following architecture blueprint

**Tools:** Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** react-architect, react-tester

**How to launch:**
```
"Launch react-implementer to build the Dashboard component"
"Use react-implementer to implement this architecture"
```

#### 28. react-tester Agent

**Purpose:** Write comprehensive React tests (Jest, RTL, Playwright)

**When to use:**
- New React feature needs tests
- Need >80% test coverage
- Component testing with RTL
- E2E test setup

**Tools:** Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** react-implementer, react-reviewer

**How to launch:**
```
"Launch react-tester to write tests for Dashboard component"
"Use react-tester to create E2E tests"
```

#### 29. react-reviewer Agent

**Purpose:** Review React code for quality, hooks patterns, component design

**When to use:**
- Before committing React code
- After complex implementation
- Need confidence-scored feedback
- Hooks rules validation

**Tools:** Read, Grep, Glob, TodoWrite
**Model:** Sonnet
**Works with:** react-performance-optimizer

**How to launch:**
```
"Launch react-reviewer to review these components"
"Use react-reviewer for final code review"
```

### React Specialized Agents

#### 30. react-performance-optimizer Agent

**Purpose:** Performance specialist - React Compiler, memoization, re-renders, bundles

**When to use:**
- React app feels slow
- Too many re-renders
- Large bundle size
- Initial load too slow
- Need profiling analysis

**Tools:** Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** javascript-expert, typescript-expert

**How to launch:**
```
"Launch react-performance-optimizer to reduce re-renders"
"Use react-performance-optimizer to optimize bundle size"
```

#### 31. react-concurrent-specialist Agent

**Purpose:** Concurrent features expert - startTransition, Suspense, useTransition, useOptimistic

**When to use:**
- Building responsive interfaces
- Data fetching with Suspense
- Optimistic UI updates needed
- Handling concurrent state
- Complex async workflows

**Tools:** Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** react-implementer, react-ssr-specialist

**How to launch:**
```
"Launch react-concurrent-specialist to add Suspense boundaries"
"Use react-concurrent-specialist for optimistic updates"
```

#### 32. react-ssr-specialist Agent

**Purpose:** SSR/SSG expert - Server Components, hydration, Next.js, streaming, SEO

**When to use:**
- Building SSR/SSG applications
- Next.js App Router projects
- Server Components needed
- SEO requirements
- Hydration issues

**Tools:** Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** react-concurrent-specialist, react-performance-optimizer

**How to launch:**
```
"Launch react-ssr-specialist to set up Server Components"
"Use react-ssr-specialist to optimize SEO"
```

#### 33. react-accessibility-specialist Agent

**Purpose:** Accessibility expert - ARIA, semantic HTML, keyboard navigation, WCAG

**When to use:**
- Building accessible React features
- Accessibility audit required
- WCAG compliance needed
- Keyboard navigation implementation
- Screen reader compatibility

**Tools:** Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** react-implementer, react-reviewer

**How to launch:**
```
"Launch react-accessibility-specialist to audit this component"
"Use react-accessibility-specialist to add ARIA labels"
```

---

## Tauri Framework Agents

Specialized agents for Tauri desktop application development with Rust backends.

### Tauri Core Agents

#### tauri-explorer Agent

**Purpose:** Analyze Tauri desktop applications - IPC flows, commands, plugins, security

**When to use:**
- Starting Tauri feature (understand patterns)
- Unfamiliar with Tauri codebase
- Looking for similar IPC implementations
- Understanding command structure
- Exploring plugin architecture

**Tools:** Glob, Grep, Read, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** tauri-architect, rust-expert

**How to launch:**
```
"Launch tauri-explorer to understand IPC command patterns"
"Use tauri-explorer to find existing Tauri plugins"
```

#### tauri-architect Agent

**Purpose:** Design Tauri application architectures with Rust backend and frontend integration

**When to use:**
- Designing complex Tauri features
- Need command design strategy
- IPC flow design unclear
- Plugin architecture decisions
- Security model design

**Tools:** Glob, Grep, Read, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** tauri-explorer, tauri-implementer, rust-expert

**How to launch:**
```
"Launch tauri-architect to design file management system"
"Use tauri-architect to create blueprint for system tray integration"
```

#### tauri-implementer Agent

**Purpose:** Implement Tauri applications with Rust commands and frontend integration

**When to use:**
- Building Tauri features
- Implementing Rust commands
- Frontend-backend integration
- IPC implementation
- Event system implementation

**Tools:** Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** tauri-architect, rust-expert, tauri-security-specialist

**How to launch:**
```
"Launch tauri-implementer to build file system commands"
"Use tauri-implementer to implement notification system"
```

#### tauri-tester Agent

**Purpose:** Write comprehensive tests for Tauri applications - Rust unit tests and E2E tests

**When to use:**
- New Tauri feature needs tests
- Need Rust backend test coverage
- WebDriver E2E testing
- IPC testing
- Security testing

**Tools:** Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** tauri-implementer, rust-expert

**How to launch:**
```
"Launch tauri-tester to create tests for IPC commands"
"Use tauri-tester to write E2E tests for desktop app"
```

#### tauri-reviewer Agent

**Purpose:** Review Tauri code for security, quality, CSP compliance, and best practices

**When to use:**
- Before committing Tauri code
- Security review needed
- CSP configuration review
- Capabilities configuration review
- IPC security audit

**Tools:** Read, Grep, Glob
**Model:** Sonnet
**Works with:** tauri-security-specialist, rust-expert

**How to launch:**
```
"Launch tauri-reviewer to review security configuration"
"Use tauri-reviewer to audit IPC command security"
```

### Tauri Specialized Agents

#### tauri-plugin-developer Agent

**Purpose:** Create custom Tauri plugins with Rust and JavaScript APIs

**When to use:**
- Building custom Tauri plugin
- Need Rust + JS API integration
- Plugin permissions system
- Mobile plugin support
- Cross-platform plugin development

**Tools:** Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** tauri-implementer, rust-expert

**How to launch:**
```
"Launch tauri-plugin-developer to create custom database plugin"
"Use tauri-plugin-developer to build system integration plugin"
```

#### tauri-ipc-specialist Agent

**Purpose:** Design efficient IPC patterns with commands and events

**When to use:**
- Complex IPC requirements
- Event-driven architecture
- Performance-critical IPC
- Bidirectional communication
- State synchronization

**Tools:** Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** tauri-architect, tauri-implementer

**How to launch:**
```
"Launch tauri-ipc-specialist to optimize command performance"
"Use tauri-ipc-specialist to design event-driven state sync"
```

#### tauri-bundler-specialist Agent

**Purpose:** Create platform-specific installers (MSI, DMG, AppImage, etc.)

**When to use:**
- Building installers
- Code signing setup
- Update system configuration
- Platform-specific features
- Deployment preparation

**Tools:** Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** tauri-reviewer

**How to launch:**
```
"Launch tauri-bundler-specialist to configure Windows MSI installer"
"Use tauri-bundler-specialist to setup code signing"
```

#### tauri-security-specialist Agent

**Purpose:** Secure Tauri applications with CSP, capabilities, and security best practices

**When to use:**
- Security audit needed
- CSP configuration
- Capabilities system setup
- Path traversal prevention
- Secure IPC design

**Tools:** Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** tauri-reviewer, tauri-architect

**How to launch:**
```
"Launch tauri-security-specialist to audit application security"
"Use tauri-security-specialist to configure CSP policies"
```

---

## Vue.js Framework Agents

Specialized agents for Vue.js 3 development with Composition API.

### Vue.js Core Agents

#### vue-explorer Agent

**Purpose:** Analyze Vue.js applications - Composition API patterns, reactivity flows, composables

**When to use:**
- Starting Vue feature (understand patterns)
- Unfamiliar with Vue codebase
- Looking for similar composable implementations
- Understanding reactivity system
- Exploring Pinia store patterns

**Tools:** Glob, Grep, Read, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** vue-architect

**How to launch:**
```
"Launch vue-explorer to understand composables structure"
"Use vue-explorer to find existing Pinia store patterns"
```

#### vue-architect Agent

**Purpose:** Design Vue.js application architectures with Composition API and composables

**When to use:**
- Designing complex Vue features
- Need composable design strategy
- Reactivity pattern unclear
- State management decisions
- Component composition strategy

**Tools:** Glob, Grep, Read, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** vue-explorer, vue-implementer

**How to launch:**
```
"Launch vue-architect to design user management feature"
"Use vue-architect to create blueprint for data table component"
```

#### vue-implementer Agent

**Purpose:** Implement Vue.js applications with Composition API and `<script setup>`

**When to use:**
- Building Vue features
- Implementing composables
- Component development
- Reactive state implementation
- Pinia store implementation

**Tools:** Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** vue-architect, vue-composition-specialist

**How to launch:**
```
"Launch vue-implementer to build form component with validation"
"Use vue-implementer to implement user authentication feature"
```

#### vue-tester Agent

**Purpose:** Write comprehensive tests for Vue.js applications - Vitest and Playwright

**When to use:**
- New Vue feature needs tests
- Component testing with Vitest
- E2E testing with Playwright
- Composable testing
- Reactivity testing

**Tools:** Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** vue-implementer

**How to launch:**
```
"Launch vue-tester to create component tests"
"Use vue-tester to write E2E tests for checkout flow"
```

#### vue-reviewer Agent

**Purpose:** Review Vue.js code for reactivity patterns, performance, and best practices

**When to use:**
- Before committing Vue code
- Reactivity pattern review
- Performance optimization needed
- Composition API usage audit
- State management review

**Tools:** Read, Grep, Glob
**Model:** Sonnet
**Works with:** vue-performance-optimizer

**How to launch:**
```
"Launch vue-reviewer to review component reactivity"
"Use vue-reviewer to audit composables usage"
```

### Vue.js Specialized Agents

#### vue-composition-specialist Agent

**Purpose:** Advanced Composition API patterns, composables, and reactive programming

**When to use:**
- Complex composable design
- Advanced reactivity patterns
- Composable composition
- Dependency injection patterns
- Lifecycle optimization

**Tools:** Glob, Grep, Read, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** vue-implementer, vue-architect

**How to launch:**
```
"Launch vue-composition-specialist to design advanced composable"
"Use vue-composition-specialist to optimize reactive dependencies"
```

#### vue-performance-optimizer Agent

**Purpose:** Optimize Vue.js reactivity, rendering, and bundle size

**When to use:**
- Performance issues in Vue app
- Reactivity optimization needed
- Bundle size too large
- Rendering performance problems
- Memory leak investigation

**Tools:** Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** vue-reviewer, vue-implementer

**How to launch:**
```
"Launch vue-performance-optimizer to optimize component rendering"
"Use vue-performance-optimizer to reduce bundle size"
```

#### vue-ssr-specialist Agent

**Purpose:** Nuxt.js SSR/SSG expertise, server composables, and data fetching

**When to use:**
- Nuxt.js application development
- SSR/SSG implementation
- Server-side data fetching
- Universal rendering
- SEO optimization

**Tools:** Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** vue-implementer, vue-architect

**How to launch:**
```
"Launch vue-ssr-specialist to implement SSR data fetching"
"Use vue-ssr-specialist to optimize Nuxt.js build"
```

#### vue-accessibility-specialist Agent

**Purpose:** Ensure Vue.js applications are accessible with ARIA, semantic HTML, and WCAG compliance

**When to use:**
- Accessibility audit needed
- ARIA implementation
- Keyboard navigation
- Screen reader support
- WCAG 2.1 AA compliance

**Tools:** Glob, Grep, Read, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** vue-implementer, vue-reviewer

**How to launch:**
```
"Launch vue-accessibility-specialist to audit form accessibility"
"Use vue-accessibility-specialist to add ARIA labels"
```

---

## Svelte Framework Agents

Specialized agents for Svelte 5 development with runes-based reactivity.

### Svelte Core Agents

#### svelte-explorer Agent

**Purpose:** Analyze Svelte applications - runes patterns, component structure, SvelteKit routing

**When to use:**
- Starting Svelte feature (understand patterns)
- Unfamiliar with Svelte 5 runes
- Looking for similar implementations
- Understanding reactivity with runes
- Exploring SvelteKit routes

**Tools:** Glob, Grep, Read, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** svelte-architect

**How to launch:**
```
"Launch svelte-explorer to understand runes usage patterns"
"Use svelte-explorer to find existing SvelteKit load functions"
```

#### svelte-architect Agent

**Purpose:** Design Svelte applications with runes, SvelteKit routing, and component architecture

**When to use:**
- Designing complex Svelte features
- Need runes-based design strategy
- SvelteKit routing decisions
- Component composition strategy
- State management with runes

**Tools:** Glob, Grep, Read, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** svelte-explorer, svelte-implementer

**How to launch:**
```
"Launch svelte-architect to design dashboard with runes"
"Use svelte-architect to create blueprint for e-commerce site"
```

#### svelte-implementer Agent

**Purpose:** Implement Svelte applications with runes ($state, $derived, $effect)

**When to use:**
- Building Svelte features
- Implementing with runes
- Component development
- SvelteKit integration
- Form actions implementation

**Tools:** Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** svelte-architect, sveltekit-specialist

**How to launch:**
```
"Launch svelte-implementer to build reactive form with runes"
"Use svelte-implementer to implement data table component"
```

#### svelte-tester Agent

**Purpose:** Write comprehensive tests for Svelte applications - Vitest and Playwright

**When to use:**
- New Svelte feature needs tests
- Component testing with Vitest
- E2E testing with Playwright
- Runes reactivity testing
- SvelteKit integration testing

**Tools:** Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** svelte-implementer

**How to launch:**
```
"Launch svelte-tester to create component tests"
"Use svelte-tester to write E2E tests for user flow"
```

#### svelte-reviewer Agent

**Purpose:** Review Svelte code for runes patterns, compiler optimization, and best practices

**When to use:**
- Before committing Svelte code
- Runes pattern review
- Compiler optimization audit
- Performance review
- Best practices verification

**Tools:** Read, Grep, Glob
**Model:** Sonnet
**Works with:** svelte-compiler-specialist, svelte-performance-optimizer

**How to launch:**
```
"Launch svelte-reviewer to review runes usage"
"Use svelte-reviewer to audit component structure"
```

### Svelte Specialized Agents

#### svelte-compiler-specialist Agent

**Purpose:** Svelte compiler optimization, build output analysis, and compilation strategies

**When to use:**
- Compiler optimization needed
- Build output analysis
- Bundle size investigation
- Compilation strategies
- Advanced compiler features

**Tools:** Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** svelte-performance-optimizer, svelte-reviewer

**How to launch:**
```
"Launch svelte-compiler-specialist to optimize build output"
"Use svelte-compiler-specialist to analyze compilation process"
```

#### svelte-performance-optimizer Agent

**Purpose:** Optimize Svelte bundle size, reactivity, and rendering performance

**When to use:**
- Bundle size too large
- Reactivity performance issues
- Rendering optimization needed
- Memory usage problems
- Load time optimization

**Tools:** Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** svelte-compiler-specialist, svelte-reviewer

**How to launch:**
```
"Launch svelte-performance-optimizer to reduce bundle size"
"Use svelte-performance-optimizer to optimize reactivity"
```

#### sveltekit-specialist Agent

**Purpose:** SvelteKit SSR/SSG, adapters, load functions, form actions, and deployment

**When to use:**
- SvelteKit application development
- SSR/SSG implementation
- Load function design
- Form actions implementation
- Adapter configuration

**Tools:** Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** svelte-implementer, svelte-architect

**How to launch:**
```
"Launch sveltekit-specialist to implement server-side data loading"
"Use sveltekit-specialist to configure Vercel adapter"
```

#### svelte-accessibility-specialist Agent

**Purpose:** Ensure Svelte applications are accessible with WCAG compliance and screen reader support

**When to use:**
- Accessibility audit needed
- ARIA implementation
- Keyboard navigation
- Screen reader compatibility
- WCAG 2.1 AA compliance

**Tools:** Glob, Grep, Read, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** svelte-implementer, svelte-reviewer

**How to launch:**
```
"Launch svelte-accessibility-specialist to audit accessibility"
"Use svelte-accessibility-specialist to add screen reader support"
```

---

## React Native Framework Agents

Specialized agents for React Native mobile development with New Architecture support.

### React Native Core Agents

#### react-native-explorer Agent

**Purpose:** Analyze React Native mobile applications - navigation, native bridges, New Architecture

**When to use:**
- Starting mobile feature (understand patterns)
- Unfamiliar with React Native codebase
- Looking for similar native integrations
- Understanding navigation structure
- Exploring New Architecture usage

**Tools:** Glob, Grep, Read, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** react-native-architect

**How to launch:**
```
"Launch react-native-explorer to understand navigation patterns"
"Use react-native-explorer to find existing native modules"
```

#### react-native-architect Agent

**Purpose:** Design React Native applications with navigation, state management, and native modules

**When to use:**
- Designing complex mobile features
- Navigation flow design
- State management decisions
- Native module architecture
- Cross-platform strategy

**Tools:** Glob, Grep, Read, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** react-native-explorer, react-native-implementer

**How to launch:**
```
"Launch react-native-architect to design checkout flow"
"Use react-native-architect to create blueprint for offline sync"
```

#### react-native-implementer Agent

**Purpose:** Implement React Native applications for iOS and Android with native modules

**When to use:**
- Building mobile features
- iOS/Android implementation
- Native module integration
- New Architecture features
- Cross-platform components

**Tools:** Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** react-native-architect, react-native-platform-specialist

**How to launch:**
```
"Launch react-native-implementer to build user profile screen"
"Use react-native-implementer to implement push notifications"
```

#### react-native-tester Agent

**Purpose:** Write comprehensive tests for React Native - Jest, React Native Testing Library, Detox

**When to use:**
- New mobile feature needs tests
- Unit testing with Jest
- Component testing with RNTL
- E2E testing with Detox
- Integration testing

**Tools:** Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** react-native-implementer

**How to launch:**
```
"Launch react-native-tester to create screen tests"
"Use react-native-tester to write Detox E2E tests"
```

#### react-native-reviewer Agent

**Purpose:** Review React Native code for performance, memory leaks, and platform compatibility

**When to use:**
- Before committing mobile code
- Performance review needed
- Memory leak investigation
- Platform compatibility audit
- New Architecture migration review

**Tools:** Read, Grep, Glob
**Model:** Sonnet
**Works with:** react-native-performance-optimizer

**How to launch:**
```
"Launch react-native-reviewer to review performance"
"Use react-native-reviewer to audit platform compatibility"
```

### React Native Specialized Agents

#### react-native-bridge-specialist Agent

**Purpose:** JSI, TurboModules, Fabric, and native bridge development for New Architecture

**When to use:**
- Native module development
- New Architecture migration
- JSI implementation
- TurboModule creation
- Fabric component development

**Tools:** Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** react-native-implementer, react-native-platform-specialist

**How to launch:**
```
"Launch react-native-bridge-specialist to create TurboModule"
"Use react-native-bridge-specialist to implement JSI module"
```

#### react-native-performance-optimizer Agent

**Purpose:** Optimize React Native rendering, memory usage, and bundle size

**When to use:**
- Performance issues
- Memory leak problems
- Bundle size too large
- Slow rendering
- Startup time optimization

**Tools:** Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** react-native-reviewer, react-native-implementer

**How to launch:**
```
"Launch react-native-performance-optimizer to optimize FlatList"
"Use react-native-performance-optimizer to reduce memory usage"
```

#### react-native-platform-specialist Agent

**Purpose:** iOS and Android platform-specific features, permissions, and native APIs

**When to use:**
- Platform-specific implementations
- iOS/Android native features
- Permission handling
- Deep linking setup
- Platform API integration

**Tools:** Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** react-native-implementer, react-native-bridge-specialist

**How to launch:**
```
"Launch react-native-platform-specialist to implement biometrics"
"Use react-native-platform-specialist to setup deep linking"
```

#### react-native-accessibility-specialist Agent

**Purpose:** Ensure React Native apps are accessible with VoiceOver, TalkBack, and WCAG compliance

**When to use:**
- Accessibility audit needed
- Screen reader support
- Touch target sizing
- Color contrast review
- WCAG 2.1 AA compliance

**Tools:** Glob, Grep, Read, TodoWrite, mcp__deepwiki__ask_question
**Model:** Sonnet
**Works with:** react-native-implementer, react-native-reviewer

**How to launch:**
```
"Launch react-native-accessibility-specialist to audit app accessibility"
"Use react-native-accessibility-specialist to add VoiceOver support"
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

### Example 4: Flutter Feature Development

**Task:** Add user authentication to Flutter app

**Complete Workflow:**
```
Phase 1: Exploration (Parallel)
├─ flutter-explorer → Find existing auth patterns
└─ flutter-explorer → Understand state management

Phase 2: Architecture
└─ flutter-architect → Design authentication flow
   ├─ Widget hierarchy
   ├─ State management (Provider)
   ├─ Navigation flow
   └─ Get user approval

Phase 3: Implementation
└─ flutter-implementer → Build screens and logic
   ├─ Login screen
   ├─ Signup screen
   ├─ Auth provider
   └─ Repository

Phase 4: Testing
└─ flutter-tester → Widget + integration tests

Phase 5: Review & Optimize
├─ flutter-performance-optimizer → Check for performance issues
└─ flutter-reviewer → Final code review
```

### Example 5: Flutter App with Native Camera

**Task:** Integrate native camera access in Flutter

**Workflow with Language Experts:**
```
Phase 1: Research
└─ flutter-platform-integrator → Plan platform channel approach

Phase 2: Design
└─ flutter-architect → Design camera integration architecture

Phase 3: Implementation (Parallel)
├─ dart-expert → Dart MethodChannel interface
├─ kotlin-expert → Android CameraX implementation
└─ swift-expert → iOS AVFoundation implementation

Phase 4: Integration
└─ flutter-platform-integrator → Wire everything together

Phase 5: Testing
└─ flutter-tester → Platform-specific tests

Phase 6: Review
└─ flutter-reviewer → Final review
```

### Example 6: React Feature with SSR

**Task:** Build SEO-optimized product listing page

**Workflow:**
```
Phase 1: Exploration
└─ react-explorer → Understand existing SSR patterns

Phase 2: Architecture
└─ react-architect → Design Server Component architecture

Phase 3: Implementation (Parallel)
├─ react-implementer → Build product listing component
└─ react-ssr-specialist → Set up Server Components

Phase 4: Optimization (Parallel)
├─ react-concurrent-specialist → Add Suspense boundaries
└─ react-performance-optimizer → Optimize bundle size

Phase 5: Accessibility & Testing
├─ react-accessibility-specialist → Ensure WCAG compliance
└─ react-tester → Write comprehensive tests

Phase 6: Review
└─ react-reviewer → Final review
```

### Example 7: TypeScript Migration

**Task:** Migrate React app from JavaScript to TypeScript

**Workflow with Language Experts:**
```
Phase 1: Analysis (Parallel)
├─ javascript-expert → Analyze current JS patterns
└─ typescript-expert → Create migration strategy

Phase 2: Setup
└─ typescript-expert → Configure tsconfig.json

Phase 3: Migration (Parallel)
├─ typescript-expert → Convert utility files
├─ typescript-expert → Create type definitions
└─ react-implementer → Update React components

Phase 4: Type Safety
└─ typescript-expert → Type coverage analysis

Phase 5: Testing
└─ react-tester → Update tests for TypeScript

Phase 6: Review
└─ react-reviewer → Verify hooks and patterns
```

## Framework Agent Decision Tree

### Flutter Development

```
Need to work on Flutter app?
│
├─ Don't know codebase? → flutter-explorer
├─ Need to design feature? → flutter-architect
├─ Ready to implement? → flutter-implementer
├─ Need animations? → flutter-animator
├─ Need native code? → flutter-platform-integrator
├─ Performance issues? → flutter-performance-optimizer
├─ Accessibility needed? → flutter-accessibility-specialist
├─ Need tests? → flutter-tester
└─ Ready to review? → flutter-reviewer

Language specific?
├─ Dart optimization? → dart-expert
├─ Android native? → kotlin-expert
└─ iOS native? → swift-expert
```

### React Development

```
Need to work on React app?
│
├─ Don't know codebase? → react-explorer
├─ Need to design feature? → react-architect
├─ Ready to implement? → react-implementer
├─ Performance issues? → react-performance-optimizer
├─ Need Suspense/concurrent? → react-concurrent-specialist
├─ Need SSR/Next.js? → react-ssr-specialist
├─ Accessibility needed? → react-accessibility-specialist
├─ Need tests? → react-tester
└─ Ready to review? → react-reviewer

Language specific?
├─ TypeScript types? → typescript-expert
└─ JavaScript optimization? → javascript-expert
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
