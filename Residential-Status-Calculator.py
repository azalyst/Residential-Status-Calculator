#basic_condition_for_residential_status
#assesement_year_2020-21

#if statement checks for three conditions:

#If the period of stay in the previous year (2019-20) is at least 182 days or more, or if it is 60 days or more and the total period of stay in the four previous years (2018-19, 2017-18, 2016-17, 2015-16) is 365 days or more, then the individual is considered "Not Ordinarily Resident".
#If the period of stay in the previous year is at least 182 days or more and the total period of stay in the four previous years is 730 days or more, then the individual is considered "Ordinarily Resident".
#If the individual does not meet the conditions for either "Not Ordinarily Resident" or "Ordinarily Resident", then the individual is considered "Resident but Not Ordinarily Resident".



print("RESIDENTIAL CALCULATOR FOR THE ASSESSMENT YEAR 2020-21")

print("Fill the details mentioned below to proceed")

P_Y = int(input("Period of stay in India in P.Y. 2019-20:- "))
a = int(input("Period of stay in 2018-19:- "))
b = int(input("Period of stay in 2017-18:- "))
c = int(input("Period of stay in 2016-17:- "))
d = int(input("Period of stay in 2015-16:- "))

P_Y_sec_all = int(a+b+c+d)

if P_Y >= 182 or P_Y >= 60 and P_Y_sec_all >=365 :
    print("Not Ordinarily Resident")
elif P_Y >= 182 and P_Y_sec_all >= 730:
    print("Ordinarily Resident")
else:
    print("Resident but Not Ordinarily Resident")
