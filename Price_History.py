# Version 3.6.1    
import requests, config, pprint

history_header = {'Authorization': 'Bearer {}'.format(config.access_token), 'Accept': 'application/json'}
history_url = '{}/v1/markets/timesales'.format(config.base_url)

dateStart = '2023-01-09 09:30'
dateEnd = '2023-01-13 16:00'

symbol = 'SPY'
interval = '5min'

history_params={'symbol': symbol, 'interval': interval, 'start': dateStart, 'end': dateEnd, 'session_filter': 'open'}

response = requests.get(
    history_url,
    params= history_params,
    headers= history_header
)

json_response = response.json()
price_history = json_response['series']['data']

for data in price_history:
    print(data['time'], data['open'], data['high'], data['low'], data['close'], data['volume'])
