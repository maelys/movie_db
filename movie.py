class Movie(object):
     
    def __init__(self,movie_path, movie_name = None, imdb_link = None,\
        cover_url = None, summary = None, imdb_rating = 0, anaelle_rating = 0):
        self.movie_name = movie_name
        self.movie_path = movie_path
        self.imdb_link = imdb_link
        self.cover_url = cover_url
        self.summary = summary
        self.imdb_rating = imdb_rating
        self.anaelle_rating = anaelle_rating
       

    def __repr__(self):
        return "<movie_name: %s, movie_path: %s, imdb_link: %s, cover_url %s, summary: %s, imdb_rating: %d, anaelle_rating: %d >" % (self.movie_name, \
            self.movie_path, self.imdb_link, self.cover_url, self.summary, \
            self.imdb_rating,   self.anaelle_rating)
        
       
         
        
        
        
      