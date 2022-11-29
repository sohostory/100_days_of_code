import datetime as dt
import pandas
import random
import smtplib

# LOGIN INFO
my_email = ""
password = ""

now = dt.datetime.now()
today = (now.month, now.day)

# PICKING RANDOM LETTER
todays_letter = f"./letter_templates/letter_{random.randint(1,3)}.txt"
PLACEHOLDER = "[NAME]"

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for(index, data_row) in data.iterrows()}

if today in birthday_dict:
    today_name = birthday_dict[today]["name"]
    today_email = birthday_dict[today]["email"]
    # print(today_name)
    with open(todays_letter) as letter_file:
        letter_contents = letter_file.read()
        new_letter = letter_contents.replace(PLACEHOLDER, today_name)
        print(new_letter)

# SEND BIRTHDAY EMAIL
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr = my_email,
        to_addrs = today_email,
        msg=f"Subject: Happy Birthday!!\n\n{new_letter}")


