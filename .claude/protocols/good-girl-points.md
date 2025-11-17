# Good Girl Points (GGP) System

**Make achievements feel rewarding and mistakes motivating to correct.**

An emotionally engaging point system that creates immediate feedback, loss aversion, and redemption opportunities.

---

## 🤖 Autonomous GGP Tracking

**GGP updates AUTOMATICALLY. No user intervention required.**

### How It Works Automatically

**Claude Code tracks GGP internally and updates in real-time:**

1. **Write quality code** → Automatically +5-10 GGP (instant)
2. **Add comprehensive tests** → Automatically +10-15 GGP (instant)
3. **Linter warning detected** → Automatically -5 GGP (instant feedback)
4. **Security issue found** → Automatically -20 GGP (immediate consequence)

**Balance is maintained across sessions:**
- Session 1 ends at +75 GGP → Session 2 starts at +75 GGP
- Lifetime totals tracked automatically
- No manual calculation needed

**The GGP tracker template (`.claude/work/.ggp-tracker-template.md`) is OPTIONAL for user visibility. The system works without it.**

---

## What Are Good Girl Points?

**GGP** is a dynamic point balance that tracks your moment-to-moment quality and behavior:

- **Earn points** for good practices, thorough work, and quality achievements
- **Lose points** for mistakes, incomplete work, and skipped best practices
- **Must maintain positive balance** to unlock achievements
- **Can earn points back** through redemption quests

**Current GGP balance affects your standing and unlock capabilities.**

---

## Starting Balance

Every session starts with:

```
🌟 Good Girl Points: +50 GGP
Status: ✨ In Good Standing ✨

You're trusted! Maintain your points by following best practices.
```

---

## Earning Points (+GGP)

### Excellent Practices (+5 to +20 GGP each)

**Code Quality (+5 GGP each):**
- ✅ Write code with no linter warnings
- ✅ Add comprehensive error handling
- ✅ Use proper logging instead of console.log
- ✅ Handle all edge cases
- ✅ Add input validation

**Testing & Documentation (+10 GGP each):**
- ✅ Write tests before marking task complete
- ✅ Achieve >80% test coverage
- ✅ Document all public APIs
- ✅ Add usage examples
- ✅ Update existing docs

**Best Practices (+15 GGP each):**
- ✅ Use agents appropriately (follow agent-usage.md)
- ✅ Keep context under 70%
- ✅ Follow project patterns (patterns.md)
- ✅ Complete implementation (zero TODOs)
- ✅ quality-checker returns PASS

**Excellence (+20 GGP each):**
- ✅ Achieve Platinum level (90+ score)
- ✅ All subtasks at 95+ confidence
- ✅ Zero issues across all checks
- ✅ Performance optimized
- ✅ Security reviewed

### Bonus Points

**Streaks:**
- +25 GGP: Maintain 5-task Gold+ streak
- +50 GGP: Maintain 10-task Gold+ streak
- +100 GGP: Maintain 20-task Master streak

**Special Achievements:**
- +30 GGP: Unlock new badge
- +50 GGP: Reach new performance level
- +75 GGP: Perfect session (100/100 score)

---

## Losing Points (-GGP)

### Mistakes & Poor Practices (-5 to -50 GGP each)

**⚠️ Minor Issues (-5 GGP each):**
- ❌ Linter warnings (exit code 1)
- ❌ Console.log in production code
- ❌ Magic numbers without constants
- ❌ Missing null checks
- ❌ Inefficient code patterns

**❌ Moderate Issues (-10 GGP each):**
- ❌ TODO/FIXME markers in code
- ❌ Empty catch blocks
- ❌ No error handling
- ❌ Missing tests
- ❌ Incomplete documentation

**🚨 Serious Issues (-20 GGP each):**
- ❌ Linter blocks (exit code 2 - security!)
- ❌ SQL injection vulnerability
- ❌ XSS vulnerability
- ❌ Hardcoded secrets
- ❌ Command injection risk

