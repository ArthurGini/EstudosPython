'''
O seguinte programa pega dados da api alpha_vantage, imprime os valores das ações do BTC na tela
 e emite um alerta caso a ultima variação do preco seja maior que 0.004
'''
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage import cryptocurrencies

api_key = 'Z92Y0437GIRE1RCO'

ts = TimeSeries(key='api_key', output_format='pandas')
function = cryptocurrencies.DIGITAL_CURRENCY_DAILY(symbol='BTC', market='USD', interval='day', outputsize='full')

print('Os dados do BTC são: ')
print(function)

#i =1
#para exportar em excel ou csv
#while i==1:
#  data.to_excel("output.xlsx")
#  time.sleep(60)

close_data = data['4. close']
percentage_change = close_data.pct_change()

print(percentage_change)

last_change = percentage_change[-1]


if abs(last_change) > 0.004:
  print('MSFT Alert'+ last_change)

  