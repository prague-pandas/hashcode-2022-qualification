import numpy as np
from ordered_set import OrderedSet


def solve(dataset):
    contributors, projects = dataset
    c_names = list(contributors)
    skills = OrderedSet()
    for contributor in contributors.values():
        for skill in contributor:
            skills.add(skill)
    conts = np.zeros((len(contributors), len(skills)), dtype=np.uintp)
    for i, contributor in enumerate(contributors.values()):
        for skill, level in contributor.items():
            j = skills.index(skill)
            conts[i, j] = level
    solution = []
    cont_free = {name: 0 for name in contributors}
    for name, project in projects.items():
        project_assignment = []
        project_start = 0
        length = project['num_days_to_complete']
        unassigned = np.ones(len(conts), dtype=bool)
        for skill_name, level in project['skills']:
            j = skills.index(skill_name)
            eligible = conts[unassigned, j] >= level
            if not np.any(eligible):
                break
            c = np.argmax(eligible)
            c_name = c_names[c]
            project_assignment.append(c_name)
            project_start = max(project_start, cont_free[c_name])
            unassigned[c] = False
        if len(project_assignment) < len(project['skills']):
            continue
        project_end = project_start + length
        if project_end <= project['best_before'] + project['score']:
            solution.append((name, project_assignment))
            for c_name in project_assignment:
                cont_free[c_name] = project_end
    return solution
