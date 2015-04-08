from datetime import datetime

now = datetime.now()
now_d = datetime.toordinal(now) # Amount of days till 0000
answer = ['YES, you can stay, she came from night today - 3',
    'NO, gotta go home, man. She works day tomorrow - 4',
    'YES, you can stay, she works day today - 1',
    'NO, gotta go home, man. She works night today - 2']
f_answer = ['YES, you can stay, she will come from night that day - 3', # Answers for queries in future
    'NO, will have to go home, man. She will work day next day - 4',
    'YES, you can stay, she works day that day - 1',
    'NO, will have to go home, man. She will work night that day - 2']
week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

print(answer[now_d % 4]) # Print current schedule

for p in range(30):

    x1 = int(input()) # Insert day or year

    if x1 > 1000: # Case where user wants to check another year

        x2 = int(input()) # Insert day
        x3 = int(input()) # Insert month

        try: # Checking for wrong date input
            now_d = datetime.toordinal(now.replace(x1,x3,x2))
        except ValueError:
            print('Insert the right date')
            continue

        week_day = week[datetime.weekday(now.replace(x1,x3,x2))]  
        print(f_answer[now_d % 4] + ' --- ' + week_day) # Print current schedule
    else:
        x2 = int(input()) # Insert month

        try: # Checking for wrong date input
            now_d = datetime.toordinal(now.replace(datetime.now().year,x2,x1))
        except ValueError:
            print('Insert the right date')
            continue

        week_day = week[datetime.weekday(now.replace(datetime.now().year,x2,x1))]  
        print(f_answer[now_d % 4] + ' --- ' + week_day) # Print schedule for future
