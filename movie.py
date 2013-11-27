# -*- coding: utf-8 -*-
class Movie(object):
     
    def __init__(self,movie_path, movie_name = None, imdb_link = None,\
        cover = None, summary = None, imdb_rating = 0, anaelle_rating = 0, \
        seen = False):
        self.movie_name = movie_name
        self.movie_path = movie_path
        self.imdb_link = imdb_link
        self.cover = cover_url
        self.summary = summary
        self.imdb_rating = imdb_rating
        self.anaelle_rating = anaelle_rating
        self.seen = seen
       

    def __repr__(self):
        return "<movie_name: %s, movie_path: %s, imdb_link: %s, cover %s, summary: %s, imdb_rating: %.1f, anaelle_rating: %d, seen: %r>" \
        % (self.movie_name, self.movie_path, self.imdb_link, self.cover, \
        self.summary, self.imdb_rating, self.anaelle_rating, self.seen)
        
    def __str__(self):
       return "movie_name: %s \n movie_path: %s \n imdb_link: %s \n cover %s \n summary: %s \n imdb_rating: %.1f \n anaelle_rating: %d \n seen: %r \n ---------------------------------------------" \
       % (self.movie_name, self.movie_path, self.imdb_link, self.cover, \
       self.summary, self.imdb_rating, self.anaelle_rating, self.seen)
         
        
        
        
      
