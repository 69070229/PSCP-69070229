"""Color"""
def main():
    """Func"""
    color1 = input()
    color2 = input()
    primary = ["Red", "Yellow", "Blue"]
    color = [color1, color2]
    if (color1 not in primary) or (color2 not in primary):
        print("Error")
    elif color1 == color2:
        print(color1)
    elif "Red" not in color:
        print("Green")
    elif "Yellow" not in color:
        print("Violet")
    elif "Blue" not in color:
        print("Orange")
main()
