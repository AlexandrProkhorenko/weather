from pygismeteo import Gismeteo


def startt():
    choise = input('Показать погоду?\n').capitalize()
    if choise == 'Y':
        weather()
    elif choise == 'N':
        print('Досвидос')



def weather():
    gm = Gismeteo()
    city = input('Введите название города\n').capitalize()
    result = gm.search.by_query(city)
    city_id = result[0].id
    current = gm.current.by_id(city_id)
    print(current.temperature.air)
    stop = input('Выключить программу?\n').capitalize()
    if stop =='Y':
        return
    elif stop == 'N'.capitalize():
        weather()



startt()






