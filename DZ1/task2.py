def triangle_exists(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "All sides must have positive lengths!!!"
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Triangle exists and is equilateral!"
        if a == b or b == c or a == c:
            return "Triangle exists and is isosceles!"
        return "Triangle exists and has all different sides."
    return "Triangle DOES NOT exist."


print(triangle_exists(3, 4, 5))
