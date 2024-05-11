import allure
from pages.main_page import main_page
from pages.events_page import events_page


def test_open_main_page(open_main_page):
    with allure.step("Проверка наличия текста подвала"):
        main_page.footer_should_have_text("© 2015 — 2023 ООО «БЕСТДОКТОР»")


def test_feedback_modal(open_main_page):
    with allure.step("Открытие  модального окна Оставить заявку"):
        main_page.open_feedback_modal()
    with allure.step("Проверка заголовка модального окна"):
        main_page.modal_should_have_title('Заполните форму<br>для подключения компании')


def test_header_menu(open_main_page):
    with allure.step("Проверка корректной навигации вверху страницы"):
        main_page.should_have_upper_menu()


def test_go_to_events(open_main_page):
    with allure.step("Переход в меню События"):
        main_page.go_to_events()
    with allure.step("Открытие страницы Прошедшие вебинары"):
        events_page.should_have_title("Прошедшие вебинары")


def test_integration_vc(open_main_page):
    with allure.step("Проверка наличия ссылок на социальные сети в футере"):
        main_page.should_have_social_medias()
    with allure.step("Переход на на платформу vc"):
        main_page.switch_to_vc()
    with allure.step("Открытие страницы bestdoctor на платформе vc"):
        main_page.open_vc()
