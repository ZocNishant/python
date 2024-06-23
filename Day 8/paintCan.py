import math

def paint_calc(height, width, cover):
    print(math.ceil((height * width) / cover))


test_h = int(input("Enter Height of wall: "))
test_w = int(input("Enter Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)