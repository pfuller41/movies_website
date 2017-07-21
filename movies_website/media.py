import webbrowser
class Movie (): #class allows us to make classes, like a blueprint, it can have data and methods
	"""This class provides a way to store movie related information"""
	VALID_RATINGS = ("G", "PG", "PG-13", "R")
	def __init__(self, movie_title, movie_director, poster_image, trailer_youtube): #init is a constructor, calls all the data, self is keyword(instance in question toy_story etc.)
		self.title = movie_title
		self.director = movie_director
		self.poster_image_url = poster_image  #all variables associated with a class, these 4 are instance variables, unique to an object, accessed with self inside class and instance name outside of class
		self.trailer_youtube_url = trailer_youtube
	def show_trailer(self): # function all functions inside a class associated with an instance and have post argument as self are called instance methods
		webbrowser.open(self.trailer_youtube_url)