import requests

url = "https://playground.learnqa.ru/ajax/api/compare_query_type"

print("http-запрос любого типа без параметра method")
response = requests.get(url)
print(response.text)

print("\nhttp-запрос не из списка\n")
response2 = requests.head(url, data={"method": "HEAD"})
print(response2.text)

print("\nзапрос с правильным значением method\n")
response31 = requests.get(url, params={"method": "GET"})
print(response31.text)
response32 = requests.post(url, data={"method": "POST"})
print(response32.text)
response33 = requests.put(url, data={"method": "PUT"})
print(response33.text)
response34 = requests.delete(url, data={"method": "DELETE"})
print(response34.text)

print("\nвсе возможные сочетания реальных типов запроса и значений параметра method\n")
methods = ["POST", "GET", "PUT", "DELETE"]

for i in methods:
    response41 = requests.get(url, params={"method": i})
    print(f"get + {i} {response41.text}")
    response42 = requests.post(url, data={"method": i})
    print(f"post + {i} {response42.text}")
    response43 = requests.put(url, data={"method": i})
    print(f"put + {i} {response43.text}")
    response44 = requests.delete(url, data={"method": i})
    print(f"delete + {i} {response44.text}")
