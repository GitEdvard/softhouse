import json


class JsonObject(object):
    """
    Dummy class, fill up with any number of fields, to be exported as json
    """
    pass


class SerializerBase(object):
    def __init__(self):
        self.json_object = JsonObject()

    def toJSON(self):
        return json.dumps(
            self.json_object,
            default=self.parse_json,
            indent=4
        )

    def parse_json(self, obj):
        # Recursive method. Iterates until a dict/list with plain objects are achieved
        if isinstance(obj, RankedListSerializer):
            return [o.json_object for o in obj.json_object.list]
        elif issubclass(type(obj), SerializerBase):
            return obj.json_object
        return obj.__dict__


class CompanyDailyDiffSerializer(SerializerBase):
    def __init__(self, rank, company_daily_diff):
        super().__init__()
        self.json_object.rank = rank
        self.json_object.name = company_daily_diff.company_abbr
        self.json_object.percent = round(company_daily_diff.change_in_percent, 2)
        self.json_object.latest = company_daily_diff.latest


class RankedListSerializer(SerializerBase):
    def __init__(self, a_list, item_serializer_class):
        super().__init__()
        self.json_object.list = \
            [item_serializer_class(ix + 1, item) for ix, item in enumerate(a_list)]


class EnvelopeSerializer(SerializerBase):
    def __init__(self, diff_list):
        super().__init__()
        self.json_object.winners = RankedListSerializer(diff_list, CompanyDailyDiffSerializer)
