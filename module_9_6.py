def all_variants(text:str):
    k = len(text)
    for x in range(1, len(text)+1):
        for j in range(0, k):
            yield text[j:j+x]
        k -= 1

for m in all_variants('abc'):
    print(m)
