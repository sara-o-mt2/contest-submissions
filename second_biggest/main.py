"""
ソート関数を使わずに
配列から2番目に大きい数を取得する関数を実装せよ
"""

def get_max_num(num_list):
    """
    配列の中で1番大きい数を返す

    Arguments:
        num_list {list}
    """
    num = num_list[0]

    for i in num_list:
        if num <= i:
            num = i

    result = num

    return result


def get_second_biggest_num(num_list):
    """
    配列の中で2番目に大きい数を返す

    Arguments:
        num_list {list}
    """
    remove_max_list = num_list

    for i in range(2):
        max_num = get_max_num(remove_max_list)

        remove_max_list = [n for n in remove_max_list if n != max_num]

    result = max_num

    print(result)
    # 5


get_second_biggest_num([3, 5, 4, 6, 1, 1, 5, 6])