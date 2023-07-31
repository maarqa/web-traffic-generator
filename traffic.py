import requests
import random
import time

url = 'https://essayloom.blogspot.com'

my_file = open("whatismybrowser-user-agent-database.txt", "r")
data = my_file.read()
user_agents = data.split("\n")
my_file.close()

reflist = ["",
"https://www.google.com/search?q=English+Essays",
'https://www.google.com',
"search.yahoo.com/search?p=Engliah+Essays",
"https://www.bing.com/search?q=English+Essays", 
"https://www.google.com/search?q=Essay+ Loom",
"https://www.google.com/search?q=essays",
'https://www.yahoo.com', 
'https://www.bing.com', 
'https://www.youtube.com',
'https://www.facebook.com',
'https://www.twitter.com',
'https://www.instagram.com', 
'https://www.linkedin.com',  
'https://www.wikipedia.org', 
'https://www.aol.com',
'https://www.imdb.com', 
'https://www.quora.com', 
'https://www.medium.com'
]
weights = [40,15,7,5,10,4,3,3,3,1,1,1,1,1,1,1,1,1,1]
no = 0
for i in range(1000):
     referer_url ="".join(random.choices(reflist,weights= weights))
     headers = {'User-Agent': random.choice(user_agents),'Referer': referer_url}
     
     response = requests.get(url, headers=headers)
     no +=1
     
     sleep = random.randint(2,10)
     print(f"Views: {no} From:{referer_url} Sleeping For:{sleep}s Result:{response.status_code}")
     time.sleep(sleep)
