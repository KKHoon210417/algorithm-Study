a = "accaaaccccceeeeeeeeeeeeeccccdasaaabbsADFcdasfaDDDDCAA"


def find_alphabet_occurrency(string):
    upper_string = string.upper()
    alphabet_occurrence_array = [0] * 26

    for char in upper_string:
        if not char.isalpha():
            continue
        char_index = ord(char) - ord("A")
        alphabet_occurrence_array[char_index] += 1

    max_occurence = 0
    max_alphabet_index = 0
    print(alphabet_occurrence_array)
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]
        if alphabet_occurrence > max_occurence:
            max_alphabet_index = index
            max_occurence = alphabet_occurrence

    count = 0
    for compare in alphabet_occurrence_array:
        if max_occurence == compare:
            count += 1

    if count >= 2:
        aaa = "?"
    else:
        aaa = chr(max_alphabet_index + ord("A"))

    return aaa

print(find_alphabet_occurrency(a))
