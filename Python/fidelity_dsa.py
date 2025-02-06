def getdays(month):
    month_days = {
        "Jan": 31, "Feb": 28, "Mar": 31, "Apr": 30,
        "May": 31, "Jun": 30, "Jul": 31, "Aug": 31,
        "Sep": 30, "Oct": 31, "Nov": 30, "Dec": 31
    }
    return month_days.get(month, "Invalid month name")

"""This function return the number of days, when you enter the month name"""
month_name = input("Enter the month name: ")
print(f"Number of days in {month_name}: {getdays(month_name)}")

    

