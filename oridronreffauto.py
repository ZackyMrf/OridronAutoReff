import json
import requests
import time
import string
import random
import secrets
import re
import config
from eth_account import Account
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from twocaptcha import TwoCaptcha
from faker import Faker
fake = Faker()
user_agent = UserAgent()
random_user_agent = user_agent.random

#created by @ylasgamers
print("Auto Reff Oridron Bypass Captcha | AirDrop Family IDN")
        
def get_lastreff(sessionid):
    url = "https://oridron.com/airdrop/profile"
    headers = {
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        "origin": "https://oridron.com",
        "referer": "https://oridron.com/airdrop/profile"
    }

    # Menambahkan sessionid ke header
    headers["cookie"] = sessionid

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("")
        soup = BeautifulSoup(response.text, "html.parser")
        print("Total Reff : ",*[h6.text for h6 in soup.find_all("h6") if 'Users' in h6.text], sep='')
        #("")
    elif response.status_code == 401:
        print("Tidak diotorisasi. Mohon periksa sessionid Anda.")
    else:
        print("Terjadi kesalahan. Kode status:", response.status_code)
        print("Respon:", response.text)
        
def process_reg(username, email, bscwallet, password, passrcaptcha, fakeip, refcode, sessionid):
    url = "https://oridron.com/airdrop/includes/process.php?signup"
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "user-agent": random_user_agent,
        "origin": "https://oridron.com",
        "referer": "https://oridron.com/airdrop/index.php?signup"
    }

    # Menambahkan sessionid ke header
    headers["cookie"] = sessionid
    
    data = {
        "username": username,
        "email": email,
        "bscwallet": bscwallet,
        "password": password,
        "g-recaptcha-response": passrcaptcha,
        "h-captcha-response": passrcaptcha,
        "check_ip": fakeip,
        "ref_code": refcode
    }
    
    response = requests.post(url, headers=headers, data=data)
    
    if response.status_code == 200:
        print("Register Success!")
        get_lastreff(sessionid)
        print("")
    elif response.status_code == 401:
        print("Tidak diotorisasi. Mohon periksa sessionid Anda.")
    else:
        print("Terjadi kesalahan. Kode status:", response.status_code)
        print("Respon:", response.text)

def rdm_pssw(size=8, chars=string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation):
    return ''.join(random.choice(chars) for _ in range(size))

#log to txt file
def log(txt):
    f = open(__file__ + '.log', "a")
    f.write(txt + '\r\n')
    f.close()
    
def ExcuteREG():
    #fake data using faker
    print("")
    print("Processing Generate Faker Data...")
    username = fake.simple_profile().get("username")
    email = fake.ascii_free_email()
    fakeip = fake.ipv4_public()
    password = rdm_pssw()
    priv = secrets.token_hex(32)
    private_key = "0x" + priv
    acct = Account.from_key(private_key)
    log('Username : '+username)
    log('Email : '+email)
    log('Password : '+password)
    log('Your Address : '+acct.address)
    log('Private Key : '+private_key)
    log('=================================================================================')
    print("Data Register User Will Save On File oridronreffauto.py.log.txt")
    print("")
    
    #solver rcaptcha using 2captcha.com
    print("Processing Solver Captcha Please Wait...")
    solver = TwoCaptcha(config.apikey)
    result = solver.hcaptcha(sitekey='1d269499-aecf-495f-a5c6-654a53b4e079', url='https://oridron.com/airdrop/?signup')
    #print("Code Get : ",result.get("code"))
    passrcaptcha = result.get("code")
    print("Solver Captcha Success!")
    print("")
    print("Processing Register Account With Code Reff : ",config.refcode)
    
    #excute register
    process_reg(username, email, acct.address, password, passrcaptcha, fakeip, config.refcode, config.phpsessid)

print("")
loop = input("How Many You Want Refferal ? : ")
for i in range(0,int(loop)):
    try:
        ExcuteREG()
    except:
        pass