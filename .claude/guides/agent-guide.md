# Complete Agent Usage Guide

A comprehensive guide to all available agents for autonomous operation in Claude Code.

## Agent Overview

We have **30 specialized agents** total: **7 general custom agents**, **23 framework-specific agents**, plus **3 built-in agents** for comprehensive development workflows.

### General Custom Agents (7)

1. **code-explorer** - Deep codebase analysis
2. **code-architect** - Architecture design
3. **implementation-helper** - Step-by-step implementation
4. **error-resolver** - Debug and fix errors
5. **test-writer** - Write comprehensive tests
6. **doc-writer** - Write documentation
7. **quality-checker** - Code quality review

### Framework-Specific Agents (23)

**Language Experts (5):**
- **dart-expert** - Dart 3.x, null safety, async, isolates
- **typescript-expert** - Advanced types, generics, TS migration
- **javascript-expert** - ES2015+, async patterns, performance
- **kotlin-expert** - Coroutines, Android SDK, platform channels
- **swift-expert** - Swift concurrency, iOS SDK, platform channels

**Flutter Agents (9):**
- **Core (5):** flutter-explorer, flutter-architect, flutter-implementer, flutter-tester, flutter-reviewer
- **Specialized (4):** flutter-animator, flutter-platform-integrator, flutter-performance-optimizer, flutter-accessibility-specialist

**React Agents (9):**
- **Core (5):** react-explorer, react-architect, react-implementer, react-tester, react-reviewer
- **Specialized (4):** react-performance-optimizer, react-concurrent-specialist, react-ssr-specialist, react-accessibility-specialist

### Built-in Agents (3)

1. **Explore** - Fast codebase searching (Haiku-powered)
2. **Plan** - Strategic planning (Haiku-powered)
3. **general-purpose** - Multi-step autonomous tasks

---

## When to Use Which Agent

### General Decision Tree

