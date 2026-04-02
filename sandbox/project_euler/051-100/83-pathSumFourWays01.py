################################################################################
# In the 5 by 5 matrix below, the minimal path sum from the top left to the
# bottom right, by moving left, right, up, and down, is indicated in bold red
# and is equal to 2297.
#
#     (131  673  234  103   18
#      201   96  342  965  150
#      630  803  746  422  111
#      537  699  497  121  956
#      805  732  524   37  331)
#
# Find the minimal path sum from the top left to the bottom right
# by only moving right and down in matrix.txt
# filename:  83=matrix.txt
################################################################################
import heapq
################################################################################
def parse(matfile):
    return [[int(n) for n in row.split(',')] for row in matfile]
################################################################################
def distance(a, b):
    return sum(abs(a[i] - b[i]) for i in range(len(a)))
################################################################################
def astar(matrix, targets, sources):
    def neighbors(position):
        (x, y) = position
        candidates = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        return [(x, y) for (x, y) in candidates if x >= 0 and x < len(matrix)
                                               and y >= 0 and y < len(matrix[0])]
    def evaluate(path):
        f = sum(matrix[y][x] for (x, y) in path)
        h = min(distance(path[-1], target) for target in targets)
        return f + h

    targets = set(targets)
    frontier = set(sources)
    explored = set()
    frontier_queue = []
    for source in sources:
        path = [source]
        heapq.heappush(frontier_queue, (evaluate(path), path))

    while frontier:
        (_, path) = heapq.heappop(frontier_queue)
        frontier.remove(path[-1])
        explored.add(path[-1])
        if path[-1] in targets:
            return path
        for neighbor in neighbors(path[-1]):
            if neighbor not in frontier | explored:
                frontier.add(neighbor)
                new_path = path + [neighbor]
                heapq.heappush(frontier_queue, (evaluate(new_path), new_path))
################################################################################
def main():
    with open('83-matrix.csv') as matfile:
        matrix = parse(matfile)
    targets = [(len(matrix) - 1, len(matrix[0]) - 1)]
    sources = [(0, 0)]
    print(sum(matrix[y][x] for (x, y) in astar(matrix, targets, sources)))
################################################################################
main()
################################################################################
#solution: 425185
################################################################################
