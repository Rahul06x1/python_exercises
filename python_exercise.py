import string

def fizzbizz(n):
    for i in range(1,n+1):
        if i%15==0:
            print('fizzbizz')
        elif i%5==0:
            print('bizz')
        elif i%3==0:
            print('fizz') 
        else:
            print(i)

def palindrome(s):
    return s == s[::-1]

def panagram(s):
    for letter in string.ascii_lowercase:
        if letter not in s.lower():
            return False
    return True

def freq(s):
    d = {}
    for charactor in s:
        if charactor in d:
            d[charactor] += 1
        else:
            d[charactor] = 1
    return d
    
def main():
    fizzbizz(9)
    print(palindrome('malayalam'))
    print(panagram("the quick brown fox jumps over the lazy dog"))
    print(freq("the quick brown fox jumps over the lazy dog"))

if __name__ == "__main__":
    main()