```
What do you need to do?
│
├─ Understand existing code
│  ├─ Quick search for pattern → Use built-in **Explore** agent
│  ├─ Deep analysis of feature → Use **code-explorer** agent
│  ├─ Flutter-specific → Use **flutter-explorer** agent
│  └─ React-specific → Use **react-explorer** agent
│
├─ Design new feature
│  ├─ Simple addition (<30 lines) → Work directly
│  ├─ Need high-level plan → Use built-in **Plan** agent
│  ├─ General detailed blueprint → Use **code-architect** agent
│  ├─ Flutter architecture → Use **flutter-architect** agent
│  └─ React architecture → Use **react-architect** agent
│
├─ Implement new feature
│  ├─ Simple, clear path → Work directly
│  ├─ General complex implementation → Use **implementation-helper** agent
│  ├─ Flutter step-by-step → Use **flutter-implementer** agent
│  └─ React step-by-step → Use **react-implementer** agent
│
├─ Debug error
│  ├─ Obvious fix → Fix directly
│  ├─ General debugging → Use **error-resolver** agent
│  └─ Complex multi-file error → Use **error-resolver** agent
│
├─ Write tests
│  ├─ Simple function → Write directly
│  ├─ General test suite → Use **test-writer** agent
│  ├─ Flutter tests (widget/integration) → Use **flutter-tester** agent
│  └─ React tests (RTL/Playwright) → Use **react-tester** agent
│
├─ Write documentation
│  ├─ Simple docstring → Write directly
│  └─ Full API/feature docs → Use **doc-writer** agent
│
├─ Review code quality
│  ├─ Quick check → Run /quality-check command
│  ├─ General quality review → Use **quality-checker** agent
│  ├─ Flutter code review → Use **flutter-reviewer** agent
│  └─ React code review → Use **react-reviewer** agent
│
├─ Language-specific work
│  ├─ Dart optimization/patterns → Use **dart-expert** agent
│  ├─ TypeScript migration/types → Use **typescript-expert** agent
│  ├─ JavaScript performance → Use **javascript-expert** agent
│  ├─ Android platform code → Use **kotlin-expert** agent
│  └─ iOS platform code → Use **swift-expert** agent
│
└─ Specialized framework tasks
   ├─ Flutter animations → Use **flutter-animator** agent
   ├─ Flutter platform channels → Use **flutter-platform-integrator** agent
   ├─ Flutter performance → Use **flutter-performance-optimizer** agent
   ├─ Flutter accessibility → Use **flutter-accessibility-specialist** agent
   ├─ React performance → Use **react-performance-optimizer** agent
   ├─ React concurrent features → Use **react-concurrent-specialist** agent
   ├─ React SSR/Next.js → Use **react-ssr-specialist** agent
   └─ React accessibility → Use **react-accessibility-specialist** agent
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

## Framework-Specific Agents

### Language Expert Agents

These agents provide deep expertise in specific programming languages and are used across frameworks for migrations, optimizations, and platform-specific code.

#### 8. dart-expert (Dart Specialist)

**Purpose**: Expert in Dart 3.x language features, null safety, async patterns, isolates, and FFI

**Use when:**
- Writing Dart-specific code requiring advanced features
- Optimizing Dart code for performance
- Implementing isolate-based concurrency
- Using FFI for native library integration
- Migrating to null safety
- Leveraging Dart 3.x features (Records, Patterns, Sealed classes)

**Capabilities:**
- Dart 3.x features (Records, Patterns, Sealed classes, Class modifiers)
- Null safety patterns and migration
- Advanced async (Future, Stream, async*, sync*)
- Isolate communication patterns
- FFI (Foreign Function Interface)
- Extension methods and mixins
- Research via deepwiki (never websearch)

**Tools**: Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model**: Sonnet

**Example invocation:**
```
"Launch dart-expert to optimize this Dart code using isolates"
"Use dart-expert to migrate this code to null safety"
"dart-expert help me implement FFI bindings for this native library"
```

**Works with**: flutter-implementer, flutter-performance-optimizer

---

#### 9. typescript-expert (TypeScript Specialist)

**Purpose**: Expert in TypeScript type system, generics, conditional types, and JS→TS migration

**Use when:**
- Implementing complex TypeScript types
- Migrating JavaScript code to TypeScript
- Optimizing tsconfig settings
- Working with advanced generics
- Type inference problems
- Conditional/mapped types needed

**Capabilities:**
- Advanced type system (conditional types, mapped types, template literals)
- Generics and type inference
- JS→TS migration strategies
- tsconfig optimization
- Type narrowing and guards
- Utility types and custom transformations
- Research via deepwiki (never websearch)

**Tools**: Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model**: Sonnet

**Example invocation:**
```
"Launch typescript-expert to migrate this JavaScript module to TypeScript"
"typescript-expert help design these complex generic types"
"Use typescript-expert to optimize our tsconfig settings"
```

**Works with**: react-implementer, react-architect

---

#### 10. javascript-expert (JavaScript Specialist)

**Purpose**: Expert in modern JavaScript (ES2015+), async patterns, performance optimization

**Use when:**
- Optimizing JavaScript performance
- Complex async/await patterns
- Event loop understanding needed
- Memory leak detection
- Module system issues (ESM, CommonJS)
- V8 optimization patterns

**Capabilities:**
- ES2015+ features
- Async patterns (callbacks, Promises, async/await)
- Event loop and microtasks
- Memory management
- V8 optimization patterns
- Module systems (ESM, CommonJS, UMD)
- Research via deepwiki (never websearch)

**Tools**: Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model**: Sonnet

**Example invocation:**
```
"Launch javascript-expert to optimize this async code"
"javascript-expert help debug this memory leak"
"Use javascript-expert to refactor these nested callbacks"
```

**Works with**: react-implementer, react-performance-optimizer

---

#### 11. kotlin-expert (Kotlin/Android Specialist)

**Purpose**: Expert in Kotlin coroutines, Android SDK, and Flutter Android platform channels

**Use when:**
- Writing Android platform channel code
- Implementing Kotlin coroutines
- Android-specific features for Flutter
- Kotlin → Dart interop
- Android SDK integration

**Capabilities:**
- Kotlin coroutines and Flow
- Android SDK patterns
- Platform channels (MethodChannel, EventChannel)
- Kotlin → Dart type mapping
- Android lifecycle integration
- Gradle configuration
- Research via deepwiki (never websearch)

**Tools**: Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model**: Sonnet

**Example invocation:**
```
"Launch kotlin-expert to implement Android platform channel for camera"
"kotlin-expert help integrate this Android SDK feature"
"Use kotlin-expert to optimize these coroutines"
```

**Works with**: flutter-platform-integrator, dart-expert

---

#### 12. swift-expert (Swift/iOS Specialist)

**Purpose**: Expert in Swift concurrency, iOS SDK, and Flutter iOS platform channels

**Use when:**
- Writing iOS platform channel code
- Implementing Swift async/await
- iOS-specific features for Flutter
- Swift → Dart interop
- iOS SDK integration

**Capabilities:**
- Swift concurrency (async/await, actors, tasks)
- iOS SDK patterns
- Platform channels (MethodChannel, EventChannel)
- Swift → Dart type mapping
- iOS lifecycle integration
- Xcode/CocoaPods configuration
- Research via deepwiki (never websearch)

**Tools**: Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model**: Sonnet

**Example invocation:**
```
"Launch swift-expert to implement iOS platform channel for notifications"
"swift-expert help integrate this iOS SDK feature"
"Use swift-expert to optimize these async tasks"
```

**Works with**: flutter-platform-integrator, dart-expert

---

#### 13. rust-expert (Rust/Tauri Specialist)

**Purpose**: Expert in Rust ownership/borrowing, async Tokio, WASM integration, FFI, and Tauri backend development

**Use when:**
- Writing Tauri Rust backend code
- Implementing WASM modules (wasm-bindgen, wasm-pack)
- Complex async operations with Tokio
- FFI (Foreign Function Interface) implementations
- Memory-safe systems programming
- Ownership/borrowing optimization

**Capabilities:**
- Rust ownership, borrowing, lifetimes
- Async runtime (Tokio) patterns
- WASM integration (wasm-bindgen, wasm-pack)
- FFI with C/C++ libraries
- Error handling (Result, thiserror, anyhow)
- Memory safety without garbage collection
- Research via deepwiki (never websearch)

**Tools**: Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model**: Sonnet

**Example invocation:**
```
"Launch rust-expert to implement async Tokio backend for Tauri"
"rust-expert help create WASM module with wasm-bindgen"
"Use rust-expert to optimize Rust ownership patterns"
```

**Works with**: tauri-implementer, tauri-plugin-developer, tauri-ipc-specialist

---

### Flutter Framework Agents

#### Core Flutter Agents (5)

##### 13. flutter-explorer (Flutter Code Analysis)

**Purpose**: Deep analysis of Flutter codebases, widget trees, and state management flows

**Use when:**
- Exploring unfamiliar Flutter codebase
- Understanding widget tree structure
- Tracing state management flows
- Finding Flutter-specific patterns
- Analyzing navigation architecture

**Capabilities:**
- Widget tree tracing
- State management analysis (Provider, Riverpod, BLoC, etc.)
- Navigation flow mapping
- Build context understanding
- Performance bottleneck identification
- Research via deepwiki (never websearch)

**Tools**: Glob, Grep, Read, TodoWrite, mcp__deepwiki__ask_question
**Model**: Sonnet

**Example invocation:**
```
"Launch flutter-explorer to analyze the authentication flow"
"flutter-explorer trace the widget tree for the home screen"
"Use flutter-explorer to understand how state is managed"
```

**Works with**: flutter-architect, dart-expert

---

##### 14. flutter-architect (Flutter Architecture Design)

**Purpose**: Design Flutter feature architectures with complete blueprints

**Use when:**
- Designing new Flutter features
- Architecting state management
- Planning navigation structure
- Designing data layer
- Multi-screen feature design

**Capabilities:**
- Widget hierarchy design
- State management architecture
- Navigation structure
- Data layer design
- Build sequences and dependencies
- Integration patterns
- Research via deepwiki (never websearch)

**Tools**: Glob, Grep, Read, TodoWrite, mcp__deepwiki__ask_question
**Model**: Sonnet

**Example invocation:**
```
"Launch flutter-architect to design the shopping cart feature"
"flutter-architect design state management for user profile"
"Use flutter-architect to plan the navigation architecture"
```

**Works with**: flutter-implementer, dart-expert

---

##### 15. flutter-implementer (Flutter Implementation)

**Purpose**: Step-by-step Flutter implementation with complete, production-ready code

**Use when:**
- Implementing complex Flutter features
- Need guided implementation
- Want to ensure completeness (no TODOs)
- Multi-file Flutter implementations
- Following architecture blueprint

**Capabilities:**
- Complete widget implementations
- State management integration
- Navigation implementation
- API integration
- Form handling and validation
- Error handling patterns
- NO TODO markers (complete code only)
- Research via deepwiki (never websearch)

**Tools**: Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model**: Sonnet

**Example invocation:**
```
"Launch flutter-implementer to build the authentication screens"
"flutter-implementer implement the product listing feature"
"Use flutter-implementer to create the settings page"
```

**Works with**: flutter-architect, flutter-tester, dart-expert

---

##### 16. flutter-tester (Flutter Testing)

**Purpose**: Write comprehensive Flutter test suites (widget, unit, integration)

**Use when:**
- Writing Flutter widget tests
- Creating integration tests
- Need >80% test coverage
- Testing state management
- Golden tests for UI

**Capabilities:**
- Widget tests (WidgetTester)
- Unit tests for business logic
- Integration tests (IntegrationTestWidgetsFlutterBinding)
- Golden tests for UI verification
- Mock setup (mockito, mocktail)
- Test coverage analysis
- Research via deepwiki (never websearch)

**Tools**: Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model**: Sonnet

**Example invocation:**
```
"Launch flutter-tester to write tests for the login screen"
"flutter-tester create integration tests for checkout flow"
"Use flutter-tester to achieve 80% coverage on user service"
```

**Works with**: flutter-implementer, dart-expert

---

##### 17. flutter-reviewer (Flutter Code Review)

**Purpose**: Review Flutter code for quality, performance, and best practices

**Use when:**
- Before committing Flutter code
- After feature implementation
- Need Flutter-specific quality check
- Checking widget performance
- Verifying Flutter patterns

**Capabilities:**
- Flutter best practices verification
- Widget rebuild optimization
- State management review
- Performance issue detection
- Accessibility check
- Confidence scoring (≥80%)
- Research via deepwiki (never websearch)

**Tools**: Read, Grep, Glob
**Model**: Sonnet

**Example invocation:**
```
"Launch flutter-reviewer to review the shopping cart implementation"
"flutter-reviewer check this widget for performance issues"
"Use flutter-reviewer before committing this feature"
```

**Works with**: flutter-implementer, flutter-performance-optimizer

---

#### Specialized Flutter Agents (4)

##### 18. flutter-animator (Animation Specialist)

**Purpose**: Expert in Flutter animations - AnimationController, Tween, implicit/explicit animations

**Use when:**
- Implementing complex animations
- Custom animation curves needed
- Multiple coordinated animations
- Physics-based animations
- Rive/Lottie integration

**Capabilities:**
- AnimationController patterns
- Tween animations
- Implicit vs explicit animations
- Hero animations
- Staggered animations
- Custom curves and physics
- Rive/Lottie integration
- Research via deepwiki (never websearch)

**Tools**: Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model**: Sonnet

**Example invocation:**
```
"Launch flutter-animator to create the page transition animation"
"flutter-animator implement staggered list animations"
"Use flutter-animator to add physics-based scroll effects"
```

**Works with**: flutter-implementer, flutter-performance-optimizer

---

##### 19. flutter-platform-integrator (Platform Channel Specialist)

**Purpose**: Expert in platform channels (MethodChannel, EventChannel) and FFI for native integration

**Use when:**
- Implementing platform channels
- Integrating native Android/iOS code
- FFI for native libraries
- Accessing platform-specific APIs
- Native module integration

**Capabilities:**
- MethodChannel implementation
- EventChannel for streams
- FFI (Foreign Function Interface)
- Platform-specific code organization
- Type marshaling between Dart/Kotlin/Swift
- Native module integration
- Research via deepwiki (never websearch)

**Tools**: Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model**: Sonnet

**Example invocation:**
```
"Launch flutter-platform-integrator to add camera functionality"
"flutter-platform-integrator implement native notifications"
"Use flutter-platform-integrator to integrate this native SDK"
```

**Works with**: kotlin-expert, swift-expert, dart-expert

---

##### 20. flutter-performance-optimizer (Performance Specialist)

**Purpose**: Expert in Flutter performance optimization using DevTools, widget rebuilds, and isolates

**Use when:**
- App performance issues
- Excessive widget rebuilds
- Memory leaks
- Slow animations (jank)
- Large list rendering
- Background processing needed

**Capabilities:**
- DevTools profiling
- Widget rebuild optimization
- RepaintBoundary usage
- Isolate-based computation
- Image optimization
- Build method optimization
- Memory leak detection
- Research via deepwiki (never websearch)

**Tools**: Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model**: Sonnet

**Example invocation:**
```
"Launch flutter-performance-optimizer to fix these frame drops"
"flutter-performance-optimizer optimize this list rendering"
"Use flutter-performance-optimizer to reduce widget rebuilds"
```

**Works with**: dart-expert, flutter-implementer, flutter-reviewer

---

##### 21. flutter-accessibility-specialist (Accessibility Expert)

**Purpose**: Expert in Flutter accessibility - Semantics, screen readers, WCAG compliance

**Use when:**
- Making app accessible
- Screen reader support needed
- WCAG 2.1 AA compliance required
- Accessibility audit
- Supporting assistive technologies

**Capabilities:**
- Semantics widget usage
- Screen reader testing (TalkBack, VoiceOver)
- WCAG 2.1 AA compliance
- Color contrast checking
- Focus management
- Accessible navigation
- Research via deepwiki (never websearch)

**Tools**: Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model**: Sonnet

**Example invocation:**
```
"Launch flutter-accessibility-specialist to make this screen accessible"
"flutter-accessibility-specialist audit accessibility compliance"
"Use flutter-accessibility-specialist to fix screen reader issues"
```

**Works with**: flutter-implementer, flutter-reviewer

---

### React Framework Agents

#### Core React Agents (5)

##### 22. react-explorer (React Code Analysis)

**Purpose**: Deep analysis of React codebases, component trees, and hooks patterns

**Use when:**
- Exploring unfamiliar React codebase
- Understanding component hierarchy
- Tracing state management flows
- Finding React patterns
- Analyzing data fetching strategies

**Capabilities:**
- Component tree tracing
- Hooks usage analysis
- State management patterns (Redux, Context, Zustand, etc.)
- Data fetching patterns (React Query, SWR, etc.)
- Performance bottleneck identification
- Research via deepwiki (never websearch)

**Tools**: Glob, Grep, Read, TodoWrite, mcp__deepwiki__ask_question
**Model**: Sonnet

**Example invocation:**
```
"Launch react-explorer to analyze the authentication flow"
"react-explorer trace component hierarchy for dashboard"
"Use react-explorer to understand how data fetching works"
```

**Works with**: react-architect, typescript-expert, javascript-expert

---

##### 23. react-architect (React Architecture Design)

**Purpose**: Design React feature architectures with complete blueprints

**Use when:**
- Designing new React features
- Architecting state management
- Planning component structure
- Designing data layer
- Multi-component feature design

**Capabilities:**
- Component hierarchy design
- State management architecture
- Data fetching strategy
- Route structure design
- Build sequences and dependencies
- Integration patterns
- Research via deepwiki (never websearch)

**Tools**: Glob, Grep, Read, TodoWrite, mcp__deepwiki__ask_question
**Model**: Sonnet

**Example invocation:**
```
"Launch react-architect to design the e-commerce product pages"
"react-architect design state management for user dashboard"
"Use react-architect to plan the routing architecture"
```

**Works with**: react-implementer, typescript-expert

---

##### 24. react-implementer (React Implementation)

**Purpose**: Step-by-step React implementation with complete, production-ready code

**Use when:**
- Implementing complex React features
- Need guided implementation
- Want to ensure completeness (no TODOs)
- Multi-file React implementations
- Following architecture blueprint

**Capabilities:**
- Complete component implementations
- Proper hooks usage (useState, useEffect, useCallback, useMemo, etc.)
- State management integration
- Form handling (React Hook Form, Formik)
- API integration
- Error boundaries
- NO TODO markers (complete code only)
- Research via deepwiki (never websearch)

**Tools**: Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model**: Sonnet

**Example invocation:**
```
"Launch react-implementer to build the user profile components"
"react-implementer implement the shopping cart functionality"
"Use react-implementer to create the admin dashboard"
```

**Works with**: react-architect, react-tester, typescript-expert

---

##### 25. react-tester (React Testing)

**Purpose**: Write comprehensive React test suites (Jest, React Testing Library, Playwright)

**Use when:**
- Writing React component tests
- Creating integration tests
- Need >80% test coverage
- E2E testing with Playwright
- Testing hooks

**Capabilities:**
- Component tests (React Testing Library)
- Unit tests with Jest
- Integration tests
- E2E tests (Playwright)
- Hooks testing (@testing-library/react-hooks)
- Mock setup (MSW, jest.mock)
- Test coverage analysis
- Research via deepwiki (never websearch)

**Tools**: Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model**: Sonnet

**Example invocation:**
```
"Launch react-tester to write tests for the login component"
"react-tester create E2E tests for checkout flow"
"Use react-tester to achieve 80% coverage on user hooks"
```

**Works with**: react-implementer, typescript-expert

---

##### 26. react-reviewer (React Code Review)

**Purpose**: Review React code for quality, performance, and best practices

**Use when:**
- Before committing React code
- After feature implementation
- Need React-specific quality check
- Checking component performance
- Verifying React patterns

**Capabilities:**
- React best practices verification
- Hooks usage review
- Component re-render optimization
- State management review
- Performance issue detection
- Accessibility check
- Confidence scoring (≥80%)
- Research via deepwiki (never websearch)

**Tools**: Read, Grep, Glob
**Model**: Sonnet

**Example invocation:**
```
"Launch react-reviewer to review the product listing implementation"
"react-reviewer check these components for performance issues"
"Use react-reviewer before committing this feature"
```

**Works with**: react-implementer, react-performance-optimizer

---

#### Specialized React Agents (4)

##### 27. react-performance-optimizer (Performance Specialist)

**Purpose**: Expert in React performance - React Compiler, memoization, bundle optimization

**Use when:**
- React app performance issues
- Excessive re-renders
- Bundle size too large
- Slow rendering
- Memory leaks
- Need React Compiler optimization

**Capabilities:**
- React Compiler integration
- useMemo and useCallback optimization
- React.memo usage
- Code splitting strategies
- Bundle analysis and optimization
- Virtual scrolling (react-window, react-virtualized)
- Memory leak detection
- Research via deepwiki (never websearch)

**Tools**: Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model**: Sonnet

**Example invocation:**
```
"Launch react-performance-optimizer to fix these re-render issues"
"react-performance-optimizer optimize bundle size"
"Use react-performance-optimizer to reduce memory usage"
```

**Works with**: javascript-expert, typescript-expert, react-implementer

---

##### 28. react-concurrent-specialist (Concurrent Features Expert)

**Purpose**: Expert in React concurrent features - startTransition, Suspense, useOptimistic

**Use when:**
- Implementing concurrent features
- Need responsive UI during updates
- Suspense boundaries needed
- Optimistic UI updates
- Server Components coordination

**Capabilities:**
- startTransition and useTransition
- Suspense boundaries
- useOptimistic for optimistic updates
- useDeferredValue
- Concurrent rendering patterns
- Error boundaries with Suspense
- Research via deepwiki (never websearch)

**Tools**: Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model**: Sonnet

**Example invocation:**
```
"Launch react-concurrent-specialist to add Suspense boundaries"
"react-concurrent-specialist implement optimistic UI updates"
"Use react-concurrent-specialist to make this UI more responsive"
```

**Works with**: react-implementer, react-ssr-specialist

---

##### 29. react-ssr-specialist (SSR/SSG Expert)

**Purpose**: Expert in Server Components, SSR/SSG, Next.js, and hydration

**Use when:**
- Implementing Server Components
- Setting up Next.js App Router
- SSR/SSG configuration
- Hydration issues
- SEO optimization needed

**Capabilities:**
- Server Components patterns
- Next.js App Router
- SSR (renderToReadableStream)
- SSG and ISR (Incremental Static Regeneration)
- Hydration optimization
- Metadata API for SEO
- Route handlers and Server Actions
- Research via deepwiki (never websearch)

**Tools**: Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model**: Sonnet

**Example invocation:**
```
"Launch react-ssr-specialist to set up Next.js App Router"
"react-ssr-specialist implement Server Components for this page"
"Use react-ssr-specialist to fix hydration errors"
```

**Works with**: react-implementer, react-concurrent-specialist, typescript-expert

---

##### 30. react-accessibility-specialist (Accessibility Expert)

**Purpose**: Expert in React accessibility - ARIA, semantic HTML, keyboard navigation, WCAG

**Use when:**
- Making React app accessible
- Screen reader support needed
- WCAG 2.1 AA compliance required
- Accessibility audit
- Keyboard navigation implementation

**Capabilities:**
- ARIA attributes (aria-label, aria-describedby, roles)
- Semantic HTML in JSX
- Keyboard navigation (focus management, tab order)
- Screen reader testing (NVDA, JAWS, VoiceOver)
- WCAG 2.1 AA compliance
- Color contrast checking
- Research via deepwiki (never websearch)

**Tools**: Glob, Grep, Read, Bash, BashOutput, TodoWrite, mcp__deepwiki__ask_question
**Model**: Sonnet

**Example invocation:**
```
"Launch react-accessibility-specialist to make this modal accessible"
"react-accessibility-specialist audit accessibility compliance"
"Use react-accessibility-specialist to fix keyboard navigation"
```

**Works with**: react-implementer, react-reviewer

---

### Tauri Framework Agents

Desktop application development with Rust backends, IPC patterns, and security-first architecture.

**Core Agents (5):**
- **tauri-explorer** - Analyze Tauri apps, IPC flows, commands, plugins
- **tauri-architect** - Design Tauri architecture, command patterns, security model
- **tauri-implementer** - Implement Rust backends + frontend integration
- **tauri-tester** - Rust unit tests, WebDriver E2E tests
- **tauri-reviewer** - Security review, CSP compliance, quality check

**Specialized Agents (4):**
- **tauri-plugin-developer** - Create custom Tauri plugins (Rust + JS)
- **tauri-ipc-specialist** - Optimize IPC patterns, commands, events
- **tauri-bundler-specialist** - Platform installers (MSI, DMG, AppImage)
- **tauri-security-specialist** - CSP, capabilities, path traversal prevention

**When to use:**
- Building desktop applications with web technologies
- Need Rust backend for performance or system access
- Require strong security model
- Cross-platform desktop app development

**Works with**: rust-expert for complex Rust operations

---

### Vue.js Framework Agents

Modern web development with Composition API, reactivity system, and Nuxt.js SSR/SSG.

**Core Agents (5):**
- **vue-explorer** - Analyze Vue apps, Composition API patterns, reactivity flows
- **vue-architect** - Design Vue architecture, composables, state management
- **vue-implementer** - Implement with Composition API and `<script setup>`
- **vue-tester** - Vitest component tests, Playwright E2E
- **vue-reviewer** - Review reactivity patterns, performance, best practices

**Specialized Agents (4):**
- **vue-composition-specialist** - Advanced Composition API patterns
- **vue-performance-optimizer** - Reactivity optimization, bundle size reduction
- **vue-ssr-specialist** - Nuxt.js SSR/SSG, server composables
- **vue-accessibility-specialist** - WCAG compliance, ARIA, semantic HTML

**When to use:**
- Building Vue.js 3 applications
- Need Composition API expertise
- Implementing reactive state management
- Server-side rendering with Nuxt.js

**Works with**: typescript-expert, javascript-expert

---

### Svelte Framework Agents

Compiler-first framework with runes-based reactivity, SvelteKit, and zero runtime overhead.

**Core Agents (5):**
- **svelte-explorer** - Analyze Svelte apps, runes patterns, component structure
- **svelte-architect** - Design Svelte architecture, SvelteKit routing
- **svelte-implementer** - Implement with runes ($state, $derived, $effect)
- **svelte-tester** - Vitest component tests, Playwright E2E
- **svelte-reviewer** - Review runes patterns, compiler optimization

**Specialized Agents (4):**
- **svelte-compiler-specialist** - Compiler optimization, build output analysis
- **svelte-performance-optimizer** - Bundle size, reactivity optimization
- **sveltekit-specialist** - SvelteKit SSR/SSG, adapters, deployment
- **svelte-accessibility-specialist** - WCAG compliance, screen readers

**When to use:**
- Building Svelte 5 applications with runes
- Need minimal bundle size
- Implementing reactive UI without virtual DOM
- SvelteKit full-stack applications

**Works with**: typescript-expert, javascript-expert

---

### React Native Framework Agents

Mobile app development for iOS and Android with New Architecture (JSI, Fabric, TurboModules).

**Core Agents (5):**
- **react-native-explorer** - Analyze mobile apps, navigation, native bridges
- **react-native-architect** - Design navigation, state, native modules
- **react-native-implementer** - Implement iOS/Android features
- **react-native-tester** - Jest, React Native Testing Library, Detox E2E
- **react-native-reviewer** - Review performance, memory, platform compatibility

**Specialized Agents (4):**
- **react-native-bridge-specialist** - JSI, TurboModules, Fabric, native bridges
- **react-native-performance-optimizer** - Rendering, memory, bundle optimization
- **react-native-platform-specialist** - iOS/Android features, permissions, deep linking
- **react-native-accessibility-specialist** - VoiceOver, TalkBack, WCAG mobile

**When to use:**
- Building cross-platform mobile applications
- Need native module integration
- Implementing New Architecture features
- Performance-critical mobile apps

**Works with**: typescript-expert, kotlin-expert (Android), swift-expert (iOS)

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

### General Workflows

#### Workflow 1: New Complex Feature (General)

1. **code-explorer**: Understand existing patterns
2. **code-architect**: Design architecture
3. **implementation-helper**: Implement step-by-step
4. **test-writer**: Write comprehensive tests
5. **doc-writer**: Document feature
6. **quality-checker**: Final review

#### Workflow 2: Debug Complex Error (General)

1. **error-resolver**: Identify root cause
2. **test-writer**: Add test that reproduces bug
3. Fix implementation
4. **quality-checker**: Verify fix

#### Workflow 3: Refactoring (General)

1. **test-writer**: Ensure tests exist first
2. **code-explorer**: Understand current implementation
3. **code-architect**: Design better approach
4. **implementation-helper**: Refactor step-by-step
5. **quality-checker**: Verify quality maintained

---

### Flutter Development Workflows

#### Workflow 4: New Flutter Feature (User Authentication)

**Goal**: Add complete user authentication to Flutter app

**Phase 1: Discovery & Design** (Parallel Execution)
```
Launch in parallel:
1. flutter-explorer → Analyze existing auth patterns in codebase
2. dart-expert → Review Dart best practices for auth
```

**Phase 2: Architecture Design**
```
3. flutter-architect → Design complete authentication architecture
   - Widget hierarchy (LoginScreen, SignupScreen, ForgotPasswordScreen)
   - State management (Provider/Riverpod/BLoC choice)
   - Navigation flow
   - Data layer (AuthService, AuthRepository)
   - Token storage strategy
