from array_string.lovanto.is_unique_string import (
    is_unique_string_with_bit_vector,
    is_unique_string_with_hashmap,
)


def test_is_unique_string_with_hashmap():
    str_1 = "abcd10jk"
    str_2 = "hutg9mnd!nk9"
    result_str_1 = is_unique_string_with_hashmap(str_1)
    assert result_str_1
    result_str_2 = is_unique_string_with_hashmap(str_2)
    print("result_str_2 ", result_str_2)
    assert not result_str_2


def test_is_unique_string_with_bit_vector():
    str_1 = "abcd10jk"
    str_2 = "hutg9mnd!nk9"
    result_str_1 = is_unique_string_with_bit_vector(str_1)
    assert result_str_1
    result_str_2 = is_unique_string_with_bit_vector(str_2)
    print("result_str_2 ", result_str_2)
    assert not result_str_2
