# create weekday and working day function

# ref. date is 05/05/2021

from datetime import timedelta, datetime, date

def number_to_weekday(number):
  # considerando a bilbliotec datetime do python
  number_weekday_list = [0, 1, 2, 3, 4, 5, 6]
  weekday_list = ['monday', 'tuesday', 'wednseday', 'thursday', 'friday', 'saturday', 'sunday']

  for i in range(len(number_weekday_list)):
    if number_weekday_list[i] == number:
      weekday = weekday_list[i]
      break
  return weekday

def day_of_the_week():
  from datetime import timedelta, datetime, date


  the_day_after_tomorrow = (date.today() + timedelta(days=2)).strftime("%Y-%m-%d") # friday
  tomorrow = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d") # thursday
  today = date.today().strftime("%Y-%m-%d") # wednesday
  yesterday = (date.today() - timedelta(days=1)).strftime("%Y-%m-%d") #tuesday
  the_day_before_yesterday = (date.today() - timedelta(days=2)).strftime("%Y-%m-%d") #monday

  week_day_after_tomorrow = (date.today() + timedelta(days=2)).weekday() # friday
  week_day_tomorrow = (date.today() + timedelta(days=1)).weekday() # thursday
  week_day_today = date.today().weekday() # wednesday
  week_day_yesterday = (date.today() - timedelta(days=1)).weekday() # tuesday
  week_day_before_yesterday = (date.today() - timedelta(days=2)).weekday() # monday

  days_obj = {
    "today": {
      "date": today,
      "number_weekday": week_day_today,
      "weekday": number_to_weekday(week_day_today)
    },
    "yesterday": {
      "date": yesterday,
      "number_weekday": week_day_yesterday,
      "weekday": number_to_weekday(week_day_yesterday)
    },
    "tomorrow":{
      "date": tomorrow,
      "number_weekday": week_day_tomorrow,
      "weekday": number_to_weekday(week_day_tomorrow)
    },
    "the_day_after_tomorrow":{
      "date": the_day_after_tomorrow,
      "number_weekday": week_day_after_tomorrow,
      "weekday": number_to_weekday(week_day_after_tomorrow)  
    },
    "the_day_before_yesterday":{
      "date": the_day_before_yesterday,
      "number_weekday": week_day_before_yesterday,
      "weekday": number_to_weekday(week_day_before_yesterday)
    }
  }

  return days_obj

print(day_of_the_week())