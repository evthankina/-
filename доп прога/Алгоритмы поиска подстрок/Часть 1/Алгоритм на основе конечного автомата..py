def build_automaton(pattern):
    m = len(pattern)
    automaton = {i: {} for i in range(m + 1)}  # Создаем словарь состояний
    automaton[0][pattern[0]] = 1  # Первый переход для первого символа шаблона

    # Заполняем переходы для остальных состояний
    for i in range(1, m):
        for char in range(ord('a'), ord('z') + 1):  # Перебираем все символы
            automaton[i][chr(char)] = automaton[0][chr(char)]  # Переход по символу в начальное состояние
        automaton[i][pattern[i]] = i + 1  # Переход по символу шаблона в следующее состояние

    return automaton


def finite_automaton_search(text, pattern):
    automaton = build_automaton(pattern)  # Строим автомат
    n = len(text)
    m = len(pattern)
    state = 0  # Начальное состояние автомата
    result = []  # Список найденных совпадений

    for i in range(n):
        state = automaton[state].get(text[i], 0)  # Проверяем переход по текущему символу
        if state == m:  # Если достигнуто состояние, соответствующее длине шаблона
            result.append(i - m + 1)  # Добавляем индекс начала совпадения

    return result


# Пример использования
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
indexes = finite_automaton_search(text, pattern)
print("Индексы совпадений:", indexes)