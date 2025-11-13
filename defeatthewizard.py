# Base Character class

import random 

class Character:

    def __init__(self, name, health, attack_power):

        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  



    def attack(self, opponent):

        damage = random.randint(int(self.attack_power * 0.8), int(self.attack_power * 1.2))
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")



    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")
    def heal(self, amount=30):
        original_health = self.health
        self.health = min(self.health + amount, self.max_health)
        healed = self.health - original_health
        print(f"{self.name} heals for {healed} health! Current health: {self.health}/{self.max_health}")



# Warrior class (inherits from Character)

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
        self.shield_up = False

    def power_strike(self, opponent):
        damage = self.attack_power * 1.8
        opponent.health -= damage
        print(f"{self.name} uses Power Strike! Devastating attack for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def shield_bash(self):
        self.shield_up = True
        print(f"{self.name} raises their shield! The next attack will reduce incoming damage by 50%!")



# Mage class (inherits from Character)

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)
        self.barrier_active = False

    def fireball(self, opponent):
        damage = self.attack_power * 2.2
        opponent.health -= damage
        print(f"{self.name} casts Fireball! Intense magical explosion for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def magic_barrier(self):
        self.barrier_active = True
        print(f"{self.name} creates a Magic Barrier! The next attack will be nullified!")



# EvilWizard class (inherits from Character)

class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)
        self.low_health_threshold = 75  # Regenerates more when health is low



    def regenerate(self):
        if self.health <= self.low_health_threshold:
            heal_amount = 10
        else:
            heal_amount = 5
        self.health = min(self.health + heal_amount, self.max_health)
        print(f"{self.name} regenerates {heal_amount} health! Current health: {self.health}/{self.max_health}")

    def dark_spell(self, opponent):
        damage = random.randint(int(self.attack_power * 1.5), int(self.attack_power * 2.5))
        opponent.health -= damage
        print(f"{self.name} casts Dark Spell! Powerful magical attack for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def choose_action(self, player):
        # If health is low, regenerate more aggressively
        if self.health <= self.low_health_threshold and random.random() < 0.4:
            return "regenerate"
        # If player has high health, use dark spell
        elif player.health > 80 and random.random() < 0.3:
            return "dark_spell"
        # Otherwise, normal attack
        else:
            return "attack"



# Archer class (inherits from Character)

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=30)
        self.evade_active = False

    def quick_shot(self, opponent):
        damage = self.attack_power * 2
        opponent.health -= damage
        print(f"{self.name} uses Quick Shot! Double arrow attack for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def evade(self):
        self.evade_active = True
        print(f"{self.name} takes an Evade stance! Next attack will be dodged!")


# Paladin class (inherits from Character) 
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=160, attack_power=20)
        self.shield_active = False

    def holy_strike(self, opponent):
        damage = self.attack_power * 1.5
        opponent.health -= damage
        print(f"{self.name} uses Holy Strike! Bonus damage attack for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def divine_shield(self):
        self.shield_active = True
        print(f"{self.name} casts Divine Shield! Next attack will be blocked!")



def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")  



    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)



