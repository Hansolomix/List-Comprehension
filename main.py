'''
List Comprehension
'''

square = []
for x in range(10):
    square.append(x**2)
print(square)

# same result by using the method below

print( [x**2 for x in range(10)] )

#  =============

'''
Conditionals in list Comprehension
'''

combs = []
for x in [1,2,3]:
  for y in [3,1,4]:
    if x!=y:
      combs.append((x,y))
print(combs)

#  same results by using the method below

print([(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]) 

#  ===========

'''
Nested List Comprehension
'''

matrix = [ [1,2,3,4],
           [5,6,7,8],
           [9,10,11,12]
           ]
           
res= [[row [x]for row in matrix]for x in range(4)]

print(res)

# same result by using method below

matrix= [ [1,2,3,4],
          [5,6,7,8],
          [9,10,11,12] ]

res= []
for x in range(4):
  res.append([row[x] for row in matrix])

print(res)

# same results by using the method below

matrix = [ [1,2,3,4],
           [5,6,7,8],
           [9,10,11,12]
           ]
res=[]
 
for x in range(4):
    res_row=[]
    for row in matrix:
        res_row.append(row[x])
    res.append(res_row)

print(res)

# same result by using the method below (list.zip)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

res = list(zip(*matrix))
# [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
print(res)





