file_handle = open('SMSSpamCollection.txt')

ham_word_total = 0
spam_word_total = 0
ham_message_count = 0
spam_message_count = 0
spam_exclamation_count = 0


for line in file_handle:
    line = line.rstrip()
    words = line.split()

    if words[0] == "ham":
        ham_word_total += len(words) - 1
        ham_message_count += 1

    elif words[0] == "spam":
        spam_word_total += len(words) - 1
        spam_message_count += 1

        if words[-1][-1] == '!':
            spam_exclamation_count += 1 

print(f"Ham prosjek: {ham_word_total / ham_message_count}")
print(f"Spam prosjek: {spam_word_total / spam_message_count}")
print(f"Spam s '!': {spam_exclamation_count}")