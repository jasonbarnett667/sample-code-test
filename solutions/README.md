# Solution Guide

This folder contains a complete, working implementation of the Shopping Cart TDD kata.

## Overview

The solution uses a dictionary-based approach to store cart items and implements all required functionality including validation, discounts, and tax calculations.

## Key Design Decisions

### 1. Data Structure Choice

**Items Storage:**
```python
self.items = {
    'Apple': {'price': 1.50, 'quantity': 2},
    'Banana': {'price': 0.75, 'quantity': 3}
}
```

**Why a dictionary?**
- O(1) lookup time for checking if item exists
- Easy to update quantities when adding same item multiple times
- Natural key-value pairing (item name → item details)
- Simple to iterate for calculations

**Alternative: List of dictionaries**
```python
self.items = [
    {'name': 'Apple', 'price': 1.50, 'quantity': 2},
    {'name': 'Banana', 'price': 0.75, 'quantity': 3}
]
```
- This works but requires O(n) search to find items
- More complex to update quantities
- Better if items can have duplicate names with different prices

### 2. Discount Storage

```python
self.discount = {
    'code': 'SAVE20',
    'type': 'percentage',
    'value': 20
}
```

**Why store as a dictionary?**
- Easy to check if discount exists (None vs dict)
- Stores all necessary information in one place
- Simple to replace with new discount (only one allowed)

### 3. Validation Strategy

**Fail fast approach:** Validate inputs immediately in `add_item()`:
```python
if price < 0:
    raise ValueError("Price cannot be negative")
if quantity <= 0:
    raise ValueError("Quantity must be greater than zero")
```

This prevents invalid data from ever entering the cart.

## Implementation Details

### Adding Items

**Combining quantities for duplicate items:**
```python
if name in self.items:
    self.items[name]['quantity'] += quantity  # Add to existing
else:
    self.items[name] = {'price': price, 'quantity': quantity}  # New item
```

**Key insight:** When same item added twice, combine quantities rather than creating duplicate entries.

### Calculating Subtotal

**Using generator expression for efficiency:**
```python
subtotal = sum(item['price'] * item['quantity'] for item in self.items.values())
return round(subtotal, 2)
```

**Always round to 2 decimal places** to handle floating point precision issues.

### Discount Logic

**Order of operations is critical:**
1. Calculate subtotal
2. Apply discount
3. Ensure result ≥ 0
4. Apply tax
5. Round final result

```python
subtotal = self.get_subtotal()

# Apply discount
if self.discount:
    if self.discount['type'] == 'percentage':
        discount_amount = subtotal * (self.discount['value'] / 100)
        subtotal -= discount_amount
    elif self.discount['type'] == 'fixed':
        subtotal -= self.discount['value']

# Prevent negative
if subtotal < 0:
    subtotal = 0

# Add tax
total = subtotal * (1 + self.TAX_RATE)

return round(total, 2)
```

### Floating Point Precision

**Problem:** `0.1 * 3 = 0.30000000000000004` in Python

**Solution:** Always use `round(value, 2)` for money calculations

**Alternative approaches:**
- Use Python's `Decimal` class for precise decimal arithmetic
- Store prices in cents (integers) instead of dollars (floats)

## Testing the Solution

From the solutions folder:

```bash
# Copy solution to main directory
cp solutions/shopping_cart.py .

# Run tests
pytest test_shopping_cart.py -v

# Run with coverage
pytest test_shopping_cart.py --cov=shopping_cart
```

Expected result: All 23 tests should pass with 100% coverage.

## Common Variations & Extensions

### 1. Multiple Discount Codes

Current implementation: Only one discount (most recent wins)

**To support multiple:**
```python
self.discounts = []  # Store list of discounts

def apply_discount(self, code, discount_type, value):
    self.discounts.append({'code': code, 'type': discount_type, 'value': value})
```

Then apply all discounts in sequence or calculate the best one.

### 2. Item Categories

Add category-based discounts:
```python
self.items[name] = {
    'price': price,
    'quantity': quantity,
    'category': 'electronics'  # New field
}
```

### 3. Quantity-Based Discounts

"Buy 2 get 1 free" logic:
```python
def calculate_discounted_quantity(self, quantity, discount_rule):
    if discount_rule == 'buy2get1':
        sets = quantity // 3
        return quantity - sets  # Every 3rd item is free
    return quantity
```

### 4. Tax Exemptions

Some items don't have tax:
```python
self.items[name] = {
    'price': price,
    'quantity': quantity,
    'taxable': True  # New field
}
```

### 5. Using Decimal for Precision

```python
from decimal import Decimal, ROUND_HALF_UP

def get_total(self) -> float:
    subtotal = Decimal(str(self.get_subtotal()))
    # ... calculations with Decimal
    return float(subtotal.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
```

## Time Complexity

- `add_item()`: O(1) - Dictionary lookup and insert
- `remove_item()`: O(1) - Dictionary pop
- `get_item_count()`: O(1) - len() on dictionary
- `get_subtotal()`: O(n) - Iterate through all items
- `get_total()`: O(n) - Calls get_subtotal()
- `apply_discount()`: O(1) - Just storing values

Where n = number of unique items in cart.

## Space Complexity

O(n) where n = number of unique items stored in the items dictionary.

## Alternative Implementation: Using Classes for Items

More object-oriented approach:

```python
class CartItem:
    def __init__(self, name: str, price: float, quantity: float):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total(self) -> float:
        return self.price * self.quantity

class ShoppingCart:
    def __init__(self):
        self.items = {}  # name -> CartItem
        self.discount = None

    def add_item(self, name: str, price: float, quantity: float) -> None:
        if name in self.items:
            self.items[name].quantity += quantity
        else:
            self.items[name] = CartItem(name, price, quantity)
```

**Pros:**
- More encapsulation
- Can add item-specific methods
- Better for complex item logic

**Cons:**
- More code for this simple use case
- Slightly more complex

## Edge Cases Handled

1. ✅ Negative prices → ValueError
2. ✅ Zero/negative quantities → ValueError
3. ✅ Removing non-existent items → Silent (no error)
4. ✅ Empty cart calculations → Returns 0
5. ✅ Discounts larger than subtotal → Total becomes 0 (not negative)
6. ✅ Floating point precision → Rounded to 2 decimals
7. ✅ Adding same item twice → Quantities combined
8. ✅ Multiple discounts → Only most recent applies

## Performance Considerations

For a real production shopping cart:

1. **Database Integration:** Items would be stored in a database, not in-memory
2. **Caching:** Cache expensive calculations like subtotal
3. **Async Operations:** For API calls to payment/inventory systems
4. **Concurrency:** Handle multiple users modifying cart simultaneously
5. **Persistence:** Save cart state between sessions
6. **Audit Trail:** Log all cart modifications for debugging

## Further Reading

- [Python Decimal Documentation](https://docs.python.org/3/library/decimal.html)
- [Floating Point Arithmetic: Issues and Limitations](https://docs.python.org/3/tutorial/floatingpoint.html)
- [Test-Driven Development by Example](https://www.oreilly.com/library/view/test-driven-development/0321146530/) by Kent Beck
