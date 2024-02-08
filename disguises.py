class Disguise:

    def __init__(self, name, color_requirements, mana_value, power, toughness, image):
        self.name = name
        self.color_requirements = color_requirements
        self.mana_value = mana_value
        self.power = power
        self.toughness = toughness
        self.image = image

    def castable(self, mana_sources):
        if len(mana_sources) < self.mana_value:
            return False
        i = 0
        while len(color_requirements) > 0:
            current = mana_sources[i]
            if (current == '*') or (color_requirements[0] in current) or (color_requirement[-1] in current):
                color_requirements.pop()
            i += 1
            if i >= len(mana_sources):
                return False
        return True
