import requests

ip_address = ' Past Your Ip Address '
response = requests.get(f'https://ipinfo.io/{ip_address}/json')
data = response.json()

print(f"IP: {data['ip']}")
print(f"City: {data['city']}")
print(f"Region: {data['region']}")
print(f"Country: {data['country']}")
print(f"Location: {data['loc']}")
print(f"ISP: {data['org']}")
