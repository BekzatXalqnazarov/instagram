import requests
async def instagram(smstext):
    url = "https://instagram-downloader-download-instagram-stories-videos4.p.rapidapi.com/convert"

    querystring = {"url":smstext}

    headers = {
        "x-rapidapi-key": "509be8d063mshedfacb4f552a9cep1e1613jsne1abf43c654a",
        "x-rapidapi-host": "instagram-downloader-download-instagram-stories-videos4.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return(response.json()['media'][0]['url'])