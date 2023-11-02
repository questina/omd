import unittest
from unittest.mock import patch, MagicMock

from what_is_year_now import what_is_year_now, API_URL


def make_cm_for_urlopen(return_val, http_code=200):
    cm = MagicMock()
    cm.getcode.return_value = http_code
    cm.read.return_value = return_val
    cm.__enter__.return_value = cm
    return cm


class TestYearGetter(unittest.TestCase):

    def test_ymd_format(self):
        with patch("urllib.request.urlopen") as mock_urlopen:
            mock_urlopen.return_value = make_cm_for_urlopen(
                '{"currentDateTime": "2026-05-07"}'
            )
            self.assertEqual(what_is_year_now(), 2026)
            self.assertEqual(mock_urlopen.call_args.args[0], API_URL)

    def test_dmy_format(self):
        with patch("urllib.request.urlopen") as mock_urlopen:
            mock_urlopen.return_value = make_cm_for_urlopen(
                '{"currentDateTime": "19.03.1965"}'
            )
            self.assertEqual(what_is_year_now(), 1965)

    def test_incorrect_format(self):
        with patch("urllib.request.urlopen") as mock_urlopen:
            mock_urlopen.return_value = make_cm_for_urlopen(
                '{"currentDateTime": "11-06-1999"}'
            )
            with self.assertRaises(ValueError, msg='Invalid format'):
                what_is_year_now()
