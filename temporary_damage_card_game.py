from card_game import CardGame
from creature import Creature


class TemporaryDamageCardGame(CardGame):
    def hit(self, attacker: Creature, defender: Creature):
            max_Life = defender.health
            defender.health -= attacker.attack
            
            if defender.health > 0:
                defender.health = max_Life
            

                    