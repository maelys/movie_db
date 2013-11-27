import sqlite3
import movie

class DatabaseManager:
    
    CREATE_TABLE = "CREATE TABLE IF NOT EXISTS movies (id integer PRIMARY KEY AUTOINCREMENT, movie_name text, \
        movie_path text, imdb_link text, cover blob, summary text, \
        imdb_rating float, anaelle_rating float, seen integer);"
        
    INSERT_QUERY = "INSERT INTO movies (id, movie_name, movie_path, imdb_link, \
        cover, summary, imdb_rating, anaelle_rating, seen) \
        VALUES (?, ?, ?, ?, ?, ?, ?, ?,?);"

    conn = ''

    c = ''
  
    def connect(self):
        self.conn = sqlite3.connect('database.sqlite')
        self.c = self.conn.cursor()
        # encodage
        self.conn.text_factory = lambda x: unicode(x, "utf-8", "ignore")
        # Create table
        self.c.execute(self.CREATE_TABLE)
        self.conn.commit()
        
    def insert(self,insert_values):
        # Insert into table
        self.c.execute(self.INSERT_QUERY, insert_values)
        # Commit the changes
        self.conn.commit()

    def select_title(self):
        self.c.execute('SELECT movie_name FROM movies')
        titles = []
        while True:
            row = self.c.fetchone()
            if row == None:
                break
            title = row[0]
            titles.append(title)
        return titles

    def import_db(self):
        self.c.execute('SELECT* FROM movies')
        movies_list = []
        while True:
            row = self.c.fetchone()
	        if row == None:
                break
	        movie_path = row[2]
	        movie_name = row[1]
	        imdb_link = row[3]
	        #cover = row[4]
	        summary = row[5]
	        imdb_rating = row[6]
	        anaelle_rating = row[7]
	        seen = row[8]
            m = movie.Movie(movie_path,movie_name,imdb_link,cover,summary,imdb_rating,anaelle_rating,seen)
            movies_list.append(m)
        return movies_list

    def print_db(self):
        # Select all
        self.c.execute('SELECT* FROM movies')
        for row in self.c:
            print row

    def close(self):
        # Close the cursor
        self.conn.close()
