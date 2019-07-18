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
        test_cases = dict()
        test_cases["bir"] = "бир"
        test_cases["Bir"] = "Бир"
        test_cases["ikki"] = "икки"
        test_cases["shimoliy"] = "шимолий"
        test_cases["g'alaba"] = "ғалаба"
        test_cases["ta'til"] = "таътил"
        test_cases["aksiya"] = "акция"
        test_cases["sharti"] = "шарти"
        test_cases["ishoq"] = "исҳоқ"
        for key, result in test_cases.items():
            self.assertEqual(await lat2cyr(key), result)

    async def test_sentence_with_e_letter(self):
        sentence = "Eshmat bugun maktabga eshakda ketdi"
        translit = "Эшмат бугун мактабга эшакда кетди"
        self.assertEqual(await lat2cyr(sentence), translit)
