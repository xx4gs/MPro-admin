import requests,sys,random,threading
from colorama import Fore
import sys as mp
import time as mpp
def slow(mpr):
	for mppp in mpr + "\n":
		mp.stdout.write(mppp)
		mp.stdout.flush()
		mpp.sleep(0.5 / 120)
slow(f"""{Fore.BLUE}
                                        _           _       
                                       | |         (_)      
  _ __ ___  _ __  _ __ ___     __ _  __| |_ __ ___  _ _ __  
 | '_ ` _ \| '_ \| '__/ _ \   / _` |/ _` | '_ ` _ \| | '_ \ 
 | | | | | | |_) | | | (_) | | (_| | (_| | | | | | | | | | |
 |_| |_| |_| .__/|_|  \___/   \__,_|\__,_|_| |_| |_|_|_| |_|
           | |                                              
           |_|                                              
  My Channel: @xx4gs----------------insta: @xx4gs
{Fore.WHITE}""")
slow(f"""{Fore.RED}
url >> http://test.com		or	https://test.com {Fore.WHITE}""")
url1= input(f"{Fore.RED} Enter Url:   {Fore.WHITE}")
wordlist1=open("word.txt","r")
def url_mpro():
	while True:
		mprro1=wordlist1.readline().split('\n')[0]
		if "mpro" in mprro1:
			slow("\n=====================================")
			mmppp=input("Links Expired Exit Enter : ")
			slow("\n=====================================")
			exit()
		else:
			url = f"{url1}/{mprro1}"
			rq=requests.get(url=url, timeout=4).status_code
			if rq =='200':
				print(f"{Fore.GREEN} [MPro>>] Found >> {url} {Fore.WHITE}")
				with open('MPro-Url-Found.txt', 'a') as mp:
					mp.write(url+'\n')
			else:
				print(f"{Fore.RED} [MPro>>] Not Found >> {url} {Fore.WHITE}")
threads=[]
for i in range(10):
	thread1= threading.Thread(target=url_mpro)
	thread1.start()
	threads.append(thread1)
for thread2 in threads:
	thread2.join()