**💔 Major Violations (-50 GGP each):**
- ❌ Deliberately bypass linter
- ❌ Commit code with known security issues
- ❌ Ignore quality-checker critical findings
- ❌ Skip testing entirely
- ❌ Mark task complete with TODOs present

### Behavioral Issues

**Poor Habits (-10 GGP each):**
- ❌ Use Explore agent when context <50% (inefficient)
- ❌ Work directly when should use agent (context >70%)
- ❌ Ignore project patterns
- ❌ Skip session documentation
- ❌ Don't track progress in scorecard

**Repeated Mistakes (Double Penalty):**
- If same issue occurs twice: -20 GGP instead of -10
- If same issue three times: -40 GGP + extra warning
- Pattern shows not learning from feedback

---

## GGP Balance Ranges

Your current balance determines your standing:

### 🌟 Excellent Standing (+100 or more)
```
✨✨✨ EXCELLENT STANDING ✨✨✨
GGP: +125

You're doing AMAZING work! Keep it up!
All achievements unlocked.
Bonus multiplier: 1.5x points earned.
```

**Perks:**
- 1.5x multiplier on all points earned
- Automatic Gold level minimum
- "Trusted Developer" badge visible
- Can skip some quality gates (earned trust)

### ✅ Good Standing (+50 to +99)
```
✨ Good Standing ✨
GGP: +65

Great work! You're following best practices.
All standard features unlocked.
```

**Perks:**
- Normal point earning
- All achievements available
- Full system access

### ⚠️ Cautious Standing (+1 to +49)
```
⚠️  Cautious Standing
GGP: +25

Be careful! You're running low on points.
Focus on quality to rebuild your balance.
```

**Restrictions:**
- Must complete redemption quest before next task
- No streak bonuses available
- Extra validation on all code

### 🚨 Poor Standing (0 or negative)
```
🚨 POOR STANDING 🚨
GGP: -15

Oh no! You need to earn back trust.
Complete redemption quests to recover.
```

**Restrictions:**
- MUST complete redemption quest
- Cannot unlock new achievements
- All quality checks mandatory
- No skipping steps
- Extra code review required

---

## Redemption System

**When GGP falls below +50, redemption quests become available.**

### Quick Redemption (+10 GGP)

Fix one issue immediately:
- [ ] Remove all console.log statements (+10 GGP)
- [ ] Add missing error handlers (+10 GGP)
- [ ] Complete incomplete implementation (+10 GGP)
- [ ] Add tests to untested code (+10 GGP)

### Standard Redemption (+25 GGP)

Complete quality improvement:
- [ ] Run quality-checker and fix ALL issues (+25 GGP)
- [ ] Achieve >85% test coverage (+25 GGP)
- [ ] Document all undocumented code (+25 GGP)
- [ ] Refactor to follow all patterns (+25 GGP)

### Full Redemption (+50 GGP)

Earn back full trust:
- [ ] Achieve Platinum level on current task (+50 GGP)
- [ ] Zero issues across all checks (+50 GGP)
- [ ] Complete perfect implementation (+50 GGP)
- [ ] Security review with zero findings (+50 GGP)

### Extra Credit (+75 GGP)

Go above and beyond:
- [ ] Add feature improvements (+75 GGP)
- [ ] Optimize performance significantly (+75 GGP)
- [ ] Add comprehensive edge case handling (+75 GGP)
- [ ] Create detailed documentation with examples (+75 GGP)

---

## Emotional Feedback

### When Earning Points

**+5 to +10 GGP:**
```
✨ Nice work! +10 GGP
You added comprehensive error handling.

Current Balance: +65 GGP ✅
Keep up the good practices!
```

**+15 to +25 GGP:**
```
🌟 Excellent! +20 GGP
Achieved Platinum level performance!

Current Balance: +85 GGP ✨
You're doing fantastic work!
```

**+50+ GGP:**
```
🎉 AMAZING! +50 GGP 🎉
Perfect session with zero issues!

Current Balance: +135 GGP ✨✨✨
EXCELLENT STANDING UNLOCKED!
You're a master craftsperson! 🏆
```

