import fileinput

def _search_and_replace(file, occurence, replace_by):
    with fileinput.FileInput(file, inplace=True) as file:
        for line in file:
            print(line.replace(occurence, replace_by), end='')


def use_scss(val):
    if val == 'yes':
        _search_and_replace('settings.py', 'USE_SCSS = False', 'USE_SCSS = True')
        print('You have enabled SCSS on your project!')
    elif val == 'no':
        _search_and_replace('settings.py', 'USE_SCSS = True', 'USE_SCSS = False')
        print('You have disabled SCSS on your project!')
    else: print('The answer you have provided does is not one of the following accepted argument: (yes|no)...')


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) == 0:
        use = input('Do you want to use SCSS in your project ? (yes|no):\n')
    else:
        use = args[0]

