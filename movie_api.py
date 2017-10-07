import requests
import json
import config
import media


def get_trailer(movie_id):
    """
    Fetches the movie's YouTube trailer key

    Attributes:
        movie_id (str or int):
            ID from TheMovieDB.org of the movie to get the trailer of
    """

    trailer_access_url = ("http://api.themoviedb.org/3/movie/{movie}/videos?"
                          "api_key={api_key}").format(
                              movie=str(movie_id),
                              api_key=config.themoviedb_v3_api_key)

    # Request movie info from TheMovieDB API
    response = requests.request("GET", trailer_access_url).json()
    trailer = response.get('results')[0]

    # Return the YouTube key if the trailer is on YouTube
    # Otherwise error.
    if(trailer.get('site') == "YouTube"):
        return trailer.get('key')
    else:
        return "Error"


def get_movie_list(list_id, movie_array):
    """
    Fetches the list provided and creates an array of Movies from it

    Attributes:
        list_id (str or int): numerical ID number of a list at TheMovieDB.org
        movie_array (array): an array to hold the Movie objects
    """

    # Image paths will need this prepended
    image_url_pre = "https://image.tmdb.org/t/p/w500"

    # YouTube key will need this prepended
    youtube_url_pre = "https://www.youtube.com/watch?v="

    list_access_url = (
        "https://api.themoviedb.org/3/list/{list}?api_key={api_key}"
        "&language=en-US").format(list=str(list_id),
                                  api_key=config.themoviedb_v3_api_key)

    # Request list from TheMovieDB API
    response = requests.request("GET", list_access_url).json()
    movies = response.get('items')

    # Adds each movie in the list to the array provided
    for item in movies:
        movie_array.append(media.Movie(item.get('title'),
                                       item.get('overview'),
                                       image_url_pre + item.get('poster_path'),
                                       youtube_url_pre + get_trailer(item.get('id'))))
