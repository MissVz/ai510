# CS 622 PE 10 BFS & Recursion by VElze
from collections import deque 

class IslandCounterClass:
  # Count number of islands in grid


  def __init__(self, grid):
    # Initialize grid

    """ Parameters
    ----------
    grid : 2d-array
        Land = 1
        Water = 0
    """
    self.grid = grid
    
    # Initialize visited matrix, set all Not Visited = 0
    self.visited = [['0' for x in range(len(grid[0]))] for y in range(len(grid))]
  

  def print_grid_visited(self):
    """ Print grids
    """
    print("Map:")
    # Tab separated grids
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.grid]))
    print("Visited:")
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.visited]))


  def count_island(self):
    """ Count islands in grid by checking every cell. Every 1 is a part of land on an island.

    Returns
    -------
    result
        A numeric value represents the number of islands found.
    """
    # Store island count
    result = 0
    #TODO: count islands while marking visited ones by calling self.mark_visited_island(x,y) function
    for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
              # If cell is land and not visited
              if self.grid[y][x] == '1' and self.visited[y][x] == '0':
                # Mark entire island visited
                self.mark_visited_island(x, y)
                result += 1  # Island found counter
    return result
  

  def mark_visited_island(self, x, y):
    """ Mark island visited using BFS
    Method starts from a set of coordinates and uses queue to find all connected land cells.
    Cells are marked visited to avoid duplicate counting.

    Parameters
    ----------
    x : integer
        X coordinate
    y : integer
        Y coordinate
    """
    # queue_x = deque() 
    # queue_y = deque() 
    #TODO: marks unvisited island
    queue = deque([(x, y)]) # Initial coordinates
    self.visited[y][x] = '1'  # Mark the starting point as visited
    
    # Continue until queue is empty
    while queue:
      curr_x, curr_y = queue.popleft() # Get current coordinates

      # Check top, bottom, left, right neighbors
      directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
      for direction in directions:
        # Calculate new coordinates
        new_x, new_y = curr_x + direction[0], curr_y + direction[1]
        
        # Check if new coordinates are valid and not visited
        if (0 <= new_x < len(self.grid[0]) and 0 <= new_y < len(self.grid) and
          self.grid[new_y][new_x] == '1' and self.visited[new_y][new_x] == '0'):
          # Mark the new position as visited and add it to the queue
          self.visited[new_y][new_x] = '1'
          queue.append((new_x, new_y))
    
