import csv
import io
import pytest
from processor import read_csv, filter_data, sort_data
from utils import aggregate, parse_aggregate

# Sample CSV content as string for testing
sample_csv_text = """name,brand,price,rating
iphone 15 pro,apple,999,4.9
galaxy s23 ultra,samsung,1199,4.8
redmi note 12,xiaomi,199,4.6
poco x5 pro,xiaomi,299,4.4
"""

# Helper: create list of dicts from CSV string
def make_fake_csv(text):
    return list(csv.DictReader(io.StringIO(text)))


def test_read_csv_from_file(tmp_path):
    file = tmp_path / "test.csv"
    file.write_text(sample_csv_text)

    data = read_csv(str(file))
    assert len(data) == 4
    assert data[0]["brand"] == "apple"
    assert data[1]["name"] == "galaxy s23 ultra"


def test_filter_numeric_gt():
    data = make_fake_csv(sample_csv_text)
    result = filter_data(data, "price>500")
    assert len(result) == 2
    assert all(float(row["price"]) > 500 for row in result)


def test_filter_string_equals():
    data = make_fake_csv(sample_csv_text)
    result = filter_data(data, "brand=xiaomi")
    assert len(result) == 2
    assert all(row["brand"] == "xiaomi" for row in result)


def test_sort_price_ascending():
    data = make_fake_csv(sample_csv_text)
    sorted_data = sort_data(data, "price=asc")
    prices = [float(row["price"]) for row in sorted_data]
    assert prices == sorted(prices)


def test_sort_name_descending():
    data = make_fake_csv(sample_csv_text)
    sorted_data = sort_data(data, "name=desc")
    names = [row["name"] for row in sorted_data]
    assert names == sorted(names, reverse=True)


def test_aggregate_avg_price():
    data = make_fake_csv(sample_csv_text)
    prices = [float(row["price"]) for row in data]
    avg_price = aggregate(prices, "avg")
    assert avg_price == sum(prices) / len(prices)


def test_aggregate_min_rating():
    data = make_fake_csv(sample_csv_text)
    ratings = [float(row["rating"]) for row in data]
    assert aggregate(ratings, "min") == 4.4


def test_aggregate_max_rating_for_xiaomi():
    data = make_fake_csv(sample_csv_text)
    filtered = filter_data(data, "brand=xiaomi")
    ratings = [float(row["rating"]) for row in filtered]
    max_rating = aggregate(ratings, "max")
    assert max_rating == 4.6


def test_combined_filter_sort_aggregate():
    data = make_fake_csv(sample_csv_text)
    filtered = filter_data(data, "brand=xiaomi")
    sorted_data = sort_data(filtered, "price=asc")
    prices = [float(row["price"]) for row in sorted_data]
    max_price = aggregate(prices, "max")
    assert max_price == 299.0


def test_parse_aggregate():
    col, op = parse_aggregate("price=avg")
    assert col == "price"
    assert op == "avg"


# -------------------
# ⚠️ Edge Case Tests
# -------------------

def test_filter_unknown_column_raises_keyerror():
    data = make_fake_csv(sample_csv_text)
    with pytest.raises(KeyError):
        filter_data(data, "notacolumn>100")


def test_aggregate_empty_list_raises_valueerror():
    with pytest.raises(ValueError):
        aggregate([], "avg")


def test_parse_aggregate_invalid_format_raises_valueerror():
    with pytest.raises(ValueError):
        parse_aggregate("badformatstring")
