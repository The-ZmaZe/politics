class UndefinedAction(Exception):
    ...


class UnauthorizedAction(Exception):
    ...


class Action:
    @classmethod
    def order(cls, authority: str, country, **kwargs):
        if cls.code in country.constitution.authorities[authority]["qualif"]:
            try:
                cls.execute(authority, country, **kwargs)
            except AttributeError:
                raise UndefinedAction(f"{cls.code} "
                                      + "has no execution process defined")
        elif cls.code in (
                country.constitution.authorities[authority]["can_propose"]):
            try:
                # TODO replace playmobils with a fully functionnal parliament
                print("The playmobils have voted, the reform was approved.")
                cls.execute(authority, country, **kwargs)
            except AttributeError:
                raise UndefinedAction(f"{cls.code} "
                                      + "has no execution process defined")
        else:
            raise UnauthorizedAction(f"{authority} isn't qualified for "
                                     + f"{cls.code} according to "
                                     + f"{country.constitution.code}")


class Constitution:
    ...


class Country:
    ...


class Laws:
    ...
