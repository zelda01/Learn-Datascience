try:
    hours = input("Enter hours:")
    h = float(hours)
    rate = input("Enter rate:")
    r = float(rate)
    computepay(10, 20)
except:
    print("Enter a number is input")
    quit()
if h > 40:
    print((40*r)+(h-40)*1.5*r)

elif h <= 40:
    print(40*r)
computepay(hours, rate)
print(computepay)
