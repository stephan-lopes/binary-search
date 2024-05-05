def binary_search(lista: list, s: str) -> bool:
    first = 0
    last = len(lista) - 1
    while last >= first:
        mid = (first + last) // 2
        if lista[mid] == s:
            return True
        else:
            if ord(s[0]) < ord(lista[mid][0]):
                last = mid - 1
            else:
                first = mid + 1
    return False


if __name__ == "__main__":
    print(binary_search(["apple", "banana", "orange", "plum"], "banana"))