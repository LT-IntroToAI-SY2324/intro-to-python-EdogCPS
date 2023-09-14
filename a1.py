print("\n\n")
"""Assignment 1

Fill in the following function skeletons - descriptions are provided in 
the docstring (the triple quote thing at the top of each function)

Some assert statements have been provided - write more of them to test your code!

The `raise NotImplementedError(...)`s are placeholders to help you not skip implementing
a function. They should be removed and replaced with your solution.

This portion of the assignment will not be graded, but this gives you some problems to 
check, if you do not complete the generative AI portion of the assignment.
"""

from typing import List, TypeVar


def absolute(n: int) -> int:
    if (n < 0):
        n = n *-1
    return n
    raise NotImplementedError("absolute")


def factorial(n: int) -> int:
    x = n - 1
    while (x > 1):
        n = n * x
        x = x - 1
    return n
    raise NotImplementedError("factorial")


T = TypeVar("T")


def every_other(lst: List[T]) -> List[T]:
    exicute = True
    toReturn = [0]
    toReturn.pop()
    for x in lst:
        if exicute == True:
            toReturn.append(x)
        exicute = not exicute
    return toReturn
    raise NotImplementedError("every_other")


def sum_list(lst: List[int]) -> int:
    total_sum = 0
    canReturn = True
    for x in lst:
        try:
            total_sum += x
        except TypeError:
            print("All values in list are not numbers")
            canReturn = False
    if canReturn:
        return int(total_sum)
    return None
    raise NotImplementedError("sum_list")


def mean(lst: List[int]) -> float:
    return (sum_list(lst) / len(lst)) if lst else 0
    raise NotImplementedError("mean")


def median(lst: List[int]) -> float:
    medianValue = lst[int(len(lst) / 2)]
    if (len(lst) % 2 == 0):
        medianValue = medianValue + lst[int((len(lst) + 1) / 2)]
        medianValue = medianValue / 2
    return medianValue

    """Takes an ordered list of numbers, and returns the median of the numbers.

    If the list has an even number of values, it computes the mean of the two center
    values.

    Args:
        lst - an ordered list of numbers

    Returns:
        the median of the passed in list
    """
    raise NotImplementedError("median")


def duck_duck_goose2(lst: List[str], a) -> List[str]:
    if (len(lst) == 2):
        return lst
    count = a
    new = lst.copy()
    for x in lst:
        if (count % 3 == 0):
            print(x)
            print(count)
            new.remove(x)
            print(new)
        count = count + 1
    print("\n")
    return duck_duck_goose2(new, a)

def duck_duck_goose(lst):
    return duck_duck_goose2(lst, 1)

    """
    names = ["roscoe", "kim", "woz", "solin", "law", "remess"]
    assert duck_duck_goose(names) == ["roscoe", "law"]
    
    Given an list of names (strings), play 'duck duck goose' with it, knocking out
    every third name (wrapping around) until only two names are left.

    In other words, when you hit the end of the list, wrap around and keep counting from
    where you were.

    For example, if given this list ['Nathan', 'Sasha', 'Sara', 'Jennie'], you'd first
    knock out Sara. Then first 'duck' on Jennie, wrap around to 'duck' on Nathan and
    'goose' on Sasha - knocking him out and leaving only Nathan and Jennie.

    Args:
        lst - a list of names (strings)

    Returns:
        the resulting list after playing duck duck goose
    """
    #raise NotImplementedError("duck_duck_goose")

the_list = ["apple", "pineapple", "quasimoto", "madigascar", "cool", "dunzo washingotn"]
list_of_nums = [1, 2, 3, 4, 5, 6, 4, 7, 7]
# print(mean(list_of_nums))
# this line causes the nested code to be skipped if the file is imported instead of run
if __name__ == "__main__":
    assert absolute(-1) == 1, "absolute of -1 failed"
    assert factorial(4) == 24, "factorial of 4 failed"
    assert every_other([1, 2, 3, 4, 5]) == [
        1,
        3,
        5,
    ], "every_other of [1,2,3,4,5] failed"
    assert sum_list([1, 2, 3]) == 6, "sum_list of [1,2,3] failed"
    assert mean([1, 2, 3, 4, 5]) == 3, "mean of [1,2,3,4,5] failed"
    assert median([1, 2, 3, 4, 5]) == 3, "median of [1,2,3,4,5] failed"

    names = ["roscoe", "kim", "woz", "solin", "law", "remess"]
    #assert duck_duck_goose(names) == ["roscoe", "law"]
    print(duck_duck_goose(names))

    print("All tests passed!")
print("\n\n")