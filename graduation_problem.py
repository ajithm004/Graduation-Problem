def probability(total_no_days):
    days = total_no_days - 4
    if total_no_days >= 8:
        days = days + 2
    power_no_days = 2 ** total_no_days
    power_days = 2 ** days
    if total_no_days >= 8:
        dd = power_days - 5
    else:
        dd = power_days + 1
    attend_class = power_no_days - (dd)
    prob = 2 ** (total_no_days - 1) - (2 ** (total_no_days - 4))
    result = str(prob) + "/" + str(attend_class)
    return result


if __name__ == "__main__":
    no_of_days = input("Enter no of days: ")
    result = probability(no_of_days)
    print result
