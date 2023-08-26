import os.path

import requests


ANILIBRIA_URL = "http://anilibria.tv"
ANILIBRIA_URL_CACHE = "http://cache.libria.fun"
API_ROUTE = "http://api.anilibria.tv/v3/"


def get_list_of_anime_by_name(user_input: str):
    request = API_ROUTE + f"title/search?search={user_input}"
    response = requests.get(url=request, headers={'Accept': 'application/json'})
    return response.json()['list']


def get_anime_titles(anime_objs: list) -> list[tuple]:
    return [(title['names']['ru'], title['id']) for title in anime_objs]


def get_anime_content_by_id(anime_id: int):
    request = API_ROUTE + f"title?id={anime_id}"
    response = requests.get(url=request, headers={'Accept': 'application/json'})
    return response.json()


def get_anime_series_by_num(anime_id: int, series_num: int):
    request = API_ROUTE + f"title?id={anime_id}&filter=code,player.list.{series_num}.hls"
    response = requests.get(url=request, headers={'Accept': 'application/json'}).json()

    anime_code = response["code"]
    response = response["player"]["list"][int(series_num)]["hls"]

    file_url = response.get("fhd") or response.get("hd") or response.get("sd")
    file_url = ANILIBRIA_URL_CACHE + file_url

    filename = "-".join([anime_code, series_num]) + ".m3u8"

    script_path = os.path.abspath(__file__)
    script_directory = os.path.dirname(script_path)
    file_path = os.path.join(script_directory, "temp_m3u8", filename)
    with open(file_path, 'wb') as ff:
        ff.write(requests.get(file_url).content)

    return file_path
