def load(f):
	f_lines = iter(f.readlines())
	num_contributors, num_projects = next(f_lines).split(' ')
	num_contributors = int(num_contributors)
	num_projects = int(num_projects)
	contributors = {}
	projects = {}
	for _ in range(num_contributors):
		contributor_name, num_skills = next(f_lines).split(' ')
		num_skills = int(num_skills)
		contributors[contributor_name] = {}
		for _ in range(num_skills):
			skill_name, skill_points = next(f_lines).split(' ')
			skill_points = int(skill_points)
			contributors[contributor_name][skill_name] = skill_points
	for _ in range(num_projects):
		project_name, *rest = next(f_lines).split(' ')
		num_days_to_complete, score, best_before, num_roles = [int(x) for x in rest]
		projects[project_name] = {
			'num_days_to_complete': num_days_to_complete,
			'score': score,
			'best_before': best_before, 
			'skills': {},
		}
		for _ in range(num_roles):
			role_type, required_skill_level = next(f_lines).split(' ')
			required_skill_level = int(required_skill_level)
			projects[project_name]['skills'][role_type] = required_skill_level
	return contributors, projects
