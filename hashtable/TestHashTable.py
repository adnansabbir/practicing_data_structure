from nose.tools import assert_equal
from hashtable.HashTable import HashTable

size = 10
HT = HashTable(size)

print("Checking Hash Function")
assert_equal(HT.hashfunction(10, size), 10 % size)
assert_equal(HT.hashfunction(0, size), 0 % size)
print("Hash Table Hash Function OK")

print("Checking ReHash Function")
assert_equal(HT.rehash(10, size), 11 % size)
assert_equal(HT.rehash(0, size), 1 % size)
print("Hash Table ReHash Function OK")


print("Checking Put Function")
for i in range(10):
    HT.put(i, "{}".format(i))
    assert_equal(HT.get(i), "{}".format(i))
for i in range(10):
    HT.put(i, "{}".format(i*10+i))
    assert_equal(HT.get(i), "{}".format(i*10+i))
print("Hash Table Put Function OK")