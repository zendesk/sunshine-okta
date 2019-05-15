import requests
import json

'''
Okta User Object mapping 

{




}

to 


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
        self.url = 'https://{}.okta.com/'.format(subdomain)
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

    def get_user(self, token=''):
        # TODO Pagination
        url = '{}/api/v1/users'.format(self.url)
        if token != '':
            url = '{}/{}'.format(url, token)

        resp = requests.get(url, headers=self.headers)
        self.users = self.users + json.loads(resp.text)
        return
