def index_words(text: str) -> list:
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result


def index_words_iter(text: str) -> iter:
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1


WORD = 'my word is none'
it = index_words_iter(WORD)
print(index_words(WORD))

print(next(it))


def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == ' ':
                yield offset


LETTER = '''
het fdsfdsf 
dsadasd fgdfdf
fdsfsd
'''
it = index_file(LETTER)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
