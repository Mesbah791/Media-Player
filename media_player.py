from abc import ABC, abstractmethod

class Description(ABC): 
    def __init__(self, description):
        self.__description = description

    def get_description(self):
        return self.__description

class Media(ABC):
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    @abstractmethod
    def play(self):
        pass 

class Music(Media, Description):
    def __init__(self,title,duration, description):
        Media.__init__(self,title, duration)
        Description.__init__(self, description)
    
    def play(self):
        print(f"title : {self.title}")

    def info(self):
        print(f"Playing : {self.title} duration : { self.duration} description : {self.get_description()}")  # Fix 3: Call get_description()

class Video(Media, Description):
    def __init__(self,title,duration, description):
        Media.__init__(self,title, duration)
        Description.__init__(self, description)
    
    def play(self):
        print(f"title : {self.title}")

    def info(self):
        print(f"Playing : {self.title} duration : { self.duration} description : {self.get_description()}")  # Fix 3: Call get_description()

class Audio_Book(Media, Description):
    def __init__(self,title,duration, description):
        Media.__init__(self,title, duration)
        Description.__init__(self, description)
    
    def play(self):
        print(f"title : {self.title}")

    def info(self):
        print(f"Playing : {self.title} duration : { self.duration} description : {self.get_description()}")  # Fix 3: Call get_description()

class Library:
    def __init__(self):
        self.__media_items  = []
        self.__media_by_genre = {}
        self.__genre = ""

    def get_media_items(self):
        return self.__media_items
    
    def get_media_by_genre(self):
        return self.__media_by_genre  

    def add_media(self, media):
        if isinstance(media, Music):
            self.__genre ="Music"
        if isinstance(media, Video):
            self.__genre = "Video"
        if isinstance(media, Audio_Book):
            self.__genre = "audiobook"
        ##ki jeno hobe##

        if self.__genre in self.__media_by_genre:
            self.__media_by_genre[self.__genre].append(media)
        else:
            self.__media_by_genre[self.__genre] = [media,]

class User(ABC):
    def __init__(self, name):
        self.__name = name
    
    @abstractmethod
    def play_media(self):
        pass

class FreeUser(User):
    def __init__(self, name):
        super().__init__(name)
    
    def play_media(self, library):
        for media in library.get_media_items():
            media.play()

class PremiumUser(User):
    def __init__(self, name):
        super().__init__(name)
        self.__favourite_genre = ""
    
    def set_favourite_genre(self, genre):
        self.__favourite_genre = genre  

    def play_media(self, library):
        if self.__favourite_genre in library.get_media_by_genre():
            for media in library.get_media_by_genre()[self.__favourite_genre]:
                media.play()

# Testing the code
music1 = Music("Song Title 1", "3:30", "A great song")
video1 = Video("Video Title 1", "5:00", "An interesting video")
audio_book1 = Audio_Book("Book Title 1", "7:00", "A fascinating book")

library = Library()
library.add_media(music1)
library.add_media(video1)
library.add_media(audio_book1)

free_user = FreeUser("John")
free_user.play_media(library)

premium_user = PremiumUser("Alice")
premium_user.set_favourite_genre("Music")
premium_user.play_media(library)
