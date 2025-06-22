# print each element of list.
num=[1,2,3]
iter_num = iter(num)
print(next(iter_num))
print(next(iter_num))
print(next(iter_num))

# Each call to next() returns the next element in the iterator.
# The iter() function in Python is used to create an iterator from an iterable object


iter_num = iter(num)
iter_num2 = iter(iter_num)


class mr:
    def __init__(self,start,end):
        self.start=start
        self.end=end

    def __iter__(self):
        return mri()
    
class mri:
    def __init__(self,iterable_obj):
        self.iterable=iterable_obj
    def __iter__(self):
        return self
    def __next__(self):
        if self.iterble.start >= self.iterble.end:
            raise StopIteration
        current = self.iterable.start
        self.iterable.start+=1
        return current
    
    