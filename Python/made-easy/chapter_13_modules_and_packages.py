"""Модуль и и пакеты."""

# +
import sys

import fibo
from fibo import fib, fib2

# import fibo as fibonacci

# from fibo import *
# from fibo import fib
# from fibo import fib as fibonacci
# -

# # 13.1. Modules
# в Python можно поместить определения
# в отдельный файл и использовать их в скриптах или в интерактивном режиме
# интерпретатора. Такой файл называется модулем. Определения из модуля можно
# импортировать в другие модули или в основной модуль.
# Модуль - это файл, содержащий определения и инструкции Python. Имя такого
# файла состоит из имени модуля и расширения ру.
# В программировании модулем называется часть программного обеспечения с
# определенной функциональностью.
# Каждый модуль - это отдельный файл, который можно редактировать независимо.
# Внутри самого модуля его имя (в виде строки) доступно как значение глобальной
# переменной _name_.

# ![image.png](attachment:image.png)

# Что если мы хотим использовать эти функции регулярно?
# Для этого мы создаем скрипт, сохраняем его с подходящим именем, например fibo,
# и расширением ру, и наш новый модуль готов к работе. В Python существуют
# тысячи встроенных модулей
# что делает функция fib ( ) без вызова модуля?
#

# ![image.png](attachment:image.png)

# Чтобы использовать наш модуль, нам нужно его импортировать. Зайдите в
# интерпретатор Python и импортируйте этот модуль с помощью следующей
# команды:
# import fibo

fibo.fib(1000)

fibo.fib2(100)

fibo.__name__

# Если вы собираетесь использовать функцию часто, вы можете присвоить ей
# локальное имя:
# fib = fibo.fib

# Модули могут импортировать и другие модули, которые будут использоваться
# в его коде. Обычно, но не обязательно, все операторы import указываются
# в начале модуля (или скрипта). Имена импортированных модулей помещаются
# в пространство имен импортирующего модуля.

# Существует возможность импортировать отдельные функции из модуля
# непосредственно в пространство имен импортирующего модуля. Например:
#

fib(500)

# Вы можете заметить разницу в способе вызова функции fib ( ) . Раньше, когда
# импортировался целиком весь модуль, функция вызывалась как имя_модуля.функция().
# Но здесь функция импортируется непосредственно в пространство импортирующего
# модуля и используется самостоятельно.
# Но тут есть одна загвоздка.
# При таком импорте имя модуля в пространство имен не попадает (поэтому в этом
# примере модуль fibo не определен). И соответственно другие функции, которые не
# импортируются, оказываются не определены. Это становится ясно из следующего
# примера, где вызов функции fib2 () выдает сообщение об ошибке.

# ![image.png](attachment:image.png)

# 13.2.3. Импорт всех имен из модуля
# Существует также способ импортировать все имена из модуля.
# from fibo import *

fib2(500)

# В большинстве случаев программисты Python не используют эту возможность,
# поскольку она вводит в интерпретатор неизвестный набор имен, которые могут пере
# определить что-то из того, что вы уже определили ранее. Кроме того, это порожда-
# ет плохо читаемый код. Однако импорт через символ ( *) можно использовать для
# экономии времени в интерактивных сессиях.

# 13.2.4. Им порт модуля под другим именем
# Если при импорте за именем модуля следует ключевое слово as, то указанное после
# него имя становится новым именем модуля.

fib(500)

# В Python есть встроенная библиотека стандартных модулей, описанная в отдельном
# документе Python Library Reference.
# Некоторые модули встроены в интерпретатор, и они предоставляют операции,
# которые не являются частью ядра языка, но тем не менее встроены по умолчанию
# для повышения эффективности или для доступа к основным средствам операционной
# системы, таким как системные вызовы. Этот набор модулей зависит от конфигурации
# и от базовой платформы.

sys.ps1

sys.ps2

sys.ps1 = " С> "

# 13.4. Функция dir()
# Встроенная функция dir() позволяет узнать, какие имена определены в указанном
# модуле. Функция возвращает отсортированный список строк.

