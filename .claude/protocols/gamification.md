# Gamification Protocol

**Based on deepwiki research from code-review, feature-dev, and agent-sdk-dev plugins.**

Motivate thorough, complete work through achievement tracking, scoring systems, and visual progress indicators.

---

## 🤖 Autonomous Operation

**This system runs AUTOMATICALLY in the background. Zero user management required.**

### How It Works

1. **Auto-Initialize** - Every session starts with Score = 0/100, GGP = +50
2. **Auto-Track** - Every action (writing code, running tests, linter checks) updates score and GGP immediately
3. **Auto-Report** - At task completion, final score and achievements are displayed automatically
4. **Auto-Persist** - Scores carry over between sessions (GGP balance, streak count, lifetime totals)

### What This Means for Claude Code

**You (Claude Code) automatically:**
- Track internal score during every session
- Update GGP balance based on actions taken
- Calculate confidence scores for subtasks
- Generate final performance report
- Award achievements based on results

**You do NOT:**
- Ask user to track scores
- Require manual template filling
- Wait for user to calculate points
- Need explicit permission to track

**The templates in `.claude/work/` are OPTIONAL references for users who want visibility. The system works without them.**

---

## Core Principles

1. **Quality over speed** - Reward thoroughness, not just completion
2. **Visible progress** - Show advancement toward goals
3. **Immediate feedback** - Score every action
4. **Continuous improvement** - Track trends over time
5. **Clear criteria** - Know exactly what "excellent" looks like

---

## Achievement System

### Level 1: Bronze (Basic Completion)
**Requirements:**
- ✅ All todos completed
- ✅ No TODOs in code
- ✅ No linter warnings (exit code 0)
- ✅ Basic tests pass

**Reward:** "Task Complete" badge

### Level 2: Silver (Quality Work)
**Requirements:**
- ✅ All Bronze requirements
- ✅ Confidence score ≥ 75 for all verifications
- ✅ No security issues (linter exit code 2)
- ✅ All error handlers implemented
- ✅ Session documented in `.claude/work/current-session.md`

**Reward:** "Quality Work" badge + 🥈

### Level 3: Gold (Excellence)
**Requirements:**
- ✅ All Silver requirements
- ✅ Confidence score ≥ 90 for all verifications
- ✅ Comprehensive tests (>80% coverage)
- ✅ Documentation complete
- ✅ quality-checker agent review: PASS
- ✅ All agents used appropriately (no context overflow)

**Reward:** "Excellent Work" badge + 🥇

### Level 4: Platinum (Mastery)
**Requirements:**
- ✅ All Gold requirements
- ✅ Confidence score = 100 for all verifications
- ✅ Zero warnings across all checks
- ✅ Performance optimized
- ✅ Security reviewed
- ✅ Accessibility considered
- ✅ Edge cases handled

**Reward:** "Master Craftsperson" badge + 🏆

---

## Scoring System

### Task Completion Score (0-100)

Based on code-review plugin confidence scoring pattern:

**Formula:**
```
Base Score (50 points):
+ 10 points: All todos complete
+ 10 points: No linter blocks (exit 0-1)
+ 10 points: No incomplete markers (TODO/FIXME)
+ 10 points: All error handlers present
+ 10 points: Session documented

Quality Bonus (30 points):
+ 10 points: No linter warnings
+ 10 points: Tests written and passing
+ 10 points: Documentation complete

Excellence Bonus (20 points):
+ 5 points: quality-checker PASS status
+ 5 points: Context managed well (<70%)
+ 5 points: Agents used appropriately
  - Appropriate agent selection (+2 pts)
  - Used agents in parallel when possible (+2 pts)
  - Context savings achieved (+1 pt)
+ 5 points: Pattern compliance verified

Total: 100 points possible
```

**Score Interpretation:**
- **90-100**: 🏆 Platinum - Exceptional work
- **75-89**: 🥇 Gold - Excellent work
- **60-74**: 🥈 Silver - Quality work
- **50-59**: 🥉 Bronze - Acceptable, needs improvement
- **< 50**: ❌ Incomplete - Must address issues

---

## Progress Tracking

### Visual Indicators

Based on feature-dev plugin multi-phase workflow pattern.

#### Phase-Based Progress

Display current phase and completion percentage:

```
Session: Add User Authentication
═══════════════════════════════════════════════

Phase: Implementation                    [4/7]
Progress: ████████████░░░░░░░░░░░░░░     60%

✅ Discovery
✅ Exploration
✅ Architecture
🔄 Implementation (IN PROGRESS)
⏳ Testing
⏳ Quality Review
⏳ Documentation

Current Score: 65/100 🥈 (Silver Track)
```

