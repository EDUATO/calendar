
DaysNameList = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def set_months_days(pair_month,february=False, leapyear=False, startDayID=0):
    months_days = []
    pair_month = pair_month

    if pair_month:
        days = 30
    elif not pair_month:
        days = 31

    if leapyear and february:
        days = 29
    if february:
        days = 28
    
    days_time = startDayID
    for day_number in range(days):
        
        
        if days_time > len(DaysNameList)-1:
            days_time = 0

        months_days.append(
            {
                "Day Number":day_number+1,
                "Day Name":DaysNameList[days_time]
            }
        )

        days_time += 1

    return months_days


if __name__ == "__main__": 
    print(set_months_days(False))



        
