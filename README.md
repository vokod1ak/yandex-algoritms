# yandex-algoritms
Практика по курсу алгоритмов в яндекс практикуме

## 1. Ближайший ноль (nearest_zero).
Улица, на которой хочет жить Тимофей, имеет длину n, то есть состоит из n одинаковых идущих подряд участков. На каждом участке либо уже построен дом, либо участок пустой. Тимофей ищет место для строительства своего дома. Он очень общителен и не хочет жить далеко от других людей, живущих на этой улице. Чтобы оптимально выбрать место для строительства, Тимофей хочет для каждого участка знать расстояние до ближайшего пустого участка. (Для пустого участка эта величина будет равна нулю –— расстояние до самого себя). Ваша задача –— помочь Тимофею посчитать искомые расстояния. Для этого у вас есть карта улицы. Дома в городе Тимофея нумеровались в том порядке, в котором строились, поэтому их номера на карте никак не упорядочены. Пустые участки обозначены нулями.

## 2. Ловкость рук (sleight_of_hand).
Гоша и Тимофей нашли необычный тренажёр для скоростной печати и хотят освоить его. Тренажёр представляет собой поле из клавиш 4× 4, в котором на каждом раунде появляется конфигурация цифр и точек. На клавише написана либо точка, либо цифра от 1 до 9. В момент времени t игрок должен одновременно нажать на все клавиши, на которых написана цифра t. Гоша и Тимофей могут нажать в один момент времени на k клавиш каждый. Если в момент времени t были нажаты все нужные клавиши, то игроки получают 1 балл. Найдите число баллов, которое смогут заработать Гоша и Тимофей, если будут нажимать на клавиши вдвоём.

## 3. Дек (deque).
Гоша реализовал структуру данных Дек, максимальный размер которого определяется заданным числом. Методы push_back(x), push_front(x), pop_back(), pop_front() работали корректно. Но, если в деке было много элементов, программа работала очень долго. Дело в том, что не все операции выполнялись за O(1). Помогите Гоше! Напишите эффективную реализацию. Внимание: при реализации нельзя использовать связный список.

## 4. Калькулятор (сalculator).
Задание связано с обратной польской нотацией. Она используется для парсинга арифметических выражений. Еще её иногда называют постфиксной нотацией. В постфиксной нотации операнды расположены перед знаками операций.

Пример 1:
3 4 + означает 3 + 4 и равно 7

Пример 2:
12 5 / Так как деление целочисленное, то в результате получим 2.

Пример 3:
10 2 4 * - означает 10 - 2 * 4 и равно 2

Разберём последний пример подробнее: Знак * стоит сразу после чисел 2 и 4, значит к ним нужно применить операцию, которую этот знак обозначает, то есть перемножить эти два числа. В результате получим 8.

После этого выражение приобретёт вид: 10 8 - Операцию «минус» нужно применить к двум идущим перед ней числам, то есть 10 и 8. В итоге получаем 2.

Рассмотрим алгоритм более подробно. Для его реализации будем использовать стек. Для вычисления значения выражения, записанного в обратной польской нотации, нужно считывать выражение слева направо и придерживаться следующих шагов:

Обработка входного символа: Если на вход подан операнд, он помещается на вершину стека. Если на вход подан знак операции, то эта операция выполняется над требуемым количеством значений, взятых из стека в порядке добавления. Результат выполненной операции помещается на вершину стека.
Если входной набор символов обработан не полностью, перейти к шагу 1.
После полной обработки входного набора символов результат вычисления выражения находится в вершине стека. Если в стеке осталось несколько чисел, то надо вывести только верхний элемент. Замечание про отрицательные числа и деление: в этой задаче под делением понимается математическое целочисленное деление. Это значит, что округление всегда происходит вниз. А именно: если a / b = c, то b ⋅ c — это наибольшее число, которое не превосходит a и одновременно делится без остатка на b. Например, -1 / 3 = -1. Будьте осторожны: в C++, Java и Go, например, деление чисел работает иначе. В текущей задаче гарантируется, что деления на отрицательное число нет.
