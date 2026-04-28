import math

# 1. Seviye: Fonksiyon tanımı
def triangle_area(base, height):
    # 2. Seviye: Fonksiyonun içi (İçeride olmalı!)
    """Calculates the area of a triangle."""
    return 0.5 * base * height

# 1. Seviye: Fonksiyon tanımı
def square_area(side):
    # 2. Seviye: Fonksiyonun içi (İçeride olmalı!)
    """Calculates the area of a square."""
    return side ** 2

# 1. Seviye: Ana çalışma bloğu
if __name__ == "__main__":
    # 2. Seviye: Bu bloğun altındakiler de içeride olmalı!
    # Demonstration of current logic
    print(f"Triangle Area (b=10, h=5): {triangle_area(10, 5)}")
    print(f"Square Area (a=4): {square_area(4)}")