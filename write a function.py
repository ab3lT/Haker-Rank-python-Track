def is_leap(year):
    leap = False
    
    if year % 4 == 0:
        leap = True
    if year % 100 == 0:
        leep = False
    if year % 400 == 0:
        leep = True
    
    return leap

year = int(input())
print(is_leap(year))