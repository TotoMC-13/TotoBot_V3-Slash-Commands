# WEB SCRAPING IMPORTS
from bs4 import BeautifulSoup
import requests
import re


def get_status(server, number_only=False):

    url = "http://www.byond.com/games/exadv1/spacestation13"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser", from_encoding="iso-8859-1")

    soup_find_all_result = soup.body.find_all(text=server)
    if len(soup_find_all_result) == 0:
        if number_only == False:
            players_names = None
            private_number = None
            current_map = None

        players_number = None

        if number_only == True:
            return players_number

        return players_names, players_number, private_number, current_map

    b_tag_parent = [b_tag_parent.parent for b_tag_parent in soup_find_all_result]

    div_tag_parent = [div_tag_parent.parent for div_tag_parent in b_tag_parent]

    div_tag_2_parent = [div_tag_2_parent.parent for div_tag_2_parent in div_tag_parent]

    final_request = [str(final_request) for final_request in div_tag_2_parent]

    if number_only == False:
        ckeys = re.findall(r'user_ckey="(\w+)"', final_request[0])
        is_private = re.findall(r'<span class="smaller">(\w+)', final_request[0])
        players_names = ", ".join(ckeys)
        private_number = " ".join(is_private)

    number = re.findall(r"Logged in: (\w+)", final_request[0])

    players_number = " ".join(number)

    if len(players_number) == 0:
        players_names = 0
        players_number = 0
        private_number = 0

    if number_only == True:
        return players_number

    find_map = re.findall(r"NSS (\w+)", str(div_tag_parent))

    if find_map:
        current_map = "NSS " + find_map[0]
    else:
        current_map = "???"

    return players_names, players_number, private_number, current_map
