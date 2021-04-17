#version number
__version__ = '0.0.1'

#importing all the necessary libraries
import requests
import re
import urllib.parse
from random import choice
from pkg_resources import resource_filename
from urllib.parse import urlparse
from bs4 import BeautifulSoup

class Google:

	#defining the googleSearch function
	def search(self, query):

		#making the url ready for requests
		url = 'https://www.google.com/search?client=ubuntu&channel=fs&q={}&ie=utf-8&oe=utf-8'.format(query)

		#fetching user agents from ua_file
		with open(resource_filename('googleScrapy', 'ua_file.txt'), 'r') as filehandle:
			user_agents = filehandle.read().splitlines()

		#defining header for the request function
		ran_head = {
				'User-Agent': choice(user_agents)
		}

		#declaring list g_clean to store the fetched urls
		g_clean=[]

		#exception handling code to make sure we don't run into errors
		try:

			#fetching the response using get method in requests
			html = requests.get(url, headers=ran_head)

			#checking the response status to be success
			if html.status_code==200:

				#parsing the fetched html in the response using html parser in beautiful soup
				soup = BeautifulSoup(html.text, 'html.parser')

				#finding all the 'a' tags, links, in the parsed html
				a = soup.find_all('a')

				#looping through the all found a tags for processing
				for i in a:

					#extracting the href attribute for the link to the search results
					k = i.get('href')

					#exception handling code to prevent running into erros
					try:

						#search for the pattern of a url to prevent unneccessary attributes in the result using re module
						m = re.search("(?P<url>https?://[^\s]+)", k)

						#fetching only the url part in the array
						n = m.group(0)

						#splitting the url upto the parameters part to get only the necessary url
						rul = n.split('&')[0]

						#parsing the url to divide it into components using urlparse
						domain = urlparse(rul)

						#checking if the fetched url belongs to google.com if true skip the url
						if(re.search('google.com', domain.netloc)):
							continue

						#else add it to the result list
						else:
							g_clean.append(rul)
					except:
						continue

		except Exception as ex:
			print(str(ex))
			
		#finally return the result urls
		finally:
			return {'status_code':html.status_code, 'links': g_clean}