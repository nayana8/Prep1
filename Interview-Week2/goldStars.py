"""
Alice is a teacher with a class of n children, each of whom has been assigned a numeric rating. The classroom is seated in a circular arrangement, with Alice at the top of the circle. She has a number of gold stars to give out based on each child's rating, but with the following conditions:

Each child must receive at least one gold star
Any child with a higher rating than his or her immediate neighbor should get more stars than that neighbor
Assuming n >= 3, what is the minimum total number of stars Alice will need to give out?

Write a program which takes as its input an int[] containing the ratings of each child, ordered by seating position, and returns an int value for the minimum total number of stars that Alice will need to give out.

Hint: this problem can be solved with an algorithm that runs in O(n) time.

For example:

In a class of three children with ordered ratings of {1, 2, 2}, Alice will need to give out {1, 2, 1} stars accordingly, for a total number of 4 stars overall
"""

import sys

def getStars(arr):
    if len(arr) == 0:
        return 0

    if len(arr) == 1:
        return 1

    stars = []
    if arr[0] > arr[1]:
        stars.append(2)
    else:
        stars.append(1)

    for i in range(1,len(arr)):
        cur = arr[i]
        neigh = arr[i-1]

        if neigh >= cur:
            stars.append(stars[i-1]-1)
        else:
            stars.append()
            stars.append(stars[i-1]+1)

    #print stars
    totalStars = 0
    for i in range(len(stars)):
        if stars[i] <= 0:
            totalStars += i + 1
        else:
            totalStars += stars[i]
        #print totalStars

    return totalStars

def main():
    arr = [7,6,5,4,3,2]
    res = getStars(arr)
    print res

if __name__ == "__main__":
    main()
        
