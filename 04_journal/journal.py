import pathlib


def load(name):
    """ """
    data = []
    filename = get_full_pathname(name)
    if filename.exists():
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())
    return data

def save(name, journal_data):
    filename = get_full_pathname(name)
    print ('........ Saving to: {}'.format(filename))

    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')

def add_entry(text, journal_data):
    journal_data.append(text)

def get_full_pathname(name):
    home_folder = pathlib.Path.cwd()
    this_name = name + '.txt'
    filename = home_folder / 'journals' / this_name
    return filename
