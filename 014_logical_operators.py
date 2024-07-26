#AND operator
'''If an applicant has high income AND good credit.
Then they are eligible for loan'''
has_high_income = True
has_good_credit = True
#has_good_credit = False
if has_high_income and has_good_credit:
    print("Eligible for LOAN")
else:
    print("NOT Eligible for LOAN")

# #OR operator
# '''If an applicant has high income OR good credit.
# Then they are eligible for loan'''
#
# has_high_income=False
# has_good_credit=True
# #has_good_credit=False
#
# if has_high_income or has_good_credit:
#     print("Eligible for LOAN")
# else:
#     print("NOT Eligible for LOAN")

# #NOT operator
# '''If applicant has good credit AND
# doesn't have any criminal record.
# Then they are eligible for loan'''
# has_good_credit = True
# has_criminal_record = False
# #has_criminal_record = tRUE
#
# if has_good_credit and not has_criminal_record:
#     print("Eligible for loan")
# else:
#     print("NOT Eligible for loan")