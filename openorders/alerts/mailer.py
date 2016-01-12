import requests
import ALERTCONFIG

def send_confirmation(text, email, subject):
    return requests.post(
        'https://api.mailgun.net/v3/{}/messages'.format(ALERTCONFIG.MAILGUN_DOMAIN),
        auth=("api", ALERTCONFIG.MAILGUN_API ),
        data={"from": ALERTCONFIG.ALERTS_EMAIL,
              "to": [ email ],
              "subject": subject,
              "text": text})
