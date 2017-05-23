import netifaces
import json
import requests
import base64
import os.path

from bws_mailer import EmailSender

# Load the config file
home_directory_path = os.path.expanduser("~")

with open(os.path.join(home_directory_path, '.imalive_config.json'), 'r') as config_file:
    config = json.load(config_file)

# We will encode the email id/pw with base64, to make them look obscure (but not really) on config files.
config['email_id'] = base64.b64decode(config['email_id']).decode('ascii')
config['email_pw'] = base64.b64decode(config['email_pw']).decode('ascii')

# 'results' will contain the message for the email
results = ''

# Let's get ip addresses assigned to each of the interfaces installed in this system
interface_list = netifaces.interfaces()

for interface in interface_list:
    results += str(interface) + '\n'
    results += str(netifaces.ifaddresses(interface)) + '\n'
    results += '\n'

# Let's get the external IP this machine is using on the internet
public_ip = requests.get('https://api.ipify.org').text

results += str(public_ip) + '\n'

# Create EmailSender instance
sender = EmailSender(
            id=config['email_id'],
            password=config['email_pw'],
            smtp_address=config['smtp_address'],
            port_number=config['smtp_port_number'],
            ssl_needed=config['smtp_ssl_needed'],
            recipient_addresses=config['email_recipient_addresses'],
            subject=config['email_subject'],
            msg_body=results
        )

# Send the email
sender.send()