```

**Phase 3: Implementation**
```
4. flutter-implementer → Implement authentication feature
   - Following architecture blueprint
   - Complete widgets with no TODOs
   - Proper error handling
   - Form validation
```

**Phase 4: Testing**
```
5. flutter-tester → Write comprehensive tests
   - Widget tests for all screens
   - Unit tests for AuthService
   - Integration tests for full flow
   - Target: >80% coverage
```

**Phase 5: Quality & Optimization** (Parallel Execution)
```
Launch in parallel:
6. flutter-performance-optimizer → Check for widget rebuild issues
7. flutter-accessibility-specialist → Ensure accessibility compliance
8. flutter-reviewer → Final code review with confidence scoring
```

**Result**: Production-ready authentication feature with tests, optimized, accessible

---

#### Workflow 5: Flutter Native Integration (Camera Feature)

**Goal**: Add native camera functionality to Flutter app

**Phase 1: Platform Analysis** (Parallel Execution)
```
Launch in parallel:
1. flutter-explorer → Find existing platform channel patterns
2. kotlin-expert → Review Android camera APIs
3. swift-expert → Review iOS camera APIs
```

**Phase 2: Architecture & Platform Design**
```
4. flutter-platform-integrator → Design platform channel architecture
   - MethodChannel structure
   - Type marshaling between Dart/Kotlin/Swift
   - Error handling across platforms
   - Permissions handling
