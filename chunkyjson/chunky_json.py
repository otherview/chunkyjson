class ChunkyJson:
    @staticmethod
    def serialize(obj, attributes=None):
        return_json = {}

        if attributes == "in-built-type":
            obj_type = type(obj)
            if obj_type is bool:
                if obj:
                    rtn_val = "true"
                else:
                    rtn_val = "false"
            elif obj_type is unicode:
                rtn_val = str(obj)
            elif obj_type is str:
                rtn_val = str(obj)
            elif obj_type is int or obj_type is long or obj_type is float:
                rtn_val = str(obj)
            elif obj_type is list:
                rtn_val = []
                for element_val in obj:
                    serializeList = "in-built-type"
                    try:
                        serializeList = element_val.serialize_list()
                    except:
                        pass

                    rtn_val.append(ChunkyJson().serialize(element_val, serializeList))
            return rtn_val

        if attributes is None:
            attributes = obj.serialize_list()

        for field in attributes:
            if hasattr(obj, field):
                obj_val = getattr(obj, field)
                obj_type = type(obj_val)
                if obj_val is None:
                    continue

                # if special_character_fields is not None:
                #     if field in special_character_fields:
                #         field = "@{0}".format(field)

                # If Object type is a list
                elif obj_type is list:
                    rtn_val = []
                    for element_val in obj_val:
                        serializeList = "in-built-type"
                        try:
                            serializeList = element_val.serialize_list()
                        except:
                            pass
                        rtn_val.append(ChunkyJson().serialize(element_val, serializeList))

                elif obj_type is bool:
                    if getattr(obj, field):
                        rtn_val = "true"
                    else:
                        rtn_val = "false"
                elif obj_type is unicode:
                    rtn_val = str(getattr(obj, field))
                elif obj_type is str:
                    rtn_val = str(getattr(obj, field))
                elif obj_type is int or obj_type is long or obj_type is float:
                    rtn_val = getattr(obj, field)
                elif field in vars(obj_val).keys(): #vars(obj_val).keys()[0] == field:
                    rtn_val = []
                    obj_val = getattr(obj_val, field)
                    for element_val in obj_val:
                        serializeList = "in-built-type"
                        try:
                            serializeList = element_val.serialize_list()
                        except:
                            pass
                        rtn_val.append(ChunkyJson().serialize(element_val, serializeList))
                else:
                    rtn_val = ChunkyJson().serialize(obj_val, obj_val.serialize_list())
                return_json[field] = rtn_val

        return return_json

    @staticmethod
    def deserialize(json_def={}, field=None, classObject=None, childType=None, defaultValue=None):
        if not field:
            print "Error: field not defined"

        if childType is not None and classObject is not None and classObject is list :
            if json_def is not None and json_def[field] is not None:
                value_list = []
                for val in json_def[field]:
                    value_list.append(childType(val))
            return value_list

        if classObject is None:
            return defaultValue if field not in json_def else json_def[field]
        return defaultValue if field not in json_def else classObject(json_def[field])
        pass
