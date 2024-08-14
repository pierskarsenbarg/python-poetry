"""A Python Pulumi program"""

import pulumi
import pulumi_random as random

pet = random.RandomPet("mypet")

pulumi.export("petname", pet.id)
