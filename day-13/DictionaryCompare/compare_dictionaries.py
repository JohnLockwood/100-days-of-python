"""
Compare Python Dictionaries
"""


dictionary = {"favorite_website": "https://codesolid.com", "attempts": 1}

# Add a key
key_added = dictionary.copy()
key_added["new"] = "New Value"
#print(dictionary == key_added)

# Remove a key
key_removed = dictionary.copy()
del(key_removed["attempts"])
#print(dictionary == key_removed)

# Change a value
value_changed = dictionary.copy()
value_changed["attempts"] = 2
#print(dictionary == value_changed)

# Change type of a value from int to float
type_changed = dictionary.copy()
assert type_changed["attempts"] == 1
type_changed["attempts"] = 1.0
#print(dictionary == type_changed)

import typing
def type_aware_equals(d1: typing.Dict, d2: typing.Dict) -> bool:
    """Compares dictionaries with strong check on equality of values"""
    
    # Return early if standard equality fails
    if d1 != d2:
        return False

    # Compare types
    values = zip(d1.values(), d2.values())
    for value in values:
        if type(value[0]) != type(value[1]):
            return False
    
    return True

print(type_aware_equals(dictionary, key_added))
print(type_aware_equals(dictionary, key_removed))
print(type_aware_equals(dictionary, value_changed))
print(type_aware_equals(dictionary, type_changed))


# Make sure equal dictionaries are reported correctly
same_dictionary = dictionary.copy()
print(type_aware_equals(dictionary, same_dictionary))

    
# block2()

# block3()