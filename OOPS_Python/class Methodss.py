# 1.__str__() method
# controls how object is printed
# used for string representation of an object.

#i) without __str__() method
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1=Person("Bob",20)
print(p1) #op: <__main__.Person object at 0x0000015828B10C20>




#ii)with __str__() method

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):  # overrides the string representation of an object.
        return f"{self.name} ({self.age})"

p2 = Person("Bob",20)
print(p2)  # op: Bob (20)
print() # inside methods for readable output.(for space between next code in o/p)

#2. can a class have Multiple methods?
# Yes, class can contain multiple methods that can work together.

"""
this eg combines:
    i)__init__
    ii)self
    iii)instance variables
    iv)multiple methods
    v)modifying object data

"""
"""
creates a blueprint called Playlist>
This blueprint can:
        i)store Playlist name
        ii)store songs
        iii)add songs
        iv)remove songs
        v)show songs

"""

class Playlist:
    def __init__(self,name):
        self.name = name
        self.songs = []

    def add_song(self,song):
        self.songs.append(song)
        print(f"Added: {song}")

    def remove_song(self,song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"Removed: {song}")

    def show_songs(self):
        print(f"\n Playlist '{self.name}':")
        for song in self.songs:
            print(f"- {song}")

my_playlist = Playlist("SEVENTEEN SONGS")

my_playlist.add_song("Cheers to you")
my_playlist.add_song("Maestro")
my_playlist.add_song("Super")
my_playlist.add_song("Tiny light")
my_playlist.add_song("Rock with you")
my_playlist.add_song("Fighting")
my_playlist.add_song("Circles")

my_playlist.remove_song("Tiny light")

my_playlist.show_songs()
print()
# instead of manual way calling we are using loop here: i) OOP concept ii)Loop

"""Loop concept:
✔ avoid repetitive code
✔ automate repeated actions"""

"""
Instead of repeatedly calling the same method, 
we can store values in a list and use a loop to process them efficiently.
"""

class Playlist:

    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        print(f"Added: {song}")

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"Removed: {song}")
        else:
            print(f"{song} not found in playlist")

    def show_songs(self):
        print(f"\nPlaylist '{self.name}':")
# Read songs from object and print
        for song in self.songs:
            print(f"- {song}")


# Creating object
my_playlist1 = Playlist("Favorites")


# List of songs
songs_list = [
    "Golden",
    "MIC Drop",
    "Tiny Light",
    "Skyfall",
    "April Shower",
    "Winter Bear",
    "Red",
    "God of light Music",
    "Mansae",
    "Pretty U"
]

# Adding songs into object using loop
for song in songs_list:
    my_playlist1.add_song(song)

# Removing  song
my_playlist1.remove_song("Red") # removed
my_playlist1.remove_song("Adore U") # not found in playlist
print()
# Display playlist
my_playlist1.show_songs()
