def count_letters(text: str):
    char_count = {}

    chars = "".join(char for char in text.lower() if char.isalpha())

    for char in chars:
        if char not in char_count:
            char_count[char] = 0
        if char in char_count:
            char_count[char] += 1

    sorted_dict = dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))

    for key, value in sorted_dict.items():
        print(f"The '{key}' character was found {value} times")


def main():
    with open("books/frankenstein.txt") as f:
        file_content = f.read()
        print(f'{len(file_content.split())} words found in the document')
        count_letters(file_content)
        print('--- End report ---')


if __name__ == "__main__":
    main()
