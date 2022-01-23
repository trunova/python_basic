import requests
import json


def episode_with_the_most_deaths(date: list):
    episodeDict = dict()
    for i_dict in date:
        if (i_dict.get("season"), i_dict.get("episode")) in episodeDict.keys():
            episodeDict[(i_dict.get("season"), i_dict.get("episode"))] += i_dict.get("number_of_deaths")
        else:
            episodeDict[(i_dict.get("season"), i_dict.get("episode"))] = i_dict.get("number_of_deaths")

    maxValue = 0
    maxKey = 1
    for i_key, i_value in episodeDict.items():
        if i_value > maxValue:
            maxValue = i_value
            maxKey = i_key
    return maxKey[0], maxKey[1], maxValue


def list_of_deaths(key, date: list) -> list:
    listDeaths = list()
    for i_dict in date:
        if i_dict.get("season") == key[0] and i_dict.get("episode") == key[1]:
            listDeaths.append(i_dict["death"])
    return listDeaths


def episode_id(key, date: list) -> int:
    for i_dict in date:
        if i_dict.get("season") == str(key[0]) and i_dict.get("episode") == str(key[1]):
            return i_dict.get("episode_id")
    else:
        return None


if __name__ == "__main__":
    breakingBad_req = requests.get('https://www.breakingbadapi.com/api/deaths/')
    data_deaths = json.loads(breakingBad_req.text)

    season_episode = episode_with_the_most_deaths(data_deaths)
    breakingBad_req = requests.get('https://www.breakingbadapi.com/api/episodes/')
    data_episode = json.loads(breakingBad_req.text)

    dict_episode = dict()
    dict_episode["Id эпизода"] = episode_id(season_episode, data_episode)
    dict_episode["Номер сезона"] = season_episode[0]
    dict_episode["Номер эпизода"] = season_episode[1]
    dict_episode["Общее количество смертей"] = season_episode[2]
    dict_episode["Список погибших"] = list_of_deaths(season_episode, data_deaths)
    print(dict_episode)

    with open('breakingBad.json', 'w', encoding="UTF8") as file:
        json.dump(dict_episode, file, indent=4, ensure_ascii=False)
