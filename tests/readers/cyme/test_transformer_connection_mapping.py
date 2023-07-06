import pytest

from ditto.readers.cyme.utils import transformer_connection_configuration_mapping


@pytest.mark.parametrize(
    "cyme_value, winding, expected",
    [
        (0, 0, "Y"),
        (0, 1, "Y"),
        (1, 0, "D"),
        (1, 1, "Y"),
        (2, 0, "Y"),
        (2, 1, "D"),
        (3, 0, "Y"),
        (3, 1, "Y"),
        (4, 0, "D"),
        (4, 1, "D"),
        (5, 0, "D"),
        (5, 1, "D"),
        (6, 0, "Y"),
        (6, 1, "D"),
        (7, 0, "D"),
        (7, 1, "Y"),
        (8, 0, "Y"),
        (8, 1, "D"),
        (9, 0, "Y"),
        (9, 1, "Y"),
        (10, 0, "Y"),
        (10, 1, "Y"),
        (11, 0, "Y"),
        (11, 1, "Z"),
        (12, 0, "D"),
        (11, 1, "Z"),
    ],
)
def test_transformer_connection_mapping(cyme_value, winding, expected):
    actual = transformer_connection_configuration_mapping(cyme_value, winding)
    assert actual == expected

    # Function also takes strings
    actual = transformer_connection_configuration_mapping(str(cyme_value), winding)
    assert actual == expected


def test_transformer_connection_mapping_invalid_type():
    with pytest.raises(ValueError):
        transformer_connection_configuration_mapping(0.0, 0)


def test_transformer_connection_mapping_invalid_winding():
    with pytest.raises(ValueError):
        transformer_connection_configuration_mapping(0.0, 2)
