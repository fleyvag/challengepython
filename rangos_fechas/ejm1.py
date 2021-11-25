from datetime import datetime

def days_between(f1, f2):
    f1 = datetime.strptime(f1, "%Y-%m-%d")
    f2 = datetime.strptime(f2, "%Y-%m-%d")
    return print(abs((f2 - f1).days))

days_between('1922-01-22','1922-10-22')

