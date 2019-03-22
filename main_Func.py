"""
This is virtual song only for the Exercise
written by Eyal Lev
Date March 21st 2019
"""

Name = "My First Exercise"                          # The name of the song
Artist = "Jhon Martin"                               # The Name of the Artist
Genre = "Eastern"
Year = 1963

SongNumbeOfWords = 97                                  # The Number of Word in the Song
NumberOfDifferentWords = 72                            # The Number of different Words
SongPlayDuration = 4.36                                # Song Play duration
NumberOfKids= 4                                        # Author number of kids
FirstSon, SecondDaughter, ThirdDaughter, YoungestSon = "Gim", "Shelly", "Rebeca", "Mark"      # Author kids name
AuthorEifeName= "Lisa"


def parameterisnotone(parameter):
    return parameter != "None"


def genre():
    return Genre


def artist():
    return Artist


def year():
    return Year


if parameterisnotone(Genre):
    print (genre())
else:
    print ("There in no definition of the Genre")


if parameterisnotone(Artist):
    print (artist())
else:
    print ("There in no definition of the Artist")


if parameterisnotone(Year):
    print (year())
else:
    print ("There in no definition of the Year")



