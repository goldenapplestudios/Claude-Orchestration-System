# Project Constraints

> **Import existing docs or add constraints here**

## Existing Documentation

**If your project has existing guidelines, import them:**

<!-- Uncomment and use your existing docs:
@../../CONTRIBUTING.md
@../../docs/guidelines.md
@../../docs/coding-standards.md
@../../.github/PULL_REQUEST_TEMPLATE.md
@../../docs/security.md
-->

**Common locations for existing constraints:**
- CONTRIBUTING.md - Contribution guidelines
- docs/security.md - Security requirements
- docs/testing.md - Testing standards
- .eslintrc / .prettierrc - Code style (reference these)

---

## Additional Constraints

> **Add Claude Code-specific constraints below** (supplements existing docs)

<!-- Only add what's NOT already documented -->

### NEVER

❌ **List things that must NEVER be done:**

Example:
- Use `any` type in TypeScript
- Store passwords in plain text
- Trust user input without validation
- Use SQL string concatenation
- Commit secrets to version control

### ALWAYS

✅ **List things that must ALWAYS be done:**

Example:
- Use TypeScript strict mode
- Validate all inputs with Zod
- Use parameterized queries
- Write tests for business logic
- Handle errors explicitly

## Technical Constraints

**Performance:**
- API response time < 200ms
- Page load time < 3 seconds

**Security:**
- All passwords hashed with bcrypt
- JWTtokens expire after 1 hour
- HTTPS only in production

**Browser Support:**
- Chrome 90+
- Firefox 88+
- Safari 14+

---

**See also:**
- architecture.md - System design
- patterns.md - Code patterns