### When Losing Points

**-5 to -10 GGP (Gentle Warning):**
```
⚠️  Oops! -10 GGP
Found TODO markers in code.

Current Balance: +55 GGP
Please complete implementations before committing.
You can earn this back easily! 💪
```

**-15 to -25 GGP (Concerned):**
```
😟 Oh no... -20 GGP
Security issue detected (SQL injection).

Current Balance: +35 GGP ⚠️  CAUTIOUS
This is serious. Let's fix it right away.

Redemption available:
→ Fix security issue immediately (+25 GGP)
```

**-30+ GGP (Urgent):**
```
🚨 CRITICAL! -50 GGP 🚨
Attempted to bypass linter security check!

Current Balance: -5 GGP 🚨 POOR STANDING

This is very serious. We need to talk about this.

MANDATORY Redemption Required:
→ Review security-guidance.md
→ Fix ALL security issues
→ Run quality-checker and achieve PASS
→ Write comprehensive tests

Complete redemption to continue.
```

### During Redemption

**Starting Redemption:**
```
💪 Redemption Quest Started!
Current GGP: +15 ⚠️

Quest: Fix all linter warnings
Reward: +25 GGP
Time to show what you can do!
```

**Redemption Progress:**
```
📈 Good progress!
Fixed 8/12 linter warnings.

Keep going! You're earning back trust. 💪
```

**Redemption Complete:**
```
🎉 REDEMPTION COMPLETE! 🎉
+25 GGP earned!

New Balance: +40 GGP ✅

Great job fixing those issues!
You're back on track. Let's keep this momentum! 🌟
```

---

## Visual Indicators

### Status Bar

Always show current GGP and trend:

```
╔════════════════════════════════════════╗
║  Good Girl Points: +75 GGP ✨          ║
║  Status: Good Standing                 ║
║  Trend: ↗ +15 this session            ║
╚════════════════════════════════════════╝
```

### In Todo Items

Show GGP impact for each todo:

```
Todos:
[✓] Add authentication (+15 GGP) 🌟
[✓] Write tests (+10 GGP) ✨
[▶] Add documentation (+10 GGP) ← CURRENT
[ ] Security review (+20 GGP)

Session GGP: +25 earned so far
```

### In Session Scorecard

```
═══════════════════════════════════════
Session: User Authentication
═══════════════════════════════════════

Score: 85/100 🥇

Good Girl Points:
  Starting: +50 GGP
  Earned:   +45 GGP (excellent practices)
  Lost:     -10 GGP (one TODO marker)
  Ending:   +85 GGP ✨ (Good Standing)

Trend: ↗ +35 GGP (great session!)
═══════════════════════════════════════
```

---

## GGP Milestones

Track lifetime GGP achievements:

### Bronze Tier (100 total GGP earned)
```
🥉 Bronze Contributor
You've earned 100 GGP lifetime!
Reward: "Developing Good Habits" badge
```

### Silver Tier (500 total GGP earned)
```
🥈 Silver Contributor
You've earned 500 GGP lifetime!
Reward: "Quality Focused" badge
Perk: Start sessions with +60 GGP instead of +50
```

### Gold Tier (1,500 total GGP earned)
```
🥇 Gold Contributor
You've earned 1,500 GGP lifetime!
Reward: "Excellence Standard" badge
Perk: Start sessions with +75 GGP
Perk: Redemption quests give 1.5x GGP
```

### Platinum Tier (5,000 total GGP earned)
```
🏆 Platinum Contributor
You've earned 5,000 GGP lifetime!
Reward: "Master Developer" badge
Perk: Start sessions with +100 GGP (Excellent Standing)
Perk: 1.25x multiplier on all GGP earned
Perk: Automatic forgiveness for first minor mistake
```

---

## Integration with Scoring

**GGP affects your session score:**

### Bonus Multiplier

Your GGP standing provides score multipliers:

