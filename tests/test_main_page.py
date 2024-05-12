from models.pages.events_page import events_page
from models.pages.main_page import main_page


def test_open_main_page(open_main_page):
    main_page.footer_should_have_text("© 2015 — 2023 ООО «БЕСТДОКТОР»")


def test_feedback_modal(open_main_page):
    main_page.open_feedback_modal()
    main_page.modal_should_have_title('Заполните форму<br>для подключения компании')


def test_header_menu(open_main_page):
    main_page.should_have_upper_menu()


def test_go_to_events(open_main_page):
    main_page.go_to_events()
    events_page.should_have_title("Прошедшие вебинары")


def test_integration_vc(open_main_page):
    main_page.should_have_social_medias()
    main_page.switch_to_vc()
    main_page.open_vc()
