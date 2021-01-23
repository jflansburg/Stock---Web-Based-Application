import smtplib
import pandas as pd
import socket
from yahoo_fin import stock_info as si
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def quote_grab(symbol):
    price = si.get_live_price(symbol)
    return price #returns price

 def message_system(body):
 	
    gmail_user = 'jflansburg12@gmail.com'
    gmail_password = 'DOZERdog12!12!'
    receive_user = 'jackf@irdatasolutions.com'
    
    email_message = MIMEMultipart()
    email_message['From'] = gmail_user
    email_message['To'] = receive_user
    email_message['Subject'] = 'Stock Alert System'from win10toast import ToastNotifier 


    email_message.attach(MIMEText(body))
    
    try:
        server = smtplib.SMTP('stmp.gmail.com',587)
        server.starttls()
        server.login(gmail_user,gmail_password)
        print('Logged in Gmail successful, sending email now')
        text = email_message.as_string()
        server.sendmail(gmail_user, receive_user, email_message) #format goes (from email address, to email address, message)
        server.quit()
    except:
        print('Job failed')



file = pd.read_csv(r'C:\\Users\\jackf\\Desktop\\Python\\Test Data\\Watchlist.csv')
body = 'Changes:\n'
chg = False
i = 0
for ticker in tickers:
    quote = quote_grab(ticker) #ticker
    
    if quote > float(price[i]) and trigger[i] ==('a\n' or 'a'):
        body = body + 'Price for %s went up to %s (threshold = %s)\n' % (ticker[i], quote, trigger[i])
        i += 1
        chg = True
        
    if quote < float(price[i]) and trigger[i] == ('b\n' or 'b'):
        body = body + 'Price for %s went down to %s (threshold = %s)\n' % (ticker[i], quote, trigger[i])
        i += 1
        chg = True
        
    if quote > float(price[i]):
        body = body + 'Price for %s is at %s' %(ticker[i], price[i])
        chg = False
if chg == False:
    print('Sending email')
    message_system(body)
    

