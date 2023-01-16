
def censure ( lines:list[str], exclude_this: str = "ИЕ") -> list[str]:
    "убираем слова из текста"
    output = []
    for line in lines:
        passed = ""
        tmp = line.split(" ")
        for word in tmp:
            if exclude_this not in word:
                passed += f"{word} " 
        passed  =passed.rstrip(" ")
        if tmp[-1].endswith('\n'):
            passed += '\n'
        output.append(passed)

    return output


def main():
    with open("text_sample.txt",encoding="utf-8") as doc:
        text = doc.readlines()
    censure(lines =text)


if __name__ == "__main__":
    main()