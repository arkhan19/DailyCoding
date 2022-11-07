def MinHealth(power, armor):
    maxDamage = float('-inf')
    damage = 0

    for p in power:
        damage += p
        maxDamage = max(maxDamage, p)

    # Armor applied
    maxDamage = min(maxDamage, armor)
    health = damage - maxDamage + 1
    return health

MinHealth([1, 2, 6, 7], 5)