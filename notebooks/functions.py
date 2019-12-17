# this file is to create all the functions needed for the project, 
# so I keep the notebooks clear.


# A FUNCTION TO APPLY THE MLROSE ALGORITHM
def best_route(dist_list):
    """
    This function applies the MLROSE Algorithm to find the best route for a number of 
    points. It is an approximation to the Travelling Salesman Problem.

    Input: A list of triplets with indexes for the cities and the distance between them.
    Output: An array with the best order of the cities and the route distance.

    Example:

    Input: [(0, 1, 906.0416003864943),
            (0, 2, 709.20506184732),
            (0, 3, 576.0433647759187),
            (1, 2, 213.3824218268996),
            (1, 3, 335.7240942715326),
            (2, 3, 179.43584263435042)
    
    Output: (array([3, 1, 2, 0]), 1834)
    """
    
    import math
    import mlrose
    
    # Initialize fitness function object using coords_sub0
    fitness_coords = mlrose.TravellingSales(distances = dist_list)
    
    # Calculating the number of circuits depending on the number of distances in list
    # The num of distances is equal to n * (n-1) / 2, being n the number of circuits.
    # we want to find n having the num of distances, this is a quadratic function:
    # x**2 - x - 2y = 0, being x = n and y = num of distances.
    # Solving the equation with math library:
    
    a = 1
    b = -1
    c = -2*len(dist_list)
    # calculate the discriminant
    d = (b**2) - (4*a*c)
    # find two solutions
    sol1 = (-b-math.sqrt(d))/(2*a)
    sol2 = (-b+math.sqrt(d))/(2*a)
    
    # assigning the positive solution to length, needed for the algorithm
    length = max(sol1, sol2)
    
    # Define optimization problem object
    problem_fit = mlrose.TSPOpt(length = length, fitness_fn = fitness_coords, 
                                maximize = False)
    
    # Solve using genetic algorithm - attempt 1
    best_order_1, best_distance_1 = mlrose.genetic_alg(problem_fit, random_state = 2)
    
    # Solve using genetic algorithm - attempt 2
    best_order_2, best_distance_2 = mlrose.genetic_alg(problem_fit, mutation_prob = 0.2, 
                                                  max_attempts = 100, random_state = 2)
    
    if best_distance_1 < best_distance_2:
        return best_order_1, round(best_distance_1)
    else:
        return best_order_2, round(best_distance_2)

 
# FUNCTIONS TO REORDER THE ROUTE DEPENDING ON LAST OR FIRST CIRCUIT

def reordering_last(array, index):
    """
    This function checks the position of one index in a non-ordered array and returns
    the array with the passed index in last position

    Input: array, index
    Output: reordered array

    Example: 
    Input: array([3, 1, 2, 0] , 2
    Output: array([0, 3, 1, 2]
    """
    import numpy as np  
    position = int(np.where(array == index)[0]) + 1
    return np.roll(array, len(array)-position)

def reordering_first(array, index):
    """
    This function checks the position of one index in a non-ordered array and returns
    the array with the passed index in first position

    Input: array, index
    Output: reordered array

    Example: 
    Input: array([3, 1, 2, 0] , 2
    Output: array([2, 0, 3, 1]
    """
    position = int(np.where(array == index)[0])
    return np.roll(array, -position)


# A FUNCTION TO SUBTRACT DISTANCES TO GET 'OPENED ROUTES'
def to_subtract(array, dist_list):
    """
    Given an array and a dist list, this function returns de distance between first
    and last element of the array. This distance can then be subtracted for the 
    previously calculated distance for a round route, to get an opened route.
    """
    for el in dist_list:
        if el[0] == array[0] and el[1] == array[-1]:
            return el[2]
        elif el[0] == array[-1] and el[1] == array[0]:
            return el[2]


# A FUNCTION TO CREATE DISTANCE LISTS AS REQUIRED FOR THE ALGORITHM
def create_dist_list(df, clusters_list):
    """
    Given an array and a list of clusters (labels), this function returns a dictionary with 
    the labels as keys and a dist list in the proper format to be passed into the MLROSE 
    algorithm as values: a triplet with index of city 1, index of citiy 2, distance between them.
    """
    from geopy import distance
    cluster_dict = {}
    for cluster in clusters_list:
        subcluster = df.loc[df['Subcluster']==cluster].reset_index(drop=True)
        dist_list = []
        for i in subcluster.index:
            for j in subcluster.index:
                if i < j: 
                    coord_i = (subcluster.loc[i,'Latitude'],subcluster.loc[i,'Longitude'])
                    coord_j = (subcluster.loc[j,'Latitude'],subcluster.loc[j,'Longitude'])

                    dist = distance.distance(coord_i, coord_j).km
                    dist_list.append((i, j, dist))
        cluster_dict[cluster] = dist_list
    return cluster_dict