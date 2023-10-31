import pytest

from morse import decode


@pytest.mark.parametrize(
    "msg,decoded_msg",
    [
        ('... --- ...', 'SOS'),
        ('.- ...- .. - ---', 'AVITO'),
        ('-.. --- ..- .... ---.. -- . ..--.. -.--.- -.--.-', 'DOUH8ME?))'),
        ('', ''),
        (' ', ''),
    ]
)
def test_decode(msg, decoded_msg):
    assert decode(msg) == decoded_msg
