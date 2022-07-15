"""
1のマスがいくつあるか

問題文
https://atcoder.jp/contests/abc081/tasks/abc081_a
"""

def get_one_count(input_list):
    """
    1のマスの数を取得する
    """
    counter = 0

    if input_list[0] == '1':
        counter += 1
    if input_list[1] == '1':
        counter += 1
    if input_list[2] == '1':
        counter += 1

    return counter


def main():
    """
    main
    """

    print(get_one_count(list(input())))

main()
