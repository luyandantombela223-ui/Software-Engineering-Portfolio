# a program to return the calander of the given input
# Luyanda Ntombela 
# 15 April 2025

import math

def is_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False

def month_num(month_name):
    month_name = month_name.capitalize()  # handle any case input
    if month_name == 'January':
        return 1
    if month_name == 'February':
        return 2    
    if month_name == 'March':
        return 3 
    if month_name == 'April':
        return 4  
    if month_name == 'May':
        return 5  
    if month_name == 'June':
        return 6 
    if month_name == 'July':
        return 7       
    if month_name == 'August':
        return 8
    if month_name == 'September':
        return 9 
    if month_name == 'October':
        return 10   
    if month_name == 'November':
        return 11 
    if month_name == 'December':
        return 12

def day_of_week(day, month_name, year):
    month_number = month_num(month_name)
    if month_number < 3:
        month_number += 12
        year -= 1
    h = (day + math.floor(13*(month_number+1)/5) + year + math.floor(year/4) - math.floor(year/100) + math.floor(year/400)) % 7
    k = (h + 5) % 7 + 1  # 1=Monday, 7=Sunday
    return k

def num_days_in(month_number, year):    
    if is_leap(year):
        if month_number == 2:
            return 29
    else:
        if month_number == 2:
            return 28
    if month_number in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    else:
        return 30

def num_weeks(month_number, year):
    start_day = day_of_week(1, month_name_from_number(month_number), year)
    days_in_month = num_days_in(month_number, year)
    end_day = (start_day + days_in_month - 1) % 7
    if end_day == 0:
        end_day = 7
    weeks = (days_in_month + start_day - 1 + (7 - end_day)) // 7
    return weeks

def week(week_number, start_day, days_in_month):
    start_date = (week_number - 1) * 7 + 1 - (start_day - 1)
    result = ""
    for i in range(7):
        day = start_date + i
        if 1 <= day <= days_in_month:
            result += f"{day:2d} "
        else:
            result += "   "
    return result.rstrip()

def month_name_from_number(month_number):
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    return months[month_number-1]

def main():
    month_name = input("Enter month:\n")
    year = int(input("Enter year:\n"))
    
    month_number = month_num(month_name)
    days_in_month = num_days_in(month_number, year)      
    start_day = day_of_week(1, month_name, year)
    weeks_in_month = num_weeks(month_number, year)

    print(f"\n{month_name.capitalize()} {year}")
    print("Mo Tu We Th Fr Sa Su")

    for w in range(1, weeks_in_month + 1):
        print(week(w, start_day, days_in_month))

if __name__ == '__main__':
    main()

