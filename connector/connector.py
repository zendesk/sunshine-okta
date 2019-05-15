import okta
import sunshine
import yaml

OKTA_API_SUBDOMAIN = 'dev-119799'
SUNSHINE_API_SUBDOMAIN = 'z3nhawaii13'

if __name__ == '__main__':
    with open('auth.yml', 'r') as config_file:
        config = yaml.safe_load(config_file)

        okta_client = okta.Okta(config['okta']['subdomain'], config['okta']['apiKey'])
        sun = sunshine.Sunshine(config['sunshine']['subdomain'],
                                config['sunshine']['username'],
                                config['sunshine']['password'])

        okta_client.get_user()
        for user in okta_client.users:
            sun.save_profile(okta.Okta.user_to_sunshine_profile(user))
