import requests
import colorama
from colorama import Fore, Style


print('''   
		   ####################################
		   #                                  #
		   #        ------------------        #                 
		   #        Admin_panel_finder        #		   
		   #        ------------------        #  
		   #          version 1.0             #
		   #                                  #
		   #                                  #
		   #       Developed by SO3HT3T       #		   
		   #################################### 
			
			''')

url = input("\n[+]Enter your site![+]:: ")
url = url.replace("https://","")
url = url.replace("http://","")
url = url.replace("/","")
url = "http://"+url

wordlist = open("wordlist.txt","r")
payload = wordlist.readlines()

for i in payload:
	url2 = requests.get(url+i)
	if url2.status_code==200:
		print(Fore.BLUE +"[+] Found! [+]",url+i)
	else:
		print(Fore.RED+"[-] Not Found! [-]",url+i)
