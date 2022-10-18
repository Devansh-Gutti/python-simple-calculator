from tkinter import messagebox

# myArea takes 5 arguments and gives us area of 2D shapes


def myArea(name, length, breadth, height, radius):
    name = name.lower()
    if name == "rectangle":
        return(length*breadth)
    elif name == "square":
        return(length**2)
    elif name == "triangle":
        return(0.5*breadth*height)
    elif name == "circle":
        return(3.14*radius**2)
    else:
        return(-1)

# myvolume takes 5 args and gives volume of 3D shapes


def myvolume(name, length, breadth, height, radius):
    name = name.lower()
    if name == "sphere":
        return(4/3*radius**3)
    elif name == "cube":
        return(length**3)
    elif name == "cone":
        return(0.33*radius**2*height)
    elif name == "cuboid":
        return(length*breadth*height)
    elif name == "cylinder":
        return(3.14*radius**2*height)
    else:
        return(-1)

# mycondition returns complementary angle for angles <=90 deg, supplementary angle for angles <= 180 deg
# error is returned in other cases
# mycondition also checks pythagoras theorem for 3 numbers and tells whether it is a py triplet or not


def mycondition(condition, a, b, c, angle):
    if condition == "Pythagorean Triplet Checker":
        if a**2+b**2 == c**2:
            return(1)
        else:
            return(2)
    if condition == "Complimentary&Supplementary Angles":
        if angle <= 90:
            com = 90-angle
            sup = 180-angle
        elif angle <= 180:
            sup = 180-angle
            com = "error"
        else:
            sup = com = "error"
        comsuplist = [com, sup]
        com1 = comsuplist[0]
        sup1 = comsuplist[1]
        messagebox.showinfo("Complementary Angle", com1)
        messagebox.showinfo("Supplementary Angle", sup1)
    return comsuplist
