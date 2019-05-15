# sunshine-okta

## Populate the config file
Make sure to grab the following and refer to auth.yml.example for structure of the file
1. Zendesk Subdomain
2. Zendesk Username
3. Zendesk Password
4. Okta Subdomain
5. Okta API Key

## Running it
```bash

cp auth.yml.example auth.yml // now go populate it!

pip install -r requirements.txt

python connector.py
```

## TODOs
1. Zendesk OAuth support
2. Better error handling for JSON and HTTP requests