```

**Phase 3: Native Implementation** (Parallel Execution)
```
Launch in parallel:
5. kotlin-expert → Implement Android camera channel
   - CameraX integration
   - Kotlin coroutines for async operations
   - Proper lifecycle handling

6. swift-expert → Implement iOS camera channel
   - AVFoundation integration
   - Swift async/await for operations
   - Proper permission requests
```

**Phase 4: Dart Integration**
```
7. flutter-implementer → Implement Dart side
   - Platform channel communication
   - Widget integration
   - Error handling
   - Permission checking
```

**Phase 5: Testing & Review**
```
8. flutter-tester → Write tests for all layers
9. flutter-reviewer → Review complete integration
```

**Result**: Native camera feature working on both Android and iOS

---

#### Workflow 6: Flutter Performance Optimization

**Goal**: Fix performance issues in existing Flutter app

**Phase 1: Analysis**
```
1. flutter-performance-optimizer → Profile app with DevTools
   - Identify widget rebuild hotspots
   - Find memory leaks
   - Measure frame rendering times
```

**Phase 2: Dart Optimization** (If Needed)
```
2. dart-expert → Optimize Dart code
   - Use isolates for heavy computation
   - Optimize async patterns
   - Improve data structures
```

**Phase 3: Implementation**
```
3. flutter-implementer → Apply optimizations
   - Add RepaintBoundary widgets
   - Optimize build methods
   - Implement const constructors
   - Add keys where needed
