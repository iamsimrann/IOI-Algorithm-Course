# BOOK SEARCH ANALYZER
# Topics: O(log n) | Binary Search | Recursion | Recursive Time | Space | Complexity Ladder


# PART 1: Setup — Sorted book IDs, target = 110

book_ids = [101, 103, 105, 107, 109, 110, 115, 120, 125, 130]
n, target = len(book_ids), 110

print("=== Book Search Analyzer (n =", n, "books) ===")
print("Book IDs:", book_ids, "| Target:", target)
print()


# PART 2: Linear Search — O(n)

steps = 0
for i in range(n):
    steps += 1
    if book_ids[i] == target:
        print("Linear search    : index =", i, "| steps =", steps, "| O(n)")
        break

print()


# PART 3: Binary Search — O(log n)

low, high, steps = 0, n - 1, 0

while low <= high:
    mid = (low + high) // 2
    steps += 1

    if book_ids[mid] == target:
        print("Binary search    : index =", mid, "| steps =", steps, "| O(log n)")
        break
    elif book_ids[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

print()


# PART 4: Recursive Binary Search — O(log n)

def recursive_search(items, low, high, target, calls=0):
    calls += 1

    if low > high:
        return -1, calls

    mid = (low + high) // 2

    if items[mid] == target:
        return mid, calls
    elif items[mid] < target:
        return recursive_search(items, mid + 1, high, target, calls)
    else:
        return recursive_search(items, low, mid - 1, target, calls)

result, calls = recursive_search(book_ids, 0, n - 1, target)

print("Recursive search : index =", result, "| calls =", calls, "| O(log n)")
print()


# PART 5: Space Complexity and Complexity Ladder

print("=== Space and Complexity Summary ===")
print("Iterative : O(1) space      — uses only low, high, mid")
print("Recursive : O(log n) space  —", calls, "stack frames for n =", n)

print()
print("Complexity ladder (n =", n, "):")
print("O(1)     : 1 step    — constant time")
print("O(log n) :", steps, "steps   — grows slowly")
print("O(n)     :", n, "steps   — linear growth")
print("O(n^2)   :", n * n, "steps  — quadratic growth")