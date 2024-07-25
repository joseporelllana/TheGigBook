class Concert:
    """
    Represents a concert.

    Attributes:
        name (str): The name of the concert.
        artist (str): The artist performing at the concert.
        venue (str): The venue of the concert.
        rating (float): The rating of the concert.
        date (str): The date of the concert.
    """
    def __init__(self, name, artist, venue, rating, date):
        self.name = name
        self.artist = artist
        self.venue = venue
        self.rating = rating
        self.date = date