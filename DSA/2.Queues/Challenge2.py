"""Write a function named maxWindowSum that gets an array of integers (a) and a sliding window size (k), 
and returns the maximum sum in the sliding window."""

from queue import Queue


def maxWindowSum(a, k):
    # Write code here
    if not a or k <= 0 :
        return 0

    q = Queue()
    max_sum = float('-inf')
    current_sum = 0

    for item in a :

        q.enqueue(item)
        current_sum += item

        if q.size() > k:
            oldest_item = q.front()
            q.dequeue()
            current_sum -= oldest_item


        if q.size() == k:
            if current_sum > max_sum:
                max_sum = current_sum

    return  max_sum                    
