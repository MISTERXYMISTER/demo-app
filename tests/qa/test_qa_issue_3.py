import unittest
from src.cart import calculate_cart_total


class TestQAIssue3VIP20Coupon(unittest.TestCase):
    """Adversarial QA edge-case and boundary tests for issue #3 (VIP20 coupon)."""

    def test_vip20_boundary_exact_50(self):
        """Boundary test: exactly $50.0 should receive a 20% discount ($40.0)."""
        items = [{"price": 50.0, "quantity": 1}]
        self.assertEqual(calculate_cart_total(items, coupon_code="VIP20"), 40.0)

    def test_vip20_boundary_just_below_50(self):
        """Boundary test: $49.99 is < $50.0 and should receive 0 discount."""
        items = [{"price": 49.99, "quantity": 1}]
        self.assertEqual(calculate_cart_total(items, coupon_code="VIP20"), 49.99)

    def test_vip20_subtotal_under_50(self):
        """Edge case: cart under $50.0 should receive no discount."""
        items = [{"price": 25.0, "quantity": 1}]
        self.assertEqual(calculate_cart_total(items, coupon_code="VIP20"), 25.0)

    def test_vip20_subtotal_well_over_50(self):
        """Edge case: cart over $50.0 with different value than the issue example."""
        items = [{"price": 200.0, "quantity": 1}]
        self.assertEqual(calculate_cart_total(items, coupon_code="VIP20"), 160.0)

    def test_vip20_empty_cart(self):
        """Edge case: empty cart with VIP20 should return 0.0, not 80.0."""
        self.assertEqual(calculate_cart_total([], coupon_code="VIP20"), 0.0)

    def test_vip20_multiple_items_reaching_threshold(self):
        """Edge case: multiple items summing to >= 50.0 receive 20% discount."""
        items = [
            {"price": 15.0, "quantity": 2},
            {"price": 30.0, "quantity": 1},
        ]
        # subtotal: 30 + 30 = 60.0 -> 20% off = 48.0
        self.assertEqual(calculate_cart_total(items, coupon_code="VIP20"), 48.0)

    def test_vip20_multiple_items_below_threshold(self):
        """Edge case: multiple items summing to < 50.0 receive 0 discount."""
        items = [
            {"price": 10.0, "quantity": 2},
            {"price": 15.0, "quantity": 1},
        ]
        # subtotal: 20 + 15 = 35.0 -> no discount = 35.0
        self.assertEqual(calculate_cart_total(items, coupon_code="VIP20"), 35.0)

    def test_vip20_default_quantity(self):
        """Edge case: items without explicit quantity default to 1."""
        items = [{"price": 60.0}]
        self.assertEqual(calculate_cart_total(items, coupon_code="VIP20"), 48.0)

    def test_vip20_cents_rounding(self):
        """Edge case: fractional cents calculation with 20% discount."""
        items = [{"price": 55.55, "quantity": 1}]
        # 55.55 * 0.80 = 44.44
        self.assertEqual(calculate_cart_total(items, coupon_code="VIP20"), 44.44)


if __name__ == "__main__":
    unittest.main()
