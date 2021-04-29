test_list = ["a", "b", "c", "AAA", "aAa", "aB", "Ab", "ac", "aC", "AC"]

def count_list(l):
    lookup = {}
    ret_map = {}

    for v in l:
        # lookup key
        l_key = v.upper()

        if not l_key in lookup: lookup[l_key] = v

        # ret_map key
        rm_key = lookup[l_key]
        ret_map[rm_key] = ret_map.get(rm_key, 0) + 1

    return ret_map

print(count_list(test_list))