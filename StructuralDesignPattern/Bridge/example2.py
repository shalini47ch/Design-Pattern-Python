#Here we will create a separate abstraction and implementation 
class MusicPlayer:
    def __init__(self,implementation):
        self.implementation=implementation
        
    def play(self,song):
        #here this will act as a bridge
        self.implementation.play_song(song)
    
#we will create implementation for spotify and apple music
class MusicPlayerImplementation:
    def play_song(self,song):
        pass
#now we will create for spotify and applemusic
class AppleMusic(MusicPlayerImplementation):
    def play_song(self,song):
        print("Playing {} on Apple Music".format(song))
        
#similarly do it for spotify

class Spotify(MusicPlayerImplementation):
    def play_song(self,song):
        print("Playing {} on Spotify Music".format(song))
        
spotify_player=MusicPlayer(Spotify())
spotify_player.play("Perfect")

apple_player=MusicPlayer(AppleMusic())
apple_player.play("Cheap Thrills")



        

        
