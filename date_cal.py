def convert_strtime(str_time):
    import datetime
    convert_date = datetime.datetime.strptime(str_time, "%Y-%m-%d").date()
    return convert_date

def timeminus(date, days):
    import datetime
    minusdate = date - datetime.timedelta(days=days)
    return str(minusdate)[:10]

if __name__=='__main__':
    date = convert_strtime("2019-05-29")
    date1 = timeminus(date, 30)
    
    date2 = timeminus(date, -30)
    print(date, date2)