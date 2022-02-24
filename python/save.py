def save(solution, f):
    """
    Schedule is a list of projects. Each project is a tuple:
    1. Project name
    2. List of names of people assigned
    """
    f.write(f'{len(solution)}\n')
    for project in solution:
        f.write(f'{project[0]}\n')
        f.write('%s\n' % ' '.join(project[1]))
