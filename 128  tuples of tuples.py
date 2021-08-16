#belowis the list of tuple

albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]

#above ,album is the list of tuples.....and each tuple has onelist of tuple which store the songs name
# we will be iterating over it now

for name,artist,year,song in albums:
    print("Album : {}, Artist : {},Year: {}, Song : {}".format(name,artist,year,song))


print()

album=albums[2]
print(album)  # getting tuple fromlist of tuple

songs=album[3]
print(songs) # getting  item arte at index 3in tuple..which is tuple itself

song=songs[1]# gettin item at index 1 from a list of  tuple
print(song)
print(song[1]) # getting only song name

#in above code  we wnated to know the exact song name from album....the sam canbe done in single line

print()
mayhem=albums[3][3][2][1]
print(mayhem)

print()
print(albums[3][3])

