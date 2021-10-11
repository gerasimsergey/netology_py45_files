import requests


API_KEY = '2619421814940190'
hero_list = ['Hulk', 'Captain America', 'Thanos']
URL = f'https://superheroapi.com/api/{API_KEY}/search/'


def smartest_superhero():
    intelligence_dict = {}
    for name in hero_list:
        r = requests.get(URL + name)
        hero = r.json()['results'][0]['powerstats']['intelligence']
        intelligence_dict[name] = int(hero)

    print(sorted(intelligence_dict.items()))

    for i in sorted(intelligence_dict.items(), key=lambda x: x[1])[::-1]:
        return f"Most Intelligence -> {i[0]}"


print(smartest_superhero())