import pytest

from probabilistic_data_structures.membership.bloom_filter import BloomFilter
from probabilistic_data_structures.membership.counting_bloom_filter import CountingBloomFilter


@pytest.fixture(scope="function")
def bloom_filter():
    return BloomFilter(1_000_000, 0.02)


@pytest.fixture(scope="function")
def counting_bloom_filter():
    return CountingBloomFilter(1_000_000, 0.02)
