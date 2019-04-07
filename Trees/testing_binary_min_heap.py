from Trees.BinaryMinHeap import BinaryHeap

bmh = BinaryHeap()
bmh.insert(9)
bmh.insert(8)
bmh.insert(7)
bmh.insert(6)
bmh.insert(5)
for i in range(bmh.currentsize):
    print(bmh.delete_min())

bmh.insert(9)
bmh.insert(8)
bmh.insert(7)
bmh.insert(6)
bmh.insert(5)

# print(bmh.delete_min())
print(bmh)