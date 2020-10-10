# 斐波那契额数   (1,1,2,3,5,8,……)
# 尽量少用递归，因为效率不高
""" 递归：
1. 函数自己调用自己
2. 有明确的结束条件
3. 但凡可以用递归写的，循环都能解决
4. 递归有时候效率会很低，尽量少用
"""


# 菲波那切数 不使用递归版
def fibo_1(n):
    a = 1
    b = 1
    while n > 2:
        a, b = b, a + b
        n -= 1
    return b


# 斐波那契数 递归普通版
def fibo_2(n):
    before = 1
    after = 2
    if n == 1 or n == 2:
        return 1
    return fibo_2(n - 1) + fibo_2(n - 2)  # 使用递归，一定一定不要调两个递归，否则越往后递归，时间会呈指数式上升


# 斐波那契数 递归升级版
def fibo_3(n, a=1, b=1):
    if n == 1 or n == 2:
        return b
    else:
        a, b = b, a + b
        return fibo_3(n - 1, a, b)


# 斐波那契数列 生成器版本 牛逼plus
def fibo(n):
    if n == 1:
        yield 1
    else:
        yield from (1, 1)
        a, b = 1, 1
        while n > 2:
            a, b = b, a + b
            yield b
            n -= 1


if __name__ == "__main__":
    num = int(input("请输入需要的第n个斐波那契数:\n"))
    import time

    start_1 = time.time()
    a = fibo_1(num)
    end_1 = time.time()
    print(f"不使用递归获取第{num}个斐波那契数为{a}，使用了{end_1 - start_1}秒")

    start_2 = time.time()
    b = fibo_2(num)
    end_2 = time.time()
    print(f"使用递归普通版获取第{num}个斐波那契数为{b}，使用了{end_2 - start_2}秒")

    start_3 = time.time()
    c = fibo_3(num)
    end_3 = time.time()
    print(f"使用递归升级版获取第{num}个斐波那契数为{c}，使用了{end_3 - start_3}秒")

    start_4 = time.time()
    fibo_li = []
    for i in fibo(num):
        fibo_li.append(i)
    print(fibo_li)
    end_4 = time.time()
    print(f"使用生成器版获取斐波那契数列，使用了{end_4 - start_4}秒")

""" 运行结果
请输入需要的第n个斐波那契数:
25
不使用递归获取第25个斐波那契数为75025，使用了0.0秒
使用递归普通版获取第25个斐波那契数为75025，使用了0.039972782135009766秒
使用递归升级版获取第25个斐波那契数为75025，使用了0.0秒
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025]
使用生成器版获取斐波那契数列，使用了0.0秒
"""
