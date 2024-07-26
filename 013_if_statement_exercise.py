''' Price of a house is $1M.
If the buyer has good credit,
they need to put down 10%
otherwise they need to put down 20%
print the down payment with good credit '''

price = 1000000
has_good_credit = True
if has_good_credit:
    down_payment = 0.1 * price
    print(down_payment)
else:
    down_payment = 0.2 * price
    print(down_payment)
# #Using only one print()
# if has_good_credit:
#     down_payment = 0.1 * price
# else:
#     down_payment = 0.2 * price
# print(f"Down payment: ${down_payment}") #100 thousand dollar


