def is_unique_string_with_hashmap(target_str: str) -> bool:
    # with ascii
    NUMBER_OF_CHARS = 128
    if len(target_str) > NUMBER_OF_CHARS:
        return False
    else:
        flags = [False] * NUMBER_OF_CHARS
        for c in target_str:
            index = ord(c)
            if flags[index] is True:
                return False
            flags[index] = True
        return True


def is_unique_string_with_bit_vector(target_str: str) -> bool:
    vec = 0
    for c in target_str:
        bit_check = 1 << ord(c)
        if vec & bit_check > 0:
            return False
        vec = vec | bit_check
    return True
