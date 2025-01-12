from bs4 import BeautifulSoup
import requests

def long_url(short_url):
    response = requests.get(short_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text,'html.parser')
        long_link = soup.find(id="long-link")
        return long_link.text

    else:return "Failed to fetch the page details"


# long_url('https://tinyurl.com/kmsvscn')
