from pynput.keyboard import Key, Controller
from beatmapLibrary import get_beatmap
import random


keyboard = Controller()

with open('mapSettings.csv', 'r') as mapSettingsFile:
    ID_SI, ID_EI, mapStatus = mapSettingsFile.read().split(',')

mapsSearchedCount = 1

while True:
    mapID, mapData, mapExists = get_beatmap(random.randint(int(ID_SI), int(ID_EI)))

    if not mapExists:
        print(f'\'{mapID}\' is not a map!')
    else:
        print(f'\'{mapID}\' found!')

        if mapData['download disabled'] == 'true':
            print(f'  -But \'{mapID}\' is not downloadable!')
        else:
            print(f'  -\'{mapID}\' has downloadability!')

            if not mapStatus == '0':
                if not mapData['status'] == mapStatus:
                    print(f'    -But \'{mapID}\' doesn\'t match the specified map status!')
                else:
                    print(f'    -\'{mapID}\' is {mapStatus}!')
                    break
            else:
                break
    mapsSearchedCount += 1

print(f'{mapsSearchedCount} maps searched through!\n')

mapLink = f'https://osu.ppy.sh/b/{mapID}'
print(f'''
ID   : {mapID}
Data : {mapData}
Link : {mapLink}''')

keyboard.type(f'!mp map {mapID}')
