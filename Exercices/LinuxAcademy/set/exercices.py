# 1. Write a Python program to create a set.
s = set([1,2,3,4])
print('1. Create:', s)

# 2. Write a Python program to iterate over sets.
print('2. Iterate: ', end='')
for n in s:
    print(n,' ', end='')

# 3. Write a Python program to add member(s) in a set.
s.add(5)
print('\n3. Add:', s)

# 4. Write a Python program to remove item(s) from set.
s.remove(3)
s.pop()     # first elt at left
print('4. Remove:', s)

# 5. Write a Python program to remove an item from a set if it is present in the set.
s.discard(3); s.discard(2)  # remove if exists
print('5. Discard:', s)

# 6. Write a Python program to create an intersection of sets.
setx = set(["green", "blue"])
sety = set(["blue", "yellow"])
print('  setx:',setx,'\n  sety:',sety)
print('6. Intersection of sets(&):', setx & sety)

# 7. Write a Python program to create a union of sets.
print('7. Union(|):', setx | sety)

# 8. Write a Python program to create set difference.
print('8. Difference(-):', sety - setx, sety.difference(setx))

# 9. Write a Python program to create a symmetric difference.
print('9. Symetric diff(^):', (setx|sety) - (setx&sety), setx ^ sety)

# 11. Write a Python program to create a shallow copy of sets.
setz = set(setx)
setzz = setx.copy()
setz.add(8)
print('11. Shallow copy:', setz, setzz, setx)

# 12. Write a Python program to clear a set.
setzz.clear()
print('12. Clear:', setzz)

# 13. Write a Python program to use of frozensets.
setz = frozenset(setz)
print('13. Frozenset(immutable):', setz)

# 14. Write a Python program to find maximum and the minimum value in a set.
s = set([1,2,3,4])
print('14. Max min:', max(s), min(s))

# 15. Write a Python program to find the length of a set.
print('15. Length:', len(s))

# 16. Write a Python program to check if a given value is present in a set or not. 
print('16. Value in:', 5 in s, 2 in s)

# 17. Write a Python program to check if two given sets have no elements in common.
x = {1,2,3,4}; y = {4,5,6,7}; z = {8}
print('17. Common elt(isdisjoint):', x.isdisjoint(y), x.isdisjoint(z), y.isdisjoint(z))

# 18. Write a Python program to check if a given set is superset of itself and superset of another given set.
x = {1,2,3,4,5,6,7,8,9}; y = {2,3,4,5,6}
print('18. Issuperset:', x.issuperset(x), x.issuperset(y), y.issuperset(x))

# 19. Write a Python program to find the elements in a given set that are not in another set.
sn1 = {1,2,3,4,5}; sn2 = {4,5,6,7,8}
print('19. Elts not in 2nd set:', sn1.difference(sn2), sn2 - sn1)

# 20. Write a Python program to check a given set has no elements in common with other given set.
sn1 = {1,2,3,4,5}; sn2 = {4,5,6,7,8}; sn3 = {0,9,10}
print('20. Isdisjoint:', sn1.isdisjoint(sn2), sn2.isdisjoint(sn3))

# 21. Write a Python program to remove the intersection of a 2nd set from the 1st set.
sn1 = {1,2,3,4,5}; sn2 = {4,5,6,7,8}
print('21. Remove inters:', sn1.difference(sn1&sn2))

