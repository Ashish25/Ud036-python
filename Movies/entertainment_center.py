import media

import tomatoes

Fury = media.Movie("Fury",
                    "A grizzled tank commander makes tough decisions as he and his crew fight their way across Germany in April, 1945.",
                     "https://upload.wikimedia.org/wikipedia/en/1/17/Fury_2014_poster.jpg",
                     "https://www.youtube.com/watch?v=-OGvZoIrXpg")

Avatar = media.Movie("Avatar",
                     "Jake, a paraplegic marine, replaces his brother on the Na'vi inhabited Pandora for a corporate mission. He is accepted by the natives as one of their own but he must decide where his loyalties lie.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

#Avatar.show_trailer()

Fences = media.Movie("Fences 2016",
                     "A working-class African-American father tries to raise his family in the 1950s",
                     "https://upload.wikimedia.org/wikipedia/en/0/0d/Fences_%28film%29.png",
                     "https://www.youtube.com/watch?v=jj-ZYPVRQbc")
#Fences.show_trailer()

School_of_rock = media.Movie("School of Rock",
                             "Dewey Finn becomes a substitute teacher of a strict elementary private school, only to try and turn it into a rock",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

The_red_turtle = media.Movie("The red turtle",
                             "story of a man shipwrecked on a tropical island inhabited by turtles, crabs and birds",
                             "https://upload.wikimedia.org/wikipedia/en/f/fe/The_Red_Turtle.png",
                             "https://www.youtube.com/watch?v=Sw7BggqBpTk")

Deadpool = media.Movie("Deapool",
                       "former Special Forces operative who now works as a mercenary",
                       "https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg",
                       "https://www.youtube.com/watch?v=9vN6DHB6bJc")


movies = [Fury, Avatar, Fences, School_of_rock, The_red_turtle, Deadpool]
#tomatoes.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)

print(media.Movie.__doc__)
