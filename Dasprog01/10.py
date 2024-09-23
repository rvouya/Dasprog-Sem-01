#get the coordinates
x1, y1 = map(float, input("Enter two coordinates separated by a space: ").split())
x2, y2 = map(float, input("Enter two coordinates separated by a space: ").split())

#compute slope of the line
import sys
def slope(x1, y1, x2, y2):
    slope = float((y2-y1)/(x2-x1))
    return slope
if x1 == x2 or y1 == y2:
    print("The line is undefined, try again.")
    sys.exit()
else:
    slope = float((y2-y1)/(x2-x1))
print(f"The slope of the line : {slope}")

#midpoint of the line segment
midpoint_x = (x1+x2)/2
midpoint_y = (y1+y2)/2

#slope of the perpendicular bisector
perp_slope = -1/slope

#y-intercept of the perpendicular bisector
y_int = (midpoint_y - (perp_slope*midpoint_x))

print(f"Equation of the perpendicular bisector: y = {perp_slope}x + {y_int}")