class Player:
    def __init__(self, name, level, health, strength, magic):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength
        self.magic = magic

    def attack(self, target):
        damage = self.strength * self.level
        target.health -= damage
        print(f'{self.name} attacks {target.name} for {damage} points of damage.')

    def cast_spell(self, spell, target):
        if self.magic < spell.cost:
            print(f'{self.name} does not have enough magic to cast {spell.name}.')
            return

        self.magic -= spell.cost
        damage = spell.damage * self.level
        target.health -= damage
      