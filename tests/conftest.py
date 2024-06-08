from pytest import fixture

from probabilistic_data_structures.membership.bloom_filter import BloomFilter
from probabilistic_data_structures.membership.counting_bloom_filter import CountingBloomFilter
from probabilistic_data_structures.frequency.count_min_sketch import CountMinSketch

@fixture(scope="function")
def bloom_filter():
    return BloomFilter(1_000_000, 0.02)


@fixture(scope="function")
def counting_bloom_filter():
    return CountingBloomFilter(1_000_000, 0.02)


@fixture(scope="function")
def count_min_sketch():
    return CountMinSketch(10, 5)
