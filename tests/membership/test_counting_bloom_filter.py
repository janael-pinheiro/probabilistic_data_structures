def test_counting_bloom_filter_may_contains(counting_bloom_filter):
    counting_bloom_filter.add("xpto")
    may_contains = counting_bloom_filter.may_contains("xpto")
    assert may_contains is True


def test_counting_bloom_filter_not_contains(counting_bloom_filter):
    counting_bloom_filter.add("xpto")
    may_contains = counting_bloom_filter.may_contains("abcd")
    assert may_contains is False


def test_counting_bloom_filter_delete(counting_bloom_filter):
    element: str = "xpto"
    counting_bloom_filter.add(element)
    may_contains = counting_bloom_filter.may_contains(element)
    counting_bloom_filter.delete(element)
    may_contains_after_deleted = counting_bloom_filter.may_contains(element)
    assert may_contains is True
    assert may_contains_after_deleted is False
