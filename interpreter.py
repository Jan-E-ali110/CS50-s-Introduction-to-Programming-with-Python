x,y,z  = input("Expression: ").strip().split(" ")


int1_x = float(x)
int2_z = float(z)


new_number = f"{int1_x, int2_z}:.1f "


if y == "+":
    print(int1_x + int2_z)

elif y == "-":
    print(int1_x - int2_z)

elif y == "*":
    print(int1_x * int2_z)

elif y == "/":
    print(int1_x / int2_z)

