class Chess:
    def __init__(self, player, points):
        self.__player = player      # private attribute
        self.__points = points      # private attribute

    def info(self):                 # same method name as Racing
        print(f"Chess    — Player: {self.__player}, Points: {self.__points}")

    def play(self):                 # same method name, different output
        print(f"{self.__player} makes a brilliant checkmate!")

    def get_points(self):           # getter
        return self.__points

    def set_points(self, new_points):  # setter
        if new_points >= 0:
            self.__points = new_points
            print(f"Points updated to {self.__points}")
        else:
            print("Points cannot be negative.")


class Racing:
    def __init__(self, driver, points):
        self.__driver = driver
        self.__points = points

    def info(self):                 # same name, different output
        print(f"Racing   — Driver: {self.__driver}, Points: {self.__points}")

    def play(self):                 # same name, different behaviour
        print(f"{self.__driver} speeds across the finish line!")

    def get_points(self):
        return self.__points

    def set_points(self, new_points):
        if new_points >= 0:
            self.__points = new_points
            print(f"Points updated to {self.__points}")
        else:
            print("Points cannot be negative.")


# Create objects
chess = Chess("Sophia", 120)
racing = Racing("Lewis", 75)

# Polymorphism — same method, different behaviour
print("=== Gaming & Racing Leaderboard ===\n")
for game in (chess, racing):
    game.info()
    game.play()
    print()

# Encapsulation — direct change does NOT work
print("--- Direct update attempt ---")
chess.__points = 999
print(f"get_points() still shows: {chess.get_points()}")

# Setter — safe update
print("\n--- Updating points ---")
chess.set_points(150)
racing.set_points(90)