dir(fibo)

dir(sys)

# Функция dir ( ) не перечисляет имена встроенных функций и переменных. Если вам
# нужен их список, они определены во встроенном модуле builtins.

# 13.5. Пакеты
# Пакет представляет собой набор модулей.
# Суть пакетов легко понять по аналогии с тем, как мы храним данные на компьютере.
# Для разных типов файлов мы используем разные папки. Например, в одной
# папке хранятся музыкальные файлы, а в другой - фотографии. Внутри папок
# могут быть вложенные папки. Аналогично этому в Python используются пакеты
# вместо папок и модули вместо файлов.
# Папка должна содержать файл с именем _init_.py, чтобы
# Python обрабатывал ее как пакет. Этот файл содержит код инициализации пакета.
# Пакеты позволяют структурировать множество пакетов и модулей, помогают
# добиться хорошо организованной иерархии и облегчают доступ к папкам и модулям.
#
# 13.5.1 . Пример пакета sound2
# Предположим, вы хотите разработать набор модулей (пакет) для обработки звуко-
# вых файлов и звуковых данных. Существует множество различных форматов зву-
# ковых файлов (обычно они отличаются по расширению, например: wav, aiff, au,
# mp3 и т. д.). Структура вашего пакета (выраженная в терминах иерархической
# файловой системы) может выглядеть так, как продемонстрировано на рис. 13.1.

# ![image.png](attachment:image.png)

# На этом рисунке показано лишь упрощенное представление о том, как пакет, под
# пакет и модули связаны друг с другом.
# Видно, что подпакеты находятся внутри блока кода пакета, а модули находятся
# внутри соответствующих подпакетов.

# ![image.png](attachment:image.png)

# Файлы _init_.py позволяют Python обрабатывать папки с файлами как пакеты.
# Это предотвращает непреднамеренное перезаписывание модулей с одинаковыми
# именами, например string. В простейшем случае файл _init_.py может быть пус
# тым файлом, но в нем может выполняться код инициализации пакета или устанав-
# ливаться переменная _all_.

# 1 3.5.2. Вызов пакета для дальнейшего использования 1
# Чтобы использовать пакет, сначала его нужно импортировать. Пользователь может
# импортировать из пакета отдельные модули. Например, вот так можно импортиро-
# вать модуль echo подпакета effects, который находится внутри пакета sound:
# import sound . effects . echo
# Эта команда загружает модуль sound . effects . echo. Теперь, если мы хотим использо-
# вать функцию echofilter ( ) из этого модуля, нам нужно вызвать ее, указав ее полное
# имя с именами пакетов и модуля:
# sound . effects . echo . echofilter (input, output, delay=0 . 7 , atten=4 )
# Это выглядит громоздко и длинно, и такой код в большой программе может стать
# источником ошибок. К счастью, существует альтернативный способ импорта под
# модуля:
# from sound . effects import echo
# Такой импорт тоже загружает подмодуль echo и делает его доступным без префикса
# пакета, поэтому его можно использовать следующим образом:
# # echo . echofilter (input , output, delay=0 . 7 , atten=4 )
# Есть также возможность прямого импорта нужной функции или переменной:
# from sound . effects . echo import echofilter
# Опять же, мы загружаем подмодуль echo, но функция echofilter ( ) при этом стано-
# вится доступна напрямую:
# echofilter ( input , output, delay=0 . 7, atten=4)

