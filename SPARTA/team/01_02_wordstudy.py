words = input().upper()
words_list = list(set(words))

count_list = []
for i in words_list:
    cnt = words.count(i)
    count_list.append(cnt)

if count_list.count(max(count_list)) > 1:
    print("?")
else:
    max_index = count_list.index(max(count_list))
    print(words_list[max_index])