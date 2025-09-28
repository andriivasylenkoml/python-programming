import math


def y_calculate():
    x_start = 2.3
    x_end = 5.4
    dx = 0.8

    x = x_start
    while x <= x_end + 1e-9: # додаємо невеликий допуск через похибку з float
        y = (x + math.cos(2 * x)) / (3 * x)
        print(f"x = {x:.1f}, y = {y:.6f}")
        x += dx


def calculate_y(x: float) -> float:
    """Обчислює значення функції y = (3x + 2)^2 / (sin(x) + 3)."""
    return (3 * x + 2) ** 2 / (math.sin(x) + 3)

def main():
    x_start = 4.8
    x_end = 7.9
    dx = 0.4
    
    x = x_start
    results = []
    
    while x <= x_end + 1e-9:
        y = calculate_y(x)
        results.append((x, y))
        x += dx
        
    # Вивід таблицею.
    print(f"{'x':>6} | {'y':>12}")
    print("-" * 22)
    for x_val, y_val in results:
        print(f"{x_val:6.2f} | {y_val:12.6f}")
    
if __name__ == "__main__":
    main()