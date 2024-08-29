from unittest import TestCase
import handystats


class AggregationsTest(TestCase):
    data = range(1, 1001)

    def test_mean(self):
        value = handystats.mean(self.data)
        self.assertEqual(value, 500.5)

    def test_stdev(self):
        value = handystats.stdev(self.data)
        self.assertGreater(value, 288)
        self.assertLess(value, 289)

    def test_min(self):
        value = handystats.min(self.data)
        self.assertEqual(value, 1)

    def test_max(self):
        value = handystats.max(self.data)
        self.assertEqual(value, 1000)

    def test_median(self):
        value = handystats.median(self.data)
        self.assertEqual(value, 500.5)

    def test_harmonic_mean(self):
        value = handystats.harmonic_mean(self.data)
        self.assertGreater(value, 133)
        self.assertLess(value, 134)

    def test_geo_mean(self):
        value = handystats.geo_mean(self.data)
        self.assertGreater(value, 369)
        self.assertLess(value, 370)

    def test_perc_n(self):
        value = handystats.perc_n(self.data, 99)
        self.assertEqual(value, 990)

    def test_perc1(self):
        value = handystats.perc1(self.data)
        self.assertEqual(value, 10)

    def test_perc5(self):
        value = handystats.perc5(self.data)
        self.assertEqual(value, 50)

    def test_perc95(self):
        value = handystats.perc95(self.data)
        self.assertEqual(value, 950)

    def test_perc99(self):
        value = handystats.perc99(self.data)
        self.assertEqual(value, 990)

    def test_variance(self):
        value = handystats.variance(self.data)
        self.assertGreater(value, 83416)
        self.assertLess(value, 83417)

    def test_pvariance(self):
        value = handystats.pvariance(self.data)
        self.assertGreater(value, 83333)
        self.assertLess(value, 83334)


class FullStatsTest(TestCase):
    data = range(1, 1001)

    def test_default(self):
        results = handystats.full_stats(self.data)
        self.assertIsInstance(results, dict)
        for key in results:
            self.assertIn(key, handystats.DEFAULT_AGGRS)

    def test_aggrs(self):
        aggrs = ('min', )
        results = handystats.full_stats(self.data, aggrs=aggrs)
        self.assertEqual(len(results), 1)
        self.assertIn('min', results)

    def test_prefix(self):
        prefix = 'foo_'
        results = handystats.full_stats(self.data, prefix=prefix)
        for key in results:
            self.assertTrue(key.startswith(prefix))
