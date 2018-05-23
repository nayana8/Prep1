import sys

def removePunctuations(string):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for ch in string:
        if ch in punctuations:
            string = string.replace(ch, "")
    return string.lower()

def wordCount(string):
    string = removePunctuations(string)
    words = string.split(" ")

    hashMap = {}
    for word in words:
        if word in hashMap:
            hashMap[word] += 1
        else:
            hashMap.setdefault(word, 1)
    return hashMap

def multiMaps(hashMap):
    newHash = {}
    for key in hashMap:
        val = hashMap[key]
        if val in newHash:
            newHash[val].append(key)
        else:
            newHash[val] = [key]
    return newHash

def main():
    string = "To be or not to be, that is the question"
    hashMap =  wordCount(string)
    print hashMap

    multimap = multiMaps(hashMap)
    print multimap

if __name__ == "__main__":
    main()
