# Imagine there’s a lemming currenly in each hole, and they’re all hungry. The lemmings in hole #3 and #5 don’t need to travel at all, but the other lemmings need to travel to find the nearest cafe:

# the lemming in hole #1 needs to travel 2m to hole #3

# the lemming in hole #2 needs to travel 1m to hole #3

# the lemming in hole #4 needs to travel 1m to hole #3 (or 1m to hole #5)

# the lemming in hole #6 needs to travel 1m to hole #5

# In this problem, you want to calculate the longest amount, in meters, any lemming needs to travel to get food. For this example, the answer would 2, since lemming in hole #1 needs to travel 2m to get to the nearest cafe.

# The Challenge
# You’ll be given two pieces of information:

# num_holes
# The number of holes

# cafes
# The indexes of those holes with food in them (note that these indexes are zero-based). This list is sorted, and a single hole will only appear at most once in it.

# You should return a single integer, for the maximum distance any of the lemmings need to travel.

# have res variable which will be furthest distance from cafes
# iterate through index len(num_holes)
# calculate the distance

def furthest_distance(num_holes, cafes):
    furthest = 0

    for hole in range(len(num_holes)):
         distance = min([abs(hole - cafe) for cafe in cafes])

         furthest = max(furthest, distance)
    
    return furthest

furthest_distance([1,2,3,4,5,6], [3,5])
