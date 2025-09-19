# Write a generator function that generates the first 10 even numbers


def even_numbers():
    num = 2
    count = 0
    while count < 10:
        yield num
        num += 2
        count += 1


for n in even_numbers():
    print(n)

print("*******************************************************************")

# Write a Python program that uses a custom iterator to iterate over a list of integers.

class ListIterator:
    """Custom iterator that walks through a list of integers."""
    def __init__(self, data):

        self._data = list(data)
        self._index = 0

    def __iter__(self):
  
        return self

    def __next__(self):
     
        if self._index >= len(self._data):
            raise StopIteration
        value = self._data[self._index]
        self._index += 1
        return value


if __name__ == "__main__":
    numbers = [10, 21, 32, 43, 54]


    print("Iterating with for-loop:")
    for num in ListIterator(numbers):
        print(num)

   
    print("\nManual iteration with next():")
    it = ListIterator(numbers)
    try:
        while True:
            print(next(it))
    except StopIteration:
        print("Reached the end of the iterator.")
