def hash_function(key):
     return sum(
         index * ord(character)
         for index, character in enumerate(repr(key).lstrip("'"), 1)
     )
     