def calculate_area(shape, x, y=0):
    if shape == "circle":
        print("Area of circle is:", 3.14 * x * x)

    elif shape == "Rectangle":
        print("Area of rectangle is:", x * y)

    elif shape == "Triangle":
        print("Area of triangle is:", 0.5 * x * y)


while True:
    shape = input("Enter a shape name (Triangle, Rectangle, circle): ")

    if shape == "circle":
        a = float(input("Enter radius of circle: "))
        calculate_area(shape, a)

    elif shape == "Rectangle":
        l = float(input("Enter length of rectangle: "))
        w = float(input("Enter width of rectangle: "))
        calculate_area(shape, l, w)

    elif shape == "Triangle":
        b = float(input("Enter base of triangle: "))
        h = float(input("Enter height of triangle: "))
        calculate_area(shape, b, h)

    elif shape == "stop":
        print("End of the program")
        break

    else:
        print("Invalid choice")