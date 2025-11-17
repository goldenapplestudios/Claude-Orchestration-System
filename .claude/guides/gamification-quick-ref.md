# Gamification Quick Reference

**1-page guide to achievement tracking and scoring in Claude Code.**

Based on deepwiki research from code-review, feature-dev, and agent-sdk-dev plugins.

---

## Performance Levels

| Level | Score | Badge | Requirements |
|-------|-------|-------|--------------|
| Bronze | 50-59 | Task Complete | Todos done, no blocks, documented |
| Silver | 60-74 | Quality Work | + Tests, no warnings, error handling |
| Gold | 75-89 | Excellent Work | + >80% coverage, quality-checker PASS |
| Platinum | 90-100 | Master Craftsperson | + Zero issues, optimized, perfect |

---

## Scoring Breakdown (100 points total)

### Base Completion (50 points)

| Points | Requirement | How to Get |
|--------|-------------|------------|
| +10 | All todos complete | Mark all TodoWrite items as complete |
| +10 | No linter blocks | Fix all security issues (no exit code 2) |
| +10 | No TODO markers | No TODO/FIXME/HACK in code |
| +10 | Error handlers | All errors caught and handled |
| +10 | Session documented | Update `.claude/work/current-session.md` |

### Quality Bonus (30 points)

| Points | Requirement | How to Get |
|--------|-------------|------------|
| +10 | No linter warnings | Fix all warnings (exit code 0) |
| +10 | Tests passing | Write tests, get >80% coverage |
| +10 | Docs complete | Document APIs, add usage examples |

### Excellence Bonus (20 points)

| Points | Requirement | How to Get |
|--------|-------------|------------|
| +5 | quality-checker PASS | Run quality-checker agent, fix issues |
| +5 | Context managed | Keep context <70%, use agents wisely |
| +5 | Agents used well | Appropriate selection (+2), parallel execution (+2), context savings (+1) |
| +5 | Pattern compliance | Follow patterns in `.claude/project/patterns.md` |

---

## Confidence Scoring (0-100)

Based on code-review plugin pattern:

```
90-100  Absolutely Certain     - Will definitely work, proven approach
75-89   Highly Confident       - Very likely correct, well-tested
50-74   Moderately Confident   - Works but could be better
25-49   Somewhat Confident     - Might work, needs verification
0-24    Not Confident          - Likely has issues, needs rework
```

**Apply to each subtask:**
```
User authentication implemented
  Confidence: 95
  Reason: Uses proven JWT library, proper error handling

Password validation added
  Confidence: 85
  Reason: Regex tested, covers edge cases

Rate limiting implemented
  Confidence: 70
  Reason: Basic implementation, could use more testing
```

---

## Achievement Badges

### Quality Badges
- **Quality Work** - Silver level (60+ score)
- **Excellent Work** - Gold level (75+ score)
- **Master Craftsperson** - Platinum level (90+ score)

### Completeness Badges
- **No TODOs** (10 tasks) - Zero incomplete markers
- **Documentation Master** (10 tasks) - Complete docs every time
- **Test Champion** (10 tasks) - >80% coverage consistently

### Security Badges
- **Security Guardian** (10 tasks) - No security issues
- **Fortress Builder** (20 tasks) - Zero vulnerabilities
- **Security Expert** - Perfect security record

### Efficiency Badges
- **Context Master** (10 tasks) - Context always <70%
- **Agent Expert** (20 uses) - Agents used appropriately
- **Speed & Quality** - Fast completion at Gold level

### Streak Badges
- **Consistent** (5 streak) - 5 consecutive Gold/Platinum
- **Reliable** (10 streak) - 10 consecutive Gold/Platinum
- **Master** (20 streak) - 20 consecutive Gold/Platinum

---

## Streak Bonuses

| Streak | Bonus | Badge |
|--------|-------|-------|
| 3 tasks | +5 pts | - |
| 5 tasks | +10 pts | Consistent |
| 10 tasks | +15 pts | Reliable |
| 20 tasks | +20 pts | Master |

**Streak Rules:**
- Only counts tasks at Gold (75+) or higher
- Resets if task scores below Gold
- Carries over between sessions

---

## Quick Checklist

Before marking task complete, verify:

### Bronze Level (50+ points)
- [ ] All TodoWrite items marked complete (+10)
- [ ] No linter blocks/security issues (+10)
- [ ] Zero TODO/FIXME/HACK markers (+10)
- [ ] All error handlers implemented (+10)
- [ ] Session documented in current-session.md (+10)

