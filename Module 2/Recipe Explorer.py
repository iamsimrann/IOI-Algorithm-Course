# ---- Movie Collection Explorer ----

# STEP 1 - Create tuples for movie details (fixed — cannot be changed)
movie1 = ("Inception", "Sci-Fi", 148, "PG-13")
movie2 = ("The Lion King", "Animation", 88, "G")

print("Movie 1:", movie1)
print("Title:", movie1[0])
print("Genre:", movie1[1])
print("Rating:", movie1[-1])

# STEP 2 - Nested tuples and slicing
all_movies = (movie1, movie2)

print("\nFirst movie title:", all_movies[0][0])
print("Second movie duration:", all_movies[1][2], "minutes")
print("Movie 1 details (sliced):", movie1[1:3])

# STEP 3 - Iterate through a tuple
print("\nMovie 1 Details:")
for detail in movie1:
    print(" -", detail)

# STEP 4 - Create sets for movie features (no duplicates allowed)
movie1_features = {"action", "dreams", "thriller", "mystery", "action"}
movie2_features = {"animation", "adventure", "family", "music", "dreams"}

print("\nMovie 1 features:", movie1_features)
print("Movie 2 features:", movie2_features)
print("Total Movie 1 features:", len(movie1_features))

# STEP 5 - Modify the set
movie1_features.add("science fiction")
movie1_features.discard("mystery")

print("\nUpdated Movie 1 features:", movie1_features)

# STEP 6 - Set operations
all_features = movie1_features.union(movie2_features)
common_features = movie1_features.intersection(movie2_features)
only_movie1 = movie1_features.difference(movie2_features)
unique_features = movie1_features.symmetric_difference(movie2_features)

print("\nAll features (union):", all_features)
print("Shared features (intersection):", common_features)
print("Only in Movie 1 (difference):", only_movie1)
print("Unique to each movie (sym. difference):", unique_features)