# tradierdata
https://documentation.tradier.com/brokerage-api

Credit for this coding goes to Part Time Larry

https://www.youtube.com/playlist?list=PLvzuUVysUFOs1W0VKsjV9DOowZ6WUl-jr

Several items need to be set for this code to work:

config.py:

account_id<br/>
access_token<br/>
base_url (it is currently set to the sandbox api. Use https://api.tradier.com/v1/ for the brokerage api)<br/>

Price_History.py:

dateStart (yyyy-mm-dd hh:mm)<br/>
dateEnd (yyyy-mm-dd hh:mm)<br/>
symbol (e.g. SPY or SPY230113C00399000)<br/>
interval (tick, 1min, 5min, 15min)<br/>

You can print this data directly to csv if you type the following into the console:<br/>
[path to python installation] [path to the specific code you are calling] > filename.csv<br/>
For example: C:/Users/name/AppData/Local/Programs/Python/Python310/python.exe c:/Users/name/Tradier/SPY_History.py > 20220812.csv
