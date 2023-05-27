import math

class Color:
    def __init__(self, value: int, hexcode: str):
        self.value = value
        self.hexcode = hexcode

class State:
    def __init__(self, value: int, notevalue: int, ccvalue: int):
        self.value = value
        self.notevalue = notevalue
        self.ccvalue = ccvalue
    
    def __repr__(self):
        return self.value

class PadType:
    def __init__(self, value: int, type: str):
        self.value = value
        self.type = type
    
    def __repr__(self):
        return self.value

class Pad:
    def __init__(self, x: int, y: int, color: Color, state: State, type: PadType):
        self.x = x
        self.y = y
        self.color = color
        self.state = state
        self.type = type

#init colors
color = {}

color["black"] = Color(0, "000000")
color["white"] = Color(3, "ffffff")

#init states
state = {}

state["static"] = State(1, 144, 176)
state["flashing"] = State(2, 145, 177)
state["pulsing"] = State(3, 146, 178)

#init pad types
type = {}

type["main"] = PadType(1, "main")
type["cc"] = PadType(2, "cc")

#init grid
grid = {}

for x in range(1, 10):
    for y in range(1, 10):
        if x == 9 or y == 9:
            grid[f"pad{x}{y}"] = Pad(x, y, color["black"], state["static"], type["cc"])
        else:
            grid[f"pad{x}{y}"] = Pad(x, y, color["black"], state["static"], type["main"])

#for padkey, padvalues in grid.items():
#    print(f"{padkey}: {padvalues.x} {padvalues.y} {padvalues.color} {padvalues.state} {padvalues.type}")