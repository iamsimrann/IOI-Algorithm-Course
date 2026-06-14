# ================================
#  MY FOOD STORE
#  File: my-food-store.py
# ================================


# PART 1 — TYPES OF DATA
item_name    = "Cookies"   # str   — text
cost         = 2.50        # float — decimal
stock        = 15          # int   — whole number
in_stock     = True        # bool  — True or False

print("Item:", item_name)
print("Cost: $", cost)
print("Stock Available:", stock)
print("Currently Available?", in_stock)

print(type(item_name))
print(type(cost))
print(type(stock))
print(type(in_stock))


# PART 2 — ARITHMETIC OPERATORS
inventory_value = cost * stock
print("Inventory value: $", inventory_value)
print("Discounted cost: $", cost - 0.50)
print("Updated stock:", stock * 2)


# PART 3 — COMPARISON OPERATORS
print("Is the cost below $3?", cost < 3)
print("Are there more than 10 items?", stock > 10)
print("Is the cost exactly $2.50?", cost == 2.50)


# PART 4 — STRING OPERATIONS
store_name = "Fresh" + " " + "Treats"
print("Store name:", store_name)
print("Characters in item name:", len(item_name))
print("Starting letter:", item_name[0])


# PART 5 — SWAPPING VALUES
cost_a = 2.50
cost_b = 4.00
print("Before swap:", cost_a, "and", cost_b)

temp   = cost_a
cost_a = cost_b
cost_b = temp

print("After swap:", cost_a, "and", cost_b)