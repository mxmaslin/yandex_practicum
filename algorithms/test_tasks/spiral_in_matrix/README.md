# D. Разгадай шифр

Шерлок Холмс и доктор Ватсон передают друг другу зашифрованные сообщения, состоящие из чисел. Каждое число может обозначать одну букву, слово или знак препинания. Получая последовательность чисел, Холмс и Ватсон могут расшифровывать сообщения друг друга. Однако они стали подозревать, что кто-то разгадал их шифр и повысили уровень безопасности. Теперь каждое сообщение зашифровано в матрице. Чтобы его прочитать, нужно распечатать значения матрицы по спирали, начиная от центра вверх и далее по часовой стрелке.

## Формат ввода

Первая строка содержит целое нечётное число m в диапазоне от 1 до 1000 — количество строк и столбцов матрицы.
В каждой из следующих m строк даны m целых чисел в диапазоне от -1000 до 1000, разделённых пробелом.

## Формат вывода

Нужно вывести значения в матрице, начиная с центра по спирали. Движение вверх, далее по часовой стрелке. Каждое число выводится в отдельной строке.

### Пример 1

| Ввод | Вывод |
|---|---|
| 5 | 6 |
| 4 10 7 10 9 | 0 |
| 5 9 0 9 8 | 9 |
| 8 3 6 0 2 | 0 |
| 8 10 3 0 0 | 0 |
| 0 9 0 7 4 | 3 |
|   | 10 |
|   | 3 |
|   | 9 |
|   | 10 |
|   | 7 |
|   | 10 |
|   | 9 |
|   | 8 |
|   | 2 |
|   | 0 |
|   | 4 |
|   | 7 |
|   | 0 |
|   | 9 |
|   | 0 |
|   | 8 |
|   | 8 |
|   | 5 |
|   | 4 |

### Пример 2

| Ввод | Вывод |
|---|---|
| 3 | 7 |
| 9 10 7| 10 | 
| 0 7 7 | 7 |
| 8 3 4 | 7 |
|   | 4 |
|   | 3 |
|   | 8 |
|   | 0 |
|   | 9 |

[**Решение**]()