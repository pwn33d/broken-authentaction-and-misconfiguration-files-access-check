import requests,sys,colorama,concurrent.futures,time
colorama.init()
def spped():
	print('''
		this script for check restriced and misconfiguration access for files\n
		and diractorys
		coded by #saad_alrby&&cop_of_tea
		''')
	url =input("Enter your url ex:http://www.site.com/ ")
	page=input("Enter ur page|diractory ex: admin or adminpanel ")
	i=["/../~"+page,".json",".bak",".xml",".zip",".tar",".txt","?%s"%page,";","/%5C","///","%2e%2e","//","%2f%2e%2e","/%5c/","%2f..","/;","/baz/%2e%2e/"+page,"~","/..;/",".","..","...","...."+page,"/."+page,"/.."+page,"/..."+page,"/...."+page,"/x/../"+page,"/x/./"+page,"/x/../../"+page,"/x/././"+page]
	for bypass in i:
		bypass=bypass
		try:
			request1=requests.get(url+page+bypass)
		except:
			print("bad url ")
			sys.exit()
		else:
			if request1.status_code==200 or str(request1.status_code)<="299":
				print(colorama.Fore.GREEN,"works good" ,request1.url)
			if request1.status_code==300 or str(request1.status_code)<="399":
				print(colorama.Fore.BLUE,"man this site keeps redirect me ",request1.url)
			if request1.status_code==400 or str(request1.status_code)<="499":
				print(colorama.Fore.RED,"404 error not works " ,request1.url)
			else:
				print(colorama.Fore.YELLOW,"misunderstood http response " ,request1.url)

with concurrent.futures.ThreadPoolExecutor() as pl:
	time.sleep(0.5)
	pl.submit(spped)