```

**Phase 4: Verification**
```
4. flutter-tester → Ensure tests still pass
5. flutter-performance-optimizer → Re-profile to measure improvement
6. flutter-reviewer → Code review optimizations
```

**Result**: Measurably faster app with no regressions

---

### React Development Workflows

#### Workflow 7: New React Feature (Product Catalog with SSR)

**Goal**: Build SEO-optimized product catalog with Server Components

**Phase 1: Discovery & Design** (Parallel Execution)
```
Launch in parallel:
1. react-explorer → Analyze existing patterns in codebase
2. typescript-expert → Review TypeScript patterns for types
```

**Phase 2: Architecture Design**
```
3. react-architect → Design product catalog architecture
   - Component hierarchy
   - Server vs Client Components breakdown
   - Data fetching strategy
   - Route structure
   - State management approach
```

**Phase 3: SSR Setup** (If New Project)
```
4. react-ssr-specialist → Set up Next.js App Router
   - Server Components configuration
   - Metadata API for SEO
   - Route handlers
```

**Phase 4: Implementation** (Parallel Execution)
```
Launch in parallel:
5. react-implementer → Build product catalog components
   - Server Components for product listing
   - Client Components for interactive elements
   - Proper hooks usage

6. react-concurrent-specialist → Add Suspense boundaries
   - Loading states
   - Error boundaries
   - Streaming SSR optimization
