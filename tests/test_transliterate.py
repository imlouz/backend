import asyncio
import asynctest
import sys

sys.path.insert(0, "..")
from transliterate.core import lat2cyr


class TestLat2CyrTransliteration(asynctest.TestCase):
    def setUp(self):
        self.my_loop = asyncio.new_event_loop()

    def tearDown(self):
        self.my_loop.close()

    async def test_upper(self):
        self.assertEqual(await lat2cyr("AQSh"), "АҚШ")

    async def test_e_letter(self):
        self.assertEqual(await lat2cyr("ketayotib"), "кетаётиб")
        self.assertEqual(await lat2cyr("eshak"), "эшак")
        self.assertEqual(await lat2cyr("kemada"), "кемада")

    async def test_sentence_with_e_letter(self):
        sentence = "Eshmat bugun maktabga eshakda ketdi"
        translit = "Эшмат бугун мактабга эшакда кетди"
        self.assertEqual(await lat2cyr(sentence), translit)
