"""Safe Password"""
def main():
    """Func"""
    char = input()
    num = int(input())
    if char != "H" and num != 4567:
        print("safe locked")
    elif char == "H" and num != 4567:
        print("safe locked - change digit")
    elif char != "H" and num == 4567:
        print("safe locked - change char")
    elif char == "H" and num == 4567:
        print("safe unlocked")
main()
