# WEB SCRAPING IMPORTS
from bs4 import BeautifulSoup
import requests
import re


def get_status(server, number_only=False):
    url = "http://www.byond.com/games/exadv1/spacestation13"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser", from_encoding="iso-8859-1")
    soup_find_all_result = soup.body.find_all(text=server)

    if not soup_find_all_result:
        if number_only:
            return None
        return None, None, None, None

    final_request = str(soup_find_all_result[0].find_parent("div").find_parent("div").find_parent("div"))

    if not number_only:
        ckeys = re.findall(r'user_ckey="(\w+)"', final_request)
        is_private = re.findall(r'<span class="smaller">(\w+)', final_request)
        players_names = ", ".join(ckeys)
        private_number = " ".join(is_private)
    else:
        players_names = private_number = None

    players_number = " ".join(re.findall(r"Logged in: (\w+)", final_request)) or 0

    if number_only:
        return players_number

    current_map = "NSS " + re.findall(r"NSS (\w+)", final_request)[0] if re.findall(r"NSS (\w+)", final_request) else "???"

    return players_names, players_number, private_number, current_map
