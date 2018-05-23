import sys

def longestNonRepeating(word):
    hashMap = {}
    maxL = 1
    start = 0

    for i,ch in enumerate(word):
        if ch in hashMap and start <= i:
            maxL = max(maxL, i - start)
            start = i
        else:
            hashMap[ch] = True

    maxL = max(maxL, len(word)-start)
    return maxL

def main():
    word = "abcabcbb"
    print longestNonRepeating(word)

    word = "aaaaaaaa"
    print longestNonRepeating(word)

if __name__ == "__main__":
    main()
