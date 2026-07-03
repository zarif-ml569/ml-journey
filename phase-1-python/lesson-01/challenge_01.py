original = [1,2,3]
print(f"original = {original}")

alias = original
print(f"alias = {alias}")

real_copy = alias.copy()
print(f"real_copy = {real_copy}")

alias.append(999)
real_copy.append(777)

print(f"original = {original}")
print(f"alias = {alias}")
print(f"real_copy = {real_copy}")

print(f"original is alias? {original is alias}")
print(f"original is real_copy? {original is real_copy}")

# Why original changed when I modified alias, but didn't change when I modified real_copy?
# Original changed because both tags (variables) were pointing to the same object,
# so modifying it through either name changes the one shared object.
# real_copy pointed to a separate, independent object created by .copy(),
# so modifying real_copy has no effect on original.