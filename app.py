def calculate_savings(base, amount):
    """Calculates total savings after a deposit with basic validation."""
    if base < 0 or amount < 0:
        raise ValueError("Base and amount must be non‑negative.")
    return base + amount
