"""Module on commits."""

# **Соглашение о коммитах**

# https://www.conventionalcommits.org/ru/v1.0.0/

# ![image.png](attachment:image.png)

# * feat - добавляет новую функцию
# * fix - исправляет баг
# * docs -  изменение в документации проекта
# * style - изменение оформления кода
# * refactor - изменение кода с целью улучшения его структуры или читаемости
# * test - добавление или изменение тестов
# * build - изменение системы сборки проекта или зависимостей
# * ci - (continuous integration) изменение в конфигурациях CI/CD (обновление скриптов автоматизации, настройка окружений...)
# * perf - (performance) улучшение производительности
# * chore - обновления зависимостей, изменения в конфигурации и другие рутинные задачи

# Представьте, что вы исправили баг в функции, которая некорректно округляет числа. Сделайте фиктивный коммит и напишите для него сообщение в соответствии с Conventional Commits (используя тип fix).


def generate_report(*args: int) -> int:
    """Generate the sum of the given integers.

    Args:
        *args (int): A variable number of integer arguments to be summed.

    Returns:
        int: The sum of the provided integers.
    """
    return sum(args)


print(
    generate_report(
        5,
        5,
    )
)

5 + 5
