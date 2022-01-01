import requests


# ssqWD = '<meta name="description" content="'  # Start Search Query Website Data
# esqWD = '<meta name="keywords" content="'  # End Search Query Website Data
# xsqWD = 'osu! - Rhythm is just a *click* away!'  # Excluded Search Query Website Data

ssqWD = '{"artist":"'  # Start Search Query Website Data
esqWD = '{"comments":'  # End Search Query Website Data
xsqWD = 'osu! - Rhythm is just a *click* away!'  # Excluded Search Query Website Data

xDataChar = [['\'', ''], ['\"', ''], ['{', ''], ['}', ''], ['_', ' '], ['availability', ''], [':download', 'download']]  # Excluded Data Characters
xMapData = ['id', 'nominations summary', 'required']  # Excluded Map Data


def get_beatmap(mapID):
    mapWebsiteData = requests.get(f'https://osu.ppy.sh/b/{mapID}').text
    mapHTML = mapWebsiteData[mapWebsiteData.find(ssqWD) + len(ssqWD):mapWebsiteData.find(esqWD) - 3]
    mapStr = ssqWD + mapHTML[:mapHTML.find('"covers":{"cover":')] + mapHTML[mapHTML.find('"creator":'):mapHTML.find('"preview_url":"')] + mapHTML[mapHTML.find('"source":"'):mapHTML.find(',"beatmaps":')]
    # mapData = mapStr.split(',"')

    if xsqWD in mapHTML:
        mapExists = False
    else:
        mapExists = True

    mapData = {}

    if mapExists:
        for i in mapStr.split(',"'):
            tempData = i
            for o in xDataChar:
                tempData = tempData.replace(o[0], o[1])
            if not tempData.split(':', 1)[0] in xMapData:
                mapData[tempData.split(':', 1)[0]] = tempData.split(':', 1)[1]

    if mapExists:
        return mapID, mapData, mapExists
    else:
        return mapID, None, mapExists
