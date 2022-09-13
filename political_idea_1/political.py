from core import *


class HelloWorld(Action):
    code = "hello_world"
    desc = "Say hi"

    @classmethod
    def execute(cls, authority, country, **kwargs):
        print(f"Hello from {authority}")


class GrossMinimumWage(Action):
    code = "gmw"
    desc = "Update the Gross Minimum Wage"

    @classmethod
    def execute(cls, authority, country, **kwargs):
        country.gross_minimum_wage = kwargs["value"]


class DevConstitution(Constitution):
    code = "dev_constitution"
    authorities = {
        "president": {
            "name": "Président.e de la République",
            "qualif": ["hello_world"]
        },
        "prime_minister": {
            "name": "Premier.ère Ministre",
            "qualif": ["hello_world", "gmw"]
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
GrossMinimumWage.order("prime_minister", DevCountry, value=1700)
print(DevCountry.gross_minimum_wage)