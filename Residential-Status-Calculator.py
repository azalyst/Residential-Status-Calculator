#basic_condition_for_residential_status
#assesement_year_2020-21
print("RESIDENTIAL CALCULATOR FOR THE ASSESSMENT YEAR 2020-21")

print("Fill the details mentioned below to proceed")

P_Y = int(input("Period of stay in India in P.Y. 2019-20:- "))

a = int(input("Period of stay in 2018-19:- "))
b = int(input("Period of stay in 2017-18:- "))
c = int(input("Period of stay in 2016-17:-"))
d = int(input("Period of stay in 2015-16:-"))

P_Y_sec_all = int(a+b+c+d)

if P_Y >= 182 or P_Y >= 60 and P_Y_sec_all >=365 :
    print("Not Ordinarily Resident")
else :
    print("Non-resident")
