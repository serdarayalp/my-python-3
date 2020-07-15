def compare_num_of_chars(txt):
    return len(txt)

word_list = ['Python', 'is', 'better', 'than', 'C']

word_list.sort()
print(word_list)

word_list = ['Python', 'is', 'better', 'than', 'C']
word_list.sort(key=compare_num_of_chars)
print(word_list)


