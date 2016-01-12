import os

EMAIL_KEY     = os.environ.get('OPENORDERS_MAIL_SECRET') or 'SOME LONG RANDOM KEY'
EMAIL_SALT    = os.environ.get('OPENORDERS_MAIL_SALT') or 'ANOTHER LONG RANDOM KEY'

MAILGUN_DOMAIN = os.environ.get('MAILGUN_DOMAIN') or "YOUR MAILGUN POST ADDRESS"
MAILGUN_API = os.environ.get('MAILGUN_API_KEY') or "YOUR API KEY"

ALERTS_EMAIL = "Alerts <alerts@mailer.openorders.ca>"
