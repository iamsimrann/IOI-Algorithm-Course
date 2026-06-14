# ── ALGORITHM ANALYSIS — Tracking Daily Savings ───────────────────────────────
# Topics: Algorithm | Pseudocode | Time Complexity | Space Complexity
#         One Problem Three Solutions | Comparing Efficiency


# ── PART 1: The problem — set n = 5 days ─────────────────────────────────────
# Save ₹1 on Day 1, ₹2 on Day 2, ... ₹n on Day n.
# Find the total savings using THREE different methods.

n = 5
print("=== Daily Savings Tracker (n =", n, "days) ===")
print()


# ── PART 2: Formula way — always 1 step ──────────────────────────────────────
# Algorithm  : Use a direct formula
# Pseudocode : total = n * (n + 1) / 2
# Time cost  : 1 step
# Space cost : 1 variable

total = n * (n + 1) // 2
print("Formula way : total =", total, "| steps = 1")


# ── PART 3: Loop way — n steps ───────────────────────────────────────────────
# Algorithm  : Add savings day by day
# Pseudocode : FOR day FROM 1 TO n: total += day
# Time cost  : n steps
# Space cost : 2 variables

total = 0
steps = 0
for day in range(1, n + 1):
    total += day
    steps += 1

print("Loop way    : total =", total, "| steps =", steps)


# ── PART 4: Nested loop way — roughly n*n steps ──────────────────────────────
# Algorithm  : Add ₹1 repeatedly for every rupee saved
# Pseudocode : FOR day FROM 1 TO n: FOR rupee FROM 1 TO day: total += 1
# Time cost  : roughly n*n steps
# Space cost : 3 variables

total = 0
steps = 0

for day in range(1, n + 1):
    for rupee in range(1, day + 1):
        total += 1
        steps += 1

print("Nested loop : total =", total, "| steps =", steps)


# ── PART 5: Try n = 12 and compare ───────────────────────────────────────────
n = 12
nested_steps = 0

for day in range(1, n + 1):
    for rupee in range(1, day + 1):
        nested_steps += 1

print()
print("=== Now with n =", n, "days ===")
print("Formula way : steps = 1        (always constant)")
print("Loop way    : steps =", n)
print("Nested loop : steps =", nested_steps, "(increases much faster)")
print()
print("Same result — but different efficiency levels. This demonstrates time complexity!")