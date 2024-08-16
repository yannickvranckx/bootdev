def take_magic_damage(health, resist, amp, spell_power):
    """
    Calculate the magic damage, you set a max damage that is equal
    spell power multiplied by your amp. The actual damage is the max damage minus
    the resistance your character might have. new health is your current health minus
    actual damage.
    """
    maximum_damage = spell_power * amp
    actual_damage = maximum_damage - resist
    new_health = health - actual_damage
    return new_health