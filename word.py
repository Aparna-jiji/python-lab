linetext="this is a a sample text"
words={}
for word in linetext.split(" "):
    if word in words.keys():
        words[word]+=1
    else:
        words[word]=1
print(words)