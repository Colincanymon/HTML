import datetime
current_year= datetime.datetime.now().year
last_year= int(input("enter the last year:"))
print("future leap years are:")
for year in range(current_year,last_year+1):
    if year % 400== 0 or(year % 4==0 and year % 100 !=0):
        print(year)