import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://www.youtube.com/watch?v=qmlabKbpTGM" + sys.argv[1])
print(json.dumps(response.json(), indent=2))