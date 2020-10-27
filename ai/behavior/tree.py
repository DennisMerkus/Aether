from enum import Enum, auto


class Sense(object):
    def emit(self, event) -> None:
        raise NotImplementedError()

    def has_state(self, state) -> bool:
        raise NotImplementedError()


class Vision(Sense):
    # Shapes, light, colors
    # w/ direction/location

    # Specific implementation of 'has_state'
    def sees(self, object) -> bool:
        raise NotImplementedError()


class Hearing(Sense):
    # Sounds
    # frequency, sounds, (human) speech, (animal) calls, signals, music, volume
    # w/ approximate direction
    pass


class Touch(Sense):
    # Texture, temperature, vibration
    pass


class Taste(Sense):
    # Sweet, sour, salt, bitter, umami, specific tastes of foods
    # and others like Coolness, Numbness, etc.
    # https://en.wikipedia.org/wiki/Taste

    # Dependent on objects that come in contact with the taste sense to contain
    # certain compounds
    pass


class Smell(Sense):
    # Specific smells, bad smells, sweet smells
    # Based on the chemical compounds they result from, like esters
    # Or just from categorical smell codes
    # Terpenes/Terpenoids: https://en.wikipedia.org/wiki/Terpene
    # Esters: https://www.stilldragon.org/discussion/2134/esters-and-their-smells

    # Dependent on physical objects emitting smell 'particles'
    pass


class Mind(object):
    # Perception and BDI

    # Senses:
    # - What can I see?
    # - What can I hear?
    # - What can I feel?
    # - Am I hungry?
    # - Am I thirsty?

    # Other Characters:
    # - Have I spoken with character before?
    # - Do I know character's name?
    # - What else do I know about character?
    # - How do I recongize character?
    pass


class Body(object):
    # Actions

    # Movement:
    # - Walk to a position in local space
    # - Run to a position in local space
    # - Change stance
    #  - Standing
    #  - Kneeling
    #  - Sitting (on sittable surface)
    #  - Prone

    # Interactions:
    # - Pick up an object
    # - Grab a grabbable thing
    # - Operate a machine or device
    # - Pick a fruit or plant
    # - Swing a held tool (axe, sword)
    #  - Tools afford certain actions and prevent others
    pass


class Limb(object):
    pass


class HumanHand(Limb):
    # - Hold objects
    #  - Including tools
    # - Touch objects
    #  - Feel temperature
    #  - Feel texture

    class Grip(Enum):
        Power = auto()
        Spherical = auto()

    pass


class HumanBody(Body):
    def walk(self):
        raise NotImplementedError()

    def pick_up(self, hand, target):
        raise NotImplementedError()


class BehaviorTree(object):
    pass


class Task(object):
    def __init__(self, mind: Mind, body: Body):
        self.mind = mind
        self.body = body

    def run(self) -> bool:
        raise NotImplementedError()
