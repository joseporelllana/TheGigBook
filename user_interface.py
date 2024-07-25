from concert import Concert
from gigbook import GigBook

class UserInterface:
    concerts = []

    @staticmethod
    def startUpPage():
        print("""
    Hello, welcome to GigBook!
    ~~~~~~~Show Your Shows~~~~~~~
    Have You Set Up Your Book Yet?
    ~~~~~~~[YES]~~~~[NO]~~~~~~~~~
        """)
        choice = input().strip().lower()
        if choice == "yes":
            UserInterface.selectionScreen()
        else:
            UserInterface.setupProcess()

    @staticmethod
    def setupProcess():
        print("""
              [GigBook]~~~~~Show Your Shows~~~
              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
               Let's track your fave tracks!
              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
              Name Your Gig Book:
        """)
        gigbook_name = input().strip()
        print("Owner of the Gig Book:")
        gigbook_owner = input().strip()
        gig_book = GigBook(gigbook_name, gigbook_owner)
        print(f"GigBook '{gig_book.name}' created for {gig_book.owner}!")
        UserInterface.selectionScreen()

    @staticmethod
    def selectionScreen():
        while True:
            print("""
            [GigBook]~~~~~Show Your Shows~~~
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            1. Add a Concert
            2. View All Concerts
            3. Exit
            """)
            choice = input("Choose an option: ").strip()
            if choice == "1":
                UserInterface.addConcert()
            elif choice == "2":
                UserInterface.viewConcerts()
            elif choice == "3":
                print("Exiting GigBook. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    @staticmethod
    def addConcert():
        print("Enter concert details:")
        name = input("Concert Name: ").strip()
        artist = input("Artist: ").strip()
        venue = input("Venue: ").strip()
        rating = float(input("Rating (0-5): ").strip())
        date = input("Date (YYYY-MM-DD): ").strip()
        concert = Concert(name, artist, venue, rating, date)
        UserInterface.concerts.append(concert)
        print(f"Concert '{concert.name}' by {concert.artist} added!")

    @staticmethod
    def viewConcerts():
        if not UserInterface.concerts:
            print("No concerts added yet.")
            return
        print("List of concerts:")
        for concert in UserInterface.concerts:
            print(f"{concert.name} by {concert.artist} at {concert.venue} on {concert.date} - Rating: {concert.rating}")

if __name__ == "__main__":
    UserInterface.startUpPage()