#### Task-Level Progress

Display subtask completion with confidence scores:

```
Current Task: Implement JWT Authentication
═══════════════════════════════════════════════

Subtasks:
[✓] Create auth middleware            [100%] 🏆
[✓] Add JWT signing                   [100%] 🏆
[✓] Implement token validation        [95%]  🥇
[▶] Add refresh token logic           [75%]  🥈 ← CURRENT
[ ] Write auth tests                  [0%]   ⏳
[ ] Document auth flow                [0%]   ⏳

Completion: 50%  (3/6 subtasks)
Quality: 90%     (Average confidence)
```

---

## Confidence Scoring

Based on code-review plugin confidence scoring (0-100).

### Scoring Rubric

**0-24: Not Confident** ❌
- False positive likely
- Pre-existing issue
- Needs verification

**25-49: Somewhat Confident** ⚠️
- Might be real issue
- Not critical
- Could be nitpick

**50-74: Moderately Confident** 🥉
- Real but minor issue
- Should fix eventually
- Pattern deviation

**75-89: Highly Confident** 🥇
- Very likely real issue
- Important to address
- Impacts functionality

**90-100: Absolutely Certain** 🏆
- Definitely real issue
- Will happen frequently
- Critical to fix now

### Applying Confidence Scores

**When writing code:**
```
✓ JWT token generation implemented
  Confidence: 95 🥇
  Reason: Uses proven bcrypt library, proper salting

✓ Error handling added
  Confidence: 85 🥇
  Reason: All edge cases covered, logged properly

⚠ Input validation present
  Confidence: 70 🥉
  Reason: Basic validation, could be more thorough

→ Overall Task Confidence: 83 🥇 (Gold Level)
```

---

## Streak Tracking

Motivate consistent high-quality work.

### Current Streak

Track consecutive tasks at each level:

```
🔥 Current Streak: 5 tasks at Gold level or higher

Recent History:
[🏆][🥇][🥇][🥇][🥇] ← Last 5 tasks

All-Time Stats:
  Platinum: 3  tasks (15%)
  Gold:     12 tasks (60%)
  Silver:   4  tasks (20%)
  Bronze:   1  task  (5%)

Average Score: 82/100 🥇
Success Rate: 95% (19/20 tasks complete)
```

### Streak Bonuses

- **3-task streak**: +5 bonus points
- **5-task streak**: +10 bonus points + "Consistent" badge
- **10-task streak**: +15 bonus points + "Reliable" badge
- **20-task streak**: +20 bonus points + "Master" badge

---

## Quality Badges

Visual achievements for specific accomplishments.

### Security Badges
- 🛡️ **Security Guardian**: No security issues in 10 tasks
- 🔒 **Fortress Builder**: Zero vulnerabilities in 20 tasks
- 🔐 **Security Expert**: All security checks pass at 100%

### Quality Badges
- 🎯 **Precision Coder**: 90+ confidence on 10 tasks
- 💎 **Quality Craftsperson**: Gold level or higher for 15 tasks
- ⚡ **Excellence Streak**: 5 consecutive Platinum tasks

### Completeness Badges
- ✅ **No TODOs**: 10 tasks without any TODO markers
- 📝 **Documentation Master**: All docs complete for 10 tasks
- 🧪 **Test Champion**: >80% coverage on 10 tasks

### Efficiency Badges
- 🎯 **Context Master**: Keep context <70% for 10 tasks
- 🤖 **Agent Expert**: Use agents appropriately 20 times
- ⚡ **Speed & Quality**: Complete in <50% of estimated time at Gold+

---

## Session Scorecard

### At Session Start

Document goals and acceptance criteria:

```markdown
# Session: Add User Profile Editing

## Success Criteria
- [ ] All CRUD operations implemented
- [ ] Input validation complete
- [ ] Tests written (>80% coverage)
- [ ] Documentation updated
- [ ] No security issues
- [ ] quality-checker: PASS

## Target Level: Gold 🥇
Target Score: 85/100

## Estimated Phases: 5
1. Discovery & Exploration (30 min)
2. Architecture Design (45 min)
3. Implementation (2 hours)
4. Testing (1 hour)
5. Quality Review (30 min)
```

### During Work

Update scorecard as you progress:

