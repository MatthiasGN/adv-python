# adv-python
Learning for advanced python concepts.

## Lambda Function
An anonymous function or function without name, defined and called in the same line of code. Called with keyword **lambda** followed by parameter, semi-colon, function method, and output. Example:
```
>>> (lambda x: x**2)(5)
>>> 25
```
- It can only contain expressions, no statements in the body. This means no `return`, `assert`, etc.
- It is known as an **IIFE** (**Immediately Invoked Function Expression**) - pronounced 'iffy'.

---



### List Filter with Lambda
A simple use of the lambda function is to filter a list. Python has a built-in function that takes a function in as a parameter: `filter(function, iterable)`. Let's use this to get a list of integers divisible by 3 from the integers 0-100.\

```
nums = list(range(0,101))
print(nums)
# [0, 1, 2, ..., 99, 100]

triples = list(filter(lambda x:x%3 == 0, nums))
print(triples)
# [0, 3, 6, ..., 96, 99]
```

Slightly more complex - filter **out** integers from 0-100 which are divisible by 2 or 3.
```
filtered_nums = list(filter(lambda x:not(x%2 == 0 or x%3 == 0), nums))
print(filtered_nums)
# [1, 5, 7, ..., 95, 97]
```

---
### Lambda with `map()`
Python's `map()` function is used to operate the passed lambda function on each item in an iterable list. For example, for adding the square and cube of each number in a list the lambda function will be:
```
lambda x:x**2 + x**3
```

Using this together with map:
```
nums = list(range(0,101))
mapped_list = list(map(lambda x:x**2 + x**3, nums))
print(mapped_list)
# [0, 2, 12, ..., 980100, 1010000]
```

---
As you can see, lambdas are very useful in cleaning up code and using fewer lines. Take care that you don't overcomplicate a single line though, readability is important.\
\
Adapted from Suraj Gurav's **Lambda Functions in Python: All You Need To Know**, https://towardsdatascience.com/lambda-functions-with-3-practical-examples-in-python-f4ed7f266e53.

---
## Hashing
We say an object is **hashable** if it has a hash value which never changes during its lifetime. All of Python's immutable built-in objects are hashable (e.g. ints, floats, strings) while mutable containers (e.g. lists, dictionaries) are not. Note that tuples are immutable containers and thus hashable.

### Hash Tables
- A data structure where the address or index of the data element is generated from a hash function.
- This makes accessing the data faster as the hash-generated index acts as a key for the data value.
- So instead of accessing an element by going index by index through an array, elements are accessed directly by this hash-generated key.
- In Python, a simple hash table is implemented using a dictionary.
- However, you can make your own using a **Linked List** and a custom hashing function.
- **Collisions** need to be accounted for. Two different strings might hash to the same value, or two different strings might have different hashcodes but the same index.
- The time complexity for insert, find & delete is generally `O(1)`, but can be `O(n)` for a terrible hash table.\

```
hash_table = dict()
hash_table["Damian Lillard"] = Player(team = "POR", age = 32, height = "6ft2")
```

### Sets
- Sort of list data structure
- Forbids duplicates
- Requires items to be **hashable**
- Checking for membership of a value in a `set` is very fast, with the same speed as checking the keys in a `dict` (i.e. hash table speeds!). Meanwhile a list takes time proportional to the list's length (`O(n)` worst case).
- So, if you have hashable items and don't care about order or duplicates, use `set` rather than `list` or `dict`.

---
### Useful Methods
Max Size
```
import sys

max_sz = sys.maxsize
list = range(max_sz)
print(len(list))
# 9223372036854775807
```
