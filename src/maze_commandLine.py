import numpy as np
import sys


class MazeCommandLine:
    """

    """

    def __init__(self):
        print('')

    def read_file(self) -> np.ndarray:
        with open(sys.argv[1]) as f:
            lines = f.readlines()
            new_maze = []
            for line in lines:
                new_item = []
                for item in line:
                    if item == '\n':
                        continue
                    new_item.append(self.convert_maze(item))
                new_item = np.array(new_item, dtype=int)
                new_maze.append(new_item)
            new_maze = np.array(new_maze)
        print(*lines)
        return new_maze

    def convert_maze(self, item):
        if item == '*':
            return '0'
        elif item == ' ':
            return '1'
        elif item == 'A':
            return '3'
        elif item == 'B':
            return '4'
        else:
            print('error:', item, '.')

    def maze_path(self) -> None:
        print('hello')


if __name__ == '__main__':
    maze = MazeCommandLine()
    maze.read_file()
