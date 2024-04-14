import pandas as pd
import random
import matplotlib.pyplot as plt

def calculate_route_distance(distances, route):
    total_distance = 0
    for i in range(len(route)):
        total_distance += distances[route[i]][route[(i + 1) % len(route)]]
    return total_distance

def hill_climbing(distances, max_iterations):
    # Generate a random initial route
    route = list(range(len(distances)))
    random.shuffle(route)
    best_route = route.copy()
    best_distance = calculate_route_distance(distances, best_route)

    for _ in range(max_iterations):
        # Explore neighboring routes by swapping two randomly chosen places
        i, j = random.sample(range(len(route)), 2)
        neighbor_route = route.copy()
        neighbor_route[i], neighbor_route[j] = neighbor_route[j], neighbor_route[i]
        neighbor_distance = calculate_route_distance(distances, neighbor_route)

        if neighbor_distance < best_distance:
            best_route = neighbor_route.copy()
            best_distance = neighbor_distance
            route = neighbor_route

    return best_route, best_distance

def visualize_results(distances, best_route):
    cities = [f"City {i+1}" for i in range(len(distances))]
    df_distances = pd.DataFrame(distances, index=cities, columns=cities)

    # Create a DataFrame for the best route
    route_df = pd.DataFrame(columns=["From", "To", "Distance"])
    for i in range(len(best_route)):
        from_city = cities[best_route[i]]
        to_city = cities[best_route[(i + 1) % len(best_route)]]
        distance = distances[best_route[i]][best_route[(i + 1) % len(best_route)]]
        route_df.loc[i] = [from_city, to_city, distance]

    # Visualize the distances between cities
    plt.figure(figsize=(10, 8))
    plt.imshow(df_distances, cmap="YlOrRd")
    plt.colorbar()
    plt.xticks(range(len(cities)), cities, rotation=90)
    plt.yticks(range(len(cities)), cities)
    plt.title("Distances between cities")
    plt.show()

    # Visualize the best route
    plt.figure(figsize=(10, 8))
    colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
    for i, (from_city, to_city, _) in enumerate(zip(route_df["From"], route_df["To"], route_df["Distance"])):
        plt.bar(from_city, route_df["Distance"][i], color=colors[i % len(colors)])
    plt.xticks(rotation=90)
    plt.xlabel("From")
    plt.ylabel("Distance")
    plt.title("Best route")
    plt.show()

# Example usage
distances = [
    [0, 7, 20, 15, 12],
    [10, 0, 6, 14, 18],
    [20, 6, 0, 15, 30],
    [15, 14, 25, 0, 2],
    [12, 18, 30, 2, 0]
]

max_iterations = 1000
best_route, best_distance = hill_climbing(distances, max_iterations)
visualize_results(distances, best_route)
print("Best distance:", best_distance)