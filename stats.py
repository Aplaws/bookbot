def count_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

def char_count(text):
    low_text = text.lower()
    char_count_dic = {}
    for char in low_text:
        if char not in char_count_dic:
            char_count_dic[char] = 1
        else:
            char_count_dic[char] += 1
    return char_count_dic

def sort_on(items):
    return items["num"]

def sort_char(dic):
    list = []
    for i in dic:
        list.append({"char" : i,"num" : dic[i]})
    list.sort(reverse=True, key=sort_on)
    return list 
