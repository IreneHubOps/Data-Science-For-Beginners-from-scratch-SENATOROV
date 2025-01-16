"""Векторы в линейной алгебре."""

# # Векторы в линейной алгебре
#
# ## Оглавление:
# 1. [Основные понятия](#1-основные-понятия)
#    - [Представление векторов](#11-представление-векторов)
#    - [Виды векторов](#12-виды-векторов)
#    - [Свойства векторов](#13-свойства-векторов)
#
# 2. [Операции с векторами](#2-операции-с-векторами)
#    - [Сложение векторов](#21-сложение-векторов)
#    - [Геометрический смысл сложения](#22-геометрический-смысл-сложения)
#    - [Способы сложения векторов](#23-способы-сложения-векторов)
#    - [Представление в программировании](#24-представление-в-программировании)
#
# 3. [Коллинеарность векторов](#3-коллинеарность-векторов)
#    - [Определение коллинеарности](#31-определение-коллинеарности)
#    - [Типы коллинеарных векторов](#32-типы-коллинеарных-векторов)
#    - [Математическое описание](#33-математическое-описание)
#
# <h2 id="basic">1. Основные понятия</h2>
#
# <h3 id="representation">1.1 Представление векторов</h3>
# <p>Векторы обычно обозначаются строчными буквами, например v.
# # Существует несколько способов записи векторов:</p>
# <ul>
#     <li><strong>Строчная запись:</strong> v = (v₁, v₂, v₃)
#         <br>где v₁, v₂, v₃ - скалярные величины, обычно действительные числа
# в пространстве R³
#     </li>
#     <li><strong>Столбцовая запись:</strong>
#         <pre>
#         v = |v₁|
#             |v₂|
#             |v₃|
#         </pre>
#     </li>
# </ul>
#
# <h4>Координаты вектора на плоскости и в пространстве</h4>
# <p>В декартовой системе координат векторы характеризуются следующими
# понятиями:</p>
# <ul>
#     <li><strong>Координатные векторы:</strong>
#         <ul>
#             <li>Векторы, направленные вдоль координатных осей</li>
#             <li>Могут иметь произвольную длину</li>
#             <li>Используются для задания положения точки</li>
#         </ul>
#     </li>
#     <li><strong>Орты (единичные координатные векторы):</strong>
#         <ul>
#             <li>Обозначаются i и j на плоскости</li>
#             <li>Имеют единичную длину</li>
#             <li>Являются стандартным базисом системы координат</li>
#         </ul>
#     </li>
#     <li><strong>Базис:</strong>
#         <ul>
#             <li>Система координатных векторов</li>
#             <li>Позволяет однозначно задать любой вектор</li>
#             <li>Обычно используются орты как базисные векторы</li>
#         </ul>
#     </li>
#     <li><strong>Ортогональность:</strong>
#         <ul>
#             <li>Координатные векторы взаимно перпендикулярны</li>
#             <li>Предпочтительно использовать термин "ортогональные" вместо
# "перпендикулярные"</li>
#             <li>Обеспечивает независимость координат</li>
#         </ul>
#     </li>
# </ul>
#
# <p><em>Примечание:</em> Координатные векторы являются базисом для построения
# любых других векторов в заданной системе координат.</p>
#
# <h4>Орты и базис</h4>
# <p><strong>Основные определения:</strong></p>
# <ul>
#     <li>Орт вектор - это вектор, длина которого единица</li>
#     <li>Орт векторы образуют базис</li>
# </ul>
#
# <p><strong>В базисе плоскости:</strong></p>
# <ul>
#     <li>Орты обозначаются (i, j)</li>
#     <li>Они ортогональны (взаимно перпендикулярны)</li>
#     <li>Имеют единичную длину</li>
# </ul>
#
# <p>Любой вектор v можно разложить по базису: v = v₁i + v₂j</p>
# <p><em>Это называют разложением вектора по базису</em></p>
#
# <h4>Пример разложения векторов по базису</h4>
#
# <p><strong>На координатной плоскости показаны три вектора:</strong></p>
# <ul>
#     <li>Вектор a = (3, 2) = 3i + 2j
#         <br><em>Пояснение: вектор идёт на 3 единицы вправо (вдоль i) и
# на 2 единицы вверх (вдоль j)</em>
#     </li>
#     <li>Вектор b = (2, 0) = 2i + 0j


