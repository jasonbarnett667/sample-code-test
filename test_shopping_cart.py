import pytest
from shopping_cart import ShoppingCart


class TestShoppingCartBasics:
    """Test basic cart operations"""

    def test_new_cart_is_empty(self):
        cart = ShoppingCart()
        assert cart.get_item_count() == 0

    def test_add_single_item(self):
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50, 1)
        assert cart.get_item_count() == 1

    def test_add_multiple_items(self):
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50, 2)
        cart.add_item("Banana", 0.75, 3)
        assert cart.get_item_count() == 2

    def test_add_same_item_multiple_times_combines_quantity(self):
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50, 2)
        cart.add_item("Apple", 1.50, 3)
        assert cart.get_item_count() == 1
        # Should have 5 apples total


class TestItemRemoval:
    """Test removing items from cart"""

    def test_remove_item_completely(self):
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50, 2)
        cart.remove_item("Apple")
        assert cart.get_item_count() == 0

    def test_remove_nonexistent_item_does_nothing(self):
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50, 2)
        cart.remove_item("Banana")  # Doesn't exist
        assert cart.get_item_count() == 1


class TestPriceCalculations:
    """Test price and total calculations"""

    def test_subtotal_single_item(self):
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50, 2)
        assert cart.get_subtotal() == 3.00

    def test_subtotal_multiple_items(self):
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50, 2)
        cart.add_item("Banana", 0.75, 4)
        assert cart.get_subtotal() == 6.00

    def test_total_with_tax_no_discount(self):
        cart = ShoppingCart()
        cart.add_item("Apple", 10.00, 1)
        # 10.00 + 8.5% tax = 10.85
        assert cart.get_total() == 10.85

    def test_empty_cart_has_zero_total(self):
        cart = ShoppingCart()
        assert cart.get_subtotal() == 0.00
        assert cart.get_total() == 0.00


class TestDiscountCodes:
    """Test discount code functionality"""

    def test_apply_percentage_discount(self):
        cart = ShoppingCart()
        cart.add_item("Item", 100.00, 1)
        cart.apply_discount("SAVE20", discount_type="percentage", value=20)
        # 100 - 20% = 80, plus 8.5% tax = 86.80
        assert cart.get_total() == 86.80

    def test_apply_fixed_amount_discount(self):
        cart = ShoppingCart()
        cart.add_item("Item", 50.00, 1)
        cart.apply_discount("5OFF", discount_type="fixed", value=5.00)
        # 50 - 5 = 45, plus 8.5% tax = 48.83 (rounded)
        assert round(cart.get_total(), 2) == 48.83

    def test_apply_multiple_discounts_only_last_applies(self):
        cart = ShoppingCart()
        cart.add_item("Item", 100.00, 1)
        cart.apply_discount("SAVE10", discount_type="percentage", value=10)
        cart.apply_discount("SAVE20", discount_type="percentage", value=20)
        # Only 20% discount should apply
        # 100 - 20% = 80, plus 8.5% tax = 86.80
        assert cart.get_total() == 86.80

    def test_discount_cannot_make_total_negative(self):
        cart = ShoppingCart()
        cart.add_item("Item", 10.00, 1)
        cart.apply_discount("HUGE", discount_type="fixed", value=50.00)
        # Total should be 0.00, not negative
        assert cart.get_total() == 0.00

    def test_percentage_discount_on_multiple_items(self):
        cart = ShoppingCart()
        cart.add_item("Item1", 50.00, 1)
        cart.add_item("Item2", 30.00, 1)
        cart.apply_discount("SAVE10", discount_type="percentage", value=10)
        # 80 - 10% = 72, plus 8.5% tax = 78.12
        assert cart.get_total() == 78.12


class TestEdgeCases:
    """Test edge cases and error handling"""

    def test_negative_quantity_raises_error(self):
        cart = ShoppingCart()
        with pytest.raises(ValueError):
            cart.add_item("Apple", 1.50, -1)

    def test_zero_quantity_raises_error(self):
        cart = ShoppingCart()
        with pytest.raises(ValueError):
            cart.add_item("Apple", 1.50, 0)

    def test_negative_price_raises_error(self):
        cart = ShoppingCart()
        with pytest.raises(ValueError):
            cart.add_item("Apple", -1.50, 1)

    def test_floating_point_precision(self):
        cart = ShoppingCart()
        cart.add_item("Item", 0.1, 3)
        # 0.1 * 3 should equal 0.30, not 0.30000000000000004
        assert cart.get_subtotal() == 0.30

    def test_total_rounded_to_two_decimals(self):
        cart = ShoppingCart()
        cart.add_item("Item", 9.99, 1)
        total = cart.get_total()
        # Should have exactly 2 decimal places
        assert total == round(total, 2)


class TestComplexScenarios:
    """Test complex real-world scenarios"""

    def test_full_shopping_scenario(self):
        cart = ShoppingCart()
        cart.add_item("Laptop", 999.99, 1)
        cart.add_item("Mouse", 29.99, 2)
        cart.add_item("Keyboard", 79.99, 1)
        cart.apply_discount("TECH15", discount_type="percentage", value=15)

        # Subtotal: 999.99 + 59.98 + 79.99 = 1139.96
        # After 15% discount: 1139.96 * 0.85 = 969.466
        # After 8.5% tax: 969.466 * 1.085 = 1051.87
        assert round(cart.get_subtotal(), 2) == 1139.96
        assert round(cart.get_total(), 2) == 1051.87

    def test_remove_item_and_recalculate(self):
        cart = ShoppingCart()
        cart.add_item("Item1", 50.00, 1)
        cart.add_item("Item2", 30.00, 1)
        cart.apply_discount("SAVE10", discount_type="percentage", value=10)
        cart.remove_item("Item1")

        # After removal: 30.00 - 10% = 27.00, plus 8.5% tax = 29.30
        assert round(cart.get_total(), 2) == 29.30

    def test_cart_with_fractional_quantities(self):
        cart = ShoppingCart()
        # Some items can be sold by weight
        cart.add_item("Apples", 2.99, 2.5)
        # 2.99 * 2.5 = 7.475
        assert round(cart.get_subtotal(), 2) == 7.48
