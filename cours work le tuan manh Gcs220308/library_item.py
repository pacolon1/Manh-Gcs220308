class LibraryItem:
    def __init__(self, name, singer, rating, season, mp3_file):
        self.name = name
        self.singer = singer
        self.rating = rating
        self.season = season
        self.mp3_file = mp3_file
        self.play_count = 0

    def info(self):
        return f"{self.name} by {self.singer} - Rating: {self.rating}, Season: {self.season}, Plays: {self.play_count}"

    def stars(self):
        stars = ""
        for i in range(self.rating):
            stars += "*"
        return stars
