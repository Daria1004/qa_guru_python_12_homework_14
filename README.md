# Проект по тестированию главной страницы сайта "bestdoctor.ru"
> <a target="_blank" href="https://bestdoctor.ru/">bestdoctor.ru</a>

![This is an image](/design/images/bestdoctor_ru_main.png)

#### Список проверок, реализованных в UI-автотестах
- [x] Открытие главной страницы сайта
- [x] Вызов модального окна "Заполните форму для подключения компании"
- [x] Наличие требуемых заголовков в верхнем меню страницы
- [x] Переход по заголовку в меню
- [x] Наличие социальных сетей в подвале сайта и переход в одну из них
- [x] Вызов модального окна 'Получить материалы'
- [x] Получение доступа к вебинару
- [x] Негативная проверка при отправке незаполненной формы

## Проект реализован с использованием
Java Gradle IntelliJ IDEA Selenide Selenoid JUnit5 Jenkins Allure Report Allure TestOps Telegram Jira

![This is an image](/design/icons/Python.png)![This is an image](/design/icons/pycharm.png)![This is an image](/design/icons/pytest.png)![This is an image](/design/icons/github.png)![This is an image](/design/icons/Selenoid.png)![This is an image](/design/icons/Jenkins.png)![This is an image](/design/icons/allure.png)![This is an image](/design/icons/Allure_Report.png)![This is an image](/design/icons/Telegram.png)

## Для запуска автотестов в Jenkins
### 1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/qa_guru_python_12_homework_14/">проект</a>

![This is an image](/design/images/jenkins1.png)

### 2. Выбрать пункт **Собрать с параметрами**/**Build with Parameters**

![This is an image](/design/images/jenkins2.png)

### 3. В случае необходимости изменить параметры
- [x] Версия браузера по умолчанию 100, вручную можно внести другое значение (99.0, 120.0 или др.)
- [x] Значение окружения можно выбрать из выпадающего списка
- [x] Также можно изменить комментарий

### 4. Нажать **Собрать**/ **Build**

![This is an image](/design/images/jenkins4.png)

### 5. Результат запуска сборки можно посмотреть в отчёте Allure

![This is an image](/design/images/jenkins5a.png)
![This is an image](/design/images/jenkins5b.png)

## Локальный запуск автотестов
Пример командной строки:
> 1. Склонировать репозиторий
> 2. Открыть проект и установить интерпретатор
> 3. Создать файл с переменными окружения `.env` по образцу в корне проекта
> 4. Запустить тесты 

Пример командной строки:
```bash
pytest .
```

Получение отчёта:
```bash
allure serve build/allure-results
```
## Пример видеозаписи прохождения теста
![Отчет в Allure](design/images/video_test.gif)

## Настроено автоматическое оповещение о результатах сборки Jenkins в Telegram-бот
![This is an image](/design/images/bot.png)
