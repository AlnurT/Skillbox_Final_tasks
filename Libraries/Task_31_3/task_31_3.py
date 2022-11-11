"""Задача 3. Во все тяжкие

Фанаты сериала Breaking Bad («Во все тяжкие») написали собственный API
по вселенной своего любимого сериала. Ссылка на документацию: Document At ion.

Внимательно изучите документацию этого API и напишите программу,
которая выводит на экран (а также в JSON-файл) информацию о том,
в каком эпизоде произошло больше всего смертей. Информация хранится в виде словаря,
который содержит:

1) ID эпизода.
2) Номер сезона.
3) Номер эпизода.
4) Общее количество смертей.
5) Список погибших.
"""
import json

import requests


def find_dict_of_max_deaths(dict_j: dict) -> dict:
    deaths_req = requests.get(dict_j["deaths"])
    deaths_list = json.loads(deaths_req.text)
    return max(deaths_list, key=lambda x: x["number_of_deaths"])


def create_new_dict_of_max_deaths(dict_j: dict, max_death_dict: dict) -> dict:
    new_deaths_dict = {}
    episodes_req = requests.get(dict_j["episodes"])
    episodes_list = json.loads(episodes_req.text)
    season = max_death_dict["season"]
    episode = max_death_dict["episode"]
    episode_id = (
        episode_n["episode_id"]
        for episode_n in episodes_list
        if episode_n["season"] == str(season) and episode_n["episode"] == str(episode)
    ).__next__()
    new_deaths_dict["episode_id"] = episode_id
    new_deaths_dict["season"] = season
    new_deaths_dict["episode"] = episode
    new_deaths_dict["number_of_deaths"] = max_death_dict["number_of_deaths"]
    new_deaths_dict["death_list"] = max_death_dict["death"]
    return new_deaths_dict


def main():
    breaking_bad_req = requests.get("https://www.breakingbadapi.com/api/")
    breaking_bad_j = json.loads(breaking_bad_req.text)
    max_death_dict = find_dict_of_max_deaths(breaking_bad_j)
    new_deaths_dict = create_new_dict_of_max_deaths(breaking_bad_j, max_death_dict)

    print(json.dumps(new_deaths_dict, indent=4))

    with open("br_bad_death.json", "w") as br_bad_death_f:
        json.dump(new_deaths_dict, br_bad_death_f, indent=4)


if __name__ == "__main__":
    main()
