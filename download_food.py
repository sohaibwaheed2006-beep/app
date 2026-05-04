import urllib.request
import urllib.parse
import json
import os

dir_path = "c:/Users/2024/OneDrive/Documents/antigravity/proj2 animated website/images"

def download_meal(query, filename):
    try:
        encoded_query = urllib.parse.quote(query)
        url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={encoded_query}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req)
        data = json.loads(response.read().decode('utf-8'))
        
        if data['meals']:
            img_url = data['meals'][0]['strMealThumb']
            print(f"Found {query}: {img_url}")
            urllib.request.urlretrieve(img_url, os.path.join(dir_path, filename))
            print(f"Downloaded {filename}")
        else:
            print(f"No results for {query}")
    except Exception as e:
        print(f"Error for {query}: {e}")

# Download Tikka
download_meal("Chicken Tikka Masala", "real_tikka.jpg")
if not os.path.exists(os.path.join(dir_path, "real_tikka.jpg")):
    download_meal("Tandoori chicken", "real_tikka.jpg")

# Download Duo Deal (A big chicken meal)
download_meal("Kentucky Fried Chicken", "real_duo_deal.jpg")

# Download Raw BBQ (A raw ingredient)
try:
    img_url = "https://www.themealdb.com/images/ingredients/Chicken-Small.png"
    urllib.request.urlretrieve(img_url, os.path.join(dir_path, "real_raw_bbq.png"))
    print("Downloaded real_raw_bbq.png")
except Exception as e:
    pass
