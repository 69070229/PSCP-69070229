"""Pro"""
def main():
    """Func"""
    x = int(input())
    y = int(input())
    a = int(input())
    z = int(input())
    price = ((z%x)*a)+((y*(z//x))*a)
    print(price)
main()
