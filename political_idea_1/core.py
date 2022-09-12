class UndefinedAction(Exception):
    ...


class UnauthorizedAction(Exception):
    ...


class Action:
    @classmethod
    def order(cls, authority: str, constitution):
        if cls.code in constitution.authorities[authority]:
            try:
                cls.execute(authority)
            except AttributeError:
                raise UndefinedAction(f"{cls.code} "
                    + "has no execution process defined")
        else:
            raise UnauthorizedAction(f"{authority} isn't qualified for "
                + f"{cls.code} according to {constitution.code}")


class Constitution:
    ...


class DevConstitution(Constitution):
    code = "dev_constitution"
    authorities = {
        "president": ["hello_world"]
    }
