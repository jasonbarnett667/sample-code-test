"""
Shopping Cart Implementation - Solution

This is a complete implementation of the ShoppingCart class that passes all tests.
"""

from decimal import Decimal, ROUND_HALF_UP


class ShoppingCart:
    """A shopping cart that manages items, discounts, and calculates totals with tax."""

    TAX_RATE = 0.085  # 8.5% tax rate

    def __init__(self):
        """Initialize an empty shopping cart."""
        # Use a dictionary to store items: {name: {'price': float, 'quantity': float}}
        self.items = {}
        # Store discount information as a dict: {'type': str, 'value': float}
        self.discount = None

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
        # Validate inputs
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")

        # If item already exists, add to existing quantity
        if name in self.items:
            self.items[name]['quantity'] += quantity
        else:
            # Create new item entry
            self.items[name] = {
                'price': price,
                'quantity': quantity
            }

    def remove_item(self, name: str) -> None:
        """
        Remove an item from the cart completely.

        Args:
            name: The name of the item to remove
        """
        # Use pop with default None to silently handle missing items
        self.items.pop(name, None)

    def get_item_count(self) -> int:
        """
        Get the number of unique items in the cart.

        Returns:
            The count of unique items (not total quantity)
        """
        return len(self.items)

    def _calculate_raw_subtotal(self) -> float:
        """
        Calculate the raw subtotal without rounding (internal use).

        Returns:
            The raw subtotal as a float
        """
        return sum(item['price'] * item['quantity'] for item in self.items.values())

    def get_subtotal(self) -> float:
        """
        Calculate the subtotal (before tax and discounts).

        Returns:
            The subtotal rounded to 2 decimal places
        """
        return round(self._calculate_raw_subtotal(), 2)

    def apply_discount(self, code: str, discount_type: str, value: float) -> None:
        """
        Apply a discount code to the cart.

        Args:
            code: The discount code name (for reference)
            discount_type: Either "percentage" or "fixed"
            value: The discount value (percentage or fixed amount)
        """
        # Store discount (most recent wins)
        self.discount = {
            'code': code,
            'type': discount_type,
            'value': value
        }

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
        # Use Decimal for precise calculations to avoid floating point errors
        subtotal = Decimal(str(self._calculate_raw_subtotal()))

        # Apply discount if one exists
        if self.discount:
            if self.discount['type'] == 'percentage':
                # Percentage discount: reduce by percentage
                discount_value = Decimal(str(self.discount['value']))
                discount_amount = subtotal * (discount_value / Decimal('100'))
                subtotal -= discount_amount
            elif self.discount['type'] == 'fixed':
                # Fixed discount: reduce by fixed amount
                subtotal -= Decimal(str(self.discount['value']))

        # Ensure total doesn't go below 0
        if subtotal < 0:
            subtotal = Decimal('0')

        # Apply tax
        tax_rate = Decimal(str(self.TAX_RATE))
        total = subtotal * (Decimal('1') + tax_rate)

        # Round to 2 decimal places using ROUND_HALF_UP
        rounded_total = total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        return float(rounded_total)
