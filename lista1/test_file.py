from vector import Vector

u = Vector()
v = Vector()

u.insert_el([1,1,1])
v.insert_el([1,2,3])

print(u, v)
print(u + v)
print(u - v)
print(v.scalar_mul(10))
print(u * v)
print(v.get_length())
print(v.get_sum())
print(v[2])
print(1 in v, 10 in v)
u.set_random_el()
print(u)

u.insert_el([0,0,0,0]) #ERROR
#u["g"] #ERROR


#help(Vector)