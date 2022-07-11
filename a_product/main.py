"""
a と b の積が偶数か奇数か判定

問題文
https://atcoder.jp/contests/abc086/tasks/abc086_a
"""
a, b = map(int, input().split())

if (a * b) % 2 == 0:
    print("Even")
else:
    print("Odd")
