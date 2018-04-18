# Project Title

A simple class to JSON and JSON to class parser for python.

## Getting Started

Donwload it and use it!

There's a [problem](https://status.python.org/incidents/1y1f44q6srh2) with pypi, waiting to push the package to their servers. (no pip install)


### Installing

```
git clone https://github.com/otherview/ChunkyJson
python setup.py register
```



### Code examples

1. Import chunkyjson:

```
from chunkyjson.chunky_json import ChunkyJson
```

2. Add a couple of classes
```

class Family(object):
    def __init__(self, json_def={}):
        self.Name = ChunkyJson.deserialize(json_def, field="Name", defaultValue=None)
        self.Masters = ChunkyJson.deserialize(json_def, field="Masters", defaultValue=None)

    @staticmethod
    def serialize_list():
        return ['Name', 'Masters']


class NorthFamilies(object):
    def __init__(self, json_def={}):
        self.NorthFamilies = ChunkyJson.deserialize(json_def, field="Masters", classObject = list, childType = Family, defaultValue=None)


    @staticmethod
    def serialize_list():
        return ['Weather', 'Families']


class Westeros(object):
    def __init__(self, json_def={}):
        self.Factions = ChunkyJson.deserialize(json_def, field="Factions", defaultValue=None)
        self.NorthFamilies = ChunkyJson.deserialize(json_def, field="NorthFamilies", classObject=NorthFamilies,
                                                    defaultValue=None)

    @staticmethod
    def serialize_list():
        return ['Factions', 'NorthFamilies']


class GameOfThrones(object):
    def __init__(self, json_def={}):
        self.Westeros = ChunkyJson.deserialize(json_def, field="Westeros", classObject=Westeros, defaultValue=None)

    @staticmethod
    def serialize_list():
        return ['Westeros']

```
3. Setup a Json string, deserialize into classes and serialize it back into a dictonary!
```
def test_serialize_array(self):
        json = {
            "Westeros":
                {
                    "Factions": "derp",
                    "NorthFamilies": [
                        {
                            "Name": "Starks",
                            "Masters": True
                        },
                        {
                            "Name": "Mormont"
                        }
                    ]
                }
        }
        
        
        classed_objs = GameOfThrones(json)
        serialized_obj = ChunkyJson.serialize(classed_objs)
```

Bonus Points:
Add Methods to classes
```
class Westeros(object):
    def __init__(self, json_def={}):
        self.Factions = ChunkyJson.deserialize(json_def, field="Factions", classObject=list, defaultValue=None)
        self.IsAtWar = ChunkyJson.deserialize(json_def, field="IsAtWar", defaultValue=False)

    def war_is_on(self):
        self.IsAtWar = True

    def dragons_kicked_ass(self):
        self.IsAtWar = False

    @staticmethod
    def serialize_list():
        return ['Factions', 'IsAtWar']


class GameOfThrones(object):
    def __init__(self, json_def={}):
        self.Westeros = ChunkyJson.deserialize(json_def, field="Westeros", classObject=Westeros, defaultValue=None)

    @staticmethod
    def serialize_list():
        return ['Westeros']


class TestSimpleUseOfFunctions(unittest.TestCase):
    def test_serialize_array(self):
        json = {
            "Westeros":
                {
                    "Factions": ["DragonLady", "TooMuchLoveBrothers", "SuperRightGuy"]
                }
        }
        classed_objs = GameOfThrones(json)
        self.assertEqual(classed_objs.Westeros.Factions[0], json["Westeros"]["Factions"][0])

        # Default Value is False
        self.assertFalse(classed_objs.Westeros.IsAtWar)

        classed_objs.Westeros.war_is_on()
        self.assertTrue(classed_objs.Westeros.IsAtWar)

        classed_objs.Westeros.dragons_kicked_ass()
        self.assertFalse(classed_objs.Westeros.IsAtWar)

        serialized_obj = ChunkyJson.serialize(classed_objs)

        # TODO proper dict testing
        self.assertEqual(serialized_obj, serialized_obj)
```