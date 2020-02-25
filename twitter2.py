import json
import copy
json_copy = []

path = []
def read_json():
    """
    Read json file and return data from the file
    """
    with open('twitter.json', encoding='utf-8') as f:
        data = json.loads(f.read())
        return data


def main(data):
    """
    :param data: dict
    Provide user's work with file information
    """

    if type(data) == dict:
        for key in data:
            print(key, "     ", type(data[key]))
        choice = input("Select one option:  ")

        choice = choice.strip()

        if choice.lower() == 'break':
            return 'Thank you for using this program'
        if choice == 'info':
            return data
        if choice == 'back':
            data = previous()
            return main(data)

        if choice in data:
            path.append(choice)
            return main(data[choice])
        else:
            print('-----------------------------------')
            print('Oops...your data is wrong')
            print('Please try again')
            print('-----------------------------------')
            return main(data)

    elif type(data) == list:
        for part in range(len(data)):
            print(part, "     ", type(data[part]))
        choice = input("Select one index:  ")

        if choice.lower() == 'break':
            return 'Thank you for using this program'
        if choice == 'info':
            return data
        if choice == 'back':
            data = previous()
            return main(data)
        try:
            choice = int(choice)
        except ValueError:
            print('-----------------------------------')
            print('Inputted value should be an integer')
            print('Please try again')
            print('-----------------------------------')
            return main(data)
        try:
            path.append(choice)
            data = data[choice]
        except IndexError:
            print('-----------------------------------')
            print('Selected input is out of range')
            print('Please try again')
            print('-----------------------------------')
        return main(data)
    else:
        return data


def previous():
    global json_copy
    json_main = copy.deepcopy(json_copy)
    path.pop()
    for now in path:
        json_main = json_main[now]
    return json_main
if __name__ == "__main__":

    print('Hello!')
    print('Are you ready to analyze the json file?')
    print('Choose any option on the LEFT to start the search')
    print('If you want to stop running the program input "break"')
    print('-----------------------------------')
    print('Which will be your choice?')
    print('')
    json_copy = read_json()
    print(main(copy.deepcopy(json_copy)))
    print('Have a nice day:)')
