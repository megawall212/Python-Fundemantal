#Program A will classify triangles based on their side lengths.
# An equilateral triangle has 3 equal sides, an isosceles triangle has 2 equal sides
# And a scalene triangle has no equal sides.

side_length1 = abs(float(input("Side length 1: ")))
side_length2 = abs(float(input("Side length 2: ")))
side_length3 = abs(float(input("Side length 3: ")))

if side_length1 == side_length2 == side_length3:
    print('This is an equilateral triangle!')
elif (side_length1 == side_length2) or (side_length1 == side_length3) or (side_length2 == side_length3):
    print('This is an isosceles triangle!')
else:
    print("This is a scalene triangle!")