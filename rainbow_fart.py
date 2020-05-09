import requests


key = '601f30cc0b364cbc6e1a64c6db6dea99'

url = 'http://api.tianapi.com/txapi/caihongpi/index?key={}'.format(key)

res = requests.get(url).text

print(res)