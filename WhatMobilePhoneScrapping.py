from lxml import html
import requests
import datetime

def stripprice(price):
    price = str(price)
    price = price.strip("['\n    ")
    price = price.rstrip(' ]\'')
    price = price.lstrip(" ''\\'n'    Rs. ")
    price = price.replace(',','')
    return price

def stripname(name):
    name = str(name)
    name = name.strip("['\n    ")
    name = name.rstrip(' ]\'')
    name = name.lstrip(" ''\\'n'    Rs. ")
    name = name.replace('\'','')
    name = name.replace(',','')

    return name

page = requests.get('https://www.whatmobile.com.pk/')
tree = html.fromstring(page.content)

phone = []


for j in range(1,7):
    for i in range(1, 7):
        name = tree.xpath('//*[@id="container"]/div[2]/div[2]/section[' + str(j) + ']/ul/li[' + str(i) + ']/a[2]/text()')
        price = tree.xpath('//*[@id="container"]/div[2]/div[2]/section[' + str(j) + ']/ul/li[' + str(i) + ']/span/text()')

        name = stripname(name)
        price = stripprice(price)
        line ="Price of "+name+" is " + price + "\n"
        print(line)

        if int(price) >= 30000:
        	with open("phones_over_30000.txt", "a+") as file:
        		file.write(line)

        else:
        	with open("phones_under_30000.txt", "a+") as file:
        		file.write(line)
			# with open("phones_over_30000.txt", "a+") as file:
			# 	file.write(line)
	        
	    



