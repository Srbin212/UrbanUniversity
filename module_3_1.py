calls = 0

def count_calls(calls):
    print(calls)

def string_info(string):
    global calls
    calls += 1
    new_tuple = (len(string), string.upper(), string.lower())
    return new_tuple

def is_contains(string, list_to_search):
    global calls
    calls += 1
    for item in list_to_search:
        new_list = []
        new_list.append(item.lower())
    if string.lower() in new_list:
        return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)