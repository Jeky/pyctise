#
# Delegating is another (dynamic) way to change the default behavior of class.
#
from typing import Callable


class Hero(object):

    def __init__(self):
        self.max_hp = 100
        self.hp = 100
        self.skills = {}

    def cast(self, skill_name: str, target: str):
        if skill_name not in self.skills:
            print('Cannot cast {}'.format(skill_name))
        else:
            print('Casting {}'.format(skill_name))
            self.skills[skill_name](self, target)

    def learn(self, skill_name: str, skill: Callable[['Hero', str], None]):
        self.skills[skill_name] = skill


def healing(hero: Hero, target: str):
    healing_point = min(hero.max_hp - hero.hp, 5)
    hero.hp += healing_point
    print('Heal {} with {} hp'.format(target, healing_point))


def fireball(hero: Hero, target: str):
    damage = 5
    print('A fireball is flying to {}. {}.hp - 5. {} is burning'.format(target, target, target))


if __name__ == '__main__':
    hero = Hero()

    hero.cast('fireball', 'Slime')
    hero.learn('fireball', fireball)
    hero.cast('fireball', 'Slime')

    hero.hp -= 10
    hero.cast('healing', 'hero')
    hero.learn('healing', healing)
    hero.cast('healing', 'hero')