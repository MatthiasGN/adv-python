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
A simple use of the lambda function is to filter a list. Python has a built-in function that takes a function in as a parameter
