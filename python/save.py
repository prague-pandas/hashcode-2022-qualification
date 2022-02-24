def save(schedule, f):
    """
    Schedule is a list of projects. Each project is a tuple:
    1. Project name
    2. List of names of people assigned
    """
    f.write(f'{len(schedule)}\n')
    for project in schedule:
        f.write(f'{project[0]}\n')
        f.write('%s\n' % ' '.join(project[1]))
