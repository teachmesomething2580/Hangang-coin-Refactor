from bs4 import BeautifulSoup
from django.db import models
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class River(models.Model):
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_river_temperature(cls):
        url = 'http://www.koreawqi.go.kr/index_web.jsp'

        options = Options()
        options.headless = True
        browser = webdriver.Firefox(options=options)

        browser.get(url)

        browser.switch_to.frame('MainFrame')
        browser.find_element_by_id('container').find_element_by_id('state')
        browser.find_element_by_class_name('tab_container').find_element_by_class_name('timetable')
        td = browser.find_element_by_xpath('//*[@id="div_layer_btn1_r1"]/table/tbody/tr[18]').get_attribute('outerHTML')
        browser.switch_to.default_content()

        soup = BeautifulSoup(td, 'html.parser')
        td_list = soup.select('td')

        temperature = td_list[0].get_text(strip=True)

        River.objects.create(
            temperature=temperature,
        )