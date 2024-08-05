def get_punched(health, armor=0): #armor=0 is telling python to use a default value
    damage = 50 - armor
    health = health - damage
    return health


def get_slashed(health, armor=0):
    damage = 100 - armor
    health = health - damage
    return health


# Don't touch below this line


def test(health, armor):
    print(f"Health: {health}, Armor: {armor}")
    print(f"Health after punch: {get_punched(health, armor)}")
    print("=====================================")
    print(f"Health: {health}, Armor: {armor}")
    print(f"Health after slash: {get_slashed(health, armor)}\n")
    print("=====================================")
    print(f"Health: {health}, Armor: no armor!")
    print(f"Health after slash: {get_slashed(health)}\n")
    print("=====================================")
    print(f"Health: {health}, Armor: no armor!")
    print(f"Health after punch: {get_punched(health)}")
    print("=====================================")


test(400, 5)
test(300, 3)
test(200, 1)

# Assignment - get punched and get slashed. Get punched does 50 damage, get slashed does 100. Damage goes off
# armor first and then health
# There should be a default value for armor set to 0