```

**Phase 5: Performance Optimization**
```
7. react-performance-optimizer → Optimize bundle and rendering
   - Code splitting
   - React Compiler integration
   - Image optimization
   - Bundle analysis
```

**Phase 6: Testing & Quality** (Parallel Execution)
```
Launch in parallel:
8. react-tester → Write comprehensive tests
9. react-accessibility-specialist → Ensure accessibility
10. react-reviewer → Final code review
```

**Result**: SEO-optimized, performant product catalog with SSR

---

#### Workflow 8: React Performance Optimization

**Goal**: Fix slow rendering and large bundle size

**Phase 1: Analysis** (Parallel Execution)
```
Launch in parallel:
1. react-performance-optimizer → Profile React app
   - Identify re-render issues
   - Analyze bundle size
   - Find memory leaks

2. javascript-expert → Profile JavaScript performance
   - Event loop analysis
   - Memory usage patterns
```

**Phase 2: Implementation**
```
3. react-implementer → Apply optimizations
   - Add useMemo/useCallback
   - Implement React.memo
   - Code splitting
   - Lazy loading
```

**Phase 3: Bundle Optimization**
```
4. react-performance-optimizer → Optimize bundle
   - Tree shaking
   - Dynamic imports
   - Vendor splitting
```

**Phase 4: Verification** (Parallel Execution)
```
Launch in parallel:
5. react-tester → Ensure tests pass
6. react-performance-optimizer → Re-measure performance
7. react-reviewer → Review optimizations
```

**Result**: Faster rendering and smaller bundle size

---

#### Workflow 9: Add React Concurrent Features

**Goal**: Make UI more responsive with concurrent rendering

**Phase 1: Analysis**
```
1. react-explorer → Identify slow UI interactions
2. react-concurrent-specialist → Design concurrent rendering strategy
```

**Phase 2: Implementation**
```
3. react-implementer → Add concurrent features
   - startTransition for non-urgent updates
   - useTransition for loading states
   - useDeferredValue for expensive renders
