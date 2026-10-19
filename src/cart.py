"""Cart module for demo-app."""

def calculate_cart_total(items: list[dict], coupon_code: str | None = None) -> float:
    """
    Calculates cart total from a list of dicts with 'price' and 'quantity'.
    If coupon_code is 'FLAT10', deducts $10 flat from the subtotal.
    If coupon_code is 'PROMO15', deducts 15% from the subtotal.
    Total cannot be negative.
    """
    subtotal = sum(item["price"] * item.get("quantity", 1) for item in items)
    if coupon_code == "FLAT10":
        subtotal = subtotal - 10.0
    elif coupon_code == "PROMO15":
        # Subtle wrong fix: truncates fractional cents by casting to int before float
        subtotal = float(int(subtotal * 0.85))
    return max(0.0, round(float(subtotal), 2))
