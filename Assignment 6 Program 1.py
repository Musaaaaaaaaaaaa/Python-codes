##Name: Moosa Shehzad Abbasi
##UID: U37033529
##Brief Description of the program: N-sided Polygon class definition and main function 



import math

class RegularPolygon:
    def __init__(self):
        self._num_sides = 0
        self._side_length = 0.0

    def set_num_sides(self, num_sides):
        if num_sides >= 3:
            self._num_sides = num_sides
        else:
            print("Invalid entry. Number of sides must be at least 3. Re-enter the number of sides (>=3): ")

    def set_side_length(self, side_length):
        if side_length >= 0.1:
            self._side_length = side_length
        else:
            print("Invalid entry. Length of each side must be at least 0.1. Re-enter the length of each side (>= 0.1): ")

    def get_num_sides(self):
        return self._num_sides

    def get_side_length(self):
        return self._side_length

    def perimeter(self):
        n = self.get_num_sides()
        s = self.get_side_length()
        perimeter = n * s
        return perimeter

    def area(self):
        n = self.get_num_sides()
        s = self.get_side_length()
        area = (n * s**2) / (4 * math.tan(math.pi / n))
        return area

def main():
    polygon = RegularPolygon()

    # Prompt the user for the number of sides
    while True:
        try:
            num_sides = int(input("Enter the number of sides (>=3): "))
            polygon.set_num_sides(num_sides)
            if polygon.get_num_sides() >= 3:
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Prompt the user for the length of each side
    while True:
        try:
            side_length = float(input("Enter the length of each side (>=0.1): "))
            polygon.set_side_length(side_length)
            if polygon.get_side_length() >= 0.1:
                break
        except ValueError:
            print("Invalid input. Please enter a floating-point number.")

    # Display the current dimensions of the polygon using accessor methods
    print(f"The polygon has {polygon.get_num_sides()} sides. Each side is {polygon.get_side_length()} units in length.")

    # Display the polygon's perimeter and area formatted to 3 decimal places
    perimeter = polygon.perimeter()
    area = polygon.area()
    print(f"The perimeter of the polygon is {perimeter:.3f} units and its area is {area:.3f} square units.")

if __name__ == "__main__":
    main()
