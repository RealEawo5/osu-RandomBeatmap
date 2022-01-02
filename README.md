# osu-RandomBeatmap

# randomMap.py

To use the program, bind the "randomMap.py" to a key or button on either your mouse or keyboard.


# mapSettins.csv

:::::::::::::::::::::

The first & second parameter in the "mapSettings.csv" is the start & end index of the range of beatmapID's the program randomly chooses from.

:: NOTE! :::::::::::: 
I recommend a range of '1,3333333' if you want the program to choose between almost all of the osu!beatmaps ever uploaded. 
If you dont want any old maps, approx. 2007-2014, then i reccomend a range of '499999,3333333'.
If you want a selection of only old maps, then i'd recommend a range of '1,499999'.
:::::::::::::::::::::


:::::::::::::::::::::

The third parameter in the "mapSettings.csv" is if you want a specific status on the beatmap as a parameter, eg. 'Ranked', 'Loved', etc...

:: NOTE! ::::::::::::
The diffrent status parameters are as follows:
 - 'ranked'
 - 'loved'
 - 'qualified'
 - 'wip'
 - 'pening'
 - 'graveyard'

If you don't want any specified status as a parameter, then set th third parameter to '0'

That being said, I DO NOT RECOMMED YOU SPECIFY A BEATMAP STATUS OTHER THAN 'GRAVEYARD', DUE TO THE LIKLINESS OF GETTING A BEATMAP WITH ANY OTHER SPECIFICATION IS SO SMALL THAT YOU MIGHT GET A COOLDOWN ON ACCSESSIG THE https://osu.ppy.sh/b/ WEBSITE BEFORE A BEATMAP CAN BE FOUND. This cooldown is to prevent DDoS attacks, and there is unfortunatly not anything i can do to prevent this from triggering. This cooldown causes a error with the program, and henche makeing the program not funcion properly for a breif perod of time. I dont have any excact data on how long this cooldown is, but you usually can accsess the webiste after 10-20min of getting this cooldown.
:::::::::::::::::::::
