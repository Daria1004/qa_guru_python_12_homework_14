import allure, time
from pages.events_page import events_page


def test_get_events(open_events_page):
    with allure.step("Открытие  модального окна Получить материалы"):
        events_page.modal_should_have_title('Получить материалы')


def test_send_empty_form(open_events_page):
    with allure.step("Отправить заявку на получение материалов"):
        events_page.send_request_for_get_materials()
    with allure.step("Получено сообщение об ошибке"):
        events_page.get_error_message('Пожалуйста, заполните все обязательные поля')


def test_send_fill_form(open_events_page):
    with allure.step("Отправить заявку на получение материалов"):
        events_page.send_request_for_get_materials()
    with allure.step("Заполнение формы"):
        events_page.fill_form()
    with allure.step("Кликнуть чекбокс персональные данные"):
        events_page.click_pers_info()
    with allure.step("Отправить заявку на получение материалов"):
        events_page.send_request_for_get_materials()
    # time.sleep(3)
    # with allure.step("Сообщение об успешном доступе к вебинару"):
    #     events_page.successful_redirect()
