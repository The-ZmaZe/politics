from data import *

class Actor:
    def __init__(self, tag) -> None:
        self.tag = tag

    def __repr__(self) -> str:
        return f"{self.tag}"


class House:
    def __init__(self, name, seats: int) -> None:
        self.name = name
        self.seats = seats
        self.assembly = []

    def attribute_seats(self, distribution):
        self.assembly = []
        for tag in distribution.keys():
            distribution[tag] *= self.seats / 100
            self.assembly += [Actor(tag) for _ in range(int(distribution[tag]))]

        sorted_reminders = list(distribution.items())
        sorted_reminders.sort(key=(lambda x: x[1] - int(x[1])))
        reminding_seats = self.seats - len(self.assembly)
        for _ in range(reminding_seats):
            self.assembly.append(Actor(sorted_reminders.pop(0)[0]))

    def order_seats(self, order=ORDER):
        self.assembly.sort(key=lambda actor: order.index(actor.tag))


class Ideology:
    def __init__(self,
                 social=0,
                 ecology=0,
                 libertarianism=0,
                 nationalism=0) -> None:
        self.social = social
        self.ecology = ecology
        self.libertarianism = libertarianism
        self.nationalism = nationalism


class Party:
    def __init__(self,
                 name,
                 informal_ideology: str,
                 ideology:Ideology,
                 vote_discipline=.9) -> None:
        self.name = name
        self.informal_ideology = informal_ideology
        self.ideology = ideology

        self.vote_discipline = vote_discipline


class Parliament:
    def __init__(self, name, houses: list) -> None:
        self.name = name
        self.houses = houses


class Country:
    def __init__(self, name, parliament) -> None:
        self.name = name
        self.parliament = parliament




an = House("Assemblée Nationale", 577)
an.attribute_seats(RESULTATS_1ER_TOUR)
an.order_seats()

print(an.assembly)

import turtle

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.width(3)
pen.up()
pen.goto(-100, 0)
pen.down()
pen.seth(-180)
for p in an.assembly:
    pen.color(COLORS[p.tag])
    pen.up()
    pen.fd(150)
    pen.down()
    pen.fd(200)
    pen.up()
    pen.back(350)
    pen.right(180/577)
turtle.exitonclick()