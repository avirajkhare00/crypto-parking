import requests
from bs4 import BeautifulSoup
import json

def get_account_bal():

    r = requests.get("https://kovan.etherscan.io/token/0xf7b05ae5cc92422125bd43edc5c2e4c5bac9b3d6?a=0x303b381a3ad3bd7e2e059973d85aeb832ca2b1f7")

    bsObj = BeautifulSoup(r.text)

    table = bsObj.find("div",{"id":"ContentPlaceHolder1_divSummary"}).findAll('td')

    return table[5].text
