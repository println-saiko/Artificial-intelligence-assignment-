import random
import matplotlib.pyplot as plt
from typing import List, Tuple

def generate_random_route(num_places: int) -> List[int]:
    """
    Generate a random initial route visiting all places.

    Args:
        num_places (int): The number of places to visit.

    Returns:
        List[int]: The initial route.2
    """
    route = list(range(num_places))
    random.shuffle(route)
    return route

def explore_neighbors(route: List[int]) -> List[int]:
    """
    Explore neighboring solutions by swapping the order of two randomly chosen places in the current route.

    Args:
        route (List[int]): The current route.

    Returns:
        List[int]: The neighboring route.
    """
    i, j = random.sample(range(len(route)), 2)
    neighbor_route = route.copy()
    neighbor_route[i], neighbor_route[j] = neighbor_route[j], neighbor_route[i]
    return neighbor_route

def calculate_route_distance(distances: List[List[int]], route: List[int]) -> int:
    """
    Calculate the total distance of a given route.

    Args:
        distances (List[List[int]]): The distance matrix.
        route (List[int]): The route to calculate the distance for.

    Returns:
        int: The total distance of the route.
    """
    total_distance = 0
    for i in range(len(route)):
        total_distance += distances[route[i]][route[(i + 1) % len(route)]]
    return total_distance

def hill_climbing(distances: List[List[int]], max_iterations: int = 1000) -> Tuple[List[int], int]:
    """
    Implement the core logic of the Hill Climbing algorithm for the Traveling Salesman Problem.

    Args:
        distances (List[List[int]]): The distance matrix, where distances[i][j] is the distance between places i and j.
        max_iterations (int): Maximum number of iterations to perform.

    Returns:
        Tuple[List[int], int]: The best route found and the total distance of the best route.
    """
    num_places = len(distances)
    best_route = generate_random_route(num_places)
    best_distance = calculate_route_distance(distances, best_route)

    for _ in range(max_iterations):
        neighbor_route = explore_neighbors(best_route)
        neighbor_distance = calculate_route_distance(distances, neighbor_route)

        if neighbor_distance < best_distance:
            best_route = neighbor_route.copy()
            best_distance = neighbor_distance
        else:
            break  # No better neighbor found, terminate

    return best_route, best_distance

def visualize_results(distances: List[List[int]], best_route: List[int]) -> None:
    """
    Visualize the results of the Hill Climbing algorithm.

    Args:
        distances (List[List[int]]): The distance matrix.
        best_route (List[int]): The best route found.
    """
    cities = [f"City {i+1}" for i in range(len(distances))]

    # Plot the distances between cities
    plt.figure(figsize=(10, 8))
    plt.imshow(distances, cmap="YlOrRd")
    plt.colorbar()
    plt.xticks(range(len(cities)), cities, rotation=90)
    plt.yticks(range(len(cities)), cities)
    plt.title("Distances between cities")
    plt.show()

    # Plot the best route
    plt.figure(figsize=(10, 8))
    x = [cities[i] for i in best_route]
    y = [calculate_route_distance(distances, best_route[:i+1]) for i in range(len(best_route))]
    plt.plot(x, y)
    plt.xticks(rotation=90)
    plt.xlabel("City")
    plt.ylabel("Distance")
    plt.title("Best route")
    plt.show()

# Example usage
distances = [
    [0, 7, 20, 15, 12],
    [7, 0, 6, 14, 18],
    [20, 6, 0, 15, 30],
    [15, 14, 15, 0, 2],
    [12, 18, 30, 2, 0]
]

best_route, best_distance = hill_climbing(distances)
print(f"Best route: {best_route}")
print(f"Best distance: {best_distance}")
visualize_results(distances, best_route)
