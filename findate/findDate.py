import calendar

def input_date():
    date = input("date(M/D/Y) : ")
    return date

def find_day(date):
    for i in range(len(date)):
        month, day, year = date.split('/')
        break

    day_number = calendar.weekday(int(year), int(month), int(day));
    days = ["Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday"]
    return days[day_number];


print(find_day(input_date()))



