import requests, re, time, geocoder, random, schedule
from bs4 import BeautifulSoup

if __name__ == '__main__':
    weather_URL = "https://weather.com/weather/today/"
    weather = requests.get(weather_URL)
    weather_bs = BeautifulSoup(weather.content, "html.parser")

    weather_regex = "(.*)Rain(.*)|(.*)Snow(.*)|(.*)Shower(.*)|(.*)Hail(.*)|(.*)Thunderstorm(.*)"

    def func():
        weather_condition = weather_bs.find('div', {'class': 'CurrentConditions--phraseValue--2Z18W'}).getText()
        temperature = weather_bs.find('span', {'class': 'TodayDetailsCard--feelsLikeTempValue--Cf9Sl'}).getText()
        study_recs = []

        print("It is " + weather_condition.lower() + " right now!\nAnd I'd say it feels like " + temperature + " outside.\n")

        if re.search(weather_regex, weather_condition) != "" and (int(re.sub('°', '', temperature)) > 32 & int(re.sub('°', '', temperature)) < 85):
            g = geocoder.ip('me')
            study_URL = f"https://www.yelp.com/search?find_desc=places+to+study&find_loc={g.lat},{g.lng}"
            study = requests.get(study_URL)
            study_bs = BeautifulSoup(study.content, "html.parser")

            for a in study_bs.find_all('a', {'href': True, 'class': 'css-1m051bw', 'target': '_blank', 'name': True, 'rel': True}):
                study_recs.append(a.get_text())
            print("Why not have a change of pace and go to " + random.choice(study_recs) + " to do some work?")
        elif re.search(weather_regex, weather_condition) == "":
            print("The weather condition doesn't seem great, but you can still relocate to another room!")
        elif int(re.sub('°', '', temperature)) < 32:
            print("Brr! It's too cold to be walking around outside! Maybe relocate to another room!")
        elif int(re.sub('°', '', temperature)) > 85:
            print("It's way too hot outside! Maybe relocate to another room!")
        else:
            print("Hmm...something went wrong")

    schedule.every(90).minutes.do(func)

    while True:
        schedule.run_pending()
        time.sleep(1)
