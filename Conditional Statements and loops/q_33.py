def no_of_days(month_name):
    if month_name.lower() == "february":
        print("No. of days: 28/29 days")
    elif month_name.lower() in ("april", "june", "september", "november"):
        print("No. of days: 30 days")
    elif month_name.lower() in ("january", "march", "may", "july", "august", "october", "december"):
        print("No. of days: 31 days")
    else:
        print("Wrong month name")


no_of_days(input("Enter a month name: "))
