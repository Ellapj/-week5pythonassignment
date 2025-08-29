# Define a base class called Superhero
class Superhero:
    # Constructor method to initialize attributes
    def __init__(self, name, alias, power, city):
        self.name = name            # Real name of the superhero
        self.alias = alias          # Superhero name
        self.power = power          # Special ability
        self.city = city            # City they protect
        self._reputation = 50       # Encapsulated attribute (starts at 50)

    # Method to introduce the superhero
    def introduce(self):
        return f"I am {self.alias}, protector of {self.city}!"

    # Method to use their power
    def use_power(self):
        return f"{self.alias} uses {self.power}!"

    # Method to increase reputation
    def boost_reputation(self, points):
        self._reputation += points
        return f"{self.alias}'s reputation increased to {self._reputation}."

    # Method to access the reputation value
    def get_reputation(self):
        return self._reputation
    
    # Number 2
class Superhero:
    # Constructor method to initialize attributes
    def __init__(self, name, alias, power, city, weakness):
        self.name = name            # Real name of the superhero
        self.alias = alias          # Superhero name
        self.power = power          # Special ability
        self.city = city            # City they protect
        self.weakness = weakness    # Their vulnerability
        self._reputation = 50       # Encapsulated attribute (starts at 50)
        self.energy = 100           # New attribute: energy level (out of 100)

    # Method to introduce the superhero
    def introduce(self):
        return f"I am {self.alias}, protector of {self.city}!"

    # Method to use their power
    def use_power(self):
        if self.energy >= 20:
            self.energy -= 20
            return f"{self.alias} uses {self.power}! Energy left: {self.energy}"
        else:
            return f"{self.alias} is too tired to use their power."

    # Method to rest and regain energy
    def recharge(self):
        self.energy = 100
        return f"{self.alias} has recharged and is back to full energy!"

    # Method to increase reputation
    def boost_reputation(self, points):
        self._reputation += points
        return f"{self.alias}'s reputation increased to {self._reputation}."

    # Method to access the reputation value
    def get_reputation(self):
        return self._reputation

    # Method to reveal weakness
    def reveal_weakness(self):
        return f"{self.alias}'s weakness is {self.weakness}."
    
    # Create multiple superhero objects with unique values
hero1 = Superhero(
    name="Tunde",
    alias="SolarMan",
    power="Solar Blast",
    city="Lagos",
    weakness="Rainstorms"
)

hero2 = Superhero(
    name="Ada",
    alias="ShadowMist",
    power="Invisibility",
    city="Abuja",
    weakness="Bright light"
)

hero3 = Superhero(
    name="Chinedu",
    alias="IronPulse",
    power="Magnetic Shockwave",
    city="Enugu",
    weakness="Rust"
)

#testing their unique behaviours

print(hero1.introduce())           # I am SolarMan, protector of Lagos!
print(hero2.use_power())           # ShadowMist uses Invisibility!
print(hero3.reveal_weakness())     # IronPulse's weakness is Rust.
print(hero1.boost_reputation(30))  # SolarMan's reputation increased to 80.
print(hero2.get_reputation())      # Returns current reputation value


#Number 4

# Define a subclass called AntiHero that inherits from Superhero
class AntiHero(Superhero):
    # Constructor method with an extra attribute: motive
    def __init__(self, name, alias, power, city, weakness, motive):
        # Call the parent constructor using super()
        super().__init__(name, alias, power, city, weakness)
        self.motive = motive  # Unique attribute for AntiHero

    # Polymorphism: override the introduce method
    def introduce(self):
        return f"{self.alias} walks a darker path... but still protects {self.city}."

    # New method specific to AntiHero
    def reveal_motive(self):
        return f"{self.alias}'s true motive: {self.motive}"