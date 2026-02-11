from math import pi

class Polygon:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")


class Rectangle(Polygon):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Square(Polygon):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class Circle(Polygon):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)


def main():
    print("Area Calculator Using OOP")
    print("1. Rectangle")
    print("2. Square")
    print("3. Triangle")
    print("4. Circle")

    choice = int(input("Choose a shape (1–4): "))

    if choice == 1:
        l = float(input("Enter length: "))
        w = float(input("Enter width: "))
        shape = Rectangle(l, w)

    elif choice == 2:
        s = float(input("Enter side: "))
        shape = Square(s)

    elif choice == 3:
        b = float(input("Enter base: "))
        h = float(input("Enter height: "))
        shape = Triangle(b, h)

    elif choice == 4:
        r = float(input("Enter radius: "))
        shape = Circle(r)

    else:
        print("Invalid choice")
        return

    print(f"Area = {shape.area()}")


if __name__ == "__main__":
    main()
