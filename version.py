import requests

print("Requests version: " + requests.__version__)

get_request = requests.get("https://www.google.com/")
print("Retrieving Google Home Page Contents\n", get_request.content)


get_script = requests.get("https://raw.githubusercontent.com/shearpaladin/CMPUT404-LAB1/main/version.py")

print(get_script.text)
