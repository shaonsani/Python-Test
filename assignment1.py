# solution function
def solve(input, i=1):
    for key, value in input.items():
        print(f'{key} {i}')
        if isinstance(value, dict):
            solve(value, i + 1)


# test data
data = {
    'key1': 1,
    'key2': {
        'key3': 1,
        'key4': {
            'key5': 4
        }
    }
}

# function call
solve(data)
