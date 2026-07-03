"""Bill"""
def main():
    """Func"""
    price = int(input())
    service = price*0.1
    if service < 50:
        service = 50
    elif service > 1000:
        service = 1000
    priser = price + service
    total = priser*1.07
    print(f"{total:.2f}")
main()
