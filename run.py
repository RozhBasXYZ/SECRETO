#!/usr/bin/python3
#bot secreto by rochmat basuki


#---[ IMPORT MODULE ]---#
import os, json, bs4, time
try:import concurrent.futures
except:os.system('pip install futures')
try:import requests
except ImportError:os.system('pip install requests')
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor


#---[ GLOBAL NAME ]---#
P = '\033[97m'  # WHITE
M = '\033[91m' # RED
H = '\033[92m'  # GREEN
K = '\033[93m'  # YELLOW
logo = f"""  _______ _______ ______ ______ _______ _______ _______ 
 |     {H}__{P}|    {H}___{P}|      |   {H}__{P} \    {H}___{P}|_     _|       | create by
 |{H}__{P}     |    {H}___{P}|   {H}---{P}|      <    {H}___{P}| |   | |   {H}-{P}   | {K}rozhbasxyz{P}
 |_______|_______|______|___|__|_______| |___| |_______| free for public!"""
ses = requests.Session()
no = 0
url_post = 'https://api.secreto.site/sendmsg'


#---[ CONVERT ID ]---#
def rever(x):
  return x[::-1]


#---[ PLACE TO SEND ]    
def namaku(url,id,pesan,kode):
	global no
	try:
		no+=1
		head = {'Host': 'api.secreto.site','content-length': '40','sec-ch-ua': '" Not;A Brand";v="99", "Chromium";v="87"','accept': '*/*','sec-ch-ua-mobile': '?1','user-agent': 'Mozilla/5.0 (Linux; Android 10; Redmi 8A Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36','content-type': 'application/json','origin': 'https://secreto.site','sec-fetch-site': 'same-site','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': url,'accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
		date = json.dumps({"id": f"{kode}_{id}","message": pesan})
		ses.post(url_post,data=date,headers=head)
		print(f'\n sukses spam ke {H}{no}{P}\n target : {H}{url}{P}\n pesan  : {H}{pesan}{P}')
	except requests.exceptions.ConnectionError:
		print(f" [{M}!{P}] tidak ada koneksi internet")
		time.sleep(10)
		namaku(url,id,pesan,kode)
	except Exception as e:
		exit(f' [{M}!{P}] gagal karena : {e}')
	

#---[ MENU ]---#
def menu():
	global no
	print(f'{logo}\n\n')
	apa = input(' apakah anda ingin spam brutal? [y/n] \n pilih  : ')
	rozh = input(' link   : ') 
	if 'https' not in rozh:exit(f' [{M}!{P}] input link yang benar')
	bas = rever(rozh).split('/')[0].split('a')[0]
	hrf = parser(ses.get(rozh,headers={'user-agent':'Mozilla/5.0 (Linux; Android 10; Redmi 8A Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36'}).content,'html.parser')
	gans = hrf.find('span',id='id').text.split('_')[0]
	xyz = input(' pesan  : ')
	limit = input(' jumlah : ')
	if apa in ['y','Y','ya']:
		with ThreadPoolExecutor(max_workers=100) as babas:
				for x in range(int(limit)):
					babas.submit(namaku,rozh,bas,xyz,gans)		
		exit(f'\n [{H}!{P}] sukses kirim spam sebanyak {H}{no}{P} kali')
	else:
		for x in range(int(limit)):
			namaku(rozh,bas,xyz,gans)		
		exit(f'\n [{H}!{P}] sukses kirim spam sebanyak {H}{no}{P} kali')
		

if __name__=='__main__':
	os.system('git pull')
	os.system('clear')
	menu()