#         <br><em>Пояснение: вектор направлен только вдоль оси i
# на 2 единицы</em>
#     </li>
#     <li>Вектор c = (0, -5) = 0i - 5j
#         <br><em>Пояснение: вектор направлен только вдоль оси j вниз
# на 5 единиц</em>
#     </li>
# </ul>
#
# <p><strong>Важные наблюдения:</strong></p>
# <ul>
#     <li>Каждый вектор однозначно определяется своими координатами в базисе
# (i,j)</li>
#     <li>Первая координата показывает смещение по оси x (множитель при i)</li>
#     <li>Вторая координата показывает смещение по оси y (множитель при j)</li>
#     <li>Отрицательные координаты означают направление в противоположную
# сторону от соответствующего орта</li>
# </ul>
#
# <p><em>Примечание: Такое представление векторов через базисные векторы
# позволяет легко выполнять операции над векторами, используя их координаты.
# </em></p>
#
# <h4>Разложение векторов в системе ортов</h4>
#
# <p><strong>Различные способы записи векторов:</strong></p>
# <ul>
#     <li>Первый способ (покоординатная запись):
#         <br>d = (i, -4j)
#         <br>e = (-3i, -3j)
#         <br><em>Пояснение: запись через координаты при соответствующих
# ортах</em>
#     </li>
#     <li>Второй способ (алгебраическая запись):
#         <br>d = i + (-4j)
#         <br>e = -3(i + j)
#         <br><em>Пояснение: запись через сумму произведений координат на
# орты</em>
#     </li>
# </ul>
#
# <p><strong>Общая формула разложения вектора:</strong></p>
# <p>v = v₁i + v₂j</p>
# <p>где:</p>
# <ul>
#     <li>v₁ - координата вектора по оси x (проекция на i)</li>
#     <li>v₂ - координата вектора по оси y (проекция на j)</li>
#     <li>i, j - единичные векторы (орты) системы координат</li>
# </ul>
#
# <p><em>Примечание: Все эти способы записи эквивалентны и используются
# в зависимости от контекста задачи.</em></p>
#
# <h4>Векторы в трехмерном пространстве</h4>
#
# <p><strong>Координаты векторов:</strong></p>
# <ul>
#     <li>a(3, 2) - вектор в плоскости XY</li>
#     <li>b(2, 0) - вектор вдоль оси X</li>
#     <li>c(0, -5) - вектор вдоль оси Z</li>
#     <li>d(1, -4) - вектор в плоскости XY</li>
#     <li>e(-3, -3) - вектор в плоскости XY</li>
# </ul>
#
# <p><strong>Базисные векторы (орты):</strong></p>
# <ul>
#     <li>i = 1·i + 0·j - единичный вектор по оси X</li>
#     <li>j = 0·i + 1·j - единичный вектор по оси Y</li>
# </ul>
#
# <p><strong>Компактная запись координат ортов:</strong></p>
# <ul>
#     <li>i(1, 0) - координаты орта оси X</li>
#     <li>j(0, 1) - координаты орта оси Y</li>
# </ul>
#
# <p><em>Важные замечания:</em></p>
# <ul>
#     <li>Орты образуют правую тройку векторов</li>
#     <li>Все орты взаимно перпендикулярны</li>
#     <li>Длина каждого орта равна единице</li>
#     <li>Любой вектор можно представить как линейную комбинацию ортов</li>
# </ul>
#
# <h3 id="types">1.2 Виды векторов</h3>
# <ul>
#     <li><strong>Геометрический вектор</strong>
#         <br>Направленный отрезок, характеризующийся:
#         <ul>
#             <li>Длиной (модулем)</li>
#             <li>Направлением в пространстве</li>
#             <li>Точкой приложения</li>
#         </ul>
#     </li>
#     <li><strong>Свободный вектор</strong>
#         <br>Вектор, который можно переносить параллельно самому себе
# в любую точку пространства
#         <br>Характеризуется:
#         <ul>
#             <li>Длиной</li>
#             <li>Направлением</li>
#             <li>Не зависит от точки приложения</li>
#             <li>Все параллельные переносы вектора считаются одним
# и тем же вектором</li>
#         </ul>
#     </li>
#     <li><strong>Абстрактный вектор</strong>
#         <br>Математический объект, обладающий:
#         <ul>
#             <li>Величиной</li>
#             <li>Направлением</li>
#             <li>Подчиняется правилам векторной алгебры</li>
#         </ul>
#     </li>
#     <li><strong>Алгебраический вектор</strong>
#         <br>Упорядоченный набор чисел, с которым можно
# производить алгебраические операции:
#         <ul>
#             <li>Сложение</li>
#             <li>Вычитание</li>
#             <li>Умножение на скаляр</li>
#             <li>Скалярное произведение</li>
#         </ul>
#     </li>
# </ul>
#
# <h3 id="properties">1.3 Свойства векторов</h3>
# <ul>
#     <li><strong>Равные векторы</strong>
#         <br>Векторы равны, если они:
#         <ul>
#             <li>Имеют одинаковую длину</li>
#             <li>Одинаково направлены</li>
#             <li>Могут быть совмещены параллельным переносом</li>
#         </ul>
#     </li>
#     <li><strong>Нулевой вектор</strong>
#         <br>Особый случай вектора:
#         <ul>
#             <li>Начало и конец совпадают</li>
#             <li>Не имеет определенного направления</li>
#             <li>Длина (модуль) равна нулю</li>
#             <li>Сонаправлен с любым вектором</li>
#         </ul>
#     </li>
# </ul>
#
# <h2 id="operations">2. Операции с векторами</h2>
#
# <h3 id="addition">2.1 Сложение векторов</h3>
# <p>Два вектора можно сложить, получив третий вектор. Обозначается:
# c = a + b</p>
#
# <p>Правила сложения:</p>
# <ul>
#     <li>Новый вектор имеет ту же размерность, что и исходные векторы</li>
#     <li>Каждый элемент нового вектора получается сложением соответствующих
# элементов исходных векторов</li>
#     <li>Операция сложения коммутативна: a + b = b + a</li>
#     <li>Операция сложения ассоциативна: (a + b) + c = a + (b + c)</li>
# </ul>
#
# <p><strong>Примеры записи сложения:</strong></p>
# <ul>
#     <li>В координатной форме: c = (a₁ + b₁, a₂ + b₂, a₃ + b₃)</li>
#     <li>В программной записи:
#         <pre>
#         c[0] = a[0] + b[0]
#         c[1] = a[1] + b[1]
#         c[2] = a[2] + b[2]
#         </pre>
#     </li>
# </ul>
#
# <h3 id="geometric">2.2 Геометрический смысл сложения</h3>
# <p>Рассмотрим два произвольных ненулевых вектора a и b.
# Для нахождения их суммы:</p>
# <ol>
#     <li>Так как векторы свободные, можно перенести вектор b,
# отложив его от конца вектора a</li>
#     <li>Сумма векторов c = a + b - это вектор, идущий
# из начала вектора a в конец вектора b</li>
# </ol>
#
# <p><strong>Важные замечания:</strong></p>
# <ul>
#     <li>При сложении векторов используется свойство свободных векторов -
# возможность параллельного переноса</li>
#     <li>Результирующий вектор не зависит от выбора начальной точки</li>
#     <li>Длина суммы векторов может быть меньше суммы длин слагаемых
# векторов</li>
# </ul>
#
# <h3 id="methods">2.3 Способы сложения векторов</h3>
# <h4>Правило параллелограмма</h4>
# <p>Для сложения двух векторов необходимо:</p>
# <ol>
#     <li>Отложить от какой-нибудь точки A вектор AB, равный a</li>
#     <li>От точки A отложить вектор AC, равный b</li>
#     <li>Достроить фигуру до параллелограмма, проведя дополнительные линии
# параллельно данным векторам</li>
#     <li>Диагональ параллелограмма - сумма векторов c = a + b</li>
# </ol>
#
# <p><strong>Свойства параллелограмма:</strong></p>
# <ul>
#     <li>Противоположные стороны параллельны и равны</li>
#     <li>Диагонали точкой пересечения делятся пополам</li>
#     <li>Диагональ является геометрическим представлением суммы векторов</li>
# </ul>
#
# <h4>Правило ломаной</h4>
# <p>Альтернативный способ сложения векторов:</p>
# <ol>
#     <li>Векторы располагаются последовательно, начало каждого следующего
# вектора совпадает с концом предыдущего</li>
#     <li>Сумма векторов - вектор, идущий из начала первого вектора
# в конец последнего</li>
# </ol>
#
# <p><strong>Преимущества правила ломаной:</strong></p>
# <ul>
#     <li>Удобно при сложении более двух векторов</li>
#     <li>Не требует построения дополнительных линий</li>
#     <li>Наглядно показывает последовательность сложения</li>
# </ul>
#
# <p><em>Примечание:</em> Оба способа (параллелограмм и ломаная)
# дают одинаковый результат.</p>
#
# <h3 id="programming">2.4 Представление в программировании</h3>
# <p>Двумерный массив — это структура данных, которая представляет
# собой таблицу, состоящую из строк и столбцов.</p>
#
# <p><strong>Особенности представления векторов в программировании:
# </strong></p>
# <ul>
#     <li>Индексация обычно начинается с 0</li>
#     <li>Доступ к элементам осуществляется через индексы</li>
#     <li>Размерность массива должна быть определена заранее</li>
# </ul>
#
# <p><strong>Примеры обращения к элементам:</strong></p>
# <pre>
# array[0][0] = 1    // Первый элемент массива (первая строка, первый столбец)
# array[1][0]        // Второй элемент первого столбца
# array[2][0]        // Третий элемент первого столбца
# </pre>
#
# <h2 id="collinearity">3. Коллинеарность векторов</h2>
#
# <h3 id="definition">3.1 Определение коллинеарности</h3>
# <p>Два вектора называются коллинеарными, если они лежат на одной прямой
# или на параллельных прямых.</p>
#
# <p><strong>Основные признаки коллинеарности:</strong></p>
# <ul>
#     <li>Векторы параллельны одной прямой</li>
#     <li>Один вектор можно получить из другого умножением на число</li>
#     <li>Векторы могут быть направлены одинаково или противоположно</li>
#     <li>Обозначение коллинеарности: a || b</li>
# </ul>
#
# <h3 id="types_col">3.2 Типы коллинеарных векторов</h3>
# <ul>
#     <li><strong>Сонаправленные векторы</strong>
#         <br>Если два ненулевых вектора коллинеарны и направлены одинаково
#         <br>Характеристики:
#         <ul>
#             <li>Лежат на параллельных прямых или одной прямой</li>
#             <li>Направлены в одну сторону</li>
#             <li>Обозначение: a ↑↑ CD, b ↑↑ KF</li>
#             <li>Коэффициент пропорциональности положительный</li>
#         </ul>
#     </li>
#     <li><strong>Противоположно направленные векторы</strong>
#         <br>Если два ненулевых вектора коллинеарны и направлены
# противоположно
#         <br>Характеристики:
#         <ul>
#             <li>Лежат на параллельных прямых или одной прямой</li>
#             <li>Направлены в противоположные стороны</li>
#             <li>Обозначение: a ↑↓ b, a ↑↓ KF</li>
#             <li>Коэффициент пропорциональности отрицательный</li>
#         </ul>
#     </li>
#     <li><strong>Нулевой вектор</strong>
#         <br>Особый случай вектора:
#         <ul>
#             <li>Сонаправлен с любым вектором</li>
#             <li>Примеры: MM ↑↑ a, MM ↑↑ b</li>
#             <li>Начало и конец совпадают</li>
#             <li>Не имеет направления</li>
#             <li>Коллинеарен любому вектору</li>
#             <li>Длина равна нулю</li>
#         </ul>
#     </li>
# </ul>
#
# <h3 id="math">3.3 Математическое описание</h3>
# <p>Один вектор линейно выражен через другой. Примеры:</p>
# <ul>
#     <li><strong>e = √3a</strong>
#         <br>Вектор e получается из вектора a умножением на √3
# (корень из трех)
#         <br>Векторы e и a сонаправлены, так как √3 > 0
#         <br>Длина вектора e в √3 раз больше длины вектора a
#     </li>
#     <li><strong>b = (1/2)a</strong>
#         <br>Вектор b получается из вектора a умножением на 1/2
# (то есть b в два раза короче a)
#         <br>Векторы b и a сонаправлены, так как 1/2 > 0
#         <br>Длина вектора b в 2 раза меньше длины вектора a
#     </li>
#     <li><strong>d = -a</strong>
#         <br>Вектор d получается из вектора a умножением на -1
#         <br>Векторы d и a противоположно направлены, так как -1 < 0
#         <br>Векторы имеют одинаковую длину, но противоположное направление
#     </li>
# </ul>
#
# <h4>Коэффициент линейной зависимости</h4>
# <p><strong>-1 < λ < 1</strong> где λ (лямбда) определяет:</p>
# <ul>
#     <li>При λ > 0: векторы сонаправлены</li>
#     <li>При λ < 0: векторы противоположно направлены</li>
#     <li>При λ = 0: один из векторов нулевой</li>
#     <li>|λ| определяет отношение длин векторов</li>
# </ul>
#
# <p><strong>Важные свойства коллинеарных векторов:</strong></p>
# <ul>
#     <li>Если векторы коллинеарны, то они линейно зависимы</li>
#     <li>Коллинеарность - это взаимное свойство векторов</li>
#     <li>Если a || b и b || c, то a || c (транзитивность)</li>
#     <li>Нулевой вектор коллинеарен любому вектору</li>
# </ul>

