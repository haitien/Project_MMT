import imaplib
import email
import account

def read_gmail_imap(user_name, password, imap_url=account.IMAP_URL):
    try:
        gmail = imaplib.IMAP4_SSL(imap_url)
        gmail.login(user_name, password)
        print('Connected to gmail!')

        gmail.select("inbox")
        _, data = gmail.search(None, "ALL")
        mail_ids = data[0]
        ids_list = mail_ids.split()

        oldest_mail_id = int(ids_list[0])
        newest_mail_id = int(ids_list[-1])

        for i in range(newest_mail_id, oldest_mail_id, -1):
            _, data = gmail.fetch(str(i), '(RFC822)')

            for res in data:
                if isinstance(res, tuple):
                    msg = email.message_from_string(res[1].decode())
                    mail_subject = msg['subject']
                    mail_from = msg['from']
                    print('From : ' + mail_from + '\n')
                    print('Subject : ' + mail_subject + '\n')

    except Exception as e:
        print(str(e))