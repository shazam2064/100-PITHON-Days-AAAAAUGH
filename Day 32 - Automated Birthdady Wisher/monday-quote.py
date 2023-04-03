import smtplib
import datetime as dt
import random

MY_EMAIL = "appbreweryinfo@gmail.com"  # This email and passwod don't wok
MY_PASSWORD = "abcd1234()"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 5:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )

# import smtplib
#
# my_email = "gabriel.salomon.2007@gmail.com"
# password = "amogus"
#
# connection = smtplib.SMTP("stmp.gmail.com",  587)
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(
#     from_addr=my_email,
#     to_addrs=my_email,
#     msg="Subject:No more tears \n\nAAAAAAAUGH"
# )
# connection.close()

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
# print(date_of_birth)