### Silver Level (60+ points)
- [ ] All Bronze requirements (+50)
- [ ] No linter warnings (exit code 0) (+10)
- [ ] Tests written and passing (+10)
- [ ] Documentation complete (+10)

### Gold Level (75+ points)
- [ ] All Silver requirements (+70)
- [ ] Test coverage >80% (+5 included in tests)
- [ ] quality-checker agent: PASS status (+5)
- [ ] Context kept under 70% (+5)
- [ ] Agents used appropriately: right agents (+2), parallel execution (+2), context saved (+1) = (+5)
- [ ] Pattern compliance verified (+5)

### Platinum Level (90+ points)
- [ ] All Gold requirements (+85)
- [ ] Confidence scores 95+ on all subtasks (+5)
- [ ] Zero warnings across all checks (+5)
- [ ] Performance optimized (+2)
- [ ] Security reviewed thoroughly (+2)
- [ ] Edge cases all handled (+1)

---

## Session Scorecard Template

Copy `.claude/work/.session-scorecard-template.md` to start tracking:

```bash
cp .claude/work/.session-scorecard-template.md \
   .claude/work/session-scorecard.md
```

Update during work:
- **Start:** Set target level and success criteria
- **During:** Score each subtask with confidence level
- **End:** Calculate final score and achievements

---

## Example Score Calculation

**Task: Add User Authentication**

```
Base Completion:
Todos complete          +10
No linter blocks        +10
No TODOs                +10
Error handlers          +10
Documented              +10
                        = 50/50

Quality Bonus:
No warnings             +10
Tests pass (82% coverage) +10
Docs complete           +10
                        = 30/30

Excellence Bonus:
quality-checker PASS    +5
Context: 45% (< 70%)    +5
Agent usage             +0  (used Explore at 25% context)
Pattern compliance      +5
                        = 15/20

FINAL SCORE: 95/100 (PLATINUM LEVEL)

Achievements:
Master Craftsperson
6-task Gold+ streak
Precision Coder
No TODOs (12th consecutive)
```

---

## Tips for High Scores

### Get to Bronze (50+)
1. Use TodoWrite to track all subtasks
2. Run linter before writing code
3. Never commit code with TODO markers
4. Always add try/catch or error checks
5. Update session doc as you work

### Reach Silver (60+)
6. Fix ALL linter warnings, not just blocks
7. Write tests as you implement
8. Document functions/APIs immediately

### Achieve Gold (75+)
9. Run quality-checker before marking complete
10. Use agents when context >50%
11. Check patterns.md for compliance
12. Aim for >80% test coverage

### Attain Platinum (90+)
13. Score every subtask 95+ confidence
14. Think performance from the start
15. Consider security at every step
16. Handle ALL edge cases
17. Zero warnings, zero compromises

---

## Common Score Gaps

**Scored 55 (Bronze)?**
- Missing: Documentation (-10)
- Fix: Update `.claude/work/current-session.md`

**Scored 68 (Silver)?**
- Missing: quality-checker PASS (-5), agent usage (-5)
- Fix: Run quality-checker, review agent-usage.md

**Scored 82 (Gold)?**
- Missing: Pattern compliance (-5), perfect confidence (-3)
- Fix: Review patterns.md, increase test coverage

**Scored 88 (Gold)?**
- Missing: Platinum excellence details (-12)
- Fix: Performance review, security audit, edge cases

---

## Track Your Progress

Keep a running scorecard:

```
All-Time Stats:
  Sessions: 25
  Average Score: 78

  Platinum: 4  (16%)
  Gold:     15 (60%)
  Silver:   5  (20%)
  Bronze:   1  (4%)

  Current Streak: 7 (Gold+)
  Best Streak: 12

  Achievements: 18/30 unlocked
```

---

## Gamification in Action

### Session Start
```
New Session: Add Payment Integration
Target: Gold (75+)
Estimated: 3 hours

Starting Scorecard...
```

### During Work
```
Subtask: Stripe API integration
  Confidence: 90
  Current Score: 62/100 (Silver)
  Gap to Gold: -13 points
```

### Session End
```
Session Complete

Final Score: 88/100 (GOLD LEVEL)

Achievements:
Excellent Work
8-task Gold streak
Precision Coder

Next session bonus: +10 points
Ready to archive
```

---

**Full System:** See `.claude/protocols/gamification.md`

**Template:** `.claude/work/.session-scorecard-template.md`

**Integration:** Automatically works with TodoWrite and linter
