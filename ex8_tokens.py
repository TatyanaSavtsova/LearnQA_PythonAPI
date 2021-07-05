import requests
import json
import time

url = "https://playground.learnqa.ru/ajax/api/longtime_job"

response = requests.get(url)
response_json = json.loads(response.text)

token = response_json["token"]
response2 = requests.get(url, params={"token": token})
response2_json = json.loads(response2.text)
print("...The task is NOT ready. Checking status...")
if response2_json["status"] == "Job is NOT ready":
    print("Status '" + response2_json["status"] + "' is correct\n")
    time.sleep(response_json["seconds"])
else:
    print("Status is NOT correct\n")

response3 = requests.get(url, params={"token": token})
response3_json = json.loads(response3.text)
print("...The task is ready. Checking status...")
if response3_json["status"] == "Job is ready":
    print("Status '" + response3_json["status"] + "' is correct")
    try:
        print("Result is " + response3_json["result"])
    except KeyError:
        print("Result is NOT found")
else:
    print("Status is NOT correct")
