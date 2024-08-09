import datas

original_text = input("Put your text: ")
original_text = original_text.lower()

for key, value in datas.dict.items():
    original_text = original_text.replace(value, key)

print(original_text)