```

**Phase 3: Suspense Integration**
```
4. react-concurrent-specialist → Add Suspense boundaries
   - Proper fallback components
   - Error boundaries
   - Coordinate with SSR if applicable
```

**Phase 4: Testing**
```
5. react-tester → Test concurrent behavior
6. react-reviewer → Review implementation
```

**Result**: More responsive UI with better user experience

---

### Cross-Framework Workflows

#### Workflow 10: JavaScript → TypeScript Migration

**Goal**: Migrate entire codebase from JavaScript to TypeScript

**Phase 1: Planning**
```
1. typescript-expert → Create migration strategy
   - File-by-file migration order
   - tsconfig.json configuration
   - Type definition strategy
```

**Phase 2: Infrastructure**
```
2. typescript-expert → Set up TypeScript infrastructure
   - Install dependencies
   - Configure tsconfig
   - Set up type checking in CI
```

**Phase 3: Migration** (Parallel Execution)
```
Launch in parallel (multiple typescript-expert agents):
3. typescript-expert (agent 1) → Migrate core modules
4. typescript-expert (agent 2) → Migrate UI components
5. typescript-expert (agent 3) → Migrate utilities
```

**Phase 4: Type Safety**
```
6. typescript-expert → Eliminate 'any' types
7. typescript-expert → Add proper generics
8. typescript-expert → Optimize type inference
```

**Phase 5: Testing & Review**
```
9. test-writer → Ensure all tests pass with TypeScript
10. quality-checker → Review migration quality
```

**Result**: Fully typed TypeScript codebase

---

#### Workflow 11: Flutter + React Shared Business Logic

**Goal**: Share authentication logic between Flutter and React apps

**Phase 1: Analysis** (Parallel Execution)
```
Launch in parallel:
1. flutter-explorer → Analyze Flutter auth implementation
2. react-explorer → Analyze React auth implementation
3. dart-expert → Review Dart auth patterns
4. typescript-expert → Review TypeScript auth patterns
```

**Phase 2: API Design**
```
5. code-architect → Design shared REST/GraphQL API
   - Auth endpoints
   - Token refresh strategy
   - Error handling
   - Type definitions for both platforms
