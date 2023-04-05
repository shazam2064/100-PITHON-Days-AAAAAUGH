from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "********@mail.com"
MY_PASSWORD = "**********"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {data_row["name"]: (data_row["month"], data_row["day"]) for (index, data_row) in data.iterrows()}

birthday_buddies = [name for name in birthdays_dict.keys() if birthdays_dict[name] == today_tuple]

for buddy in birthday_buddies:
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", buddy)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthdays_dict[buddy]["email"],
            msg=f"Subject:Happy Birthday! - testing project \n\n{contents}"
        )
