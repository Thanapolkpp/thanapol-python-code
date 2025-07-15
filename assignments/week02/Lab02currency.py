menu = int(input("what is your choose menu (1: THB to USD or 2: USD to THB) :"))
money = float(input("Amount to convert :"))

if menu==1 :
    result = money/ 35.5
    print(f"Result {result:.1f}$ USD")
elif menu==2:
    result = money* 35.5
    print(f"Result {result:.1f}฿ THB")
else :
    print("Your enter Fail")