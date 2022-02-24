import os

from load import load

filename = {
	'a': 'a_an_example.in.txt',
	'b': 'b_better_start_small.in.txt',
	'c': 'c_collaboration.in.txt',
	'd': 'd_dense_schedule.in.txt',
	'e': 'e_exceptional_skills.in.txt',
	'f': 'f_find_great_mentors.in.txt',
}

if __name__ == '__main__':
	with open(os.path.join('../input_data', filename['e'])) as f:
		contributors, projects = load(f)
		print(contributors)
		print(projects)
