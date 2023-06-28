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

As you can see, lambdas are very useful in cleaning up code and using fewer lines. Take care that you don't overcomplicate a single line though, readability is important.\
\
Adapted from Suraj Gurav's **Lambda Functions in Python: All You Need To Know**, https://towardsdatascience.com/lambda-functions-with-3-practical-examples-in-python-f4ed7f266e53.