# <h2 id="broadcasting">4. Броадкастинг (Broadcasting)
# в векторных операциях</h2>
#
# <h3 id="broadcasting-definition">4.1 Определение броадкастинга</h3>
# <p>Броадкастинг - это механизм, который позволяет выполнять арифметические
# операции между массивами разных размерностей или между массивом и скаляром.
# </p>
#
# <p><strong>Основные принципы броадкастинга:</strong></p>
# <ul>
#     <li>Автоматическое расширение размерности меньшего массива до
# размерности большего</li>
#     <li>Копирование значений вдоль новых осей</li>
#     <li>Выполнение поэлементных операций</li>
# </ul>
#
# <h3 id="broadcasting-rules">4.2 Правила броадкастинга</h3>
# <p><strong>Два основных правила:</strong></p>
# <ol>
#     <li>Если массивы имеют разное количество измерений, форма массива
# с меньшей размерностью дополняется единицами слева</li>
#     <li>Если форма массивов в каком-то измерении не совпадает, массив
# с размером 1 в этом измерении растягивается до большего размера</li>
# </ol>
#
# <h3 id="broadcasting-advantages">4.4 Преимущества броадкастинга</h3>
# <ul>
#     <li><strong>Эффективность памяти:</strong>
# Не требуется создавать копии данных</li>
#     <li><strong>Производительность:</strong>
# Оптимизированные векторные операции</li>
#     <li><strong>Читаемость кода:</strong>
# Упрощает написание векторизованных операций</li>
#     <li><strong>Гибкость:</strong> Позволяет работать
# с данными разных размерностей</li>
# </ul>
#
# <h3 id="broadcasting-applications">4.5 Практическое применение</h3>
#

