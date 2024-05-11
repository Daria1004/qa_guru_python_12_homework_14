import time
from pages.events_page import events_page


def test_get_events(open_events_page):
    events_page.modal_should_have_title('Получить материалы')


def test_send_empty_form(open_events_page):
    events_page.send_request_for_get_materials()
    events_page.get_error_message('Пожалуйста, заполните все обязательные поля')


def test_send_fill_form(open_events_page):
    events_page.fill_form()
    events_page.click_pers_info()
    events_page.send_request_for_get_materials()
    events_page.successful_redirect()
    # time.sleep(3)
    # with allure.step("Сообщение об успешном доступе к вебинару"):
    #     events_page.successful_redirect()
