import sqlite3

class DatabaseManager:
    
    CREATE_TABLE = "CREATE TABLE IF NOT EXISTS movies (movie_name PRIMARY KEY \
        text, movie_path text, imdb_link text, cover_url text, summary text \
        imdb_rating int, anaelle_rating int);"
        
    INSERT_QUERY = "INSERT INTO movies (movie_name, movie_path, imdb_link, \
        cover_url, summary, imdb_rating, anaelle_rating) \
        VALUES (?, ?, ?, ?, ?, ?, ?);"

    conn = ''

    c = ''
  
    def connect(self):
        self.conn = sqlite3.connect('database.sqlite')
        self.c = self.conn.cursor()
        # Create table
        self.c.execute(self.CREATE_TABLE)
        self.conn.commit()
        
    def insert(self,insert_values):
        # Insert into table
        self.c.execute(self.INSERT_QUERY, insert_values)
        # Commit the changes
        self.conn.commit()

    def print_db(self):
        # Select all
        self.c.execute('SELECT* FROM movies')
        for row in self.c:
            print row

    def close(self):
        # Close the cursor
        self.conn.close()