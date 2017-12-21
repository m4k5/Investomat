"""
notyfing user
Currently supports:
- sending email
"""
import smtplib


def send_email(subject, receipent, content, login, password, server, port=587):
    """
    sending emails
    """
    mail = 'From: %s\nSubject: %s\n%s' % (login, subject, content)
    s = smtplib.SMTP(host=server, port=port)
    s.starttls()
    s.login(login, password)
    s.sendmail(login, receipent, mail)
    s.quit()
