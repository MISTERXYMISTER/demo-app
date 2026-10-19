import unittest
from src.cart import calculate_cart_total


class TestCartTotal(unittest.TestCase):
    def test_empty_cart(self):
        self.assertEqual(calculate_cart_total([]), 0.0)

    def test_single_item(self):
        items = [{"price": 25.0, "quantity": 2}]
        self.assertEqual(calculate_cart_total(items), 50.0)

    def test_multiple_items(self):
        items = [
            {"price": 10.0, "quantity": 1},
            {"price": 15.0, "quantity": 2},
        ]
        self.assertEqual(calculate_cart_total(items), 40.0)

    def test_flat10_coupon_deduction(self):
        items = [{"price": 50.0, "quantity": 1}]
        self.assertEqual(calculate_cart_total(items, coupon_code="FLAT10"), 40.0)

    def test_flat10_coupon_cannot_drop_below_zero(self):
        items = [{"price": 8.0, "quantity": 1}]
        self.assertEqual(calculate_cart_total(items, coupon_code="FLAT10"), 0.0)

    def test_vip20_coupon_sample(self):
        items = [{"price": 100.0, "quantity": 1}]
        self.assertEqual(calculate_cart_total(items, coupon_code="VIP20"), 80.0)


if __name__ == "__main__":
    unittest.main()
