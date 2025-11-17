# Anti-Patterns to Avoid

> Common mistakes and their corrections

## Code Anti-Patterns

### ❌ Incomplete Implementation

**Wrong:**
```typescript
function validateUser(user: User): boolean {
  // TODO: Add validation
  return true;
}
```

**Right:**
```typescript
function validateUser(user: User): boolean {
  if (!user.email || !isValidEmail(user.email)) {
    return false;
  }
  if (!user.password || user.password.length < 12) {
    return false;
  }
  return true;
}
```

### ❌ Ignoring Errors

**Wrong:**
```typescript
try {
  await criticalOperation();
} catch (e) {
  // Ignore
}
```

**Right:**
```typescript
try {
  await criticalOperation();
} catch (error) {
  console.error('Critical operation failed:', error);
  throw new AppError('Operation failed', 500);
}
```

### ❌ Using `any` Type

**Wrong:**
```typescript
function processData(data: any) {
  return data.items.map((item: any) => item.value);
}
```

**Right:**
```typescript
interface DataItem {
  value: string;
}

function processData(data: { items: DataItem[] }): string[] {
  return data.items.map(item => item.value);
}
```

## Process Anti-Patterns

### ❌ Reading Many Files Instead of Using Explore

**Wrong:**
```
Read file1.ts
Read file2.ts
Read file3.ts
...
Context now 70% full
```

**Right:**
```
Use Explore agent to search
Get summary
Read only necessary files
Context stays <30%
```

### ❌ Working on Multiple Tasks Simultaneously

**Wrong:**
```
Start auth feature
Switch to bug fix
Back to auth
Context confused
```

**Right:**
```
Complete auth feature
Archive session
Start fresh for bug fix
Clear context
```

## Remember

- If it feels like a shortcut, it probably is
- If you think "I'll fix this later", fix it now
- If you're unsure if it's complete, it's not
- If there's a TODO, it's not done

