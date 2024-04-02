import requests

def get_pexels_images(api_key, query, per_page=10):
    url = f"https://api.pexels.com/v1/search?query={query}&per_page={per_page}"
    headers = {"Authorization": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    images = [photo['src']['original'] for photo in data['photos']]
    return images
