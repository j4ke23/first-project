#import libraries
import imaplib, email

user = 'jacob.kh23@gmail.com'
password = 'yankees23'
imap_url = 'imap.gmail.com'

# grabbing email content (body)
def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None, True)
    
# searching for key value pair
def search(key, value, con):
    result, data = con.search(None, key, '"{}"'.format(value))
    return data

# getting the list of emails under this label
def get_emails(result_bytes):
    msgs = [] # publishes all email data in this array
    for num in result_bytes[0].split():
        typ, data = con.fetch(num, '(RFC822)')
        msgs.append(data)

# making the SSI connection with GMAIL
con = imaplib.IMAP4_SSL(imap_url)

# logging the user in
con.login(user, password)

# calling the function to check for email under the listed label
con.select('Inbox')

# grabbing emails from the listed email address
msgs = get_emails(search('FROM', 'crystala.bickle@gmail.com', con))

# Uncomment next statement to see the actual data
print(msgs)

# finding the required content from our msgs
# can make changes to this section as needed to grab required content

# printing them by the order they are displayed in the gmail
for msg in msgs[::-1]:
    for sent in msg:
        if type(sent) is tuple:

            # encoding set as utf-8
            content = str(sent[1], 'utf-8')
            data = str(content)

            # handling errors related to unicode
            try:
                indexstart = data.find("ltr")
                data2 = data[indexstart + 5: len(data)]
                indexend = data2.find("</div>")

                # printing the required content needed to extract the email
                print(data2[0: indexend])
            except UnicodeEncodeError as e:
                pass