# 13.5.3. Популярные пакеты в Python
# 13.5.3.1. Сбор данных
# Scrapy
# Эта библиотека Python для работы с данными, помогает создавать программы
# сканирования (ботов) для извлечения из Интернета структурированных данных,
# например URL-aдpeca или контактную информацию.
#
# 13.5.3.2. Обработка данных и моделирование
# NumPy
# NumPy (Numerical Python) -  инструмент для научных вычислений и выполнения
# простых и более сложных операций над массивами.Библиотека помогает обрабаты-
# вать массивы, в которых хранятся значения одного типа, и упрощает выполнение
# математических операций над массивами (и их векторизацию).
# SciPy
# Эта библиотека содержит модули для выполнения вычислений из линейной алгебры,
# интегрирования, оптимизации и статистики. Ее основная функциональность была
# построена на NumPy, поэтому вычисления с массивами она тоже поддерживает.
# В библиотеке есть эффективные численные процедуры, такие как численная оптимизация,
# интегрирование и другие функции.
# Pandas
# Эта библиотека создана с целью помочь разработчикам в обработке «маркированных»
# и «реляционных» данных. Работа библиотеки опирается на две основные структуры
# данных: Series (одномерный список элементов) и DataFrame (двумерная структура
# вроде таблицы с несколькими столбцами). Pandas позволяет преобразовывать структуры
# данных в объекты DataFrame, обрабатывать отсутствующие данные, добавлять/удалять
# столбцы из DataFrame, вводить отсутствующие файлы и строить графики и гистограммы.
# Библиотека применяется для обработки и визуализации данных.
# Scikit-learn
# Scikit-learn - это группа пакетов в SciPy Stack, которые были созданы для конкретных
# задач, например, для обработки изображений. В Scikit-learn для выполнения мате-
# матических операций используется библиотека SciPy, предоставляющая удобный
# интерфейс для наиболее распространенных алгоритмов машинного обучения.
# Специалисты по данным используют эту библиотеку для выполнения стандартных
# задач машинного обучения и интеллектуального анализа данных, таких как класте-
# ризация, регрессия, выбор модели, уменьшение размерности и классификация.
# А еще библиотека поставляется с качественной документацией и обладает высокой
# производительностью.
# TensorFlow
# TensorFlow - это лучший инструмент для таких задач, как идентификация объектов,
# распознавание речи и многих других задач. Он помогает в работе с искусственными
# нейронными сетями, которым необходимо обрабатывать несколько наборов данных.
#
# 13.5.3.3. Визуализация данных
# Matplotlib
# Это стандартная библиотека Data Science, которая позволяет визуализировать дан-
# ные, такие как двумерные диаграммы и графики (гистограммы, диаграммы рассея-
# ния и графики в недекартовых координатах). Matplotlib - одна из тех библиотек
# построения графиков, которые полезны в проектах по Data Science благодаря
# объектно-ориентированному API для встраивания графиков в приложения.
# Seaborn
# Библиотека Seabom создана на основе Matplotlib и служит полезным инструментом
# машинного обучения Python для визуализации статистических моделей - тепловых
# карт и других типов визуализаций, в которых приводится сводка данных и
# отображаются общие распределения. При использовании этой библиотеки вам
# доступна широкая галерея визуализаций (включая сложные средства, такие как
# временные ряды, совместные графики и скрипичные диаграммы).
# Bokeh
# Эта библиотека - отличный инструмент для создания интерактивных и масштаби-
# руемых визуализаций внутри браузеров с помощью виджетов JavaScript. Библиоте-
# ка полностью независима от Matplotlib. Она ориентирована на интерактивность и
# представляет визуализации в современных браузерах.
# Plotly
# Этот веб-инструмент для визуализации данных, библиотека очень хорошо работает
# в интерактивных веб-приложениях. Ее создатели активно расширяют библиотеку
# новой графикой и функциями для поддержки нескольких связанных представлений,
# анимации и интеграции перекрестной интеграции.

# 13.6. Резюме
# 1. Я узнала об организации проекта Python и о многократном использовании своего
# кода.
# 2. Изучила модули и пакеты.
# Модули - это инструмент Python для хранения кода в виде файлов, и модули можно
# вызывать в любой момент, когда они нам нужны.
# Пакеты позволяют организовать эти файлы или модули. Они берут на себя задачу
# идентификации и поиска нужного модуля и представляют собой репозиторий других
# подпакетов и модулей.
# 3. Познакомилась с популярными пакетами в Python для Data Science.
#

