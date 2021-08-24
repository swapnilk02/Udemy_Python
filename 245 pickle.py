#similar to java .....pythin also provide the mechanism serialise and deserialisation....called pickling

import pickle     # we are importing the pickle module  here


imelda = ('More Mayhem',
          'IMelda May',
          '2011',
          ((1, 'Pulling the Rug'),
           (2, 'Psycho'),
           (3, 'Mayhem'),
           (4, 'Kentish Town Waltz')))


with open("amelda.pickel","wb") as pickle_file:
    pickle.dump(imelda,pickle_file)




with open("amelda.pickel","rb") as imelda_pickled:
    imelda2=pickle.load(imelda_pickled)



print(imelda2)
album,artist,year,track_list=imelda2

print(album)
print(artist)
print(year)
print(track_list)
for track in track_list:
    track_number,track_title=track
    print(track_number,track_title)


#what we did  here is we first wrote a object on the file in byte format and then retrived it again


# we are using the pickling for serialisation