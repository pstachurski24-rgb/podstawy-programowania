# Section 4, item 6: use separate functions in emails.py.
from emails import email_sender, email_recipient, email_subject, email_body

print('Sender:', email_sender())
print('Recipient:', email_recipient())
print('Subject:', email_subject())
print('Body:')
print(email_body())
