albums = [("welcome to my nightmare", "alice cooper", 1975),
          ("bad company", "bad company", 1974),
          ("nightfight", "Budgie", 1981),
          ("more mayhem", "emila day", 2011),
          ("ride th lighting", "metallica", 1984),
          ]

# above is the list of 5 tuple
print(len(albums))

print("------------------------way 1--------------------------------")

# way one to unpack
for album in albums:
    print("album: {}, Artist: {}, Year: {}".format(album[0], album[1], album[2]))

# way 2 to unpack
print("------------------------way 2--------------------------------")
for name, artist, year in albums:
    print("album: {}, Artist: {}, Year: {}".format(name, artist, year))

#way 3 to upack
print("------------------------way 3--------------------------------")

for album in albums:
    name, artist, year=album
    print("album: {}, Artist: {}, Year: {}".format(name, artist, year))


