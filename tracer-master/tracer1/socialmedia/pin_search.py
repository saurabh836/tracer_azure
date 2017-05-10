import requests, pprint, json
from bs4 import BeautifulSoup as bs


class pinterest:
    def pin_user_search(self, nam):
        url = "https://www.pinterest.com/search/people/?q=" + nam.replace(" ", "%20")
        result = requests.get(url)
        c = result.content
        soup = bs(c, "lxml")

        samples = soup.find_all("div", {"class": "item"})
        samples_new = []
        for sample in samples:
            img = sample.find("img", {'class': "userFocusImage"})['src']
            nam = sample.find("h3", {'class': "username"}).get_text().strip()
            pin_link = "https://www.pinterest.com" + sample.find("a", {'class': "userWrapper"}).get('href')
            sam_dict = {"Name": nam.encode("ascii", 'ignore'), "Image_url": img.encode("ascii", 'ignore'), "Pintrest_link": pin_link.encode("ascii", 'ignore')}
            samples_new.append(sam_dict)
        return json.dumps(samples_new)



def gplus_search(nam):
    r = requests.get("https://www.googleapis.com/plus/v1/people?query="
                     + nam + "&key=AIzaSyCSQzemPc7tzY_2yW1e_1wi1fmeP7c5XxU")
    result = r.json()['items']
    return json.dumps(result)


def bing_search(nam):
    url = 'https://api.cognitive.microsoft.com/bing/v5.0/search'
    payload = {'q': nam}
    headers = {'Ocp-Apim-Subscription-Key': '9ab7e0a56ef94a49b7980a1529b59f05'}
    r = requests.get(url, params=payload, headers=headers)
    return json.dumps(r.json().get('webPages', {}).get('value', {}))
