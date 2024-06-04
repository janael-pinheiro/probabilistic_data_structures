def test_bloom_filter_may_contains(bloom_filter):
    element: str = "xpto"
    bloom_filter.add(element)
    may_contains = bloom_filter.may_contains(element)
    assert may_contains is True
    assert element in bloom_filter


def test_bloom_filter_not_contains(bloom_filter):
    element: str = "abcd"
    bloom_filter.add("xpto")
    may_contains = bloom_filter.may_contains(element)
    assert may_contains is False
    assert element not in bloom_filter
