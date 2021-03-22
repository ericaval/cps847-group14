#CheckSeason
def checkSeason(month):
    if month == "December" or month == "January" or month == "February":
        result = "Winter"
    elif month == "March" or month == "April" or month == "May":
        result = "Spring"
    elif month == "June" or month == "July" or month == "August":
        result = "Summer"
    else:
        result = "Fall"
    return result
