#firefox
from selenium import webdriver
options = webdriver.FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)
driver.get("https://www.google.com")
driver.save_screenshot("/sdcard/download/screenshot.png")
driver.quit()
#chrome
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com")
driver.save_screenshot("/sdcard/download/screenshot.png")
print("Please check screenshot image")
driver.quit()
#countdown code
import time

def countdown(t):
    """
    This function counts down from a given time in seconds.
    """

    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Time is up!')

if __name__ == '__main__':
    # Set the time in seconds (24 hours = 86400 seconds)
    t = 86400 

    countdown(t)
#email
# Importing libraries
import imaplib, email
 
user = input("User:")
password = input("Password:")
imap_url = 'imap.gmail.com'
 
# Function to get email content part i.e its body part
def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None, True)
 
# Function to search for a key value pair 
def search(key, value, con): 
    result, data = con.search(None, key, '"{}"'.format(value))
    return data
 
# Function to get the list of emails under this label
def get_emails(result_bytes):
    msgs = [] # all the email data are pushed inside an array
    for num in result_bytes[0].split():
        typ, data = con.fetch(num, '(RFC822)')
        msgs.append(data)
 
    return msgs
 
# this is done to make SSL connection with GMAIL
con = imaplib.IMAP4_SSL(imap_url) 
 
# logging the user in
con.login(user, password) 
 
# calling function to check for email under this label
con.select('Inbox') 
 
 # fetching emails from this user "tu**h*****1@gmail.com"
msgs = get_emails(search('FROM', 'MY_ANOTHER_GMAIL_ADDRESS', con))
 
# Uncomment this to see what actually comes as data 
# print(msgs) 
 
 
# Finding the required content from our msgs
# User can make custom changes in this part to
# fetch the required content he / she needs
 
# printing them by the order they are displayed in your gmail 
for msg in msgs[::-1]: 
    for sent in msg:
        if type(sent) is tuple: 
 
            # encoding set as utf-8
            content = str(sent[1], 'utf-8') 
            data = str(content)
 
            # Handling errors related to unicodenecode
            try: 
                indexstart = data.find("ltr")
                data2 = data[indexstart + 5: len(data)]
                indexend = data2.find("</div>")
 
                # printing the required content which we need
                # to extract from our email i.e our body
                print(data2[0: indexend])
 
            except UnicodeEncodeError as e:
                pass
