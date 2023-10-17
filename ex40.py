#Making a song class
class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you"],
                  ["Happy birthday to you"],
                  ["Happy Birthday Dear (name)"],
                  ["Happy birthday to you"])

happy_bday.sing_me_a_song()
