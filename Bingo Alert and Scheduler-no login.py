#!/usr/bin/env python
# coding: utf-8

# In[1]:


##Some of the indentations are wrong as I copied and pasted without email and passwords.


# In[4]:


import datetime as dt

now=dt.datetime.now()
today_year=now.year
today_month=now.month
today_day=now.day
month_year=(now.year,now.month,now.day)


# In[6]:


import pandas as pd
df=pd.read_csv('test_bingo_alerts.csv')
df


# In[1]:


schedule={(df_row['year'],df_row["month"],df_row["day"]):df_row for(index,df_row)in df.iterrows()}
idx=2
total_sum_today=sum(month_year)
print(schedule.items())

for key, val in schedule.items():
    day_key= key[idx]
    month_key=key[idx-1]
    year_key=key[idx-2]
    tots=day_key+month_key+year_key
    if total_sum_today==tots-5:
        this_shift=schedule[key]
        email_to_text=this_shift["email"]
        import smtplib
        my_email="fake@gmail.com"
        password="password"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(from_addr=my_email,
                    to_addrs= email_to_text,
                    msg="Subject:Bingo Reminder\n\n This is a reminder that your Bingo shift is in 5 days. If you have an issue with this time please do not respond to this email but text me.\n Thank you! \n -Lauren")
    else:
        print("no email")
    
    if total_sum_today==tots-2:
        this_shift=schedule[key]
        cell_to_text=this_shift["cell"]
        import os
        from twilio.rest import Client

        account_sid=os.environ['TWILIO_ACCOUNT_SID']='TWILIO SID CODE'
        auth_token=os.environ['TWILIO_AUTH_TOKEN']='TWILIO PASSWORD'
        client = Client(account_sid, auth_token)

        message = client.messages \
                .create(
                     body="Friendly Reminder You have a Bingo shift in 2 days. Please contact me(Lauren) asap if there is any issue",
                     from_='twilio phone number',
                     to=cell_to_text
                 )
    else:
        print("no text")


# In[ ]:




