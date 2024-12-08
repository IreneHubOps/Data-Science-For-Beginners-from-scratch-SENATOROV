"""Классы."""

# 11.1. Основные понятия
# Классы предоставляют способ объединения данных и функциональности. Создание
# нового класса - это, по сути, создание нового типа объектов, с помощью
# которого # в дальнейшем можно создавать новые объекты (экземпляры класса).
# У каждого # экземпляра класса могут быть атрибуты, хранящие информацию о его
# состоянии. Экземпляр класса также может иметь методы (определенные в его
# классе), # которые # позволяют менять состояние экземпляра.
# Классы помогают программисту использовать парадигму объектно-ориентированного
# программирования в Python.
# 11.1.1. Введение в объектно-ориентированное программирование
# Python поддерживает разные подходы к программированию. Во всех программах,
# которые мы писали до сих пор, мы строили нашу программу вокруг функций, т.е.
# блоков кода, которые манипулируют данными. Это процедурно-ориентированное
# программирование. В этом случае мы организовываем программу в виде пошаговой
# схемы или рецепта. Части программы выполнены в виде блоков кода и функций
# (рис. 11.1), которые выполняются в нужной последовательности для выполнения
# определенной задачи.

# ![image.png](attachment:image.png)

# В большинстве случаев легко использовать именно этот подход, но при написании
# больших программ или в случае, когда удобнее оперировать объектами, лучше ис-
# пользовать другой подход - объектно-ориентированное программирование. Это
# один из самых популярных подходов к решению задач программирования - создание
# объектов.
# Объектно-ориентированное программирование (ООП) - это парадигма
# программирования, # в которой программу структурируют таким образом, чтобы
# данные и функциональность # объединялись в отдельные объекты (рис. 11.2).

# ![image.png](attachment:image.png)

# Другими словами, ООП - это подход к моделированию в программе конкретных
# реальных объектов, таких как автомобили, а также отношений между разными объ-
# ектами, например студент и колледж, игрок и тренер и т.д. В ООП объекты
# реаль# ного мира моделируются как объекты программы. Эти объекты хранят
# некоторые # ассоциированные данные и могут выполнять определенные действия.
# У объекта есть две характеристики: атрибуты и поведение.
# Например, у класса «Человек» могут быть такие атрибуты, как имя, возраст,
# рост, # вес, адрес и т.д., а его поведение - это ходить, разговаривать,
# спать, есть и т. д.
# Основные понятия и принципы, используемые в ООП, приведены на рис. 11.3.

# 11.1.2. Введение в понятие класса
# Все в Python является объектом.
# Встроенные структуры данных Python (число, строка, список и т. д.)
# предназначены # для представления простых данных, таких как имя человека,
# возраст, зарплата и т.д.
# Классы используются для создания новых пользовательских структур данных,
# содержащих информацию о чем-либо. В упомянутом выше случае мы можем создать
# класс Employee для # работы с информацией обо всех сотрудниках компании,
# а также для выполнения над ними # некоторых действий или функций. Класс - это
# лишь структура данных или шаблон, пока# зывающий, как что-то должно быть
# определено, но самих данных в классе не содержится.
# Класс Employee может указывать на то, что для сотрудника нужно знать его имя,
# квалификацию и возраст, но сам класс не хранит имя, квалификацию или возраст
# конкретного сотрудника.
#
# Внутри класса есть два типа объектов:
# ♦ объекты экземпляров;
# ♦ объекты методов.
# Объекты экземпляров можно понимать как имеющиеся атрибуты.
# Объекты методов можно понимать как имеющееся поведение.
# 11.2. Объект класса
# Класс - это шаблон объектов. И класс сам по себе тоже является объектом
# в Python.
# Можно представить класс как пустой бейдж сотрудника (рис. 11.4). На бейдже
# есть информация об имени, контактном номере, отделе, возрасте,
# идентификаторе со# трудника и т.д. На основе этих данных мы можем больше
# # узнать о сотруднике.
# Здесь сотрудник - это объект.
# Можно также считать, что класс - это представление о каком-то реальном
# # объекте. # Пустой бейдж эквивалентен классу. В компании будут сотни

# сотрудников с заполненными бейджами. Их данные будут организованы в
# класс Employee.

# ![image.png](attachment:image.png)

# Создать новый объект класса в Python очень просто. Чтобы создать класс с
# именем Employee, просто запустите следующие две строки кода:
#
# class Employee :
# 				pass
#
# Здесь для определения пустого класса Employee мы используем ключевое слово
# class. На основе класса мы создаем экземпляры. Экземпляр - это конкретный
# # объект, созданный из определенного класса. Теперь мы можем создавать
# экземпляры класса Employee. Мы создали пустой класс, и на шаблон он пока не
# похож, потому что в нем нет ни чего, что позволило бы отличить один
# экземпляр от другого.
# Предположим, у нас есть данные о двух сотрудниках по имени Нилаб и Сандип.
# Теперь посмотрим, как создать класс и экземпляры класса.
#
# 11.2.1. Метод _init_
# Давайте определим метод _init_ в классе Employee:
#


# +
class Employee:
    """Class representing a person."""

    # атрибут класса ( общий для всех экземпляров класса )
    company = "Python Enterprises."
    # атрибуты экземпляра

    def __init__(self, name: str, age: int, dept: str) -> None:
        """Represent a person."""
        self.name = name
        self.age = age
        self.dept = dept

    def __str__(self) -> str:
        """Print personal data."""
        return (
            f"My name is {self.name}, my age is {self.age} "
            f"and I work in {self.dept} department of {self.company}."
        )

    def year_of_birth(self, current_year: int) -> int:
        """Count year of birth."""
        return current_year - self.age  # Fixed elf to self


# Создаем объект класса Employee
employee = Employee("Ivan", 25, "IT")

# Вызываем метод year_of_birth
birth_year = employee.year_of_birth(2024)
print(f"Год рождения: {birth_year}")

# Вызываем метод __str__ через print
print(employee)
# -

# Метод _init_ запускается в момент, когда создается объект экземпляра класса.
# Этот метод нужен для инициализации создаваемого объекта (например, для пере-
# дачи вашему объекту начальных значений).

# 11.3. Объекты экземпляров
# Если класс является шаблоном, то экземпляр класса - это копия класса с
# # заданными значениями, т.е. готовый объект, принадлежащий определенному
# классу. Это # больше не абстрактная идея, а настоящий сотрудник, например,
# с именем Нилаб и идентификатором 9469 (рис. 11.5).

# ![image.png](attachment:image.png)

# Итак, как мы поняли, класс - это пустой шаблон. Он определяет необходимую
# информацию. После заполнения шаблона получается экземпляр класса, который
# содержит реальную информацию.
# Вы можете заполнить несколько копий шаблона для создания множества экземпля-
# ров, но если бы шаблон не был определен изначально, вы не знали бы, какую
# информацию требуется указать. Следовательно, прежде чем создавать отдельные
# экземпляры класса, вы должны сначала задать, что именно вам нужно, путем
# определения класса.

# 11.3.1 . Создание экземпляров класса

# создание экземпляров класса Employee
nilabh = Employee("Nilabh", 22, "Production")
sandip = Employee("Sandip", 28, "Marketing")

# 11.3.2. Как это работает
# Все объекты экземпляров класса содержат атрибуты (или характеристики). Мы ис-
# пользуем метод _init_ для инициализации начальных значений атрибутов экзем-
# пляров класса. Для этого в метод и передаются соответствующие параметры.
# В случае с нашим классом Employee у каждого сотрудника есть имя, возраст и
# отдел,
# которые необходимо знать при создании сотрудника.
# У метода также есть первый параметр self, который указывает на сам объект.
# С помощью self можно обращаться к атрибутам и методам создаваемого экземпля-
# ра класса.
#
# ПРИМЕЧАНИЕ
# Вызывать метод _init_ вручную не требуется, т. к. он автоматически
# вызывается при создании нового экземпляра Employee.
#
# Хотя атрибуты экземпляров специфичны для каждого объекта, атрибуты самого
# класса одинаковы для всех экземпляров. В нашем случае это название компании,
# т.к. все сорудники работают в одной и той же компании.
# 11.3.3. Пример использования экземпляров класса

# обращение к атрибутам экземпляров
print(
    f"{nilabh.name} and {sandip.name} are two employees"
    f"of {Employee.company} company.",
)
print(
    f"{nilabh.name} is {nilabh.age} and works in {nilabh.dept}"
    f"department of {nilabh.company}.",
)
print(
    f"{sandip.name} is {sandip.age} and works in {sandip.dept}"
    f"department of {sandip.company}.",
)

# Мы создали новый экземпляр класса Employee, присвоили его переменной nilabh
# и передали ему три аргумента, Nilabh, 22 и Production, которые соответствуют
# имени, возрасту и отделу этого сотрудника.
# Затем эти аргументы передаются методу _init_, который вызывается каждый раз,
# когда мы создаем новый экземпляр класса, чтобы назначить объекту имя,
# возраст и
# отдел. Вам может быть любопытно, почему при создании новых экземпляров класса
# не пришлось передавать аргумент self. Это и есть магия Python. Когда мы
# создаем
# новый экземпляр класса, Python автоматически определяет, что такое self (в
# данном
# случае сотрудник), и передает его методу _init_.
# После создания объекта экземпляра класса мы можем обращаться к его атрибутам.
# Синтаксис выглядит как имя_экземпляра.атрибут.
# Кроме того, в приведенном выше примере вы можете заметить, что в первом
# выводе
# значение Employee.company содержит тот же результат, что и nilabh.company и
# sandip.company в следующих двух выводах. Это потому, что company является
# атрибутом класса Employee и, следовательно, автоматически передается всем
# экземплярам этого класса. Он общий для всех объектов экземпляров. Но атрибуты
# экземпляров, которые мы передаем в качестве аргументов при их создании,
# такие как имя, возраст и отдел, специфичны для каждого экземпляра класса.
# Здесь, после того как мы создали экземпляры класса Employee, т.е. nilabh и
# sandip, мы использовали функцию print() для генерации текстовой строки,
# которую мы # написали отдельно, вне определения класса (обратите внимание на
# отсутствие отступа перед функцией print()).
# Что будет, если мы просто выведем экземпляр как есть?

print(nilabh)

# Выводится только тип объекта и его адрес в памяти.

nilabh = Employee("Nilabh", 22, "Production")
sandip = Employee("Sandip", 28, "Marketing")

print(nilabh)

# 11.4. Объекты методов
# Методы - это функции, определенные внутри тела класса. Они используются для
# определения поведения объекта.
# Мы определим метод в том же классе, который использовали ранее. Метод сооб-
# щит нам год рождения сотрудника в зависимости от его возраста (который
# является атрибутом экземпляра) и текущего года (который является параметром
# метода).

print(f"Nilabh was born in {nilabh.year_of_birth(2020)}.")


# Как вы могли заметить, метод YOB() определяется так же, как пользовательская
# функция. Однако разница заключается в синтаксисе вызова. В этом и заключается
# основное различие между функцией и методом.
# Здесь метод находится внутри класса Employee и, следовательно, не является
# глобальным методом, а вызывается только на экземпляре этого класса.

# 11.5. Наследование
# Наследование - это мощный принцип объектно-ориентированного программирования.
# Его значение следует из названия - объект может что-то наследовать от
# родителя.
# В данном случае дочерний класс наследует атрибуты и методы от своего
# родитель# ского класса.
# Наследование позволяет определить новый класс, внеся небольшие изменения
# в существующий класс или даже без них. Новый класс называется производным
# (или дочерним) классом, а тот, от которого он наследуется, называется базовым
# (или родительским) классом (рис. 11.6).
#

# ![image.png](attachment:image.png)

# Синтаксис наследования в Python:
#
# class Базовый класс:
# 				Тело базового класса
# class Производный_ класс (Базовый_ класс):
# 				Тело производного класса
#
# Наследование позволяет нам определить класс, который перенимает функциональ-
# ность от родительского класса. Мы также можем добавить производному классу
# дополнительный функционал.
# У наследования есть много преимуществ.
# ♦ Наглядно отображает отношения в реальном мире.
# ♦ Обеспечивает возможность повторного использования кода. Нам не приходится
# писать один и тот же код снова и снова. Кроме того, это позволяет нам добав-
# лять в класс дополнительную функциональность, не изменяя его.
# ♦ Наследование носит транзитивный характер, а это означает, что если класс B
# на следуется от класса А, то все подклассы B автоматически также наследуются
# от класса А.


# +
# Базовый или родительский класс Person


class Person:
    """Class representing a person."""

    def __init__(self, name: str) -> None:
        """Represent a person."""
        self.name = name


# производный или дочерний класс Ernployee (Person)
# функция super ( ) используется для родительского класса


class NewEmployee(Person):
    """Class representing a person."""

    def __init__(self, employee_id: int, name: str) -> None:
        """Represent a person."""
        super().__init__(name)
        self.employee_id = employee_id


# -

new_employee = NewEmployee(52, "Peter")
print(new_employee)


# 11.6. Множественное наследование
# Когда дочерний класс наследуется от нескольких родительских классов, это
# называется множественным наследованием (рис. 11.7).

# ![image.png](attachment:image.png)

# При множественном наследовании функциональность всех базовых классов насле-
# дуется в производном класс. Синтаксис множественного наследования аналогичен
# одиночному наследованию.
# Синтаксис множественного наследования Python:
# class Базовый класс1:
# 				тело базового класса 1
# class Базовый класс2:
# 				тело базового класса 2
# class Производный_класс(Базовый_класс1, Базовый_класс2) :
# 				тело производного класса
#
#
# Обратите внимание на разделенные запятой имена двух базовых классов в объяв-
# лении производного класса. У него может быть любое количество родительских
# классов, от которых он наследует свою функциональность.
# В простейших случаях поиск атрибутов, унаследованных от родительского класса,
# выполняется как поиск в глубину слева направо, а не двойной поиск на одном
# уровне иерархии. Таким образом, если атрибут не найден в производном классе,
# он ищется в базовом классе 1, затем (рекурсивно) в родительских классах
# базового класса 1, и если он не был найден в этой ветке иерархии, то тогда
# поиск продолжается в базовом классе 2 и т.д.


# +
class Base1:
    """Class printing Base1."""

    def __init__(self) -> None:
        """Represent a person."""
        self.str1 = "Person1"
        print("Base1")


class Base2:
    """Class printing Base2."""

    def __init__(self) -> None:
        """Represent a person."""
        self.str2 = " Person2"
        print("Base2")


class Derived(Base1, Base2):
    """Class printing Derived."""

    def __init__(self) -> None:
        """Represent a person."""
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")

    # вызов конструктора Base1
    # и конструктора Base2

    def print_strs(self) -> None:
        """Print words."""
        print(self.str1, self.str2)


# создание экземпляра класса Derived
person = Derived()

# method printStrs() производного класса person выводит
# строки из базовых классов "Personl " и " Person2"
person.print_strs()


# -

# Наследование не ограничивается одним родителем и одним ребенком. Наследова-
# ние может быть намного более сложным, многоуровневым и гибридным. Определить
# новый производный класс также довольно просто. Дпя этого нужно лишь записать
# имена всех классов, от которых он наследуется, в круглых скобках через
# запятую.


# +
# базовый класс


class Person1:
    """Class representing a person."""

    def __init__(self, name: str, surname: str, year: int) -> None:
        """Represent a person."""
        self.name = name
        self.surname = surname
        self.year = year

    def age(self, current_year: int) -> int:
        """Define age."""
        return current_year - self.year

    def __str__(self) -> str:
        """Print persanal data."""
        return f"{self.name} {self.surname} born in {self.year}."


# -

nilabh1 = Person1("Nilabh", "Nishchhal", 1998)
print(nilabh1)


# +
class Student(Person1):
    """Class representing a person."""

    def __init__(self, st_id: int, name: str, surname: str, year: int) -> None:
        """Represent a person."""
        super().__init__(name, surname, year)
        self.student_id = st_id


siddharth = Student(1, "Siddharth", "Tiwari", 1985)
print(siddharth)


# -

# Объект siddharth ведет себя так же, как Person, но у него в числе прочего
# есть еще ID студента. Класс Person - базовый класс для Student, а класс
# Student - один из # производных классов Person. Производный класс
# наследуется не только от # своих базовых классов, но и от их базовых
# классов, образуя дерево наследования,
# которое начинается с самого базового объекта.
# Вы также можете заметить, что в подклассе Student нет метода _ str_, поэтому
# для строкового представления используется метод родительского класса.
#
# 11.6.1. Переопределение методов
# При наследовании можно добавлять в дочерний класс новые методы и атрибуты.
# А чтобы изменить поведение метода, определенного в родительском классе, можно
# переопределить этот метод в дочернем классе. Чтобы переопределить метод,
# достаточно просто определить его еще раз.


# +
class Student1(Person1):
    """Class representing a person."""

    def __init__(self, st_id: int, name: str, surname: str, year: int) -> None:
        """Represent a person."""
        super().__init__(name, surname, year)
        self.student_id = st_id

    def __str__(self) -> str:
        """Print personal data."""
        return (
            f"{self.name} {self.surname} (student id "
            f"{self.student_id}) was born in year {self.year}."
        )


siddharth1 = Student1(1, "Siddharth", "Tiwari", 1985)
print(siddharth1)
# -

# Существует интересный способ заглянуть в объект класса. С помощью функции
# help() вы можете узнать все подробности об объекте. Кроме того, эта же
# функция позволяет понять порядок разрешения методов. Для примера рассмотрим
# информа# цию об объекте siddharth, который мы создали как экземпляр класса
# Student.

help(siddharth)


# 11.7. Полиморфизм
# Полиморфизм в общем означает наличие ярких или разных форм одного и того же.
# В мире программирования полиморфизм - это способность функции с одним и
# тем же именем выполнять разные операции для разных данных. Полиморфизм по-
# зволяет создавать структуру, которая может работать с объектами разных типов.
# Это позволяет функциям использовать объекты разных типов в разное время.
# В объектно-ориентированном программировании полиморфизм позволяет исполь
# зовать объект, относящийся к определенному классу, таким же образом, как если
# бы это бьm объект совершенно другого класса.
# В отличие от многих других популярных объектно-ориентированных языков про-
# граммирования, таких как Java, Python не поддерживает полиморфизм во время
# компиляции или перегрузку методов. Если у класса или в скрипте Python есть не
# сколько методов с одинаковым именем, метод, определенный последним, переоп
# ределяет предыдущий.
# Поэтому полиморфизм методов в Python не поддерживается.
#
# 11.8. Абстракция и инкапсуляция
# Абстракция и инкапсуляция - две основные концепции ООП, наряду с наследова-
# нием и полиморфизмом.
# Абстракция означает сокрытие сложности объекта и отображение только его ос-
# новных характеристик. Другими словами, абстракция означает сокрытие реальной
# реализации, а «наружу» пользователю показывается только то, что ему нужно для
# использования.
# Инкапсуляция является одной из фундаментальных концепций ООП. Инкапсуляци-
# ей называют идею обертывания данных и работающих с ними методов в один мо-
# дуль. Это накладывает ограничения на прямой доступ к переменным и методам
# и помогает предотвратить порчу данных. Чтобы избежать случайного изменения,
# к переменной объекта можно обращаться только в методах объекта. Такие пере-
# менные называются приватными.
# При работе с классами предоставление глобального доступа ко всем переменным,
# используемым в программе, - не лучший выбор. Инкапсуляция дает нам возмож-
# ность открыть доступ только к необходимым переменным объекта, не предоставляя
# программе полного доступа ко всем данным объекта.
# Класс - это пример инкапсуляции, поскольку он объединяет все связанные с объ-
# ектом данные и функции.
# 11.9. Как контролировать доступ
# Приватных переменных экземпляра, к которым можно получить доступ только
# внутри объекта, в Python не существует. Но существует соглашение между про-
# граммистами, которому соответствует большая часть кода Python: имя с
# префиксом подчеркивания (например, _spam) должно рассматриваться как
# защищенная часть API (будь то функция, метод или данные). Это следует
# рассматривать как нюансы реализации, и такие компоненты могут быть изменены
# без какого-либо уведомления'.
# Существуют 3 типа переменных:
# ♦ публичные;
# ♦ защищенные;
# ♦ приватные.
# Когда мы объявляем переменные в классе Python, они изначально являются обще-
# доступными (публичными), например self.name = name.
# Чтобы сделать переменную защищенной, перед именем переменной ставится сим-
# вол подчеркивания, например self._name = name. Доступ к защищенной переменной
# могут получить произвдные классы. Чтобы сделать переменную приватной
# (закрытой), перед именем переменной ставят два символа подчеркивания,
# например self._name = name.
# К приватной переменной производные классы доступа не имеют.
#
# Резюме:
# 1. Я познакомилась с объектно-ориентированным программированием и концепцией
# классов в Python
# 2. Узнала, как определять и инициализировать классы, создавать экземпляры
# классов.
# 3. Узнала, как функции, определенные внутри класса, работают как методы
# объекта этого класса.
# 4. Изучила концепцию наследования и множественного наследования в классе.
# 5. Узнала такие понятия как  полиморфизм, абстракция и инкапсуляция.
# 6. Узнала о приватных, защищенных и публичных переменных.

# 11.11.1. Ответьте на вопросы
# 1. Что такое объектно-ориентированное программирование? В чем его преимуще-
# ства по сравнению процедурным программированием?
# ОТВЕТ:ООП - это парадигма программирования, в которой программу
# структурируют таким # образом, чтобы данные и функциональность объединялись
# в отдельные объекты, в отличии от процедурного программирования, где
# программа строится вокруг функций, т.е.
# блоков кода, которые манипулируют данными.
# 2. Расскажите, чем отличаются объект и класс.
# ОТВЕТ: Класс - некая абстракция, логическая структура, описывающая поведение
# и характеристики. Объект - конкретный экземпляр класса.
# 3. Какие типы объектов бывают внутри класса? Чем они отличаются?
# ОТВЕТ: объекты экземпляров и объекты методов.
# 4. Класс - это шаблон объекта. Что это значит?
# ОТВЕТ: Это логическая конструкция, по средствам которой можно создать
# новый объект.
# 5. Что делает метод init?
# ОТВЕТ: Инициализирует значение атрибутов объекта класса.
# 6. В чем разница между методом и функцией?
# ОТВЕТ: Методы принадлежат объектам, функции - нет, методы могут быть только
# внутри класса, когда функции могут быть в глобальной области.
# 7. Что такое наследование?
# ОТВЕТ: Наследование позволяет получить новый класс, немного отличающийся от
# старого, # без повторного написания кода.
# 8. Какое значение имеет функция super()?
# ОТВЕТ: передает функциональность от родительского класса.
# 9. Что происходит, когда в родительском и дочернем классах объявляются функ-
# ции с одним и тем же именем?
# ОТВЕТ: В дочернем классе метод переопределяется.
# 10. Как сделать любую переменную в Python приватной?
# ОТВЕТ: необходимо добавить одинарное подчеркивание перед переменной:
# self._name = name

# 11.11.2. Правда или ложь
# 1. Класс представляет собой шаблон, определяющий объекты одного типа.
# ПРАВДА
# 2. Ключевое слово class обозначает начало определения класса.
# ПРАВДА
# 3. Для инициализации атрибутов экземпляров класса нужно определить метод
# init.
# ПРАВДА
# 4. Параметр self нужно передать в конструктор при создании экземпляра.
# ЛОЖЬ
# 5. Параметр self ссылается на создаваемый объект.
# ПРАВДА
# 6. Объект может содержать в себе другие объекты.
# ПРАВДА
# 7. Атрибут класса имеет общее значение для всех экземпляров этого класса.
# ПРАВДА
# 8. В родительском классе есть ссылка на список со всеми его дочерними
# классами.
# ЛОЖЬ
# 9. По умолчанию при создании экзепляра класса вызывается метод _init_.
# ПРАВДА
# 10. Когда мы определяем переменные в классе Python, они по умолчанию являются
# приватными.
# ЛОЖЬ

# 11.11.3. Практические задания
# 1. Рассмотрим следующее определение класса:
# Напишите команду для создания объекта класса Yourclass.


# +
class Student2:
    """Class representing a student."""

    def __init__(self, student_marks: int, name: str) -> None:
        """Initialize student's marks and name."""
        self.marks = student_marks
        self.name = name

    def __str__(self) -> str:
        """Return a string representation of the student."""
        return f"{self.marks}, {self.name}"


# Create an instance of the Student class
my_student = Student2(10, "АБС")
print(my_student)


# -

# 2. Напишите класс с именем Rectangle, состоящий из длины и ширины, и метода,
# который будет вычислять площадь прямоугольника.


# +
class Rectangle:
    """Class defining triangle parameters."""

    def __init__(self, length: int, width1: int) -> None:
        """Initialize length and width."""
        self.length = length
        self.width = width1

    def calculate_sq(self) -> float:
        """Calculate square."""
        area = (self.length * self.width) / 2
        return area


my_rectangle = Rectangle(3, 8)
print(my_rectangle.calculate_sq())


# -

# 3. Напишите класс, который имеет два метода get_String() и print_String().
# Метод get_string() принимает строку от пользователя, а print_String
# выводит строку в верхнем регистре.


# +
class Makestring:
    """Class making upper string."""

    def __init__(self) -> None:
        """Initialize string."""
        self.string = ""

    def get_string(self) -> None:
        """Get string."""
        self.string = input("Enter the string: ")

    def print_string(self) -> None:
        """Print string."""
        print(self.string.upper())


my_string = Makestring()
my_string.get_string()
my_string.print_string()


# -

# 4. Напишите класс, который меняет порядок слов в строке. Строка "hello world"
# превращается в "world hello" .


# +
class Reverseword:
    """Class reversig a word."""

    def __init__(self) -> None:
        """Initialize string."""
        self.string = "hello world"

    def reverse_words(self) -> None:
        """Reverse word."""
        print(" ".join(list(reversed(self.string.split()))))


reverser = Reverseword()
reverser.reverse_words()


# -

# 5 . Напишите класс для преобразования целого числа в римские цифры.


# +
class Romandigit:
    """Class transforming digit."""

    @staticmethod
    def transformation(num: int) -> str:
        """Transform digit."""
        digit_num_1 = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        digit_num_10 = ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        digit_num_100 = ["C"]
        romans = {1: digit_num_1, 10: digit_num_10, 100: digit_num_100}
        roman = ""
        i = 1
        while num:
            digit, num = num % 10, num // 10

            if digit > 0:
                roman = romans[i][digit - 1] + roman

            i *= 10
        return roman


number = int(input("enter a digit from 1 to 100"))
print(Romandigit.transformation(number))


# -

# 6. Определите класс с именем Shape(фигура) и его дочерний класс Square
# (квадрат).
# Класс square имеет метод инициализации, который принимает в качестве аргу-
# мента сторону квадрата. Оба класса имеют метод вычисления площади, который
# может выводить площадь на экран. Площадь фигуры Shape по умолчанию равна О.


# +
class Shape:
    """Base class for shapes."""

    def calculate_sq(self) -> int:
        """Calculate square."""
        return 1


class Square(Shape):
    """Class representing a square."""

    def __init__(self, width: int) -> None:
        """Initialize width."""
        self.width = width

    def calculate_sq(self) -> int:
        """Calculate area of the square."""
        return self.width**2

    def printing(self) -> None:
        """Print the area of the square."""
        print(f"Площадь квадрата: {self.calculate_sq()}")


square = Square(100)
square.printing()


# -

# 7. Определите класс Student с заданными характеристиками.
# Атрибуты экземпляра:
# • номер курса;
# • имя.
# Методы:
# • getdata() - для ввода номера курса и имени;
# • printdata() - для вывода номера курса и имени.


# +
class Student4:
    """Class representing a student."""

    def __init__(self) -> None:
        """Initialize name and course."""
        self._name = ""
        self._course = 1

    def getdata(self) -> None:
        """Get name and course of student."""
        self._name = input("Enter name")
        self._course = int(input("Enter number of course"))

    def printdata(self) -> None:
        """Print name and course of student."""
        print(f"{self._name} study at {self._course} course")


katya = Student4()
katya.getdata()
katya.printdata()


# -

# 8. Определите класс Marks, производный от класса Student.
# Переменная экземпляра:
# • Оценки по пяти предметам.
# Методы:
# • inputdata() - вызов getdata() и ввод 5 оценок;
# • outdata() - вызов printdata() и отображение 5 оценок.
# Реализуйте классы на Python.


# +
class Marks(Student4):
    """Class showing student's marks."""

    def __init__(self) -> None:
        """Initialize name, course and marks."""
        super().__init__()
        self._marks: list[str] = []

    def inputdata(self) -> None:
        """Get name, course and marks of student."""
        super().getdata()
        self._marks = input("Enter 5 marks: ").split()

    def outdata(self) -> None:
        """Print name, course and marks of student."""
        super().printdata()
        print(f"has marks: {','.join(self._marks)}")


marks = Marks()
marks.inputdata()
print()
marks.outdata()


# -

# 9. Гостиница xyz предлагает проживание, питание.
# а. Создайте класс Accommodation с номером комнаты, типом комнаты, ценой арен-
# ды и т. д.
# б. Создайте класс меаl, содержащий код обеда, название, цену и т. д.
# в. Создайте класс customer, содержащий номер клиента, его имя, адрес и т. д.
# г. Класс Customer должен наследоваться от Accommodation и Meal.


# +
class Accommodation:
    """Class representing an accommodation room."""

    def __init__(
        self,
        room_number: int,
        room_type: str,
        rent_price: int,
        capacity: int,
    ) -> None:
        """Initialize the accommodation details.

        Args:
            room_number (int): The number of the room.
            room_type (str): The type of the room (e.g., standard, deluxe).
            rent_price (int): The rent price for the room.
            capacity (int): The maximum capacity of the room.
        """
        self.room_number = room_number
        self.room_type = room_type
        self.rent_price = rent_price
        self.capacity = capacity

    def inforoom(self) -> str:
        """Return information about the room.

        Returns:
            str: A string containing details about the room.
        """
        return (
            f"Information about the room {self.room_number}: "
            f"Room Type: {self.room_type}, Rent Price: {self.rent_price}, "
            f"Room Capacity: {self.capacity}"
        )


class Meal:
    """Class representing a meal."""

    def __init__(
        self,
        idmeal: int,
        mealname: str,
        price: int,
        classification: str,
    ) -> None:
        """Initialize the meal details.

        Args:
            idmeal (int): The ID of the meal.
            mealname (str): The name of the meal.
            price (int): The price of the meal.
            classification (str): The classification of the
            meal (e.g., appetizer, dessert).
        """
        self.idmeal = idmeal
        self.mealname = mealname
        self.price = price
        self.classification = classification

    def infomeal(self) -> str:
        """Return information about the meal.

        Returns:
            str: A string containing details about the meal.
        """
        return (
            f"Information about the meal: ID - {self.idmeal}, "
            f"Name: {self.mealname}, Price: {self.price}, "
            f"Meal Type: {self.classification}"
        )


class Customer(Accommodation, Meal):
    """Class representing a customer with.

    accommodation and meal preferences.
    """

    def __init__(
        self,
        fullname: str,
        phonenum: str,
        room_number: int,
        idmeal: int,
    ) -> None:
        """Initialize customer details.

        Args:
            fullname (str): The full name of the customer.
            phonenum (str): The phone number of the customer.
            room_number (int): The room number associated with the customer.
            idmeal (int): The ID of the meal associated with the customer.
        """
        Accommodation.__init__(self, room_number, "", 0, 0)
        Meal.__init__(self, idmeal, "", 0, "")
        self.phonenum = phonenum
        self.fullname = fullname

    def custinfo(self) -> str:
        """Return information about the customer.

        Returns:
            str: A string containing customer details.
        """
        return (
            f"Name: {self.fullname}, "
            f"Phone Number: {self.phonenum}, "
            f"Room Number: {self.room_number}, "
            f"Meal ID: {self.idmeal}"
        )


# Example usage
room1 = Accommodation(1, "Standard", 30, 3)
print(room1.inforoom())

meal1 = Meal(1, "Prague", 5, "Dessert")
print(meal1.infomeal())

client1 = Customer("Jake Paul", "+1 983 233 543", 23, 145)
print(client1.custinfo())
