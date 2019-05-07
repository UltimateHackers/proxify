import requests
import re
import random

def check_argument(url_check):
	if url_check == 'us':
		url_proxy = 'https://www.us-proxy.org/'
	#elif url_check == 'socks':
	#	url_proxy = 'https://www.socks-proxy.net/'
	#elif url_check == 'ssl':
	#	url_proxy = 'https://www.sslproxies.org/'
	#elif url_check == 'google':
	#	url_proxy = 'http://www.google-proxy.net/'
	elif url_check == 'anonimous':
		url_proxy = 'https://free-proxy-list.net/anonymous-proxy.html'
	elif url_check == 'uk':
		url_proxy = 'https://free-proxy-list.net/uk-proxy.html'
	#elif url_check == 'web':
	#	url_proxy = 'https://free-proxy-list.net/web-proxy.html'
	else:
		url_proxy = 'https://free-proxy-list.net/'
	return url_proxy

def make_request(url_check): # Function to extract proxy data. Returns list.
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
	           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	           'Accept-Encoding': 'none',
	           'Accept-Language': 'en-US,en;q=0.8',
		   'Connection': 'keep-alive',
	           'Content-Encoding': 'gzip',
	           'Content-Type': 'text/html; charset=utf-8',}
	response = requests.get(url_check, headers=headers).text # makes request to the site and retrieves source code
	# Regex to extract "valuable stuff" from the source code.
	return re.findall(r"<tr><td>[^<]*</td><td>[^<]*</td><td>[^<]*</td><td class='hm'>[^<]*</td><td>[^<]*</td><td class='hm'>[^<]*</td><td class='hx'>[^<]*</td><td class='hm'>[^<]*</td></tr>", response)

def one(url_check = 'new'): # function to fetch one proxy. Returns string.
	url_proxy = check_argument(url_check)
	match = random.choice(make_request(url_proxy)) # selects random item from "valuable stuff" list
	result = match.split('</td>') # makes list of match by spliting it from '</td>'
	ip_address = result[0].strip('<tr><td>') # fetches first item of result list and removes '<tr><td>' from it
	port = result[1].strip('</td>') # fetches 2nd item of result list and removes '</td>' from it
	if result[6].strip('<td class=\'hx\'>') == 'yes': # fetches fifth item of result list and removes ''<td class='hx'>'' from it and checks if its equal to 'yes'
		typ = 'https'
	else:
		typ = 'http'
	return typ + '://' + ip_address + ':' + port # returns http(s)://ip_address:port

def many(url_check = 'new'): # function to fetch many proxies. Returns list.
	url_proxy = check_argument(url_check)
	proxies = [] # list to store proxies, obvious lmao
	for match in make_request(url_proxy): # iterating over the "valueable stuff" list
		result = match.split('</td>') # makes list of match by spliting it from '</td>'
		ip_address = result[0].strip('<tr><td>') # fetches first item of result list and removes '<tr><td>' from it
		port = result[1].strip('</td>') # fetches 2nd item of result list and removes '</td>' from it
		if result[6].strip('<td class=\'hx\'>') == 'yes': # fetches fifth item of result list and removes ''<td class='hx'>'' from it and checks if its equal to 'yes'
			typ = 'https'
		else:
			typ = 'http'
		proxies.append(typ + '://' + ip_address + ':' + port)
	return proxies

def get(number,url_check = 'new'): # function to fetch specific number of proxies. Returns list.
	url_proxy = check_argument(url_check)
	proxies = [] # list to store proxies, obvious lmao
	if number > 300: # Maximum number of proxies we can fetch in one is 300
		number = 300
	matches = make_request(url_proxy)[:number] # fetching n items from the "valueable stuff" list
	for match in matches: # iterating over the n items
		result = match.split('</td>') # makes list of match by spliting it from '</td>'
		ip_address = result[0].strip('<tr><td>') # fetches first item of result list and removes '<tr><td>' from it
		port = result[1].strip('</td>') # fetches 2nd item of result list and removes '</td>' from it
		if result[6].strip('<td class=\'hx\'>') == 'yes': # fetches fifth item of result list and removes ''<td class='hx'>'' from it and checks if its equal to 'yes'
			typ = 'https'
		else:
			typ = 'http'
		proxies.append(typ + '://' + ip_address + ':' + port)
	return proxies
