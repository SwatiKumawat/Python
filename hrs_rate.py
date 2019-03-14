hrs = input("Enter Hours:")
h = float(hrs)
rate_per_hrs=input("Enter rate per hours")
rate=float(rate_per_hrs)
if h<=40:
    gross_pay=h*rate
else:
    new=h-40;
    gross_pay1=40*rate
    gross_pay2=1.5*new*rate
    gross_pay=gross_pay1+gross_pay2
print(gross_pay)