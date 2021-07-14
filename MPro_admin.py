import requests
import threading
import sys as p
import time as mp
def slow(m2):
	for m1 in m2 + '\n':
		p.stdout.write(m1)
		p.stdout.flush()
		mp.sleep(1. / 120)
slow("""
__________________________________
|                                |
|    __________________          |
|   |  Telegram:xx4gs  |         |
|   |  Instagram:xx4gs |         |
|   |__________________|         |
|     ______________________     |
|    |  MohammedPro💉      |     |
|    |  MPro_admin.py💉    |     |
|    |_____________________|     |
|________________________________|
""")
slow("حط اخر الموقع ذي /")
print("  ")
urlmpro=input("[MPro url] >> ")
mprofile='mpro-list.txt'
mprofile1=open(mprofile,'r')
def mpro_admin():
	while True:
		mprofile2 = mprofile1.readline().split('\n')[0]
		if "MohammedPro" in mprofile2:
			mmppp=input("Examination is over Exit Enter : ")
			print(mmppp)
			exit()
		else:
			mprourl= urlmpro+mprofile2
			reqmpro=requests.get(url=mprourl).status_code 
			if reqmpro == 200:
				print('[MPro Found] >> ', mprourl, '\n')
				print("____")
				with open("Found_MPro.txt", "a") as mppr:
					mppr.write(f"[MPro Found] >> {mprourl}\n")
			else:
				print('[MPro Not Found] >> ', mprourl, '\n')
				print("____")
threads=[]
for i in range(1):
	thread1= threading.Thread(target=mpro_admin)
	thread1.start()
	threads.append(thread1)
for thread2 in threads:
	thread2.join()
