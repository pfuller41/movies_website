import fresh_tomatoes
import media

apocalypse_now = media.Movie("Apocalypse Now",\
							 "Francis Ford Coppola",\
	 						 "https://upload.wikimedia.org/wikipedia/en/thumb/c/c2/Apocalypse_Now_poster.jpg/220px-Apocalypse_Now_poster.jpg",\
	  						 "https://www.youtube.com/watch?v=IkrhkUeDCdQ")

raging_bull = media.Movie("Raging Bull",\
						  "Martin Scorsese",\
						  "https://upload.wikimedia.org/wikipedia/en/thumb/5/5f/Raging_Bull_poster.jpg/220px-Raging_Bull_poster.jpg",\
						  "https://www.youtube.com/watch?v=PVMnl4sBl8A")

the_deer_hunter = media.Movie("The Deer Hunter",\
							  "Michael Cimino",\
							  "https://upload.wikimedia.org/wikipedia/en/thumb/5/57/The_Deer_Hunter_poster.jpg/220px-The_Deer_Hunter_poster.jpg",\
							  "https://www.youtube.com/watch?v=SKHZ5-JThFE")

the_silence_of_the_lambs = media.Movie("The Silence of the Lambs",\
 									   "Jonathan Demme",\
 									   "https://upload.wikimedia.org/wikipedia/en/8/86/The_Silence_of_the_Lambs_poster.jpg",\
 									   "https://www.youtube.com/watch?v=Lr3OavheNu0")

the_godfather = media.Movie("The Godfather",\
 							"Francis Ford Coppola",\
 							"https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",\
 							"https://www.youtube.com/watch?v=l6KNrO86UnE")

a_clockwork_orange = media.Movie("A Clockwork Orange",\
 								 "Stanley Kubrick",\
 								 "https://upload.wikimedia.org/wikipedia/en/thumb/4/48/Clockwork_orangeA.jpg/220px-Clockwork_orangeA.jpg",\
 								 "https://www.youtube.com/watch?v=9JIc_1v7i88")

movies = [apocalypse_now, raging_bull, the_deer_hunter, the_silence_of_the_lambs, the_godfather, a_clockwork_orange]
fresh_tomatoes.open_movies_page(movies)