def battle(player, wizard):
    turn = 1
    while wizard.health > 0 and player.health > 0:
        print(f"\n{'='*50}")
        print(f"TURN {turn} - Battle Status")
        print(f"{'='*50}")
        print(f"{player.name}'s Health: {player.health}/{player.max_health}")
        print(f"{wizard.name}'s Health: {wizard.health}/{wizard.max_health}")
        print(f"{'='*50}\n")
        print("--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")



        choice = input("Choose an action (1-4): ")



        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            if isinstance(player, Archer):
                print("\n--- Archer Abilities ---")
                print("1. Quick Shot (2x damage)")
                print("2. Evade (dodge next attack)")
                ability_choice = input("Choose ability (1-2): ")
                if ability_choice == '1':
                    player.quick_shot(wizard)
                elif ability_choice == '2':
                    player.evade()
                else:
                    print("Invalid ability choice. Your turn is wasted.")
            elif isinstance(player, Paladin):
                print("\n--- Paladin Abilities ---")
                print("1. Holy Strike (1.5x damage)")
                print("2. Divine Shield (block next attack)")
                ability_choice = input("Choose ability (1-2): ")
                if ability_choice == '1':
                    player.holy_strike(wizard)
                elif ability_choice == '2':
                    player.divine_shield()
                else:
                    print("Invalid ability choice. Your turn is wasted.")
            elif isinstance(player, Warrior):
                print("\n--- Warrior Abilities ---")
                print("1. Power Strike (1.8x damage)")
                print("2. Shield Bash (reduce next damage by 50%)")
                ability_choice = input("Choose ability (1-2): ")
                if ability_choice == '1':
                    player.power_strike(wizard)
                elif ability_choice == '2':
                    player.shield_bash()
                else:
                    print("Invalid ability choice. Your turn is wasted.")
            elif isinstance(player, Mage):
                print("\n--- Mage Abilities ---")
                print("1. Fireball (2.2x damage)")
                print("2. Magic Barrier (nullify next attack)")
                ability_choice = input("Choose ability (1-2): ")
                if ability_choice == '1':
                    player.fireball(wizard)
                elif ability_choice == '2':
                    player.magic_barrier()
                else:
                    print("Invalid ability choice. Your turn is wasted.")
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
            print(f"{wizard.name}'s Stats - Health: {wizard.health}/{wizard.max_health}, Attack Power: {wizard.attack_power}")
        else:
            print("Invalid choice. Please enter 1-4.")
            continue

        if wizard.health > 0:
            print(f"\n--- {wizard.name}'s Turn ---")

            # Wizard chooses an action strategically
            wizard_action = wizard.choose_action(player)
            if wizard_action == "regenerate":
                wizard.regenerate()
            elif wizard_action == "dark_spell":
                wizard.dark_spell(player)
            else:  # normal attack
                wizard.regenerate()
                wizard.attack(player)

            # Handle player defensive abilities
            if isinstance(player, Archer) and player.evade_active:
                print(f"{player.name} evades the wizard's attack!")
                player.evade_active = False
            elif isinstance(player, Paladin) and player.shield_active:
                print(f"{player.name}'s Divine Shield blocks the wizard's attack!")
                player.shield_active = False
            elif isinstance(player, Warrior) and player.shield_up:
                print(f"{player.name}'s Shield Bash reduces incoming damage!")
                player.health += wizard.attack_power * 0.5
                print(f"{player.name}'s health is restored due to shield! Current health: {player.health}/{player.max_health}")
                player.shield_up = False
            elif isinstance(player, Mage) and player.barrier_active:
                print(f"{player.name}'s Magic Barrier nullifies the wizard's attack!")
                player.barrier_active = False



        if player.health <= 0:
            print(f"\n{'='*50}")
            print(f"DEFEAT!")
            print(f"{'='*50}")
            print(f"{player.name} has been defeated by {wizard.name}!")
            print(f"Final Health: {player.health}/{player.max_health}")
            print(f"Turns Survived: {turn}")
            print(f"\nThe wizard's dark magic was too powerful...")
            print(f"Better luck next time, brave hero!")
            print(f"{'='*50}\n")

            break

        turn += 1



    if wizard.health <= 0:
        health_percentage = (player.health / player.max_health) * 100
        print(f"\n{'='*50}")
        print(f"🎉 VICTORY! 🎉")
        print(f"{'='*50}")
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")
        print(f"\n--- Battle Statistics ---")
        print(f"Remaining Health: {player.health}/{player.max_health}")
        print(f"Health Percentage: {health_percentage:.1f}%")
        print(f"Total Turns: {turn}")
        print(f"Wizard's Final Health: {wizard.health}/{wizard.max_health}")
        
        if health_percentage > 80:
            print(f"\n⭐ Outstanding Victory! You barely took any damage!")
        elif health_percentage > 50:
            print(f"\n✨ Great Victory! You defeated the wizard!")
        elif health_percentage > 25:
            print(f"\n💪 Hard-fought Victory! You persevered!")
        else:
            print(f"\n🏆 Narrow Victory! You survived against the odds!")
        print(f"{'='*50}\n")



def main():
    print(f"\n{'='*50}")
    print(f"DEFEAT THE EVIL WIZARD")
    print(f"{'='*50}")
    print("Welcome, brave hero! You must defeat the evil wizard")
    print("who has cast darkness upon the land.")
    print(f"{'='*50}\n")

    player = create_character()

    print(f"\n{player.name} the {player.__class__.__name__} steps forward!")
    print(f"Health: {player.health}, Attack Power: {player.attack_power}\n")
    
    input("Press Enter to begin the battle...")

    wizard = EvilWizard("The Dark Wizard")

    print(f"\nA dark figure emerges from the shadows...")
    print(f"The {wizard.name} appears before you!")
    print(f"Health: {wizard.health}, Attack Power: {wizard.attack_power}\n")
    
    input("Press Enter to start the battle...")

    battle(player, wizard)



if __name__ == "__main__":

    main()