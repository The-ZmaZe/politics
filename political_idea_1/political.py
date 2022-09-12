from core import *


class HelloWorld(Action):
    code = "hello_world"
    desc = "Say hi"

    @classmethod
    def execute(cls, authority):
        print(f"Hello from {authority}")


class DevConstitution(Constitution):
    code = "dev_constitution"
    authorities = {
        "president": {
            "name": "Président de la République",
            "qualif": ["hello_world"]
        }
    }


class DevCountry(Country):
    code = "dev_country"
    desc = "Debug Country"
    constitution = DevConstitution

    population = 100 * 10 ^ 6
    death_rate = 10             # per 1000
    birth_rate = 13             # per 1000
    capital_city = "duckburg"

    gross_minimum_wage = 1500


HelloWorld.order("president", DevCountry)
