# ── INVENTORY TRACKER ─────────────────────────────────────────────────────────
# Topics: Asymptotic Analysis | Big-O | Omega | Theta
#         Best / Worst / Average Case | O(1) O(n) O(n^2)


# ── PART 1: Product Inventory ────────────────────────────────────────────────
# Five products and their quantities.

products   = ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"]
quantity   = [15,       40,      25,         10,        8]
n = len(quantity)

print("=== Inventory Tracker (n =", n, "products) ===")
for i in range(n):
    print(i + 1, ". ", products[i], " : ", quantity[i], sep="")
print()


# ── PART 2: Theta(1) — direct index access ───────────────────────────────────
# Accessing the first quantity always takes one step.

steps = 1
print("Quantity at index 0 :", quantity[0], "| steps =", steps, "| Theta(1) - constant time")
print()


# ── PART 3: O(n) — linear search ─────────────────────────────────────────────
# Search for a product name.

target = "Laptop"
steps = 0

for item in products:
    steps += 1
    if item == target:
        break

print("Search for", target, "| steps =", steps, "| Omega(1) - best case")

target = "Printer"
steps = 0

for item in products:
    steps += 1
    if item == target:
        break

print("Search for", target, "| steps =", steps, "| O(n) =", n, "- worst case")
print()


# ── PART 4: O(n^2) — compare product quantities ──────────────────────────────
# Find all product pairs with a combined quantity of 50.

steps = 0
target_total = 50

print("Pairs with total quantity =", target_total, ":")

for i in range(n):
    for j in range(i + 1, n):
        steps += 1
        if quantity[i] + quantity[j] == target_total:
            print(" ", products[i], "+", products[j], "=", quantity[i] + quantity[j])

print("Total comparisons :", steps, "| O(n^2) - quadratic growth")
print()


# ── PART 5: Asymptotic Summary ───────────────────────────────────────────────
print("=== Asymptotic Summary ===")
print("Theta(1) : direct access - constant time")
print("Omega(1) : best search   - found immediately")
print("O(n)     : linear search - up to n =", n, "checks")
print("O(n^2)   : pair compare  -", n * (n - 1) // 2, "comparisons")
print()
print("Focus on the dominant growth term when analyzing efficiency!")