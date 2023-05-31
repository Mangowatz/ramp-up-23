import requests

#make sure server is started cmd: pyhton3 main:app --reload
#--reload makes it such that we don't need to re run our app to reflect changes on site

request = requests.get('http://127.0.0.1:8000/')
print(request.json())