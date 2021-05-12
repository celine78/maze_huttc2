from typing import Tuple
import numpy as np


class MazeFiles:
    """
    The maze class reads a maze from a file and prints a path from a starting point A to an end point B.
    When no path can be found or if there are cycles, the user will be informed.
    """

    def __init__(self) -> None:
        try:
            """
            Initialize the encodings in the mate, the starting and end point, the steps taken during the path and a new
            Numpy array to store the maze converted to integers.
            """
            self.recorded_steps = []
            self.start_i = 0
            self.start_j = 0
            self.maze_array = np.ndarray
            self.cycles = []
            self.encoding = {
                '*': 0,  # wall
                ' ': 1,  # free space
                'A': 2,  # starting point
                'B': 3,  # end point
                'S': 4,  # south
                'N': 5,  # north
                'E': 6,  # east
                'W': 7,  # west
                'R': 9,  # returned
                'C': 10  # cycle
            }
        except Exception as e:
            print('Error occurred during the initialization: ', e)

    def read_file(self, filename) -> np.ndarray:
        """
        Reading of the text file from the console and converting the maze into a Numpy array of integers
        :param filename: the text file with the maze
        :return: Numpy array
        """
        try:
            with open(filename) as f:
                lines = f.readlines()
                new_maze = []
                for line in lines:
                    new_item = []
                    [new_item.append(self.encode_maze2int(item)) for item in line if item != '\n']
                    new_item = np.array(new_item, dtype=int)
                    new_maze.append(new_item)
                new_maze = np.array(new_maze)
            return new_maze
        except Exception as e:
            print('Error reading the file: ', e)

    def encode_maze2int(self, item) -> int:
        """
        Encoding of the string symbols into integers, according to the encoding dictionary
        :param item: symbol as string
        :return: corresponding encoding as integer
        """
        try:
            for k, v in self.encoding.items():
                if item == k:
                    return v
        except Exception as e:
            print('Error encoding the maze to int: ', e)

    def encode_maze2str(self, item) -> str:
        """
        Encoding of the integers into string symbols, according to the encoding dictionary
        :param item: integer values
        :return: corresponding encoding as string symbols
        """
        try:
            for k, v in self.encoding.items():
                if item == v:
                    return k
        except Exception as e:
            print('Error encoding the maze to string: ', e)

    def convert_maze2str(self, maze_final) -> np.ndarray:
        """
        Converting a maze with integer values into string symbols
        :param maze_final: the maze to convert
        :return: converted maze as string
        """
        try:
            for i in range(len(maze_final)):
                for j in range(len(maze_final[i])):
                    maze_final[i][j] = self.encode_maze2str(int(maze_final[i][j]))
            return maze_final
        except Exception as e:
            print('Error converting the maze to string: ', e)

    def get_start(self, maze_array) -> Tuple[int, int]:
        """
        Finding the starting point of the maze in the top left quarter
        :param maze_array: the maze as Numpy array
        :return: The row and column of the starting point as integers
        """
        try:
            for i in range(int(len(maze_array) / 2)):
                for j in range(int(len(maze_array[i]) / 2)):
                    if maze_array[i][j] == 2:
                        return i, j
        except Exception as e:
            print('Error while getting the maze start: ', e)

    def check_cycles(self, i, j, i_print, j_print, enc_i, enc_j):
        """
        Checking of cycles in the maze. Cycles are assumed to be present when the next step is free and two
        steps further there is no wall, no free space and it is not the end point. Thus meaning, that this step
        has already been visited.
        :param i: the row number of two steps ahead
        :param j: the column number of two steps ahead
        :param i_print: the current row number
        :param j_print: the current column number
        :param enc_i: the row number of the next step (which is free)
        :param enc_j: the column number of the next step (which is free)
        """
        try:
            # two steps ahead should not be free (1), be a wall (0) or the end point (3)
            if self.maze_array[i][j] != 1 and self.maze_array[i][j] != 0 and self.maze_array[i][j] != 3:
                # cycles are being saved
                self.cycles.append([i_print, j_print])
                # encoding for showing cycles points on the maze (might get overwritten)
                self.maze_array[enc_i][enc_j] = 10
        except Exception as e:
            print('Error looking for cycles: ', e)

    def make_step(self, i, j, encoding):
        """
        Making one step ahead and recording it
        :param i: the row number of the next step
        :param j: the column number of the next step
        :param encoding: encoding for the coordinates
        """
        try:
            self.maze_array[i][j] = encoding
            self.recorded_steps.append(encoding)
            self.find_path(i, j)
        except Exception as e:
            print('Error making a step: ', e)

    def step_backwards(self, i, j, i_now, j_now, encoding):
        """
        Going one step backwards if no path lies in front
        :param i: the row number of the backward step
        :param j: the column number of the backward step
        :param i_now: current row number
        :param j_now: current column number
        :param encoding: coordinate of the last step taken before being blocked
        """
        try:
            self.maze_array[i][j] = encoding
            # encoding of current step to show used paths on the maze
            self.maze_array[i_now][j_now] = 9
            self.recorded_steps.pop()
            # recursive call
            self.find_path(i, j)
        except Exception as e:
            print('Error making a step backwards: ', e)

    def go_backwards(self, i, j):
        """
        Going into the opposite direction from the last step taken
        :param i: current row number
        :param j: current column number
        """
        try:
            number_steps = len(self.recorded_steps)
            last_step = self.recorded_steps[number_steps - 1]
            # if going back north and not at the boundary of the maze
            if i - 1 >= 0 and last_step == 4:
                self.step_backwards(i - 1, j, i, j, 4)
            # if going back south and not at the boundary of the maze
            elif i + 1 < len(self.maze_array) and last_step == 5:
                self.step_backwards(i + 1, j, i, j, 5)
            # if going back west and not at the boundary of the maze
            elif j - 1 >= 0 and last_step == 6:
                self.step_backwards(i, j - 1, i, j, 6)
            # if going back east and not at the boundary of the maze
            elif j + 1 < len(self.maze_array[0]) and last_step == 7:
                self.step_backwards(i, j + 1, i, j, 7)
            else:
                print('Could not get the last step taken or path going outside maze boundary.')
        except Exception as e:
            print('Error going backwards: ', e)

    def maze_path(self, maze_array) -> None:
        """
        Getting and printing the path for the maze
        :param maze_array: the maze in form of integers
        """
        try:
            # temporarily allow more recursions to avoid a stack overflow error
            import sys
            sys.setrecursionlimit(10000)

            self.maze_array = maze_array
            # getting the starting point
            self.start_i, self.start_j = self.get_start(self.maze_array)
            # finding the path
            self.find_path(self.start_i, self.start_j)
            # saving into a Numpy string array for printing
            maze_final = np.array(self.maze_array, dtype=str)
            # resetting encoding of starting point, in case it got overwritten
            maze_final[self.start_i][self.start_j] = 2
            # converting the integers into symbols
            maze_final = self.convert_maze2str(maze_final)
            # print the maze with the path
            print('\n'.join([''.join(['{:2}'.format(item) for item in row]) for row in maze_final]))
            # print the cycles found
            if len(self.cycles) > 0: [print(f'Cycle found at row {i} and column {j}') for i, j in self.cycles]
            # inform, if no path could be found, else print the path
            if len(self.recorded_steps) == 0:
                print('No path found')
            else:
                for i in range(len(self.recorded_steps)):
                    self.recorded_steps[i] = self.encode_maze2str(self.recorded_steps[i])
                print('Maze path: ', self.recorded_steps)

            # reset to default allowed recursion limit
            import sys
            sys.setrecursionlimit(1000)
        except Exception as e:
            print('Error getting the maze path: ', e)

    def find_path(self, i, j):
        """
        Finding the path from staring point to end point
        :param i: row number from which to go further
        :param j: column number from which to go further
        :return: the maze array with the path
        """
        try:
            # if next step is 3, end point has been found
            if (self.maze_array[i + 1][j] or self.maze_array[i - 1][j]
                    or self.maze_array[i][j + 1] or self.maze_array[i][j - 1]) == 3:
                return self.maze_array

            # check if the next field in the south is free
            if i + 1 < len(self.maze_array) and self.maze_array[i + 1][j] == 1:
                # look for a cycle
                self.check_cycles(i + 2, j, i, j, i + 1, j)
                # make a step south
                self.make_step(i + 1, j, 4)
            # check if the next field in the north is free
            elif i - 1 >= 0 and self.maze_array[i - 1][j] == 1:
                # look for a cycle
                self.check_cycles(i - 2, j, i, j, i - 1, j)
                # make a step north
                self.make_step(i - 1, j, 5)
            # check if the next field in the east is free
            elif j + 1 < len(self.maze_array[0]) and self.maze_array[i][j + 1] == 1:
                # look for a cycle
                self.check_cycles(i, j + 2, i, j, i, j + 1)
                # make a step east
                self.make_step(i, j + 1, 6)
            # check if the next field in the west is free
            elif j - 1 >= 0 and self.maze_array[i][j - 1] == 1:
                # look for a cycle
                self.check_cycles(i, j - 2, i, j, i, j - 1)
                # make a step west
                self.make_step(i, j - 1, 7)
            else:
                # if no space available, go backwards
                number_steps = len(self.recorded_steps)
                # if the whole path has been made backwards and no space is available, we assume there is no path
                if number_steps == 0:
                    self.maze_array[i][j] = 9
                    return self.maze_array
                self.go_backwards(i, j)
            return self.maze_array
        except Exception as e:
            print('Error searching for a path: ', e)


if __name__ == '__main__':
    maze = MazeFiles()
    converted_maze = maze.read_file('../maze-cycle.txt')
    maze.maze_path(converted_maze)
