# The definition is a function, it calls to do area of circle of the a value called radius
def area_of_circle(radius):
    pi = 3.14
    area = pi * radius * radius
    return area


sword_length = 1.0
spear_length = 2.0

# don't touch above this line

sword_area = area_of_circle(sword_length) # Here we call the function with a value variable we have defined, and we put it in another variable. Later we can print that variable
spear_area = area_of_circle(spear_length)

# don't touch below this line

print("Sword length:", sword_length, "meters.")
print("Sword attack area:", sword_area, "square meters")

print("Spear length:", spear_length, "meters.")
print("Spear attack area:", spear_area, "square meters")