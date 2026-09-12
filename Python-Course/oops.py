class Camera:
    def take_photo(self):
        print("Taking a photo...")

class musicPlayer:
    def play_music(self):
        print("Playing music...")

class smartPhone2(Camera, musicPlayer):
    pass

sp2 = smartPhone2()
sp2.take_photo()
sp2.play_music()