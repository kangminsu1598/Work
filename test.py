import random
from pprint import pprint
import json
import requests

url = "https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
connect = requests.get(url)
lotto = connect.json()
pprint(lotto)

