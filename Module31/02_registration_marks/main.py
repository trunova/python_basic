import re

numbers: str = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

if __name__ == "__main__":
    taxiNumbers = list(re.findall(r'[ABEKMHOPCTYXАВЕКМНОРСТУХ]{2}\d{5,6}', numbers))
    privateCarNumbers = list(re.findall(r'[ABEKMHOPCTYXАВЕКМНОРСТУХ]\d{3}[ABEKMHOPCTYXАВЕКМНОРСТУХ]{2}\d{2,3}', numbers))
    print('Список номеров частных автомобилей: {privateCarNumbers}\nСписок номеров такси: {taxiNumbers}'.format(
        privateCarNumbers=privateCarNumbers,
        taxiNumbers=taxiNumbers
    ))

