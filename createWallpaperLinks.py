import pathlib
import requests
from bs4 import BeautifulSoup


def create():
    path = pathlib.Path("wallpapersLinks.txt")
    if path.exists():
        # print("File \"wallpaperLinks.txt\" file already exists. Delete to recreate if needed.")
        return
    create_file()


def create_file():
    print("File doesn't exist. Creating...")
    links = get_links()
    with open("wallpapersLinks.txt", "w+") as f:
        f.writelines(links)


def get_links():
    link_skeleton = "https://wallpaperscraft.com/all/ratings/1920x1080/page"
    href_tags = []
    for i in range(1, 101):
        print("Iteration ", i, "out of 100")
        link = link_skeleton + str(i)
        response = requests.Request

        try:
            response = requests.get(link)
        except requests.ConnectionError:
            print("Connection error")
            exit()

        print("Response: ", response.status_code)
        if response.status_code != 200:
            return href_tags
        soup = BeautifulSoup(response.text, "html.parser")
        wallpapers_links_pre = soup.find_all(class_="wallpapers__link")
        for el in wallpapers_links_pre:
            href_tags.append(el['href'])
    href_tags = [l.replace("/download/", "") for l in href_tags]
    href_tags = [l.replace("/", "_") for l in href_tags]
    href_tags = ["https://images.wallpaperscraft.com/image/" + l + ".jpg\n" for l in href_tags]
    return href_tags
