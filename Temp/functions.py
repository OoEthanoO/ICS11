def draw_rect(x: int, y: int, w: int, h: int) -> None:
    if w <= 0 or h <= 0:
        raise ValueError("Width and height must be positive")
    
    print(f"Drawing {w}x{h} at ({x}, {y})")

draw_rect(52, 35, 150, 200)
draw_rect(52, 35, -150, 200)