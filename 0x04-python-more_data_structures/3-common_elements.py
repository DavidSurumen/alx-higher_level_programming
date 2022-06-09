#!/usr/bin/python3
def common_elements(set_1, set_2):
    if not set_1 or not set_2:
        return {}
    common = set()
    for i in set_1:
        for j in set_2:
            if j == i:
                common.add(j)
    return common
