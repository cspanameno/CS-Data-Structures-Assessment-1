"""In the file called runtime.py, there are 5 functions.

What is the runtime for string_compare? Add your answer to the end of the function’s docstring.
What is the runtime for has_exotic_animals? Add your answer to the end of the function’s docstring.
What is the runtime for sum_zero_1? Add your answer to the end of the function’s docstring.
What is the runtime for sum_zero_2? Add your answer to the end of the function’s docstring.
What is the runtime for sum_zero_3? Add your answer to the end of the function’s docstring."""



def string_compare(s1, s2):
    """Given two strings, figure out if they are exactly the same (without using ==).

    Put runtime here:
    -----------------
    [      O(n)       ]


    """

    if len(s1) != len(s2): #O(1)
        return False #O(1)

    for i in range(len(s1)): #O(n)
        if s1[i] != s2[i]: #O(1)
            return False # O(1)

    return True #O(1)

    #O(1)*O(1) + O(n)*


def has_exotic_animals(animals):
    """Determine whether a list of animals contains exotic animals.

    Put runtime here:
    -----------------
    [         O(n)      ]

    """

    if "hippo" in animals or "platpypus" in animals: #O(n) + O(n)
        return True #O(1)
    else:
        return False #O(1)


def sum_zero_1(numbers):
    """Find pairs of integers that sum to zero.

    Put runtime here:
    -----------------
    [    O(n)           ]

    """

    result = [] #O(1)

    # Hint: the following line, "s = set(numbers)", is O(n) ---
    # we'll learn exactly why later
    s = set(numbers) #O(n)

    for x in s: #O(n)
        if -x in s: #O(1)
            result.append([-x, x]) #O(1)

    return result #O(1)


def sum_zero_2(numbers):
    """Find pairs of integers that sum to zero.

    Put runtime here:
    -----------------
    [     O(n^2)          ]

    """

    result = [] #O(1)

    for x in numbers: #O(n)
        for y in numbers: #O(n)
            if x == -y: #O(1)
                result.append((x, y)) #O(1)
    return result #O(1)


def sum_zero_3(numbers):
    """Find pairs of integers that sum to zero.

    This version gets rid of duplicates (it won't add (1, -1) if (-1, 1) already there.

    Put runtime here:
    -----------------
    [       O(n^3)      ]

    """

    result = [] #O(1)

    for x in numbers: #O(n)
        for y in numbers: #O(n)
            if x == -y and (y, x) not in result: #O(n)
                result.append((x, y)) #O(1)
    return result #O(1)
