paragraph = 'cat dog mouse cat rat cat mouse'
counts = {}
for word in paragraph.split():
    counts[word] = counts.get(word,0) + 1
for word,count in counts.items():
    print(word, count)
