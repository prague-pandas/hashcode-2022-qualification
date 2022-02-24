import os
import numpy as np
import pandas as pd

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
	stats = {
		'skills (avg)': [],
		'skills (std)': [],
		'score (avg)': [],
		'score (std)': [],
		'num_days (avg)': [],
		'num_days (std)': [],
		'best_before (avg)': [],
		'best_before (std)': [],
		'diff num days and best before (avg)': [],
		'diff num days and best before (std)': [],
	}
	for i in 'abcdef':
		with open(os.path.join('../input_data', filename[i])) as f:			
			contributors, projects = load(f)
			contributor_num_skills_np_array = np.asarray([len(contributor) for contributor in contributors])
			stats['skills (avg)'].append(np.average(contributor_num_skills_np_array))
			stats['skills (std)'].append(np.std(contributor_num_skills_np_array))
			project_info_np_array = np.asarray([[
				project['score'],
				project['num_days_to_complete'],
				project['best_before'],
				project['best_before'] - project['num_days_to_complete']] 
					for project in projects.values()])
			score_avg, num_days_to_complete_avg, best_before_avg, diff_avg = np.average(project_info_np_array, axis=0).tolist()
			score_std, num_days_to_complete_std, best_before_std, diff_std = np.std(project_info_np_array, axis=0).tolist()
			stats['score (avg)'].append(score_avg)
			stats['score (std)'].append(score_std)
			stats['num_days (avg)'].append(num_days_to_complete_avg)
			stats['num_days (std)'].append(num_days_to_complete_std)
			stats['best_before (avg)'].append(best_before_avg)
			stats['best_before (std)'].append(best_before_std)
			stats['diff num days and best before (avg)'].append(diff_avg)
			stats['diff num days and best before (std)'].append(diff_std)

	stats_df = pd.DataFrame.from_dict(stats)
	print(stats_df)

		
