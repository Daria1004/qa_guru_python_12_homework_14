import allure
from selene import browser, have, command, be


class MainPage:
    header = browser.element('#t-header')
    footer = browser.element('#t-footer')

    def open(self):
        with allure.step("Открытие главной страницы"):
            browser.open('/')

    def footer_should_have_text(self, value):
        with allure.step("Проверка наличия текста подвала"):
            self.footer.perform(command.js.scroll_into_view)
            self.footer.should(have.text(value))

    def open_feedback_modal(self):
        with allure.step("Открытие  модального окна Оставить заявку"):
            browser.element('[href="#popup:myform-dms"]').perform(command.js.click)

    def modal_should_have_title(self, value):
        with allure.step("Проверка заголовка модального окна"):
            value = value.replace('<br>', '\n').strip()
            browser.element('[field="tn_text_1470209944682"]').should(have.text(value))

    def go_to_events(self):
        with allure.step("Переход в меню События"):
            browser.all("a").element_by(have.exact_text("События")).click()

    def should_have_upper_menu(self):
        with allure.step("Проверка корректной навигации вверху страницы"):
            self.header.should(be.visible)
            self.header.element('[data-elem-id="1663269457691"]').element('a').should(
                have.attribute('href', 'https://bestdoctor.ru/dms/'))
            self.header.element('[data-elem-id="1680249993768"]').element('a').should(
                have.attribute('href', 'https://bestdoctor.ru/about/'))
            self.header.element('[data-elem-id="1653047602052"]').element('a').should(
                have.attribute('href', 'https://bestdoctor.ru/events/'))
            self.header.element('[data-elem-id="1653048299711"]').element('a').should(
                have.attribute('href', 'https://blog.bestdoctor.ru/'))

    def should_have_info(self):
        browser.element.element('[data-elem-id="1652883525054"]').should(
            have.text('Когда страховая — главный эксперт в ДМС'))
        browser.element.element('[data-elem-id="1652883525054"]').should(have.text('Когда ДМС удобно пользоваться'))
        browser.element.element('#sbs-473291340-1652883525054').should(
            have.text('Когда HR свободен от рутины и проблем'))
        browser.element.element('#sbs-473291343-1652883525054').should(have.text('Когда сотрудники довольны сервисом'))

    def should_have_social_medias(self):
        with allure.step("Проверка наличия ссылок на социальные сети в футере"):
            self.footer.perform(command.js.scroll_into_view)
            self.footer.should(be.visible)
            self.footer.element('[data-elem-id="1690544179272"]').element('a').should(
                have.attribute('href', 'https://vc.ru/bestdoctor'))
            self.footer.element('[data-elem-id="1690544192637"]').element('a').should(
                have.attribute('href', 'https://vk.com/bestdoctor'))
            self.footer.element('[data-elem-id="1605874985072"]').element('a').should(
                have.attribute('href', 'https://t.me/bestdoctormedia'))
            self.footer.element('[data-elem-id="1690544762473"]').element('a').should(
                have.attribute('href', 'https://ok.ru/group/70000003501952'))
            self.footer.element('[data-elem-id="1705913572432"]').element('a').should(
                have.attribute('href', 'https://dzen.ru/bestdoctor'))

    def switch_to_vc(self):
        with allure.step("Переход на на платформу vc"):
            browser.element('[data-elem-id="1663269457691"]').click()

    def open_vc(self):
        with allure.step("Открытие страницы bestdoctor на платформе vc"):
            browser.open("https://vc.ru/bestdoctor")


main_page = MainPage()
