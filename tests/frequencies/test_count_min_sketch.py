from pytest import mark


@mark.parametrize("item, count", [("xpto", 9), ("abcd", 34), ("bit", 12)])
def test_count_min_sketch_estimate(count_min_sketch, item, count):
    count_min_sketch.update(item, count)
    actual: int = count_min_sketch.estimate(item)
    assert actual == count


@mark.parametrize("item, count", [("xpto", 9), ("abcd", 34), ("bit", 12)])
def test_count_min_sketch_estimate_item(count_min_sketch, item, count):
    count_min_sketch[item] = count
    actual: int = count_min_sketch[item]
    assert actual == count
