#!/usr/bin/env python3


import random
import time
import os
import creature

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Societic: # 'Societic' is a evolution simulator for the Terpy game engine.
    def __init__(self, evolution_speed=0.1, mutation_rate=0.01, print_status=True, listofcreatures:list=[], end_limit=100000):
        self.evolution_speed = evolution_speed
        self.end_limit = end_limit
        self.print_status = print_status
        self.mutation_rate = mutation_rate
        self.dead = []
        self.listofcreatures = listofcreatures

        self.current_cycle = 0 


    def get_all_unique_species(self):
            unique_species = set()
            for creature in self.listofcreatures:
                unique_species.add(tuple(creature.__getall__()))
            return [list(species) for species in unique_species]
    
    def get_all_extinct_species(self):
            unique_species = set()
            for creature in self.dead:
                unique_species.add(tuple(creature.__getall__()))
            return [list(species) for species in unique_species]


    def print_statuses(self):
            clear()
            print(f"Creatures left: {len(self.listofcreatures)}")
            print(f"Extinct species: {len(self.get_all_extinct_species())}")
            print(f"Unique species: {len(self.get_all_unique_species())}")
            print(f"Current cycle: {self.current_cycle}")
            print(f"Current creature: {self.listofcreatures[self.current_cycle]}")
            print(f"Next creature: {self.listofcreatures[self.current_cycle + 1]}") 
            print(f"Current comparison: {self.listofcreatures[self.current_cycle]},{self.listofcreatures[self.current_cycle + 1]}")

    def compare_and_eliminate(self, a:creature.Creature, b:creature.Creature):
            if a.strength > b.strength:
                if a.age < a.lifespan:
                    a.age += 1
                else:
                    self.dead.append(a)
                    self.listofcreatures.remove(a)
            elif b.strength > a.strength:
                if b.age < b.lifespan:
                    b.age += 1
                else:
                    self.dead.append(b)
                    self.listofcreatures.remove(b)
            elif a.strength == b.strength:
                if a.age < a.lifespan and b.age < b.lifespan:
                    a.age += 1
                    b.age += 1
                elif a.age < a.lifespan and b.age >= b.lifespan:
                    a.age += 1
                    self.dead.append(b)
                    self.listofcreatures.remove(b)
                elif b.age < b.lifespan and a.age >= a.lifespan:
                    b.age += 1
                    self.dead.append(a)
                    self.listofcreatures.remove(a)
                else:
                    self.dead.append(a)
                    self.dead.append(b)
                    self.listofcreatures.remove(a)
                    self.listofcreatures.remove(b)

            else:
                self.dead.append(a)
                self.listofcreatures.remove(a)

    def evolve(self):
            if self.current_cycle % 2:
                for i in self.listofcreatures:
                    i.age += 1
            if self.listofcreatures[self.current_cycle].reproduction_rate > random.gauss(1, 2):
                if max(0, float(random.uniform(0, 1))) > self.mutation_rate:
                    offspring = creature.Creature(
                        reproduction_rate = max(1, min(10, self.listofcreatures[self.current_cycle].reproduction_rate + random.choice([-1,0,1]) if random.random() < self.mutation_rate else self.listofcreatures[self.current_cycle].reproduction_rate)),
                        strength = max(1, min(10, self.listofcreatures[self.current_cycle].strength + random.choice([-1,0,1]) if random.random() < self.mutation_rate else self.listofcreatures[self.current_cycle].strength)),
                        lifespan = max(1, min(10, self.listofcreatures[self.current_cycle].lifespan + random.choice([-1,0,1]) if random.random() < self.mutation_rate else self.listofcreatures[self.current_cycle].lifespan))
                    )
                else:
                     offspring = creature.Creature(
                          reproduction_rate=self.listofcreatures[self.current_cycle].reproduction_rate,
                          strength=self.listofcreatures[self.current_cycle].strength,
                          lifespan=self.listofcreatures[self.current_cycle].lifespan
                     )
                self.listofcreatures.append(offspring)
            if self.print_status:
                self.print_statuses()
            self.compare_and_eliminate(self.listofcreatures[self.current_cycle], self.listofcreatures[self.current_cycle + 1])
            time.sleep(self.evolution_speed)
            self.current_cycle += 1
            if self.current_cycle >= len(self.listofcreatures)  - 1:
                self.current_cycle = 0
            

    def evolution(self):
            while not len(self.listofcreatures)  > self.end_limit and len(self.listofcreatures) > 0:
                self.evolve()
                

creature_list = [creature.Creature(reproduction_rate=random.randint(1,10), strength=random.randint(1,10), lifespan=random.randint(1,10))]
society = Societic(evolution_speed=0.0, mutation_rate=0.05, print_status=True, listofcreatures=creature_list)
society.evolution();print("Evolution complete!"); print(f"Survivor: {society.listofpeople[0]}")