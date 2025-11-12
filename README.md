# Shopping Cart TDD Kata

## Problem Description

Implement a shopping cart system that handles items, prices, discounts, and tax calculations.

## Requirements

Your `ShoppingCart` class should support:

1. **Adding items** with name, price, and quantity
2. **Removing items** from the cart
3. **Applying discount codes** with different types:
   - Percentage discounts (e.g., "SAVE20" for 20% off)
   - Fixed amount discounts (e.g., "5OFF" for $5 off)
4. **Calculating subtotal** (before tax and discounts)
5. **Calculating total** (after discounts and tax)
6. **Handling edge cases**:
   - Negative quantities should raise ValueError
   - Negative prices should raise ValueError
   - Invalid discount codes should be ignored
   - Discount cannot make total go below $0

## Business Rules

- Tax rate is 8.5%
- Discount codes can only be applied once
- Discounts are applied before tax
- Item prices should be stored as floats
- Final totals should be rounded to 2 decimal places

## Getting Started

1. Run the tests: `python -m pytest test_shopping_cart.py -v`
2. Implement the `ShoppingCart` class in `shopping_cart.py`
3. Make all tests pass!

## Running Tests

```bash
# Install pytest if you haven't already
pip install pytest

# Run all tests
python -m pytest test_shopping_cart.py -v

# Run tests with coverage
pip install pytest-cov
python -m pytest test_shopping_cart.py --cov=shopping_cart
```

## Tips

- Start with the simplest tests first
- Think about data structures to store items
- Consider using a dictionary or list to track cart items
- Remember to handle floating point precision carefully
- Use descriptive variable names

Good luck!
