# https://documentation.tradier.com/

account_id = 'ABC123'
access_token = 'ABC123'
base_url = 'https://sandbox.tradier.com'

history_header = {'Authorization': 'Bearer {}'.format(access_token), 'Accept': 'application/json'}
history_url = '{}/v1/accounts/{}/history'.format(base_url,account_id)