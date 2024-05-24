import numpy as np
import copy

test_pattern = [
    [0, 1, 1, 0, 1, 1],
    [1, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 1],
    [0, 1, 1, 1, 0, 0]
]


def return_neighbours(life_map, array_i, cell_i):
    neighbours = []
    max_row, max_col = life_map.shape
    schema = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1), (0, 1),
              (1, -1), (1, 0), (1, 1)]

    for rel in schema:
        row = array_i + rel[0]
        col = cell_i + rel[1]
        if 0 <= row < max_row and 0 <= col < max_col:
            neighbours.append(life_map[row, col])
    # print(neighbours)
    return np.array(neighbours)


def print_map(life_map, iteration):
    print(f"\n{iteration} generation")
    for row in life_map:
        print((' '.join(str(cell) for cell in row)).replace('0', '.').replace('1', 'X'))


def main(pattern):
    iteration = 0
    previous_map = pattern.copy()
    while True:
        iteration += 1
        current_map = copy.deepcopy(previous_map)
        print_map(current_map, iteration)
        for ia, arr in enumerate(previous_map):
            for ic, cell in enumerate(arr):
                neighbours = return_neighbours(life_map=previous_map,
                                               array_i=ia,
                                               cell_i=ic)
                live_cells = (neighbours == 1).sum()

                if cell == 1 and live_cells < 2:
                    current_map[ia, ic] = 0
                elif cell == 1 and live_cells in (2, 3):
                    current_map[ia, ic] = 1  # live
                elif cell == 1 and live_cells > 3:
                    current_map[ia, ic] = 0  # die
                elif cell == 0 and live_cells == 3:
                    current_map[ia, ic] = 1  # live

        if (previous_map == current_map).all():
            print('The Life map has stopped.')
            break
        previous_map = current_map


if __name__ == '__main__':
    pattern = np.random.choice([0, 1], size=(25, 25))
    main(np.array(pattern))

