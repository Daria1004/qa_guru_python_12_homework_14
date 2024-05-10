from selene import browser, have, command, be

class EventsPage:
    def open(self):
        browser.open('https://bestdoctor.ru/events/')
        return self

    def data_blocks(self):
        return browser.element('[class ="t774 "]')

    def should_have_title(self, value):
        browser.element('[data-elem-id="1605710160795"]>.tn-atom').should(have.exact_text(value))

    def open_modal_get_record(self):
        browser.element('#cardbtn3_357052737').click()

    def modal_should_have_title(self, value):
        browser.element('#popuptitle_356924244').should(have.text(value))

    def send_request_for_get_materials(self):
        browser.element('.t-submit').click()

    def get_error_message(self, value):
        browser.element('.t-form__errorbox-link').should(have.text(value))

    def fill_form(self):
        browser.element('#input_1495810354468').should(be.blank).set_value('Ivan')
        browser.element('#input_1495810359387').should(be.blank).set_value('Durian')
        browser.element('#input_1631785246187').should(be.blank).set_value('QA')
        browser.element('#input_1631785318817').should(be.blank).set_value('bestdoctor')
        browser.element('#input_1495810410810').should(be.blank).set_value('9987654321')
        browser.element('#input_1631780843865').should(be.blank).set_value('example@example.com')

    def click_pers_info(self):
        browser.element('[data-input-lid="1631785426890"]').element('a').perform(command.js.remove)
        browser.element('[data-input-lid="1631785426890"]').element('label').click()

    def successful_redirect(self):
        browser.should(have.url('https://bestdoctor.ru/events-success-page'))
