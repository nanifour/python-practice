#calculate pay using hours and rate of pay + overtime(>40hr) pay
def computepay(h, r):
    global overRate
    overtimeHrs = h - 40.0

    if overtimeHrs >= 1.0:
        overRate = r * 1.5
    ot = overRate * overtimeHrs
    pay = (40.0 * r) + ot

    if h <= 40:
        pay = h * r

    return pay

hrs = input("Enter Hours: ")
h = float(hrs)

rate = input("Enter Rate: ")
r = float(rate)

p = computepay(h, r)
print("Pay", p)
