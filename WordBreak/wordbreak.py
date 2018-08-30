import sys

words = list()
n = None
split_seq = None 
answer = list()

def append_answer(word):
    answer.append(word)

def append(word):
    words.append(word)

def dict(w):
    if w in words:
        return True
    return False

def iterative_attempt(x):
    global n
    n = len(x)
    
    global split_seq
    split_seq = [False] * (n+1)
    split_seq[n] = True

    for i in range(n, -1, -1):
        for j in range(i, n, 1):
            if dict(x[i:j+1]) is True and split_seq[j+1] is True:
                split_seq[i] = True

    if split_seq[0] is True:
        print("YES, can be split")
        for i in range(0, n+1):
            for j in range(i, n+1, 1):
                if dict(x[i:j+1]) is True and split_seq[j+1] is True:
                    print(x[i:j+1], end=' ')
                    i = j+1
                    if j+1 == n:
                        print('\n\n')
                        return 
    else:
        print("NO, cannot be split")
        print('\n')
        return            


def driver():
    # Get all of the lines from the given file
    lines = list()
    num_lines = int(sys.stdin.readline().strip())
    for i in range(num_lines):
        line = str(sys.stdin.readline().strip())
        lines.insert(i, line)

    # Store all of the words from the dictionary file
    f = open('dictionary.txt', 'r').read().splitlines()
    for line in f:
        append(str(line))

    # Print solutions
    for i in range(0, num_lines, 1):
        print("phrase number:", i+1)
        print(lines[i])
        print()
        print("iterative attempt:")
        iterative_attempt(lines[i])

if __name__ == "__main__":
    driver()
