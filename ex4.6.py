#Ex 4.6
def computepay(hours, rate):
    print("In computepay", hours, rate)
    if fh > 40 :
        reg = fr * fh
        ot = (fh-40.0) * (fr * 0.5)
        p = reg + ot
    else:
        p = fh * fr
    print("Returning", p)
    return p

hr = input("Enter Hours: ")
r = input("Enter Rate: ")
fh = float(hr)
fr = float(r)
p = computepay(fh,fr)

print("pay:", p)
