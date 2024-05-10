from selene import browser, have, command, be

class MainPage:
    header = browser.element('#t-header')
    footer = browser.element('#t-footer')


    def open(self):
        browser.open('/')
        return self

    def footer_should_have_text(self, value):
        self.footer.perform(command.js.scroll_into_view)
        self.footer.should(have.text(value))

    def open_feedback_modal(self):
        browser.element('[data-artboard-recid="473291348"].t396__filter').perform(command.js.remove)
        browser.element('[data-artboard-recid="473291348"].t396__carrier').perform(command.js.remove)
        browser.element('[href="#popup:myform-dms"]').perform(command.js.scroll_into_view)
        browser.element('a[href="#popup:myform-dms"]').click()

    def modal_should_have_title(self, value):
        browser.element('[field="tn_text_1470209944682"]').should(have.text(value))

    def go_to_events(self):
        browser.all("a").element_by(have.exact_text("События")).click()

    def should_have_upper_menu(self):
        self.header.should(be.visible)
        self.header.element('[data-elem-id="1663269457691"]').element('a').should(have.attribute('href', 'https://bestdoctor.ru/dms/'))
        self.header.element('[data-elem-id="1680249993768"]').element('a').should(have.attribute('href', 'https://bestdoctor.ru/about/'))
        self.header.element('[data-elem-id="1653047602052"]').element('a').should(have.attribute('href', 'https://bestdoctor.ru/events/'))
        self.header.element('[data-elem-id="1653048299711"]').element('a').should(have.attribute('href', 'https://blog.bestdoctor.ru/'))

    def should_have_info(self):
        browser.element.element('[data-elem-id="1652883525054"]').should(have.text('Когда страховая — главный эксперт в ДМС'))
        browser.element.element('[data-elem-id="1652883525054"]').should(have.text('Когда ДМС удобно пользоваться'))
        browser.element.element('#sbs-473291340-1652883525054').should(have.text('Когда HR свободен от рутины и проблем'))
        browser.element.element('#sbs-473291343-1652883525054').should(have.text('Когда сотрудники довольны сервисом'))

    def should_have_social_medias(self):
        self.footer.perform(command.js.scroll_into_view)
        self.footer.should(be.visible)
        self.footer.element('[data-elem-id="1690544179272"]').element('a').should(have.attribute('href', 'https://vc.ru/bestdoctor'))
        self.footer.element('[data-elem-id="1690544192637"]').element('a').should(have.attribute('href', 'https://vk.com/bestdoctor'))
        self.footer.element('[data-elem-id="1605874985072"]').element('a').should(have.attribute('href', 'https://t.me/bestdoctormedia'))
        self.footer.element('[data-elem-id="1690544762473"]').element('a').should(have.attribute('href', 'https://ok.ru/group/70000003501952'))
        self.footer.element('[data-elem-id="1705913572432"]').element('a').should(have.attribute('href', 'https://dzen.ru/bestdoctor'))

    def switch_to_vc(self):
        browser.element('[data-elem-id="1663269457691"]').click()

    def open_vc(self):
        browser.open("https://vc.ru/bestdoctor")
