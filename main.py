with open('D:\\number\\24.txt', "r+") as file:
    text = file.read()

all_words = {}

#list(all_words.keys())
for i in range(0, len(text)-1):
    if text[i] == "A" and i != len(text)-1:
        if text[i+1] in list(all_words.keys()):
            all_words[text[i+1]] += 1
        else:
            all_words.update({text[i+1]: 1})



max_value = max(all_words.values())
max_item = {k:v for k, v in all_words.items() if v == max_value}
print("Самый частовстречаемый символ: '{}'. Кол-во совпадений: {}".format(list(max_item.keys())[0], list(max_item.values())[0],))
