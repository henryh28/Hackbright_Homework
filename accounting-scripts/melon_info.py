"""Print out all the melons in our inventory."""

from melons import melons

def print_melon(key, value):
    """Print each melon with corresponding attribute information."""
    have_or_have_not = 'have'
    if value["seedlessness"]:
        have_or_have_not = 'do not have'

    print(f'{key}s {have_or_have_not} seeds and are ${value["prices"]}')

for key, value in melons.items():
    print_melon(key, value)
