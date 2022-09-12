from core import *


class HelloWorld(Action):
    code = "hello_world"
    desc = "Say hi"

    @classmethod
    def execute(cls, authority):
        print(f"Hello from {authority}")



HelloWorld.order("president", DevConstitution)