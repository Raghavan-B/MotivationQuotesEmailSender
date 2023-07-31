import smtplib
import datetime as dt
import random

#Enter the user email and password
my_email = "user1@gmail.com"
password = "some_pass"

# import datetime
current_day = dt.datetime.now().weekday()

def random_quote_generator():
    with open("quotes.txt","r") as quotes:
        
        quotes_content = quotes.read()
        quotes_list = quotes_content.split("\n")
        random_quote = random.choice(quotes_list)
    return random_quote

if current_day == 0:
    quote = random_quote_generator()
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email,
                        #enter the receiver userid
                        to_addrs="user@gmail.com",
                        msg = f"Subject:Monday Motivation\n\n {quote}")
    connection.close()
        
