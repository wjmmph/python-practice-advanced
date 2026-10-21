odd = {1, 3, 5, 7, 9}
even = {0, 2, 4, 6, 8}
prime = {2, 3, 5, 7}

#both methods don't modify in place
union = odd.union(even)
intersection = odd.intersection(even)
print(f"Union: {union}\nIntersection: {intersection}")