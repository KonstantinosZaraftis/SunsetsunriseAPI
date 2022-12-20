import requests
#make parameters in dictionary
#the parameters will be lat and lng
# make constants the lat and lng
my_lat=36.891180
my_lng=27.283390

parametersendpoint={
    "lat":my_lat,
    "lng":my_lng,
}

response=requests.get("https://api.sunrise-sunset.org/json" ,params=parametersendpoint)
response.raise_for_status()
data=response.json()
print(data)