# +
# Примеры использования броадкастинга в NumPy:
# 1. Операции скаляра с вектором
# 2. Операции векторов разной размерности
# 3. Операции матрицы с вектором
# 4. Нормализация матрицы
# 5. Масштабирование векторов

import numpy as np

# Пример 1: Скаляр и вектор
vector = np.array([1, 2, 3])
SCALAR = 2
result1 = vector * SCALAR
print("Скаляр * вектор:", result1)  # Выводит [2, 4, 6]

# Пример 2: Векторы разной размерности
v1 = np.array([1, 2, 3])  # Горизонтальный вектор формы (3,)
v2 = np.array([[4], [5], [6]])  # Вертикальный вектор формы (3,1)
result2 = v1 + v2
print("\nСложение векторов:\n", result2)

# Пример 3: Матрица и вектор
matrix = np.array([[1, 2, 3], [4, 5, 6]])  # Матрица размера 2x3
vector = np.array([10, 20, 30])
result3 = matrix + vector
print("\nМатрица + вектор:\n", result3)

# Пример 4: Нормализация матрицы
matrix_norm = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# Вычисляем среднее значение по каждому столбцу
column_means = matrix_norm.mean(axis=0)
# Вычитаем средние значения из каждой строки
normalized = matrix_norm - column_means
print("\nНормализованная матрица:\n", normalized)

