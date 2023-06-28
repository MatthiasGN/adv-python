nums = list(range(0,101))
print(nums)

triples = list(filter(lambda x:x%3 == 0, nums))
print(triples)

filtered_nums = list(filter(lambda x:not(x%2 == 0 or x%3 == 0), nums))
print(filtered_nums)

nums = list(range(0,101))
mapped_list = list(map(lambda x:x**2 + x**3, nums))
print(mapped_list)