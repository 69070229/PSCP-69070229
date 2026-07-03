"""Elo"""
def main():
    """Function"""
    ra = int(input())
    rb = int(input())
    rate = input()
    ea = 1/(1+10**((rb-ra)/400))
    eb = 1/(1+10**((ra-rb)/400))
    if rate == "A":
        print(f"{ea:.2f}")
    elif rate == "B":
        print(f"{eb:.2f}")
main()
