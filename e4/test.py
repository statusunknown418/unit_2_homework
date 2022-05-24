from faker import Faker

from Movie import Movie
from Spectator import Spectator
from Theater import Theater

# Very useful library heavily used in Web Development (my area of expertise with Typescript) to simulate random real data
fake = Faker()

# Simulate a populated theater
theater = Theater(Movie("The Matrix", "Wachowski", 1999, 18), 10)

spectators = [Spectator(name=fake.name(),
                        age=fake.random_int(18, 60),
                        available_cash=fake.random_int(100, 1000)) for _ in range(int(input("Simulation size: ")))]


def simulate_spectator_arriving(theater: Theater, spectator: Spectator):
    if theater.current_movie.minimum_age > spectator.age:
        print(f"{spectator.name} is too young to watch {theater.current_movie}")
        return

    if theater.get_available_seats() == 0:
        print(f"{theater.current_movie} is sold out")
        return

    if spectator.available_cash < theater.ticket_price:
        print(f"{spectator.name} can't afford {theater.current_movie}")
        return


def simulate_spectator_taking_random_seat(theater: Theater, spectator: Spectator):
    # Get a random seat
    row = theater.seats.shape[0]
    col = theater.seats.shape[1]
    seat = (fake.random_int(0, row - 1), fake.random_int(0, col - 1))

    # Check if seat is available
    if theater.seats[seat] == True:
        print("Another spectator is already here, looking for another seat")
        simulate_spectator_arriving(theater, spectator)
        return

    theater.seats[seat] = True
    spectator.available_cash -= theater.ticket_price
    print(f"{spectator.name} has bought a seat at {seat}")


if __name__ == "__main__":
    for spectator in spectators:
        simulate_spectator_arriving(theater, spectator)
        simulate_spectator_taking_random_seat(theater, spectator)

    print(
        f"Final distribution after simulation:\n{theater.get_distribution_of_seats()}")
