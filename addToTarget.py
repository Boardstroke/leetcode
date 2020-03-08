# Worst case scenario the algorithm is of O(n^2) for time complexity, but for space we have constant time
# Brute force try
def nonRepeat(arr):
  for el in arr:
    if(arr.count(el) > 1):
      arr.remove(el)

def forceBrute(arr, target):
  for i in range(0,len(arr)):
    for j in range(i+1, len(arr)):
      if (arr[i] + arr[j] == target):
        return [i,j]

  return -1


# Using hash to find improve the time complexity, but by other hand we have to storage n elements
def storageInHash(arr):
  dic = {}
  for i in range(0, len(arr)):
    dic[arr[i]] = i

  return dic

def searchInHash(h, target):
  for el in h.keys():
    complement = target - el
    if(complement in h.keys()):
      return [h[el], h[complement]]


def main():
  arr = [2,3,6,8]

  h = storageInHash(arr)
  print(searchInHash(h, 5))

if __name__ == "__main__":
    main()