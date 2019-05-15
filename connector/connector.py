import okta
import sunshine
import yaml
import time

OKTA_API_SUBDOMAIN = 'dev-119799'
SUNSHINE_API_SUBDOMAIN = 'z3nhawaii13'

if __name__ == '__main__':
    with open('auth.yml', 'r') as config_file:
        config = yaml.safe_load(config_file)

        okta_client = okta.Okta(config['okta']['subdomain'], config['okta']['apiKey'])
        sun = sunshine.Sunshine(config['sunshine']['subdomain'],
                                config['sunshine']['username'],
                                config['sunshine']['password'])

        # Once backfill is done
        okta_client.get_user()
        for user in okta_client.users:
            sun.save_profile(okta.Okta.user_to_sunshine_profile(user))

        okta_client.users = []
    while True:
        okta_client.pull_users()
        for user in okta_client.users:
            sun.save_profile(okta.Okta.user_to_sunshine_profile(user))
        # Sleep for 5 seconds in between pulls
        time.sleep(5)
