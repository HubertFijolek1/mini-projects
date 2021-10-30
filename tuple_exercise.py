#we check if all elements in a given tuple are in the other tuple

tuple1 = (3,4,5)
tuple2 = (1,2,3,4,5,6,7,8,9)

def check_tuples(tuple1, tuple2):
    for element in tuple1:
        if element not in tuple2:
            return False
    return True


print(check_tuples(tuple1, tuple2))

tuple3 = (5,3,2,456)
print(check_tuples(tuple3, tuple2))