import numpy as np
from ordered_set import OrderedSet
from tqdm import tqdm


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
    found = True
    finished = set()
    t = tqdm()
    while found:
        found = False
        for name in schedule:
            if name in finished:
                continue
            project = projects[name]
            project_assignment = []
            project_start = 0
            length = project['num_days_to_complete']
            assigned = set()
            # TODO: Sort by level (?).
            mentor_levels = np.zeros(len(skills), dtype=np.uintp)
            for skill_name, level in project['skills']:
                j = skills.index(skill_name)
                if mentor_levels[j] >= level:
                    level -= 1
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
                for sn, l in contributors[c_name].items():
                    jj = skills.index(sn)
                    mentor_levels[jj] = max(l, mentor_levels[jj])
            if len(project_assignment) < len(project['skills']):
                continue
            project_end = project_start + length
            if project_end <= project['best_before'] + project['score']:
                solution.append((name, project_assignment))
                found = True
                finished.add(name)
                for c_name, (skill_name, level) in zip(project_assignment, project['skills']):
                    cont_free[c_name] = project_end
                    j = skills.index(skill_name)
                    c = c_names.index(c_name)
                    if conts[c, j] <= level:
                        conts[c, j] += 1
        t.update()
    return solution
