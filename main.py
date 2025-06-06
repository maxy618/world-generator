import numpy as np
import matplotlib.pyplot as plt

from biomes import BIOMES, WATER


DIRECTIONS = (
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
)


def generate_world(num_rows, num_cols, number_of_seeds, growth_probability=0.55, frame_delay=0.001):
    grid = np.full((num_rows, num_cols, 3), WATER, dtype=np.uint8)
    depth_map = np.full((num_rows, num_cols), -1, dtype=int)
    biome_map = np.full((num_rows, num_cols), None, dtype=object)
    max_depth_reached = 0

    biome_names_list = list(BIOMES.keys())
    active_seeds = set()

    for _ in range(number_of_seeds):
        seed_row = np.random.randint(0, num_rows)
        seed_col = np.random.randint(0, num_cols)
        chosen_biome = np.random.choice(biome_names_list)
        active_seeds.add((seed_row, seed_col, 0, chosen_biome))
        depth_map[seed_row, seed_col] = 0
        biome_map[seed_row, seed_col] = chosen_biome

    plt.figure(figsize=(6, 6))

    while active_seeds:
        next_seeds = set()
        temp_visual = np.full((num_rows, num_cols, 3), WATER, dtype=np.uint8)
        land_positions = np.where(depth_map >= 0)
        temp_visual[land_positions] = np.array([200, 200, 200], dtype=np.uint8)

        plt.clf()
        plt.imshow(temp_visual)
        plt.axis('off')
        plt.pause(frame_delay)

        for (current_row, current_col, current_depth, current_biome) in active_seeds:
            depth_map[current_row, current_col] = current_depth
            biome_map[current_row, current_col] = current_biome

            if np.random.rand() > growth_probability:
                continue

            for row_offset, col_offset in DIRECTIONS:
                neighbor_row = current_row + row_offset
                neighbor_col = current_col + col_offset
                neighbor_depth = current_depth + 1

                if not (0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols):
                    continue
                if depth_map[neighbor_row, neighbor_col] != -1:
                    continue

                next_seeds.add((neighbor_row, neighbor_col, neighbor_depth, current_biome))
                if neighbor_depth > max_depth_reached:
                    max_depth_reached = neighbor_depth

        active_seeds = next_seeds

    for row_index in range(num_rows):
        for col_index in range(num_cols):
            depth_value = depth_map[row_index, col_index]
            if depth_value == -1:
                grid[row_index, col_index] = WATER
                continue

            biome_name = biome_map[row_index, col_index]
            palette = BIOMES[biome_name]
            palette_length = len(palette)
            if max_depth_reached > 0:
                ratio = depth_value / max_depth_reached
                idx = int(round(ratio * (palette_length - 1)))
            else:
                idx = 0

            if idx < 0:
                idx = 0
            if idx >= palette_length:
                idx = palette_length - 1

            grid[row_index, col_index] = palette[idx]

    plt.clf()
    plt.imshow(grid)
    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    final_map = generate_world(
        num_rows=200,
        num_cols=200,
        number_of_seeds=10,
        growth_probability=0.58,
        frame_delay=0.001
    )

