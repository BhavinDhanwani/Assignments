# Write a Python function that takes a list of words and returns the length of the longest one.

a=["bhavin","karan","ashutosh","shivarsh"]

long_word=""
long_len=0

for word in a:
    # print(word)
    length=0

    for alpha in word:
        # print(alpha)
        length+=1

    if length>long_len:
        long_len=length
        long_word=word

if long_len>0:
    print("Longest word is: ",long_word)
    print("The length is: ",long_len)