import base64
import requests


def encode(username, password):
    return base64.b64encode('{}:{}'.format(username, password).encode('UTF-8')).decode('UTF-8')


class Sunshine:
    def __init__(self, subdomain, username, password):
        self.url = 'https://{}.zendesk.com/api/sunshine'.format(subdomain)
        self.headers = {
            'Authorization': 'Basic {}'.format(encode(username, password))
        }

        print('header', self.headers)

    def save_profile(self, profile):
        resp = requests.post('{}/profile'.format(self.url), json=profile, headers=self.headers)
        print('resp', resp)
        return
