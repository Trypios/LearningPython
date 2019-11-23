# GRAPHING
# -POINT SLOPE
# -SLOPE INTERCEPT


# INTRODUCTION
print("Insert the coordinates of two points of a 2D Cartesian plane, to calculate\n")
print("* slope,")
print("* y-intercept,")
print("* point slope formula,")
print("* slope intercept formula\n\n")

# VALUES 
pointA_x = float(input("insert pointA x:"))
pointA_y = float(input("insert pointA y:"))
pointB_x = float(input("insert pointB x:"))
pointB_y = float(input("insert pointB y:"))
print()

pointA_xy = (pointA_x,pointA_y)
pointB_xy = (pointB_x,pointB_y)
points_xy = (pointA_xy,pointB_xy)

# SLOPE
m = (pointA_y- pointB_y) / (pointA_x - pointB_x)

# Y INTERCEPT
y = (pointA_y-pointB_y)
b = (pointA_y - m*pointA_x)

# POINT SLOPE FORMULA
point_slope_formula = ((pointA_y-pointB_y) == m*(pointA_x - pointB_x))

# SLOPE INTERCEPT FORMULA
slope_intercept_formula = ((pointA_y - pointB_y) == m*(pointA_x - pointB_x))

# RESULTS
print("Point A coordinates:",pointA_xy)
print("Point B coordinates:",pointB_xy)
print("Y intercept coordinates:","(0,",b,")")
print("Slope:","m =","%.2f" % m)
print()
print("Graph equation in Point Slope form:","y =",m,"* x +",b,)
print("Graph equation in Slope Intercept form: (",pointA_y,"-",pointB_y,") =",m,"* (",pointA_x,"-",pointB_x,")\n")
print("Plug in x value to solve for y")
print()
x_value = float(input("Plug in x value to solve for y:"))
y_value = m*x_value + b
print(y_value)