# 13.7. Упражнения
#
# 13.7.1. Ответьте на вопросы
# 1. Что имеется в виду под «созданием скрипта»? Чем это полезно для
# программиста?
# Ответ:
# Создание скрипта - это способ хранения кода в виде файлов, которые можно вызывать
# в любой момент, когда они нам нужны. Это полезно для программиста, так как позволяет
# решать задачи и проблемы, которые могут возникнуть в процессе работы.
# 2. Что имеется в виду под модулем Python? В чем важность модулей?
# Ответ:
# Модуль Python - это файл, содержащий определения и инструкции Python. Модули
# позволяют структурировать код, делать его более организованным и повторно
# используемым.
# 3. Как написать свой собственный модуль?
# Ответ:
# Чтобы написать свой собственный модуль, нужно создать файл с расширением .py и
# внутри него определить необходимые функции, классы и переменные.
# 4. Как использовать созданный ранее модуль в своем нынешнем проекте?
# Ответ:
# Чтобы использовать созданный ранее модуль в своем нынешнем проекте, нужно
# импортировать его в проект с помощью команды import.
# 5. Что такое пакет? Как он связан с модулем?
# Ответ:
# Пакет - это набор модулей, которые хранятся в отдельной папке. Пакеты позволяют
# организовать модули, делать их более структурированными и повторно используемыми.
# 6. Как Python узнает, что нужно рассматривать какую-либо папку как пакет
# Python? Верно ли это и для подпакетов?
# Ответ:
# Python узнает, что нужно рассматривать какую-либо папку как пакет, если в ней
# содержится файл с именем _init_.py. Этот файл позволяет Python обрабатывать папку
# как пакет.
# 7. Какими способами можно импортировать модуль, находящийся внутри пакета?
# Ответ:
# Можно импортировать модуль, находящийся внутри пакета, с помощью команды import,
# указав полное имя модуля. Также можно использовать альтернативный способ импорта
# через символ ( * ), но он менее предпочтителен, так как может вызвать конфликты
# имен.
# 8. Зачем создавать пакеты? Чем они полезны?
# Ответ:
# Пакеты позволяют структурировать код, делать его более организованным и повторно
# используемым. Они помогают организовать множество модулей и подпакетов, делать
# иерархию и облегчают доступ к папкам и модулям.
# 9. Какой вклад вносят общедоступные пакеты в язык вроде Python? Чем они полезны
# для нового программиста или пользователя?
# Ответ:
# Общедоступные пакеты в языке вроде Python предоставляют полезные функции и инструменты,
# которые могут быть использованы для решения различных задач. Они помогают новым
# программистам и пользователям быстрее освоить язык и начать работать над проектами.
# 1О. Назовите 5 общедоступных пакетов.
# Ответ:
# Scrapy, NumPy, SciPy, Pandas, Scikit-learn.

# 13.7.2. Правда или ложь
# 1. Если функции и переменные были определены хотя бы один раз, то они будут
# доступны вам всегда, даже если вы вышли из интерпретатора.
# Ответ:
# Правда.
# 2. Текстовый редактор ничем не отличается от любого текстового редактора,
# такого как MS Word.
# Ответ:
# Ложь.
# 3. Определения из модуля можно импортировать в другие модули.
# Ответ:
# Правда.
# 4. Имя файла модуля имеет расширение ру.
# Ответ:
# Ложь.
# 5. В Python нет встроенных модулей.
# Ответ:
# Ложь.
# 6. При импорте модуля с использованием синтаксиса from модуль import *
# импортируются все имена, кроме тех, которые начинаются с символа _.
# Ответ:
# Правда.
# 7. dir ( ) - встроенная функция, позволяющая узнать, какие имена определены
# в модуле.
# Ответ:
# Правда.
# 8. Пакет может содержать один или несколько модулей.
# Ответ:
# Правда.
# 9. NumPy - популярный пакет интеллектуального анализа данных в Python.
# Ответ:
# Правда.
# 1О. Самая популярная библиотека визуализации в Python - это Matplotlib.
# Ответ:
# Правда.
