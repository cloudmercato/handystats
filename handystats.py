#!/usr/bin/env python
"""Handy library for making quick basic statistics"""
import builtins
import math
import statistics

VERSION = (1, 0, 0)
__version__ = '.'.join([str(v) for v in VERSION])
__author__ = "Anthony Monthe"
__email__ = "anthony@cloud-mercato.com"


def mean(values):
    values = [v for v in values if v is not None]
    if not values:
        return
    return statistics.mean(values)


def stdev(values):
    values = [v for v in values if v is not None]
    if not values:
        return
    if len(values) == 1:
        return .0
    return statistics.stdev(values)


def min(values):
    values = [v for v in values if v is not None]
    if not values:
        return
    return builtins.min(values)


def max(values):
    values = [v for v in values if v is not None]
    if not values:
        return
    return builtins.max(values)


def median(values):
    values = [v for v in values if v is not None]
    if not values:
        return
    return statistics.median(values)


def harmonic_mean(values):
    values = [v for v in values if v is not None]
    if not values:
        return
    return statistics.harmonic_mean(values)


def geo_mean(values):
    values = [v for v in values if v is not None]
    if not values:
        return
    return statistics.geometric_mean(values)


def perc_n(values, n):
    values = [v for v in values if v is not None]
    if not values:
        return
    if len(values) == 1:
        return values[0]
    size = len(values)
    return sorted(values)[int(math.ceil((size * n) / 100)) - 1]


def perc1(values):
    return perc_n(values, 1)


def perc5(values):
    return perc_n(values, 5)


def perc95(values):
    return perc_n(values, 95)


def perc99(values):
    return perc_n(values, 99)


def variance(values):
    values = [v for v in values if v is not None]
    if not values:
        return
    return statistics.variance(values)


def pvariance(values):
    values = [v for v in values if v is not None]
    if not values:
        return
    return statistics.pvariance(values)


def full_stats(data, aggrs=None, prefix=''):
    aggrs = aggrs or DEFAULT_AGGRS
    results = {}
    for aggr in aggrs:
        key = f'{prefix}{aggr}'
        results[key] = AGGREGATIONS[aggr](data)
    return results


DEFAULT_AGGRS = ('mean', 'stdev', 'min', 'max')
AGGREGATIONS = {
    'mean': mean,
    'stdev': stdev,
    'min': min,
    'max': max,
    'median': median,
    'harmonic_mean': harmonic_mean,
    'geo_mean': geo_mean,
    'perc1': perc1,
    'perc5': perc5,
    'perc95': perc95,
    'perc99': perc99,
    'variance': variance,
    'pvariance': pvariance,
}
