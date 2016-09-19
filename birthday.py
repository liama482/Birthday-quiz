"""
birthday.py
Author: Liam A.
Credit: <list sources used, if any>
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:
  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:
  Happy birthday!

Otherwise respond with a statement like this:
  Peter, you are a winter baby of the nineties.

Example Session
  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""

from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day

user=input("Please tell me your name: ")
birth_month=input("Please tell me your month of birth: ")
birthyear=input("Please tell me your year of birth: ")
day_month=input("Please tell me the day of that month: ")
prtd = no

if birth_month == "january" or birth_month == "february" or birth_month == "december":
    g = winter
if birth_month == "april" or birth_month == "may" or birth_month == "march":
    g = spring
if birth_month == "july" or birth_month == "august" or birth_month == "june":
    g = summer
if birth_month == "september" or birth_month == "october" or birth_month == "november":
    g = fall
if birthyear >= 2000:
    h = "two thousands"
if birthyear >= 1990 and birthyear <2000:
    h = "nineties"
if birthyear >= 1980 and birthyear <1990:
    h = "eighties"
if birthyear < 1980:
    h = "Stone Age"

s1 = "{0}, you are a {1} baby of the {2}."
if birth_month == "october" and day_month == 31:
    print ("You were born on Halloween!")
    prtd = yes
if birth_month == todaymonth and day_month == todaydate:
    print ("Happy birthday!")
    prtd = yes
if prtd == no:
    print (s1.format(user,g,h))