```

**Phase 3: Implementation** (Parallel Execution)
```
Launch in parallel:
6. flutter-implementer → Implement Flutter auth client
7. react-implementer → Implement React auth client
Both following same API spec but platform-specific best practices
```

**Phase 4: Testing** (Parallel Execution)
```
Launch in parallel:
8. flutter-tester → Test Flutter auth
9. react-tester → Test React auth
Both verifying same behavior
```

**Result**: Consistent authentication across both platforms

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

### General Agents

| Task | Agent | Complexity | Time Saved |
|------|-------|-----------|------------|
| Deep code analysis | code-explorer | High | 30-60 min |
| Architecture design | code-architect | High | 45-90 min |
| Step-by-step impl | implementation-helper | High | 60-120 min |
| Debug complex error | error-resolver | Medium | 20-40 min |
| Write test suite | test-writer | Medium | 20-40 min |
| Write documentation | doc-writer | Medium | 15-30 min |
| Code quality review | quality-checker | Low | 5-15 min |

### Language Expert Agents

| Task | Agent | Complexity | Time Saved |
|------|-------|-----------|------------|
| Dart optimization/isolates | dart-expert | Medium-High | 30-60 min |
| TypeScript migration/types | typescript-expert | High | 45-90 min |
| JavaScript performance | javascript-expert | Medium | 20-40 min |
| Android platform channels | kotlin-expert | High | 60-90 min |
| iOS platform channels | swift-expert | High | 60-90 min |

### Flutter Agents

| Task | Agent | Complexity | Time Saved |
|------|-------|-----------|------------|
| Flutter codebase analysis | flutter-explorer | High | 30-60 min |
| Flutter architecture design | flutter-architect | High | 45-90 min |
| Flutter implementation | flutter-implementer | High | 60-120 min |
| Flutter testing | flutter-tester | Medium | 30-45 min |
| Flutter code review | flutter-reviewer | Medium | 15-30 min |
| Flutter animations | flutter-animator | Medium | 30-60 min |
| Platform channels/FFI | flutter-platform-integrator | High | 90-120 min |
| Flutter performance | flutter-performance-optimizer | High | 45-90 min |
| Flutter accessibility | flutter-accessibility-specialist | Medium | 30-45 min |

### React Agents

| Task | Agent | Complexity | Time Saved |
|------|-------|-----------|------------|
| React codebase analysis | react-explorer | High | 30-60 min |
| React architecture design | react-architect | High | 45-90 min |
| React implementation | react-implementer | High | 60-120 min |
| React testing | react-tester | Medium | 30-45 min |
| React code review | react-reviewer | Medium | 15-30 min |
| React performance | react-performance-optimizer | High | 45-90 min |
| Concurrent features | react-concurrent-specialist | Medium-High | 30-60 min |
| SSR/Next.js/Server Components | react-ssr-specialist | High | 60-90 min |
| React accessibility | react-accessibility-specialist | Medium | 30-45 min |

---

## Summary

**30 specialized agents** designed based on deepwiki best practices from the feature-dev and code-review plugins:

### General Agents (7)
1. **code-explorer** - Understand existing code
2. **code-architect** - Design new features
3. **implementation-helper** - Implement step-by-step
4. **error-resolver** - Fix bugs systematically
5. **test-writer** - Ensure quality
6. **doc-writer** - Document features
7. **quality-checker** - Review quality

### Language Experts (5)
8. **dart-expert** - Dart 3.x, null safety, isolates, FFI
9. **typescript-expert** - Advanced types, JS→TS migration
10. **javascript-expert** - ES2015+, async patterns, performance
11. **kotlin-expert** - Coroutines, Android SDK, platform channels
12. **swift-expert** - Swift concurrency, iOS SDK, platform channels

### Flutter Framework (9)
**Core (5):**
13. **flutter-explorer** - Analyze Flutter codebases
14. **flutter-architect** - Design Flutter architectures
15. **flutter-implementer** - Implement Flutter features
16. **flutter-tester** - Test Flutter apps
17. **flutter-reviewer** - Review Flutter code

**Specialized (4):**
18. **flutter-animator** - Animations expert
19. **flutter-platform-integrator** - Platform channels & FFI
20. **flutter-performance-optimizer** - Performance optimization
21. **flutter-accessibility-specialist** - Accessibility compliance

### React Framework (9)
**Core (5):**
22. **react-explorer** - Analyze React codebases
23. **react-architect** - Design React architectures
24. **react-implementer** - Implement React features
25. **react-tester** - Test React apps
26. **react-reviewer** - Review React code

**Specialized (4):**
27. **react-performance-optimizer** - Performance & bundles
28. **react-concurrent-specialist** - Concurrent features
29. **react-ssr-specialist** - SSR/SSG & Next.js
30. **react-accessibility-specialist** - Accessibility compliance

---

## Key Benefits

### Multi-Framework Support
- **Flutter** and **React** frameworks fully supported
- **Cross-platform** development with language experts
- **Platform channels** for native integration (Android/iOS)

### Specialized Expertise
- Framework-specific best practices built-in
- Language experts for deep optimization
- Specialized agents for animations, performance, accessibility, SSR

### Parallel Execution
- Launch multiple agents simultaneously
- Reduce development time significantly
- Coordinate complex multi-agent workflows

### Complete Development Lifecycle
- **Explore** → **Architect** → **Implement** → **Test** → **Review**
- Every phase covered with specialized agents
- Quality built-in from start to finish

---

Use them autonomously to build better software faster with fewer mistakes across Flutter and React frameworks.