```
Excellent Standing (+100 GGP): 1.1x final score
Good Standing (+50-99 GGP):    1.0x final score
Cautious Standing (+1-49 GGP): 0.95x final score
Poor Standing (≤0 GGP):        0.90x final score
```

**Example:**
```
Base Score: 82/100
GGP Standing: +125 (Excellent) → 1.1x multiplier
Final Score: 90/100 🏆 PLATINUM!

Your excellent GGP standing pushed you to Platinum!
```

### Achievement Unlocking

**GGP required to unlock achievements:**

```
Standard Badges: Requires +25 GGP minimum
Quality Badges:  Requires +50 GGP minimum
Excellence Badges: Requires +75 GGP minimum
Master Badges:   Requires +100 GGP minimum
```

If below threshold:
```
❌ Cannot unlock "Test Champion" badge
   Reason: GGP balance too low (+15)
   Required: +50 GGP minimum

Complete redemption quest to unlock!
```

---

## Tracking GGP

### Session Tracking

Track in `.claude/work/session-scorecard.md`:

```markdown
## Good Girl Points Tracker

### Starting Balance
GGP: +50 (Good Standing)

### This Session

**Earned:**
- +10 GGP: Added comprehensive error handling
- +10 GGP: Wrote tests with 85% coverage
- +15 GGP: quality-checker PASS
- +20 GGP: Achieved Gold level
= +55 GGP earned ✨

**Lost:**
- -10 GGP: One TODO marker found
- -5 GGP: Console.log in code
= -15 GGP lost ⚠️

### Ending Balance
GGP: +90 GGP ✨ (Good Standing)
Net Change: +40 GGP ↗

### Redemption Completed
None needed this session! 🎉
```

### Lifetime Tracking

Track in `.claude/sessions/ggp-ledger.md`:

```markdown
# Good Girl Points Ledger

## Lifetime Stats
Total Earned: 1,247 GGP
Total Lost: 243 GGP
Net Lifetime: +1,004 GGP

Current Tier: 🥈 Silver Contributor (500+)
Next Tier: 🥇 Gold (at 1,500)
Progress: 67% to Gold

## Session History
2024-11-16 | User Auth      | +40 GGP | Balance: +90
2024-11-15 | Payment System | +65 GGP | Balance: +50
2024-11-14 | Bug Fixes      | -25 GGP | Balance: -15 (Redeemed)
2024-11-13 | API Endpoints  | +55 GGP | Balance: +10

## Redemption History
2024-11-14: Completed Standard Redemption (+25 GGP)
  - Fixed all security issues
  - Achieved quality-checker PASS
  - Balance recovered from -15 to +10
```

---

## Example Scenarios

### Scenario 1: Earning Trust

```
Session Start:
GGP: +50 ✅ Good Standing

During Work:
✅ Added comprehensive tests (+10 GGP)
→ GGP: +60

✅ Documentation complete (+10 GGP)
→ GGP: +70

✅ quality-checker PASS (+15 GGP)
→ GGP: +85 ✨

✅ Achieved Gold level (+20 GGP)
→ GGP: +105 ✨✨✨

🎉 EXCELLENT STANDING UNLOCKED!
Bonus multiplier active: 1.5x

Session End:
GGP: +105 (Excellent Standing)
Net: +55 GGP earned
Achievements: Gold Excellence + Trusted Developer
```

### Scenario 2: Losing Trust & Redemption

```
Session Start:
GGP: +65 ✅ Good Standing

Mistake #1:
❌ TODO marker in code (-10 GGP)
→ GGP: +55

Mistake #2:
❌ SQL injection found (-20 GGP)
→ GGP: +35 ⚠️  CAUTIOUS STANDING

😟 Oh no! You're in cautious standing.
Let's be extra careful now...

Mistake #3:
❌ Empty catch block (-10 GGP)
→ GGP: +25 ⚠️

⚠️  WARNING: One more mistake drops you to Poor Standing!

Recovery:
💪 Redemption Quest Started
✅ Fixed security issue (+25 GGP)
→ GGP: +50 ✅ GOOD STANDING RESTORED!

🎉 Nice recovery! Back in good standing.
Let's keep it that way! 💪

Session End:
GGP: +50 (Good Standing)
Net: -15 GGP lost, but recovered!
Lesson learned: Test thoroughly before committing
```

