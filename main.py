import smtplib
from datetime import datetime
import random
import pandas as pd

my_email = "sudip000kc@gmail.com"
password = "ebzjiubtqhhhcvdw"

today = datetime.now()
month = today.month
day = today.day
today_tuple=(month,day)
time=today.time().hour

file = pd.read_csv("birthdays.csv")
file_dict = {(row["month"], row["day"]): row for (index, row) in file.iterrows()}
if today_tuple  in file_dict: 
    birth_day_person=file_dict[today_tuple]

    with open(f"letter_templates\letter_{random.randint(1,3)}.txt", "r") as letter:
            message = letter.read().replace("[NAME]", birth_day_person["name"])


            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(my_email,  password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=birth_day_person["email"],
                    msg=f"Subject:Happy Birthday\n\n{message}".encode("utf-8"),
                )
