inp = lambda name: print(name)
inp("hari")

def dummy(firstname, lastname, formatter):
    return formatter(firstname, lastname)
hello = dummy("hari", "haran", lambda firstname, lastname: f"{firstname} {lastname}")
print(hello)


def get_full_name(first_name, last_name, formatter):
    return formatter(first_name, last_name)
full_name = get_full_name(
    'John',
    'Doe',
    lambda first_name, last_name: f"{first_name} {last_name}"
)
print(full_name)
full_name = get_full_name(
    'John',
    'Doe',
    lambda first_name, last_name: f"{last_name} {first_name}"
)
print(full_name)

      