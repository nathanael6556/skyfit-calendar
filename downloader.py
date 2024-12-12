import requests
import config


response = requests.get(config.URL)
with open(config.HTML_FILENAME, "wb") as f:
    f.write(response.content)