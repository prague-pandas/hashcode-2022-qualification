import numpy as np
from ordered_set import OrderedSet


def solve(dataset, rng=None):
    if rng is None:
        rng = np.random.default_rng(0)
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

    def score(name):
        project = projects[name]
        return project['best_before']

    schedule = sorted(projects, key=lambda name: score(name))
    solution = []
    cont_free = {name: 0 for name in contributors}
    for name in schedule:
        project = projects[name]
        project_assignment = []
        project_start = 0
        length = project['num_days_to_complete']
        assigned = set()
        for skill_name, level in project['skills']:
            j = skills.index(skill_name)
            eligible = conts[:, j] >= level
            eligible = np.nonzero(eligible)[0]
            eligible = [e for e in eligible if e not in assigned]
            if len(eligible) == 0:
                break
            c = rng.choice(eligible)
            c_name = c_names[c]
            project_assignment.append(c_name)
            project_start = max(project_start, cont_free[c_name])
            assigned.add(c)
            contributors[c_names[c]][skill_name] = contributors[c_names[c]][skill_name] + 1
        if len(project_assignment) < len(project['skills']):
            continue
        project_end = project_start + length
        if project_end <= project['best_before'] + project['score']:
            solution.append((name, project_assignment))
            for c_name in project_assignment:
                cont_free[c_name] = project_end
    return solution
