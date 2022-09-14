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


class InheritanceTax(Action):
    code = "inheritance_tax"
    desc = "Update the Inheritance Tax"

    @classmethod
    def execute(cls, authority, country, **kwargs):
        country.Taxes.inheritance = kwargs["value"]


class DevConstitution(Constitution):
    code = "dev_constitution"
    authorities = {
        "president": {
            "name": "Président.e de la République",
            "qualif": ["hello_world"]
        },
        "prime_minister": {
            "name": "Premier.ère Ministre",
            "qualif": ["hello_world", "gmw"],
            "can_propose": ["inheritance_tax"]
        },
        "government": {
            "name": "Gouvernement Dev I",
            "ministries": {
                "ecology": {
                    "name": "Ministère de la Transition Écologique",
                    "minister_name": "Ministre de la Transition Écologique"
                }
            }
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

    class Taxes:
        inheritance = {
            150000: 10  # The first layer start at 150000 and is a tax of 10%
        }


HelloWorld.order("president", DevCountry)

GrossMinimumWage.order("prime_minister", DevCountry, value=1700)
print(DevCountry.gross_minimum_wage)

InheritanceTax.order("prime_minister",
                     DevCountry,
                     value={
                         500000: 5,
                         1000000: 10,
                         2000000: 20,
                         3000000: 30,
                         4000000: 40,
                         5000000: 50,
                         6000000: 60,
                         7000000: 70,
                         8000000: 80,
                         9000000: 90,
                         10000000: 100
                     })
print(DevCountry.Taxes.inheritance)