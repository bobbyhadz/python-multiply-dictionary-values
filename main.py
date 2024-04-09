# Multiply dictionary values by a constant in Python

my_dict = {'a': 2, 'b': 3, 'c': 4}

# ✅ multiply dictionary values by number (in place)
my_dict.update(
  (key, value * 2) for key, value in my_dict.items()
)

# 👇️ {'a': 4, 'b': 6, 'c': 8}
print(my_dict)