# Пример 5: Масштабирование векторов
vectors = np.array([[1, 2, 3], [4, 5, 6]])
# Создаем вектор масштабирования и преобразуем в столбец
scales = np.array([10, 100])[:, np.newaxis]
# Умножаем каждую строку на соответствующий коэффициент
scaled_vectors = vectors * scales
print("\nМасштабированные векторы:\n", scaled_vectors)

# Результаты демонстрируют разные случаи броадкастинга:
# - Расширение скаляра до размера вектора
# - Автоматическое расширение векторов разной размерности
# - Применение вектора к каждой строке матрицы
# - Вычитание вектора из каждой строки матрицы
# - Поэлементное умножение с автоматическим расширением размерности
# -

#
# <h3 id="broadcasting-warnings">4.6 Предостережения</h3>
# <p><strong>Возможные проблемы при использовании броадкастинга:</strong></p>
# <ul>
#     <li>Неявное создание больших массивов при несовместимых размерностях</li>
#     <li>Сложность отладки при неочевидных правилах расширения</li>
#     <li>Потенциальные ошибки при неправильном понимании размерностей</li>
# </ul>
#
# <h3 id="broadcasting-importance">4.7 Значение броадкастинга</h3>
#
# <p>Броадкастинг - это мощный механизм в NumPy и других библиотеках для
# работы с векторами и матрицами, который предоставляет следующие преимущества:
#
# <ul>
#     <li><strong>Гибкость операций:</strong> Возможность выполнять операции
# между массивами разных размерностей</li>
#     <li><strong>Оптимизация памяти:</strong> Экономия памяти за счёт
# отсутствия необходимости создавать временные массивы</li>
#     <li><strong>Чистота кода:</strong> Возможность писать более чистый и
# понятный код</li>
#     <li><strong>Производительность:</strong> Оптимизация вычислений на
# уровне библиотеки</li>
# </ul>
#
# <h4 id="broadcasting-rules-importance">Важность понимания правил
# броадкастинга</h4>
#
# <p>Глубокое понимание правил броадкастинга необходимо для:</p>
#
# <ul>
#     <li><strong>Предотвращения ошибок:</strong> Избегание проблем
# при работе с массивами разных размерностей</li>
#     <li><strong>Оптимизации:</strong> Эффективное использование
# векторизованных операций</li>
#     <li><strong>Проектирования:</strong> Правильное проектирование
# алгоритмов обработки данных</li>
# </ul>
