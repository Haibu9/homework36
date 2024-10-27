
def all_variants(text):
    for i in range(1, len(text) + 1):
        j0 = i / len(text)
        j1 = j0
        x = 0
        start = 0
        end = i
        while j1 <= 1:
            if i == 1:
                yield text[x]
                j1 += j0
                x += 1
            else:
                if end <= len(text):
                    y = []
                    for num in range(start, end):
                        y.append(text[num])
                    yield ''.join(y)
                    if start != 0:
                        j1 += j0
                    if end >= len(text):
                        j1 += 1
                    y = []
                    start, end = end, i + end
                else:
                    start, end = start - 1, end - 1

a = all_variants("abc")
for i in a:
    print(i)
"""Если логика не правильная, то пожалуйста напишите в коментарии что эта функция по вашему мнению должна выводить 
при запросе:
a = all_variants("abcd") # из 4 символов
for i in a:
    print(i)
"""