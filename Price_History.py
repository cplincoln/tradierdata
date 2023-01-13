# Version 3.6.1    
import requests, config, pprint

spy_history_header = {'Authorization': 'Bearer {}'.format(config.access_token), 'Accept': 'application/json'}
spy_history_url = '{}/v1/markets/timesales'.format(config.base_url)

weekStart = '2023-01-09 09:30'
weekEnd = '2023-01-13 16:00'

symbol = 'SPY'

spy_history_params={'symbol': symbol, 'interval': '5min', 'start': weekStart, 'end': weekEnd, 'session_filter': 'open'}

response = requests.get(
    spy_history_url,
    params= spy_history_params,
    headers= spy_history_header
)

json_response = response.json()
price_history = json_response['series']['data']

for data in price_history:
    print(data['time'], data['open'], data['high'], data['low'], data['close'], data['volume'])