import allure
from selene import browser, have, command, be

class EventsPage:

    def open(self):
        with allure.step("Открытие страницы Прошедшие вебинары"):
            browser.open('/events')

    def should_have_title(self, value):
        with allure.step("Открытие страницы Прошедшие вебинары"):
            browser.element('[data-elem-id="1605710160795"]>.tn-atom').should(have.exact_text(value))

    def open_modal_get_record(self):
        with allure.step("Получить запись"):
            browser.element('#cardbtn3_357052737').click()

    def modal_should_have_title(self, value):
        with allure.step("Открытие  модального окна Получить материалы"):
            browser.element('#popuptitle_356924244').should(have.text(value))

    def send_request_for_get_materials(self):
        with allure.step("Отправить заявку на получение материалов"):
            browser.element('.t-submit').click()

    def get_error_message(self, value):
        with allure.step("Получено сообщение об ошибке"):
            browser.element('.t-form__errorbox-link').should(have.text(value))

    def fill_form(self):
        with allure.step("Заполнение формы"):
            browser.element('#input_1495810354468').should(be.blank).set_value('Ivan')
            browser.element('#input_1495810359387').should(be.blank).set_value('Durian')
            browser.element('#input_1631785246187').should(be.blank).set_value('QA')
            browser.element('#input_1631785318817').should(be.blank).set_value('bestdoctor')
            browser.element('#input_1495810410810').should(be.blank).set_value('9987654321')
            browser.element('#input_1631780843865').should(be.blank).set_value('example@example.com')

    def click_pers_info(self):
        with allure.step("Кликнуть чекбокс персональные данные"):
            browser.element('[data-input-lid="1631785426890"]').element('a').perform(command.js.remove)
            browser.element('[data-input-lid="1631785426890"]').element('label').click()

    def successful_redirect(self):
        with allure.step("Сообщение об успешном доступе к вебинару"):
            browser.should(have.url('https://bestdoctor.ru/events-success-page'))


events_page = EventsPage()
