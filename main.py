import requests
from requests.auth import HTTPBasicAuth
from time import sleep

#auth = HTTPBasicAuth('alayouey@gmail.com', 'shiro123', 'GDmzexCFXz')
request = requests.Session()



obj = request.request(
    'get', 
    'https://firefaucet.win/start',
    cookies={
        'session': 'e59670da-60ae-4559-a555-12f533cd317c.0vtn4o3qMik_cK3hJliW2uKCQUM'
    }
)

html = open('request_html.html', 'w')
#html.write(f'{obj.text}')
html.close()
print(obj)


#
#
# print(request.headers)






 # cookies='e59670da-60ae-4559-a555-12f533cd317c.0vtn4o3qMik_cK3hJliW2uKCQUM'