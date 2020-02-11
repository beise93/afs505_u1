class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])
#study drill 1 adding more lyrics and songs
old_black_hen = Song(["Old Black Hen is that you again",
                    "Singing the Bad Luck Lullaby",
                    "Come right on in, it's midnight again"])

streets_no_name = Song(["I want to run, I want to hide",
                        "I want to tear down the walls that hold me inside",
                        "I wanna reach out and touch the flame"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

old_black_hen.sing_me_a_song()

streets_no_name.sing_me_a_song()

#study drill 2, putting lyrics to a variable, then passing that to the class

girlfriend_coma_lyrics = ["Girlfriend in a coma", "I know I know, it's serious"]

girlfriend_coma = Song(girlfriend_coma_lyrics)
girlfriend_coma.sing_me_a_song()
