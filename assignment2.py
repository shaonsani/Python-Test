class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father


def solve(input, i=1):
    flag = False
    if isinstance(input, Person):
        input = vars(input)
        flag = True
    for key, value in input.items():
        if flag or isinstance(value,Person):
            print(f'{key}: {i}')
        else:
            print(f'{key} {i}')
        if isinstance(value, dict) or isinstance(value,Person):
            solve(value, i + 1)


person_a = Person('User', '1', None)
person_b = Person('User', '2', person_a)
data = {
    'key1': 1,
    'key2': {
        'key3': 1,
        'key4': {
            'key5': 4,
            'user': person_b
        }
    }
}
solve(data)
