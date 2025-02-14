"""Ответы на вопросы по Issues."""

# ## Список вопросов и ответов на вопросы по теме issues:
#
# ### Общие вопросы
# 1. Что такое Issues на GitHub и для чего они используются?
#
# Issues на GitHub - это инструмент для управления и отслеживания задач, багов, запросов на добавление функционала и других обсуждений, связанных с проектом. Issues можно также использовать для того, чтобы другие разработчики нам рассказывали про свой код или обучали нас программированию.
#
# 2. Чем Issues отличаются от других инструментов управления задачами?
#
# Issues тесно интегрированы с репозиториями кода на GitHub. Это позволяет легко связывать задачи с коммитами, pull requests и ветками, обеспечивая прозрачность и отслеживаемость изменений. Они доступны для всех участников проекта и сообщества, что способствует открытому обсуждению и совместной работе.
#
# 3. Какие основные компоненты (поля) есть у каждого Issue?
#
# Title, description, labels, milestones, assignees, type, projects, relationships, author, linked issues, comments.
#
# ### Создание Issues
# 4. Как создать новое Issue в репозитории?
#
# в репозитории на гитхабе нажимаем на Issues -> New issue -> вписываем title и description (если проблема в файле, то в title нужно указать название файла) -> Create.
#
# 5. Какие данные рекомендуется указывать в описании Issue для лучшего понимания задачи?
#
#  - Информативный title с названием файла, в котором есть проблема или который хотим, чтобы нам объяснили. Так же там можно вписать код ошибки, трассировку из терминала, то есть там должны быть ключевые слова, по которым мы сможем найти ошибку.
#  - Ссылка на функцию, строки в функции или вставка этой функции/строк в description.
#
# 6. Какие теги (labels) можно добавить к Issue? Какие из них стандартные?
#
# Стандартные:
#  - bug - ошибка в коде.
#  - documentation - улучшение/добавление документации.
#  - duplicate - issue с такой проблемой уже существует.
#  - enhancement - предложения по улучшению.
#  - good first issue - для задач, подходящим новичкам в проекте.
#  - help wanted - требуется помощь для решения данной задачи.
#  - invalid - указывает на некорректный issue.
#  - question - если есть вопросы по коду.
#  - wontfix - проблему невозможно решить, она не будет исправлена.
#
# Нестандартные (примеры):
#  - discussion
#  - urgent
#  - performance
#  - security
#  - SENATOROV
#  - writer
#
# 7. Как прикрепить Assignees (ответственных) к Issue?
#
# В поле Assignees нажимаем на шестеренку и выбираем пользователя.
#
#
# ### Работа с Issues
# 8. Как использовать Labels для классификации задач?
#
# В поле Labels нажимаем на шестеренку, выбираем нужный тег из стандартных или создаем свой, который будет отражать суть issue.
#
# 9. Для чего нужен Milestone, и как связать его с Issue?
#
# Milestone нужен для установки дедлайна для данного issue или приоритета задачи, чтобы сосредоточиться на наиболее важных. Milestone можно выбрать из имеющихся или создать свой.
#
# 10. Как привязать Issue к пул-реквесту (Pull Request)?
#
# При создании Pull Request в title в скобках указать (#ISSUE_NUMBER), в description указать #ISSUE_NUMBER.
#
# 11. Как добавить комментарий к существующему Issue?
#
# Внизу issue есть специальное поле для комментариев.
#
# ### Закрытие и завершение Issues
# 12. Как закрыть Issue вручную?
#
# Под комментариями внизу страницы есть кнопка Close issue.
#
# 13. Можно ли автоматически закрыть Issue с помощью сообщения в коммите или пул-реквесте? Как это сделать?
#
# Можно автоматически закрыть Issue. Для этого необходимо в описании коммита или в description Pull Request написать Closes #ISSUE_NUMBER. Это приведет к автоматическому закрытию Issue.
#
# 14. Как повторно открыть закрытое Issue, если работа ещё не завершена?
#
# Внизу под комментариями закрытого Issue есть кнопка Reopen issue.
#
#
# ### Фильтрация и поиск
# 15. Как найти все открытые или закрытые Issues в репозитории?
#
# Заходим во вкладку Issues. Открытые Issues можно посмотреть нажав на Open, закрытые - на Closed. Рядом будет указано количество открытых и закрытых Issues соответственно.
#
# 16. Как использовать фильтры для поиска Issues по меткам, исполнителям или другим критериям?
#
# Во вкладке Issues в той же строке, где мы можем посмотреть открытые и закрытые Issues чуть левее есть фильтры для поиска конкретных Issues. Их можно отсортировать по автору, label, проекту, дедлайну/приоритету (milestone), ответственным за Issue (assignees), по типу. При выборе какого-то фильтра нам выйдет результат с конкретными Issue.
#
# 17. Как сортировать Issues по приоритету, дате создания или другим параметрам?
#
# Во вкладке Issues есть строка Search issues. При нажатии на нее будут выпадать разные параметры для сортировки, выбираем параметр и через двоеточие от него выбираем значение этого параметра  (например is:open label:bug). Так же можно отсортировать issues через опцию в правом верхнем углу по дате создания, только что созданным ишьюсам, последним обновленным и другим.
#
#
# ### Интеграции и автоматизация
# 18. Как настроить автоматические уведомления о новых или изменённых Issues?
#
# Заходим во вкладку Issues, выбираем какой-нибудь открытый Issue и проваливаемся в него. Справой стороны будет раздел Notifications и кнопка Subscribe - нажимаем на нее.
#
# 19. Что такое Projects в контексте GitHub, и как связать их с Issues?
#
# Projects на GitHub - это инструмент для управления задачами и проектами, позволяющий организовать работу в визуальных досках. Предварительно такую доску можно создать во вкладке Projects на странице вашего или командного репозитория. Чтобы связать Issue с Project нужно перейти в Issues, с правой стороны нажать на вкладку projects и выбрать конкретный project, с которым мы хотим связать наш issue.
#
# 20. Какие сторонние инструменты можно использовать для автоматизации работы с Issues (например, боты, Webhooks)?
#
# Можно использовать GitHub Actions - это встроенный в GitHub инструмент, который позволяет автоматизировать различные задачи, связанные с разработкой, сборкой, тестированием и развертыванием кода.
#
# Из сторонних инструментов можно использовать Webhooks, Zapier, Microsoft Power Automate, Mergify и другие.
#
#
# ### Коллаборация
# 21. Как упомянуть другого пользователя в комментарии к Issue?
#
# Это можно сделать через @имя_пользователя.
#
# 22. Как запросить дополнительные данные или уточнения у автора Issue?
#
# В комментарии к issue.
#
# 23. Что делать, если Issue неактуально или его нужно объединить с другим?
#
# Если issue стал неактуальным, его нужно закрыть - внизу под комментариями будет кнопка Close issue. Если этот issue нужно объединить с другим, то нажимаем на стрелочку кнопки Close issue и выбираем Close as duplicate. В комментарий к обоим issue нужно добавить #ISSUE_NUMBER и причину, по которой мы объединяем эти ишьюсы.
#
#
# ### Практические аспекты
# 24. Как использовать шаблоны для создания Issues?
#
# В корне репозитория создать папку .github. В ней создать папку ISSUE_TEMPLATE. Внутри папки ISSUE_TEMPLATE создайте файл для каждого шаблона, который вы хотите использовать. Файлы шаблонов должны иметь расширение .md (Markdown).
#
# Например:
#  - bug_report.md - шаблон для багов
#  - feature_request.md - шаблон для запросов на добавление функционала
#
# При создании Issue выбираем один из доступных шаблонов, которые мы создали, заполняем поля шаблона и создаем issue.
#
# 25. Что такое Linked Issues, и как создать связь между задачами?
#
# Linked Issues на GitHub позволяют устанавливать связи между задачами, что помогает лучше организовать и отслеживать работу в проекте. Связанные задачи помогают видеть зависимости и взаимосвязи между различными Issues и Pull Requests.
#
# Можно связать Issue с другим, нажав на Relationships -> Add parent -> выбираем из списка issue, с которым хотим связать этот. Или в комментарии или описании к Issue упомянуть связанное issue через #ISSUE_NUMBER.
#
# 26. Какие метрики (например, время выполнения) можно отслеживать с помощью Issues?
#
#  - Количество открытых и закрытых issues
#  - Время до закрытия issue
#  - Количество повторяющихся метрик
#  - Количество issues по labels
#  - Milestones и их прогресс
#  - Количество issues по исполнителям
#  - Связанные issues и Pull Requests
#
# 27. Какие best practices рекомендуются при работе с Issues в команде?
#
#  - Определить стандарты и шаблоны для Issues
#  - Использовать labels для классификации задач
#  - Определить владельцев и исполнителей issues
#  - Вовлекать команду в обсуждение
#  - Отслеживать прогресс и приоритизировать задачи
#  - Связывать issue с Pull Request
#

#
