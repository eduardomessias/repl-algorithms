# Simple linear search
def linear_search(arr, val):
  for i in arr:
    if arr[i] == val:
      return i

print ("Simple linear search for 4 in [10, 56, 74, 9, 4]")
print (linear_search([10, 56, 74, 9, 4], 4))