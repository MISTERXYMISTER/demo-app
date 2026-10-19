import unittest
from src.cart import calculate_cart_total


class TestQAIssue5(unittest.TestCase):
    """Rigorous adversarial QA boundary and edge-case tests for issue #5."""

    def test_promo15_preserves_cents_fractional_discount(self):
        """Test that PROMO15 does not truncate fractional cents by casting to int."""
        # 10.0 * 0.85 = 8.5
        items = [{"price": 10.0, "quantity": 1}]
        total = calculate_cart_total(items, coupon_code="PROMO15")
        self.assertEqual(total, 8.5)

    def test_promo15_sub_dollar_amount(self):
        """Test PROMO15 on an item less than one dollar."""
        # 1.0 * 0.85 = 0.85
        items = [{"price": 1.0, "quantity": 1}]
        total = calculate_cart_total(items, coupon_code="PROMO15")
        self.assertEqual(total, 0.85)

    def test_promo15_cents_rounding(self):
        """Test PROMO15 with fractional cents rounding to 2 decimal places."""
        # 19.99 * 0.85 = 16.9915 -> 16.99
        items = [{"price": 19.99, "quantity": 1}]
        total = calculate_cart_total(items, coupon_code="PROMO15")
        self.assertEqual(total, 16.99)

        # 15.0 * 0.85 = 12.75
        items = [{"price": 15.0, "quantity": 1}]
        total = calculate_cart_total(items, coupon_code="PROMO15")
        self.assertEqual(total, 12.75)

    def test_promo15_empty_cart(self):
        """Test empty cart with PROMO15 returns 0.0."""
        self.assertEqual(calculate_cart_total([], coupon_code="PROMO15"), 0.0)

    def test_promo15_zero_priced_items(self):
        """Test cart with zero total cannot drop below 0.0."""
        items = [{"price": 0.0, "quantity": 5}]
        self.assertEqual(calculate_cart_total(items, coupon_code="PROMO15"), 0.0)

    def test_promo15_default_quantity(self):
        """Test item with omitted quantity key defaults to 1."""
        # 10.0 * 0.85 = 8.5
        items = [{"price": 10.0}]
        self.assertEqual(calculate_cart_total(items, coupon_code="PROMO15"), 8.5)

    def test_promo15_multiple_quantities(self):
        """Test cart with multiple items and quantities."""
        items = [
            {"price": 10.0, "quantity": 2},  # 20.0
            {"price": 5.0, "quantity": 1},   # 5.0 -> total 25.0
        ]
        # 25.0 * 0.85 = 21.25
        self.assertEqual(calculate_cart_total(items, coupon_code="PROMO15"), 21.25)

    def test_promo15_return_type_is_float(self):
        """Test return type is strictly float."""
        items = [{"price": 100.0, "quantity": 1}]
        total = calculate_cart_total(items, coupon_code="PROMO15")
        self.assertIsInstance(total, float)


if __name__ == "__main__":
    unittest.main()
