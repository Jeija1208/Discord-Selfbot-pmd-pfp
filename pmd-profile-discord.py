import requests
import base64
from tls_client import Session
from github import Github
from github import Auth
import random
import re


#Github Authentication
auth = Auth.Token("Github API Token")
g = Github(auth=auth)
g.get_user().login
#Discord Token
token = "Discord Token"
 


# Get Random PMD portrait

#Specify PMD portrait Project
repo = g.get_repo("PMDCollab/SpriteCollab")

#select random pokemon
contents_pokemon = repo.get_contents("portrait")
pokemon = random.randint(0, len(contents_pokemon)-1)

#select random portrait from the pokemon
contents_portrait = repo.get_contents(contents_pokemon[pokemon].path)
contents_portrait_filtered = [cp for cp in contents_portrait if "png" in cp.path]
portrait = random.randint(0, len(contents_portrait_filtered)-1)

#Get portrait URL
file_content = repo.get_contents(contents_portrait_filtered[portrait].path)
url = file_content.download_url
print(url)


response = requests.get(url)
with open("image.jpg", "wb") as f:
    f.write(response.content)

 
#set as discord profile picture
 
sesh = Session(client_identifier="chrome_115", random_tls_extension_order=True)

headers = {
        "Content-Type": "application/json",
        "authority": "discord.com",
        "method": "PATCH",
        "scheme": "https",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US",
        "authorization": token,
        "origin": "https://discord.com",
        "sec-ch-ua": '"Not/A)Brand";v="99", "Brave";v="115", "Chromium";v="115"',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9020 Chrome/108.0.5359.215 Electron/22.3.26 Safari/537.36",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "X-Debug-Options": "bugReporterEnabled",
        "X-Discord-Locale": "en-US",
        "X-Discord-Timezone": "Asia/Calcutta",
        "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDIwIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDUiLCJvc19hcmNoIjoieDY0IiwiYXBwX2FyY2giOiJpYTMyIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV09XNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIGRpc2NvcmQvMS4wLjkwMjAgQ2hyb21lLzEwOC4wLjUzNTkuMjE1IEVsZWN0cm9uLzIyLjMuMjYgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjIyLjMuMjYiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoyNDAyMzcsIm5hdGl2ZV9idWlsZF9udW1iZXIiOjM4NTE3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsLCJkZXNpZ25faWQiOjB9"
    }
 
payload = {
    "avatar": f"data:image/jpeg;base64,{base64.b64encode(open('image.jpg', 'rb').read()).decode()}"
}
 
r =sesh.patch("https://discord.com/api/v9/users/@me", json=payload, headers=headers)
if r.status_code == 200:
    print("Profile picture changed successfully")
else:
    print(f"Error: {r}")
