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

## Environment Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Initial Setup

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone https://github.com/jasonbarnett667/sample-code-test.git
   cd sample-code-test
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   # Create virtual environment
   python3 -m venv venv

   # Activate virtual environment
   # On macOS/Linux:
   source venv/bin/activate

   # On Windows:
   venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Getting Started

1. **Run the tests** to see all failures (Red phase of TDD):
   ```bash
   python -m pytest test_shopping_cart.py -v
   ```

2. **Implement the `ShoppingCart` class** in `shopping_cart.py`

3. **Run tests frequently** as you implement each method

4. **Make all tests pass!** (Green phase of TDD)

## Running Tests

```bash
# Run all tests with verbose output
python -m pytest test_shopping_cart.py -v

# Run tests with coverage report
python -m pytest test_shopping_cart.py --cov=shopping_cart

# Run a specific test class
python -m pytest test_shopping_cart.py::TestShoppingCartBasics -v

# Run a specific test
python -m pytest test_shopping_cart.py::TestShoppingCartBasics::test_new_cart_is_empty -v
```

## Tips

- Start with the simplest tests first
- Think about data structures to store items
- Consider using a dictionary or list to track cart items
- Remember to handle floating point precision carefully
- Use descriptive variable names

---

## For Interviewers: How to Conduct This Assessment

### Overview
This TDD kata is designed as a 60-90 minute coding assessment that evaluates:
- Test-driven development methodology
- Python fundamentals and OOP concepts
- Problem-solving and debugging skills
- Handling edge cases and validation
- Code organization and readability

### Pre-Interview Setup (5 minutes)

1. **Share the repository** with the candidate ahead of time:
   ```
   https://github.com/jasonbarnett667/sample-code-test
   ```

2. **Have them complete environment setup** before the interview:
   - Clone the repo
   - Set up virtual environment
   - Install dependencies
   - Run tests to confirm setup works

### Interview Structure (60-90 minutes)

#### Phase 1: Introduction (5 minutes)
- Explain the TDD approach: Red → Green → Refactor
- Review the requirements in the README
- Confirm they can run tests and see failures
- Encourage them to ask questions as they work
- Remind them to run tests frequently

#### Phase 2: Implementation (45-60 minutes)

**Suggested Order of Implementation:**

1. **Start Simple - Basic Cart Operations** (10-15 min)
   ```python
   # Guide them to implement:
   - __init__() - Initialize data structures
   - get_item_count() - Return number of unique items
   - add_item() - Basic adding (no validation yet)
   ```
   - Run: `pytest test_shopping_cart.py::TestShoppingCartBasics -v`
   - Look for: Choice of data structure (dict vs list)

2. **Add Validation** (10 min)
   ```python
   # Guide them to add error handling:
   - Validate negative prices
   - Validate zero/negative quantities
   ```
   - Run: `pytest test_shopping_cart.py::TestEdgeCases -v`
   - Look for: Proper exception handling, input validation

3. **Implement Calculations** (10-15 min)
   ```python
   # Guide them through:
   - get_subtotal() - Sum all items
   - get_total() - Add tax (no discounts yet)
   - remove_item() - Remove from cart
   ```
   - Run: `pytest test_shopping_cart.py::TestPriceCalculations -v`
   - Look for: Floating point precision handling, rounding

4. **Add Discount Logic** (15-20 min)
   ```python
   # This is the most complex part:
   - apply_discount() - Store discount info
   - Update get_total() to apply discounts
   - Handle percentage vs fixed discounts
   - Prevent negative totals
   ```
   - Run: `pytest test_shopping_cart.py::TestDiscountCodes -v`
   - Look for: Logic complexity, order of operations, edge cases

#### Phase 3: Review and Discussion (10-15 minutes)

1. **Run full test suite**:
   ```bash
   pytest test_shopping_cart.py -v
   ```

2. **Code Review Discussion**:
   - Ask them to explain their data structure choice
   - Discuss alternative approaches
   - Ask about potential improvements or optimizations
   - Discuss how they'd extend this (coupons, taxes by region, etc.)

3. **Testing Coverage**:
   ```bash
   pytest test_shopping_cart.py --cov=shopping_cart
   ```
   - Review coverage report together
   - Discuss any uncovered branches

### What to Look For

#### Strong Candidates Will:
- ✅ Run tests frequently (after each method implementation)
- ✅ Start with simplest cases first
- ✅ Write clean, readable code with good variable names
- ✅ Handle edge cases thoughtfully
- ✅ Ask clarifying questions about requirements
- ✅ Use appropriate data structures (dict for items)
- ✅ Properly round floating point numbers
- ✅ Complete most or all tests within time limit

#### Red Flags:
- ❌ Don't run tests until the end
- ❌ Ignore test failures and move on
- ❌ Poor variable naming (x, y, z, temp, etc.)
- ❌ No input validation
- ❌ Overcomplicate simple solutions
- ❌ Can't debug failing tests
- ❌ Don't ask any questions about ambiguous requirements

### Difficulty Adjustments

**Make it Easier:**
- Give hints about data structures: "A dictionary might work well here"
- Point them to specific failing tests: "Let's focus on this test first"
- Provide pseudocode for complex logic (discount calculation)
- Allow them to skip edge case tests initially

**Make it Harder:**
- Add time pressure (45 minutes instead of 60)
- Ask them to implement additional features:
  - Tax rates that vary by item type
  - Multiple discount codes that stack
  - Item categories with category-specific discounts
  - Quantity-based discounts (buy 2 get 1 free)
- Request they write additional test cases
- Ask them to refactor for better design patterns

### Sample Walkthrough Script

When guiding a candidate, you might say:

> "Let's start by getting the first test to pass. Run the TestShoppingCartBasics tests. What data structure do you think would work well for storing cart items? Once you've decided, implement `__init__` and `get_item_count`, then run the tests again."

> "Great! Now let's implement `add_item`. What validations do you think we need? Run the edge case tests to see what's expected."

> "Now that items are working, let's calculate the subtotal. How would you sum up all the items in the cart?"

> "The discount logic is the trickiest part. Let's think about the order of operations: subtotal → discount → tax. How do we handle the different discount types?"

### Evaluation Rubric

| Criteria | Poor (1) | Fair (2) | Good (3) | Excellent (4) |
|----------|----------|----------|----------|---------------|
| **TDD Approach** | Rarely runs tests | Runs tests occasionally | Runs tests after each method | Follows Red-Green-Refactor strictly |
| **Code Quality** | Hard to read, poor naming | Somewhat readable | Clean and organized | Exceptionally clear and maintainable |
| **Problem Solving** | Struggles with basic logic | Completes basic features | Handles most requirements | Completes all + handles edge cases |
| **Debugging** | Can't fix failing tests | Fixes with heavy hints | Debugs independently | Debugs efficiently and explains issues |
| **Communication** | Silent, no questions | Minimal communication | Explains thinking clearly | Great collaboration and questions |

### Common Pitfalls & How to Help

1. **Floating Point Precision**
   - Issue: `0.1 * 3 = 0.30000000000000004`
   - Hint: "Python's `round()` function can help here"

2. **Discount Order of Operations**
   - Issue: Applying tax before discount or vice versa
   - Hint: "Check the business rules - what order should these be applied?"

3. **Negative Totals**
   - Issue: Discount makes total negative
   - Hint: "What should happen if a $100 discount is applied to a $50 cart?"

4. **Item Quantity Combining**
   - Issue: Adding same item twice creates two entries
   - Hint: "If I add 2 apples, then add 3 more apples, how many apples should be in the cart?"

Good luck with your interviews!
