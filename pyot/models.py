class OtList(list):
    pass


class OtModel(object):

    def __init__(self, api):
        self._api = api

    @classmethod
    def parse(cls, api, json):
        obj = cls(api)
        for (key, value) in json.items():
            setattr(obj, key, value)
        return obj

    @classmethod
    def parse_list(cls, api, json):
        ot_list = OtList()
        for json_object in json['objects']:
            ot_list.append(cls.parse(api, json_object))
        return ot_list


class Topic(OtModel):

    def __repr__(self):
        return self.name


class Channel(OtModel):
    pass


class News(OtModel):
    pass