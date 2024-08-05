def become_warrior(first_name, last_name, power): # This line are parameters
    title = first_name + " " + last_name + " " + "the warrior"
    new_power = power + 1
    return title, new_power


# Don't edit below this line


def main():
    test("Frodo", "Baggins", 5) # These are arguments
    test("Bilbo", "Baggins", 10)
    test("Gandalf", "The Grey", 9000)


def test(first_name, last_name, power):
    title, new_power = become_warrior(first_name, last_name, power)
    print(title, "has a power level of:", new_power)


main()

# The function called to create a warrior, the title of the warrior was their first and last name + the warrior added
# The power level was their powerlevel + 1, created a new var inside of the function