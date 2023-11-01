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

def test_generate_diff():
    assert generate_diff("tests/fixtures/test1.json", "tests/fixtures/test2.json") == result1
    assert generate_diff("tests/fixtures/test1.json", "tests/fixtures/test3.json") == result2
