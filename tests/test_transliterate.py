import asyncio
import asynctest
import sys

sys.path.insert(0, "..")
import transliterate


class TestLat2CyrTransliteration(asynctest.TestCase):
    def setUp(self):
        self.my_loop = asyncio.new_event_loop()

    def tearDown(self):
        self.my_loop.close()

    async def test_upper(self):
        self.assertEqual(await transliterate.lat2cyr("AQSH"), "АҚШ")

    async def test_e_letter(self):
        self.assertEqual(await transliterate.lat2cyr("ketayotib"), "кетаётиб")
        self.assertEqual(await transliterate.lat2cyr("eshak"), "эшак")
        self.assertEqual(await transliterate.lat2cyr("kemada"), "кемада")
