class TriangleChecker:
    @staticmethod
    def is_triangle(a, b, c):
        if type(a) != int or type(b) != int or type(c) != int:
            return "Vuvedi samo chisla"
        elif a < 0 or b < 0 or c < 0:
            return "Ne stava s otr chisla"
        elif a + b > c and a + c > b and b + c > a:
            return "Stava triugulnik"
        else:
            return "Ne stava triugulnik"

print(TriangleChecker.is_triangle(1, 2, 3))
print(TriangleChecker.is_triangle(1, -2, 3))
print(TriangleChecker.is_triangle(3, 4, 5))
print(TriangleChecker.is_triangle(1, "2", 3))