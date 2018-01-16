import smtplib
import weather
import mailer
def get_emails():
    #Reading emails from a file
    emails={}
    try:
        with open('email2.txt','r') as f:
            for line in f:
                (email,name)=line.split(',')
                emails[email]=name.strip()
    except FileNotFoundError as err:
        print(err)
    return emails
def get_schedule():
    #Reading schedules from a file
    schedule=None
    try:
        with open('Schedule.txt','r') as f1:
            schedule=f1.read()
    except FileNotFoundError as ferr:
        print(ferr)
    return schedule

def main():
    emails=get_emails()
    schedule=get_schedule()
    forecast=weather.get_weather_forecast()
    mailer.send_email(emails,schedule,forecast)
main()