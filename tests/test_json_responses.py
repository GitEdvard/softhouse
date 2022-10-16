import pytest
from stock_winners.domain import StockValue
from stock_winners.serializers import SerializerBase
from stock_winners.serializers import EnvelopeSerializer
from stock_winners.serializers import RankedListSerializer
from tests.resources.resource_bag import EXAMPLE_RESPONSE
from tests.resources.resource_bag import EXAMPLE_ENVELOPED_RESPONSE


def test_generate_json():
    test_field = "ABC"
    serializer = ExampleSerializer(1, test_field)

    json = serializer.toJSON()

    assert json == EXAMPLE_RESPONSE.strip()

@pytest.mark.now
def test_enveloped_json():
    test_field = "ABC"
    serializer = ExampleEnvelopeSerializer([test_field])

    json = serializer.toJSON()

    assert json == EXAMPLE_ENVELOPED_RESPONSE.strip()


class ExampleSerializer(SerializerBase):
    def __init__(self, rank, test_field):
        super().__init__()
        self.json_object.rank = rank
        self.json_object.test_field = test_field


class ExampleEnvelopeSerializer(SerializerBase):
    def __init__(self, example_list):
        super().__init__()
        self.json_object.topnode = RankedListSerializer(example_list, ExampleSerializer)
