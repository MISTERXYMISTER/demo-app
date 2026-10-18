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


if __name__ == "__main__":
    unittest.main()
