def compute_prefix_function(pattern):
    m = len(pattern)
    prefix_function = [0] * m
    k = 0
    for i in range(1, m):
        while k > 0 and pattern[i] != pattern[k]:
            k = prefix_function[k - 1]
        if pattern[i] == pattern[k]:
            k += 1
        prefix_function[i] = k
    return prefix_function


def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    result = []

    # Вычисляем префиксную функцию для шаблона
    prefix_function = compute_prefix_function(pattern)

    # Основной цикл поиска
    i = 0
    j = 0
    while i < n:
        while j > 0 and text[i] != pattern[j]:
            j = prefix_function[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            result.append(i - m + 1)
            j = prefix_function[j - 1]
        i += 1

    return result


# Пример использования
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
indexes = kmp_search(text, pattern)
print("Индексы совпадений:", indexes)