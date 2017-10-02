import media
import fresh_tomatoes

toyStory = media.Movie("Toy Story",
                       "A story of a boy and his toys that come to life.",
                       "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                       "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=a0CDJZu4M5I")

yourSistersSister = media.Movie("Your Sister's Sister",
                                "Iris invites her friend Jack to stay at her family's island getaway after the death of his brother. At their remote cabin, Jack's drunken encounter with Hannah, Iris' sister, kicks off a revealing stretch of days.",
                                "https://upload.wikimedia.org/wikipedia/en/6/67/Your_Sister%27s_Sister_poster.jpg",
                                "https://www.youtube.com/watch?v=l0mmrBfIc4s")

ratatouille = media.Movie("Ratatouille",
                          "A rat who can cook makes an unusual alliance with a young kitchen worker at a famous restaurant.",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnightInParis = media.Movie("Midnight in Paris",
                          "While on a trip to Paris with his fiancée's family, a nostalgic screenwriter finds himself mysteriously going back to the 1920s everyday at midnight.",
                          "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                          "https://www.youtube.com/watch?v=FAfR8omt-CY")

hungerGames = media.Movie("The Hunger Games",
                          "Katniss Everdeen voluntarily takes her younger sister's place in the Hunger Games: a televised competition in which two teenagers from each of the twelve Districts of Panem are chosen at random to fight to the death.",
                          "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                          "https://www.youtube.com/watch?v=mfmrPu43DF8")

movies = [toyStory, avatar, yourSistersSister, ratatouille, midnightInParis, hungerGames]
fresh_tomatoes.open_movies_page(movies)

