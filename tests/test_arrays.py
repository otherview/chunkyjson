import unittest

from chunkyjson.chunky_json import ChunkyJson


class Family(object):
    def __init__(self, json_def={}):
        self.Name = ChunkyJson.deserialize(json_def, field="Name", defaultValue=None)
        self.Masters = ChunkyJson.deserialize(json_def, field="Masters", defaultValue=None)

    @staticmethod
    def serialize_list():
        return ['Name', 'Masters']


class Westeros(object):
    def __init__(self, json_def={}):
        self.Factions = ChunkyJson.deserialize(json_def, field="Factions", defaultValue=None)
        self.NorthFamilies = ChunkyJson.deserialize(json_def, field="NorthFamilies", classObject=list, childType = Family, defaultValue=None)

    @staticmethod
    def serialize_list():
        return ['Factions', 'NorthFamilies']


class GameOfThrones(object):
    def __init__(self, json_def={}):
        self.Westeros = ChunkyJson.deserialize(json_def, field="Westeros", classObject=Westeros, defaultValue=None)

    @staticmethod
    def serialize_list():
        return ['Westeros']



class TestSimpleArray(unittest.TestCase):
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

        self.assertEqual(classed_objs.Westeros.Factions, json["Westeros"]["Factions"])
        self.assertEqual(len(classed_objs.Westeros.NorthFamilies), len(classed_objs.Westeros.NorthFamilies))
        self.assertEqual(classed_objs.Westeros.NorthFamilies[0].Name, json["Westeros"]["NorthFamilies"][0]["Name"])
        serialized_obj = ChunkyJson.serialize(classed_objs)
        self.assertEqual(serialized_obj, serialized_obj)


if __name__ == '__main__':
    unittest.main()