```markdown
## Progress Update

**Completed:**
✅ Discovery (Confidence: 100 🏆)
✅ Exploration (Confidence: 95 🥇)
✅ Architecture (Confidence: 90 🥇)

**In Progress:**
🔄 Implementation (Current: 60%, Confidence: 75 🥈)
   - Edit endpoint: ✓ (100 🏆)
   - Validation: ✓ (95 🥇)
   - Error handling: ▶ (75 🥈) ← CURRENT
   - Tests: ⏳
   - Docs: ⏳

**Current Score: 68/100** 🥈 (Silver)
**Target: 85/100** 🥇 (Gold)
**Gap: -17 points** - Need testing & quality review
```

### At Session End

Final scorecard with achievements:

```markdown
## Session Complete! 🎉

### Final Score: 88/100 🥇 GOLD LEVEL

**Breakdown:**
- Base Score: 50/50 ✅
  - All todos complete
  - No linter blocks
  - No TODO markers
  - Error handlers present
  - Session documented

- Quality Bonus: 28/30 ✅
  - No linter warnings: ✓
  - Tests passing: ✓ (85% coverage)
  - Documentation complete: ✓

- Excellence Bonus: 10/20 ⚠️
  - quality-checker PASS: ✓
  - Context managed: ✓ (45% max)
  - Agents used well: ✗ (used Explore when could work direct)
  - Pattern compliance: ✗ (missed one pattern)

### Achievements Unlocked:
🥇 Quality Work
🎯 Precision Coder (90+ confidence)
✅ No TODOs (10th task)
🔥 5-Task Gold Streak

### Areas for Improvement:
- Agent usage: Check agent-usage.md before launching
- Pattern compliance: Review patterns.md more carefully

### Next Session Bonus: +10 points (streak bonus)
```

---

## Real-Time Feedback

Provide immediate feedback during work.

### After Each Subtask

```
✓ JWT middleware implemented

📊 Subtask Score: 95/100 🥇
  + Base: 50/50 (complete, no TODOs)
  + Quality: 30/30 (no warnings, tested, documented)
  + Excellence: 15/20 (quality-checker PASS, pattern compliant)

⚠️  Improvement Opportunity:
  - Consider edge case: token expiry during request
  - Add integration test for refresh flow

🎯 Add these to reach Platinum (100):
  - Performance test (token validation speed)
  - Security review (check for timing attacks)
```

### Quality Gate Checks

Before marking task complete, verify criteria:

```
🚦 Quality Gate Check: Implementation Phase

✅ All subtasks complete (6/6)
✅ No linter blocks (exit code 0)
✅ No incomplete markers (0 TODOs)
✅ Error handling present (100%)
⚠️  Tests written (85% coverage)
    → Target: >80% ✓
    → Suggestion: Add edge case tests for 90%+

Current Score: 85/100 🥇 GOLD

✓ PASSED - Ready to proceed to Quality Review

🎉 Gold Level maintained!
🔥 Streak continues: 6 consecutive Gold+ tasks
```

---

## Motivation Messages

Contextual encouragement based on performance.

### When Struggling (Score <60)

```
⚡ Keep Going! You're at 55/100 (Bronze level)

📈 To reach Silver (60+):
  1. Add error handlers to API calls (+10)
  2. Document current work in session.md (+5)
  3. Run quality-checker and address issues (+10)

💡 Tip: Use error-resolver agent if stuck on same issue 2+ times

🎯 You're 5 points from Silver! Let's finish strong.
```

### When Improving (Score 60-74)

```
🥈 Good Progress! You're at 68/100 (Silver level)

🎯 To reach Gold (75+):
  1. Complete test suite (currently 45%, need 80%) (+10)
  2. Run quality-checker for PASS status (+5)
  3. Eliminate remaining linter warnings (+5)

💡 Tip: Use test-writer agent for comprehensive test coverage

🔥 3-task streak bonus available at Gold level!
```

### When Excelling (Score 75-89)

```
🥇 Excellent Work! You're at 82/100 (Gold level)

🏆 Close to Platinum (90+)! Just need:
  1. Increase test coverage to 90%+ (+3)
  2. Add performance considerations (+2)
  3. Document edge cases (+3)

💎 You're 8 points from Platinum mastery!
🔥 Current streak: 4 Gold-level tasks

Keep up the exceptional work! 🌟
```

### When Achieving Mastery (Score 90+)

```
🏆 PLATINUM LEVEL! 94/100

Outstanding work! You've achieved:
✓ Zero issues
✓ Comprehensive tests (92% coverage)
✓ Complete documentation
✓ Pattern compliance
✓ Context managed expertly

🎉 Achievements Unlocked:
🏆 Master Craftsperson (94/100 score)
💎 Quality Craftsperson (15th Gold+ task)
🔥 Excellence Streak (2nd consecutive Platinum)

🌟 You're in the top 5% of sessions!

Next challenge: Maintain Platinum for 5 consecutive tasks
```

