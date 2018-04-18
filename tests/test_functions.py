import unittest

from chunkyjson.chunky_json import ChunkyJson


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


if __name__ == '__main__':
    unittest.main()
