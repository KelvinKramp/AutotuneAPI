import requests
from secret_vars import *


PATH = "get-profile"


# print(BASE + api_url_part + "run-autotune", {"--nightscout":NS_HOST, "--start-date":start_date, "--end-date":end_date})

response = requests.get(BASE + api_url_part + PATH, {"--nightscout":NS_HOST, "--start-date":start_date, "--end-date":end_date})
print(response)
print(response.text)