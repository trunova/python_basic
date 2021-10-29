alphabet = 'abcdefghijklmnopqrstuvwxyz'
text_file = open('text.txt', 'r')
cipher_text_file = open('cipher_text.txt', 'a')
k = 1
for i_line in text_file:
    for i_letter in i_line:
        if i_letter == '\n':
            cipher_text_file.write(i_letter)
            break
        i = alphabet.index(i_letter.lower()) + k
        if i > len(alphabet) - 1: i -= len(alphabet)
        newLetter = alphabet[i]
        if i_letter != i_letter.lower(): newLetter = newLetter.upper()
        cipher_text_file.write(newLetter)
    k += 1
text_file.close()
cipher_text_file.close()