def most_freq(arr):
    freq = {}
    for i in arr:
        freq[i] = freq.get(i, 0) + 1
    for i in freq:
        print("i is: ",i, "key is: ", freq.get(i))
    return max(freq, key = freq.get)

print(most_freq([1, 2, 3, 1, 2, 1]))

#Time Complexity: O(N), where N is the number of elements in arr.
# Building the dictionary takes O(N) time (dictionary lookups and insertions are O(1) on average).
# Finding the maximum key takes O(K) time, where K is the number of unique elements (K <= N).
# Space Complexity: O(K), where K is the number of unique elements stored in the dictionary 
# (worst case O(N) if all elements are distinct).