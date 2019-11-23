# PART1 - CALCULATING THE MIDPOINT BETWEEN 3 POINTS in 3D
#   Original formula: midpoint = [(x1+x2)/2 , (y1+y2)/2 , (z1+z2)/2]
# PART2 - CALCULATING THE DISTANCE BETWEEN 2 POINTS IN 3D
#   Original formula: distance = √[(x1-x2)^2 + (y1-y2)^2 + (z1-z2)^2]


# INTRODUCTION
print("Insert the coordinates of two points of a 3D Cartesian plane, to calculate\n")
print("* the midpoint")
print("* the distance between them\n\n")

# VALUES 
pointA_x = float(input("insert pointA x:"))
pointA_y = float(input("insert pointA y:"))
pointA_z = float(input("insert pointA z:"))
print()
pointB_x = float(input("insert pointB x:"))
pointB_y = float(input("insert pointB y:"))
pointB_z = float(input("insert pointB z:"))
print()

pointA_xyz = (pointA_x,pointA_y,pointA_z)
pointB_xyz = (pointB_x,pointB_y,pointB_z)
points_xyz = (pointA_xyz,pointB_xyz)

# MIDPOINT IN 3D FORMULA
midpoint_x = ((pointA_x + pointB_x)/2.0)
midpoint_y = ((pointA_y + pointB_y)/2.0)
midpoint_z = ((pointA_z + pointB_z)/2.0)
midpoint = (midpoint_x,midpoint_y,midpoint_z)

# DISTANCE BETWEEN 2 POINTS IN 3D FORMULA1
# LONG FORMAT
distance = (((pointA_x - pointB_x)**2)+((pointA_y - pointB_y)**2)+((pointA_z - pointB_z)**2))**0.5

# DISTANCE BETWEEN 2 POINTS IN 3D FORMULA2
# CLEANER FORMAT
"""
square_x = (pointA_x - pointB_x)**2
square_y = (pointA_y - pointB_y)**2
square_z = (pointA_z - pointB_z)**2
root_xyz = (midpoint_x, midpoint_y, midpoint_z)**0.5
distance = (root_xyz)
"""

print("The midpoint of Point-A",pointA_xyz,"and Point-B",pointB_xyz)
print("is",midpoint)
print()
print("The distance between those points")
print("is","%.2f" % distance)
