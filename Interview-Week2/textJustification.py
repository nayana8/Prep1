"""
Given an natural language text, write an algorithm which will format the text by splitting it into lines of a specified length, with each line justified such that the text is evenly spaced according to specific rules.

Inputs:

String text - the text to format
int length - the line length for the output
Output: a String[] that meets the following requirements:

Each line should have exactly length characters, including whitespace
Each line should contain as many words as will fit, and the algorithm should return as few lines as possible
Each line should be padded with spaces, distributed as evenly as possible
If the number of spaces required to pad a line do not divide evenly between words, add the extra spaces between the leftmost words first
The last line of the output should be left justified, with no extra spaces between words and all padding added to the right.
Example:

Given the inputs:

String text = "This is an example of text justification.";
int length = 16;
...the output array should be:

String[] output = {
  "This    is    an",
    "example  of text",
      "justification.  "
      };
"""

def textJustify(sentence, n):
    lines = []

    if len(sentence) <= n:
        return sentence

    words = sentence.split()
    arr = []
    arr.append(words[0])
    line = ""
    space = 0
    remSpaces = 0
    q = 0
    r = 0
    length = len(words[0])
    for i in range(1,len(words)):
        word = words[i]
        if len(word)+length+1 <= n:
            arr.append(word)
            length += 1+len(word)  # 1 is for space.
            space += 1
        else:
            if length < n:
                if len(arr) == 1:
                    line += arr[0]
                else:
                    remSpaces = n - length
                    if space != 0:
                        q = remSpaces / space
                        r = remSpaces % space
                    else:
                        q = 0
                        r = 0
                    for j in range(len(arr)):
                        wrd = arr[j]
                        line += wrd
                        if r > 0:
                            sp = q+1+r
                            r -= 1
                        else:
                            sp = q+1
                        if len(line) < n:
                            line += " " * sp
            lines.append(line)
            arr = []
            line = ""
            space = 0  
            remSpaces = 0
            q = 0
            r = 0
            length = 0
            arr.append(word)
            length = len(word)

    if length < n:
        if len(arr) == 1:
            line += arr[0]
        else:
            remSpaces = n - length
            if space != 0:
                q = remSpaces / space
                r = remSpaces % space
            else:
                q = 0
                r = 0
            for i in range(0,len(arr)-1):
                wrd = arr[i]
                line += wrd
                if r > 0:
                    sp = q+1+r
                    r -= 1
                else:
                    sp = q+1
                if len(line) < n:
                    line += " " * sp
    lines.append(line)

    print lines

def main():
    text = "This is an example of text justification."
    textJustify(text,16)

if __name__ == "__main__":
    main()
