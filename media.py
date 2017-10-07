class Movie():
    """
    This class provides a way to store movie related information

    Attributes:
        title (string): title of the movie
        storyline (string): synopsis of the movie's plot
        poster_image_url (string): URL of the movie's poster
        trailer_youtube_url (string): URL of the movie's trailer on YouTube
    """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube_id):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_id = trailer_youtube_id
