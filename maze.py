from typing import Tuple

import numpy as np


class Maze:
    """

    """

    def __init__(self):
        self.recorded_steps = []
        self.start_i = 0
        self.start_j = 0
        self.maze_array = np.ndarray
        self.encoding = {
            '*': 0,
            ' ': 1,
            'A': 2,
            'B': 3,
            'S': 4,
            'N': 5,
            'E': 6,
            'W': 7,
            'R': 9,
            'C': 10
        }

    def read_file(self, filename) -> np.ndarray:
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
        try:
            for k, v in self.encoding.items():
                if item == k:
                    return v
        except Exception as e:
            print('Error encoding the maze to int: ', e)

    def encode_maze2str(self, item) -> str:
        try:
            for k, v in self.encoding.items():
                if item == str(v):
                    return k
        except Exception as e:
            print('Error encoding the maze to string: ', e)

    def convert_maze2str(self, maze_final):
        for i in range(len(maze_final)):
            for j in range(len(maze_final[i])):
                maze_final[i][j] = self.encode_maze2str(maze_final[i][j])
        return maze_final

    def get_start(self, maze_array) -> Tuple[int, int]:
        try:
            for i in range(int(len(maze_array) / 2)):
                for j in range(int(len(maze_array[i]) / 2)):
                    if maze_array[i][j] == 2:
                        return i, j
        except Exception as e:
            print('Error while getting the maze start: ', e)

    def maze_path(self, maze_array) -> None:
        self.maze_array = maze_array
        self.start_i, self.start_j = self.get_start(self.maze_array)
        self.make_step(self.start_i, self.start_j)
        maze_final = np.array(self.maze_array, dtype=str)
        maze_final[self.start_i][self.start_j] = 2
        maze_final = self.convert_maze2str(maze_final)
        print('\n'.join([''.join(['{:2}'.format(item) for item in row])
                         for row in maze_final]))

    def make_step(self, i, j):
        if (self.maze_array[i + 1][j] or self.maze_array[i - 1][j]
                or self.maze_array[i][j + 1] or self.maze_array[i][j - 1]) == 3:
            print('arrived')
            print(self.recorded_steps)
            return
        """
        if self.maze_array[i - 1][j] == 3:
            print('arrived')
            print(self.recorded_steps)

            return
        if self.maze_array[i][j + 1] == 3:
            print('arrived')
            print(self.recorded_steps)

            return
        if self.maze_array[i][j - 1] == 3:
            print('arrived')
            print(self.recorded_steps)

            return
        if self.maze_array[i + 1][j] == 3:
            print('arrived')
            print(self.recorded_steps)
            return
        if self.maze_array[i - 1][j] == 3:
            print('arrived')
            print(self.recorded_steps)

            return
        if self.maze_array[i][j + 1] == 3:
            print('arrived')
            print(self.recorded_steps)

            return
        if self.maze_array[i][j - 1] == 3:
            print('arrived')
            print(self.recorded_steps)

            return
        """
        if i + 1 < len(self.maze_array) and self.maze_array[i + 1][j] == 1:
            if self.maze_array[i + 2][j] != 1 and self.maze_array[i + 2][j] != 0 and self.maze_array[i + 2][j] != 3:
                print('CYCLE AT', 'i', i, 'j', j, 'i+2', self.maze_array[i + 2][j], 'i+1', self.maze_array[i + 1][j])
                self.maze_array[i + 1][j] = 10
                # return
            self.maze_array[i + 1][j] = 4
            self.recorded_steps.append(4)
            print('Been here S')
            self.make_step(i + 1, j)
        elif i - 1 >= 0 and self.maze_array[i - 1][j] == 1:
            if self.maze_array[i - 2][j] != 1 and self.maze_array[i - 2][j] != 0 and self.maze_array[i - 2][j] != 3:
                print('CYCLE AT', 'i', i, 'j', j, 'i-2', self.maze_array[i - 2][j], 'i-1', self.maze_array[i - 1][j])
                self.maze_array[i - 1][j] = 10
                # return
            self.maze_array[i - 1][j] = 5
            self.recorded_steps.append(5)
            print('Been here N')
            self.make_step(i - 1, j)
        elif j + 1 < len(self.maze_array[0]) and self.maze_array[i][j + 1] == 1:
            if self.maze_array[i][j + 2] != 1 and self.maze_array[i][j + 2] != 0 and self.maze_array[i][j + 2] != 3:
                print('CYCLE AT', 'i', i, 'j', j, 'j+2', self.maze_array[i][j + 2], 'j+1', self.maze_array[i][j + 1])
                self.maze_array[i][j + 1] = 10
                # return
            self.maze_array[i][j + 1] = 6
            self.recorded_steps.append(6)
            print('Been here E')
            self.make_step(i, j + 1)
        elif j - 1 >= 0 and self.maze_array[i][j - 1] == 1:
            if self.maze_array[i][j - 2] != 1 and self.maze_array[i][j - 2] != 0 and self.maze_array[i][j - 2] != 3:
                print('CYCLE AT', 'i', i, 'j', j, 'j-2', self.maze_array[i][j - 2], 'j-1', self.maze_array[i][j - 1])
                self.maze_array[i][j - 1] = 10
                # return
            self.maze_array[i][j - 1] = 7
            self.recorded_steps.append(7)
            print('Been here W')
            self.make_step(i, j - 1)
        else:
            print('nowhere to go')
            rec = len(self.recorded_steps)
            if rec == 0:
                print('length zero')
                self.maze_array[i][j] = 9
                return self.maze_array

            last_step = self.recorded_steps[rec - 1]
            print('ls', last_step)
            print(self.maze_array[i][j])
            print('rec', self.recorded_steps)
            rec = len(self.recorded_steps)
            last_step = self.recorded_steps[rec - 1]
            print('last step: ', last_step)
            if i - 1 >= 0 and last_step == 4:
                self.maze_array[i - 1][j] = 4
                self.maze_array[i][j] = 9
                self.recorded_steps.pop()
                self.make_step(i - 1, j)
            elif i + 1 < len(self.maze_array) and last_step == 5:
                self.maze_array[i + 1][j] = 5
                self.maze_array[i][j] = 9
                self.recorded_steps.pop()
                self.make_step(i + 1, j)
            elif j - 1 >= 0 and last_step == 6:
                self.maze_array[i][j - 1] = 6
                self.maze_array[i][j] = 9
                self.recorded_steps.pop()
                self.make_step(i, j - 1)
            elif j + 1 < len(self.maze_array[0]) and last_step == 7:
                self.maze_array[i][j + 1] = 7
                self.maze_array[i][j] = 9
                self.recorded_steps.pop()
                self.make_step(i, j + 1)
            elif self.maze_array[i][j] == 8:
                print(last_step)
                # self.maze_array[i][j] = 10
                print('path already used')

            else:
                print('Loop found')

        return self.maze_array


if __name__ == '__main__':
    maze = Maze()
    converted_maze = maze.read_file('maze-cycle.txt')
    maze.maze_path(converted_maze)