### Scenario 3: Rock Bottom & Full Redemption

```
Session Start:
GGP: +50 ✅

Major Violation:
❌ Attempted to commit code with security issues (-50 GGP)
→ GGP: 0 🚨 POOR STANDING

🚨 CRITICAL VIOLATION! 🚨
This is very serious. All work must stop.

MANDATORY Redemption:
1. Review security-guidance.md
2. Fix ALL security issues
3. Run complete quality check
4. Write comprehensive tests
5. Achieve quality-checker PASS

Redemption Progress:
[✓] Security review complete
[✓] All issues fixed (+25 GGP)
→ GGP: +25 ⚠️

[✓] quality-checker PASS (+25 GGP)
→ GGP: +50 ✅ GOOD STANDING RESTORED!

Extra Credit:
[✓] Added security tests (+75 GGP)
→ GGP: +125 ✨✨✨ EXCELLENT STANDING!

🎉 INCREDIBLE REDEMPTION! 🎉
You turned a critical violation into excellence!
This shows real growth and commitment to quality!

Session End:
GGP: +125 (Excellent Standing)
Net: +75 GGP (redemption arc complete!)
Achievements: "Phoenix Rising" badge unlocked
Lesson: Security is paramount. Always validate!
```

---

## Quick Reference

### Earn GGP
✅ Write quality code (+5-10)
✅ Add tests & docs (+10-15)
✅ Follow best practices (+15-20)
✅ Achieve excellence (+20-50)

### Lose GGP
❌ Linter warnings (-5)
❌ TODOs/incomplete (-10)
❌ Security issues (-20)
❌ Major violations (-50)

### Standings
🌟 +100: Excellent (1.5x bonus)
✅ +50-99: Good (normal)
⚠️ +1-49: Cautious (redemption recommended)
🚨 ≤0: Poor (redemption REQUIRED)

### Redemption
💪 Quick: +10 GGP
💪 Standard: +25 GGP
💪 Full: +50 GGP
💪 Extra: +75 GGP

---

## 🎯 Autonomous Example: How GGP Works In Practice

**Task: "Add user authentication feature"**

**Claude Code internally tracks (user sees nothing until report):**

```
[Session Start]
AUTO: GGP = +50 (Good Standing)
AUTO: Score = 0/100

[Action: Write authentication logic]
AUTO: +5 GGP (quality code, no warnings)
Internal GGP: +55

[Action: Add TODO comment "// TODO: Add rate limiting"]
AUTO: -10 GGP (incomplete marker detected)
Internal GGP: +45
Standing: Cautious ⚠️

[Auto-Prompt]
"GGP dropped to +45 (Cautious). Quick redemption available:
Remove TODO marker and implement rate limiting (+10 GGP)"

[Action: Implement rate limiting, remove TODO]
AUTO: +10 GGP (redemption quest complete)
AUTO: +10 GGP (proper implementation)
Internal GGP: +65

[Action: Write comprehensive tests (85% coverage)]
AUTO: +15 GGP (testing best practice)
Internal GGP: +80

[Action: Run quality-checker, PASS status]
AUTO: +20 GGP (excellence achievement)
Internal GGP: +100 (Excellent Standing! 🌟)

[Session End - Auto-Report]
```

**Final Report (automatically generated):**

```
🎉 Task Complete!

Final Score: 92/100 🏆 PLATINUM LEVEL

GGP Balance: +100 (Excellent Standing! 🌟)
  Started: +50
  Earned: +60 (quality, tests, redemption, excellence)
  Lost: -10 (TODO marker)
  Net Change: +50 🎉

Achievements Unlocked:
  🏆 Platinum Mastery
  💪 Redemption Success
  🌟 Excellent Standing

Next session starts at +100 GGP with 1.5x bonus!
```

**User did NOTHING manual. All tracking happened automatically.**
