# Практикум SDET: задание UI
Проект содержит UI тесты для Chrome и FireFox<br>
 Объект тестирования:
 https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager
 ## Тесты
1. Создание клиента (Add Customer).
2. Сортировка клиентов по имени (First Name).
3. Удаление клиента.

## Технологии и инструменты
* Python 3.10
* Selenium Webdriver
* Pytest
* pytest-xdist
* POM (Page Object Model)
* Allure
* CI/CD с GitHub Actions
* GitHub Pages

## Работа с проектом локально (Windows)
1. Установить python 3.10
2. Склонировать проект на компьютер через терминал Git Bash на Windows
git clone https://github.com/solar-owl/Practice_SDET_UI.git
3. Создать виртуальное окружение
```
python -m venv venv
```
4. Установить необходимые пакеты
```
pip install -r requirements.txt
```
5. Запуск тестов (в 3 потока)
```
pytest -v
```
6. Генерация отчетов Allure (необходимо, чтобы был скачан Allure)
```
pytest -v -s --alluredir reports
allure serve reports
```

## Запуск автотестов в GitHub Actions
1. В вкладке **Actions** перейти в workflow: **Automated tests**
2. Нажать **Run workflow**
3. В окне в выпадающем списке выбрать тест, который нужно запустить, или все (автоматически выбран запуск всех автотестов)
4. Нажать на кнопку **Run workflow**

## Allure Reports
Allure отчеты дочтупны по ссылке: https://solar-owl.github.io/Practice_SDET_UI/