---

## Integration with Existing Protocols

### With TodoWrite

Todos automatically contribute to scoring:

```json
{
  "todos": [
    {
      "content": "Implement authentication middleware",
      "status": "completed",
      "activeForm": "Implementing auth",
      "confidence": 95,
      "quality_score": 18
    },
    {
      "content": "Write authentication tests",
      "status": "in_progress",
      "activeForm": "Writing tests",
      "confidence": 75,
      "quality_score": 12
    }
  ],
  "session_score": 68,
  "level": "silver",
  "streak": 3
}
```

### With Quality Linter

Linter results affect scores automatically:

```
Linter Result: Exit Code 0 (INFORMS)
  → +10 points (No blocking issues)
  → +10 points (No warnings)
  → Confidence: 90 (High quality code)
  → Level maintained: Gold 🥇
```

### With Agents

Agent usage tracked for efficiency scoring:

```
Agent Used: code-explorer (Context: 75%)
  ✓ Appropriate usage (context >70%)
  → +5 points (Efficient context management)

Agent Used: Explore (Context: 25%)
  ✗ Could have worked directly (context <50%)
  → -3 points (Inefficient agent usage)
  → Tip: Review agent-usage.md
```

---

## Session Summary Template

```markdown
# Session Summary: [Task Name]

## 🏆 Final Achievement

**Level:** Gold 🥇
**Score:** 88/100
**Confidence:** 92 (Very High)

## 📊 Scorecard

**Base Completion (50/50):**
✅ All todos complete (10/10)
✅ No linter blocks (10/10)
✅ No TODO markers (10/10)
✅ Error handlers present (10/10)
✅ Session documented (10/10)

**Quality Bonus (28/30):**
✅ No linter warnings (10/10)
✅ Tests passing - 85% coverage (9/10)
✅ Documentation complete (9/10)

**Excellence Bonus (10/20):**
✅ quality-checker PASS (5/5)
✅ Context managed well - 45% max (5/5)
⚠️  Agent usage (0/5) - used Explore unnecessarily
⚠️  Pattern compliance (0/5) - missed validation pattern

## 🎖️ Achievements

🥇 Quality Work badge
🔥 5-task Gold streak
🎯 Precision Coder (90+ confidence)
✅ No TODOs (10th consecutive)

## 📈 Improvement Areas

1. **Agent Usage (-5 points)**
   - Used Explore agent when could work directly (context was 25%)
   - Review: .claude/protocols/agent-usage.md
   - Next time: Check context level before launching agents

2. **Pattern Compliance (-5 points)**
   - Missed input validation pattern in user input handling
   - Review: .claude/project/patterns.md
   - Next time: Check patterns before implementing

## 🎯 Next Session

**Streak Bonus:** +10 points (5-task Gold streak)
**Target:** Maintain Gold level (75+)
**Challenge:** Achieve Platinum (90+) by improving agent usage and pattern compliance

## 📝 Key Learnings

- JWT implementation works well with bcrypt
- Error handling pattern from project improves clarity
- Test coverage tool helps maintain quality

---

**Session archived:** .claude/sessions/archive/2024-11-16-user-auth.md
**Ready for next task!** 🚀
```

---

## Quick Reference

### Scoring Cheat Sheet

| Points | Requirement | How to Achieve |
|--------|------------|----------------|
| +10 | All todos complete | Mark all todos as complete before ending |
| +10 | No linter blocks | Fix all security issues (exit code ≠ 2) |
| +10 | No TODO markers | Complete all implementations, no stubs |
| +10 | Error handlers | Handle all errors, no empty catch blocks |
| +10 | Session documented | Update .claude/work/current-session.md |
| +10 | No warnings | Fix all linter warnings |
| +10 | Tests passing | Write tests, ensure >80% coverage |
| +10 | Docs complete | Document APIs, add usage examples |
| +5 | quality-checker PASS | Run quality-checker agent, address issues |
| +5 | Context managed | Keep context <70%, use agents wisely |
| +5 | Agents used well | Follow agent-usage.md protocols |
| +5 | Pattern compliance | Follow patterns in .claude/project/patterns.md |

### Level Requirements

| Level | Score | Key Requirements |
|-------|-------|-----------------|
| 🥉 Bronze | 50-59 | All todos done, no blocks, documented |
| 🥈 Silver | 60-74 | + No warnings, tests exist, error handling |
| 🥇 Gold | 75-89 | + High coverage (>80%), quality-checker PASS |
| 🏆 Platinum | 90-100 | + Perfect execution, zero issues, optimized |

---
