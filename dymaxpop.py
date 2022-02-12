import requests
from pathlib import Path






url = 'http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg'
loc = Path('ppp_2020_1km_Aggregated.tif')

def download_and_save(url, loc):
    print('Beginning file download with requests')

    r = requests.get(url)

    with open(loc, 'wb') as f:
        f.write(r.content)

    # Retrieve HTTP meta-data
    print(r.status_code)
    print(r.headers['content-type'])
    print(r.encoding)