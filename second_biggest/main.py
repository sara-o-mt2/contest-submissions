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

    return num


def get_second_biggest_num(num_list):
    """
    配列の中で2番目に大きい数を返す

    Arguments:
        num_list {list}
    """
    max_num = get_max_num(num_list)
    remove_max_list = [n for n in num_list if n != max_num]
    second_biggest_num = get_max_num(remove_max_list)

    return second_biggest_num


def main():
    """
    main
    """
    print(get_second_biggest_num([3, 5, 4, 6, 1, 1, 5, 6]))
    # 想定解: 5

main()
