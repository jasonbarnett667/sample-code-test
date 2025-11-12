"""
Shopping Cart Implementation

Implement the ShoppingCart class to make all tests pass.
Follow TDD principles: run tests frequently and implement one feature at a time.
"""


class ShoppingCart:
    """A shopping cart that manages items, discounts, and calculates totals with tax."""

    TAX_RATE = 0.085  # 8.5% tax rate

    def __init__(self):
        """Initialize an empty shopping cart."""
        # TODO: Initialize data structures to store cart items and discount info
        pass

    def add_item(self, name: str, price: float, quantity: float) -> None:
        """
        Add an item to the cart.

        Args:
            name: The name of the item
            price: The price per unit
            quantity: The quantity to add

        Raises:
            ValueError: If price is negative or quantity is <= 0
        """
        # TODO: Implement item adding logic
        # Remember to:
        # - Validate price and quantity
        # - Handle adding the same item multiple times (combine quantities)
        # - Store the item information
        pass

    def remove_item(self, name: str) -> None:
        """
        Remove an item from the cart completely.

        Args:
            name: The name of the item to remove
        """
        # TODO: Implement item removal
        # Should silently do nothing if item doesn't exist
        pass

    def get_item_count(self) -> int:
        """
        Get the number of unique items in the cart.

        Returns:
            The count of unique items (not total quantity)
        """
        # TODO: Return the number of unique items
        pass

    def get_subtotal(self) -> float:
        """
        Calculate the subtotal (before tax and discounts).

        Returns:
            The subtotal rounded to 2 decimal places
        """
        # TODO: Calculate and return subtotal
        # Sum up (price * quantity) for all items
        pass

    def apply_discount(self, code: str, discount_type: str, value: float) -> None:
        """
        Apply a discount code to the cart.

        Args:
            code: The discount code name (for reference)
            discount_type: Either "percentage" or "fixed"
            value: The discount value (percentage or fixed amount)
        """
        # TODO: Store discount information
        # Only one discount can be active at a time (most recent wins)
        pass

    def get_total(self) -> float:
        """
        Calculate the total cost after discounts and tax.

        Returns:
            The final total rounded to 2 decimal places

        Business logic:
            1. Calculate subtotal
            2. Apply discount (if any)
            3. Ensure discounted amount doesn't go below 0
            4. Apply tax to the discounted amount
            5. Round to 2 decimal places
        """
        # TODO: Implement total calculation with discounts and tax
        # Order: subtotal -> discount -> tax
        # Make sure total never goes below 0
        pass
