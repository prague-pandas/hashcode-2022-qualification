import logging
import os

import numpy as np
from tqdm import tqdm

from load import load
from save import save
from solve import solve

filename = {
    'a': 'a_an_example.in.txt',
    'b': 'b_better_start_small.in.txt',
    'c': 'c_collaboration.in.txt',
    'd': 'd_dense_schedule.in.txt',
    'e': 'e_exceptional_skills.in.txt',
    'f': 'f_find_great_mentors.in.txt',
}


def main():
    logging.basicConfig(level=logging.INFO)
    logging.getLogger('matplotlib').setLevel(logging.INFO)
    np.random.seed(0)

    for letter in tqdm('abcdef', unit='dataset'):
        fn = filename[letter]

        with open(os.path.join('../input_data', fn)) as f:
            task = load(f)

        solution = solve(task)

        out_dir = '../out'
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, fn), 'w') as f:
            save(solution, f)


if __name__ == '__main__':
    with np.errstate(all='raise'):
        main()
