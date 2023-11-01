from gendiff.generator import generate_diff


result1 = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
result2 = """{
    follow: false
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}"""


def test_generate_diff_json():
    assert generate_diff("tests/fixtures/test1.json", "tests/fixtures/test2.json") == result1
    assert generate_diff("tests/fixtures/test1.json", "tests/fixtures/test3.json") == result2


def test_generate_diff_yaml():
    assert generate_diff("tests/fixtures/test1.yml", "tests/fixtures/test2.yml") == result1
    assert generate_diff("tests/fixtures/test1.yml", "tests/fixtures/test3.yml") == result2