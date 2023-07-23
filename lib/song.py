class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self , name , artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genre(self.genre)
        self.add_to_artist(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(total):
        total.count += 1
    
    @classmethod 
    def add_to_genre(total, genre):
        if genre != total.genres:
            total.genres.append(genre)

    @classmethod 
    def add_to_artist(total,artist):
        if artist != total.artists:
            total.artists.append(artist)  


    @classmethod
    def add_to_genre_count(total, genre):
        if total.genre_count.get(genre):
            total.genre_count[genre] += 1
        else:
            total.genre_count[genre] = 1         

    @classmethod
    def add_to_artist_count(total, artist):
        if total.artist_count.get(artist):
            total.artist_count[artist] += 1
        else:
            total.artist_count[artist] = 1        