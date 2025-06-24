import requests
import json

def celebration(month, day):
    my_key ="bde23207-8e25-4f88-8710-aecc941d96f7"
    url = 'https://holidayapi.com/v1/holidays?'
    parameters = {
        'key': my_key,
        'country': 'RUS',
        'year': 2024,
         'month': month,
         'day': day
    }
    holidays = requests.get(url, params=parameters)
    data = holidays.json()
    if data['holidays'] == []:
        print(f"{day}.{month} праздника нет(")
        return
    else:
        dict_ = data['holidays'][0]
        week = dict_['weekday']
        print(f"Праздник: {dict_['name']}")
        print(f"День недели: {week['date']['name']}")

if __name__ == '__main__':
    months = input("Введите, пожалуйста, 2 ваших любимых месяца в году (числами и через пробел)\n").split()
    days = input("А теперь 2 даты, соответствующие любимым месяцам:)\n").split()
    celebration(int(months[0]), days[0])
    celebration(int(months[1]), days[1])