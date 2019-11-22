import createWallpaperLinks
import random
import requests
from pathlib import Path
import ctypes

# get links to wallpapers
createWallpaperLinks.create()
random.seed()
links = []
with open("wallpapersLinks.txt", "r") as f:
    links = f.read().splitlines()
# select random wallpaper
number = random.randint(0, 1500)

r = requests.Request
try:
    r = requests.get(links[number], stream=True)
except requests.ConnectionError:
    exit()

if r.status_code == 200:
    open("todayWallpaper.jpg", "wb").write(r.content)

with open("log.txt", "a") as f:
    f.write('\n')
    f.write(links[number])
# get path to wallpaper and set it
wallpaper_path = str(Path().absolute()) + "\\todayWallpaper.jpg"
ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper_path, 0)
