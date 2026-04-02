word_count = {}

with open("song.txt") as song_file:
    for line in song_file:
        line = line.rstrip()   
        words = line.split()   
        
        for word in words:
            if word not in word_count:
                word_count[word] = 1
            else:
                word_count[word] += 1

unique_words = 0
for word in word_count:
    if word_count[word] == 1:
        unique_words += 1
        print(f"{word} : {word_count[word]}")

print("Broj riječi koje se pojavljuju samo jednom:", unique_words)