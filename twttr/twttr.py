
def main():
    sentence = input("Input: ").strip()
    print(f'Output: {shorten(sentence)}')


def shorten(sentence):
    vowels = {"a", "e", 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    result = ''.join(char for char in sentence if char not in vowels)
    return result
