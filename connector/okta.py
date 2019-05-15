import requests
import json
from datetime import datetime


'''
Okta User Object mapping
{
    'profile': {
        'source': 'okta',
        'type': 'user',
        'identifiers': {
            'id': '....',
            'login': '...'
        }, 
        'attributes': {
            'name': '...',
            'mobilePhone': '...',            
            'primaryEmail': '...',
            'emails': [ ... ],
            'status': '...',
            'created': '...',
            'lastUpdated': '...'
        }
    }
}
'''


class Okta:
    def __init__(self, subdomain, apiKey):
        self.url = 'https://{}.okta.com'.format(subdomain)
        self.users = []
        self.headers = {
            'Authorization': 'SSWS {}'.format(apiKey)
        }

    @staticmethod
    def user_to_sunshine_profile(user=None):
        if user is None:
            return {}

        return {
            'profile': {
                'source': 'okta',
                'type': 'user',
                'identifiers': {
                    'id': user['id'],
                    'login': user['profile']['login']
                },
                'attributes': {
                    'name': '{} {}'.format(user['profile']['firstName'], user['profile']['lastName']),
                    'primaryEmail': user['profile']['email'],
                    'emails': user['credentials']['emails'],
                    'status': user['status'],
                    'created': user['created'],
                    'lastUpdated': user['lastUpdated']
                }
            }
        }

    @staticmethod
    def parse_pagination_header(header=''):
        if header == '':
            return None
        parts = header.strip().split(',')
        if len(parts) <= 1:
            # Only has self href
            return None
        try:
            url = parts[1][parts[1].index('<')+1:parts[1].index('>')]
        except:
            return None
        return url

    def get_user(self, url=''):
        if url == '':
            url = '{}/api/v1/users'.format(self.url)
        resp = requests.get(url, headers=self.headers)

        pagination_header = resp.headers.get('link')

        self.users = self.users + json.loads(resp.text)

        if pagination_header is not None:
            next_page = Okta.parse_pagination_header(pagination_header)
            if next_page is not None:
                self.get_user(next_page)
        return

    def pull_users(self, time=None):
        if time is None:
            # Set it to current time
            time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"

        return self.get_user(url='{}/api/v1/users?filter=lastUpdated gt "{}"'.format(self.url, time))
