# -*- coding: iso-8859-15 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os, logging, json, pickle


class Linkedin(object):
    # driver = webdriver.PhantomJS() # service_log_path="C:/Tracer/tracer-master/logs/slog.log")

    def link(self, nam):
        driver = webdriver.PhantomJS()
        driver.get("https://www.linkedin.com")
        src_url = "https://www.linkedin.com/pub/dir/?firstName=" + nam.split(" ", 1)[0] + \
              "&lastName=" + nam.split(" ", 1)[1]
        driver.get(src_url)
        logging.debug(driver.current_url)
        lis = []
        if src_url != driver.current_url:
            try:
                d1 = driver.find_element_by_xpath('.//div[@class="profile-overview"]').text
                d = d1.split("\n", 1)[1]
                n = d1.split("\n", 1)[0]
            except NoSuchElementException:
                d = ''
                n = ''
            try:
                i = driver.find_element_by_xpath('.//div[@class="profile-picture"]/a').get_attribute('href')
            except NoSuchElementException:
                i = "https://static.licdn.com/scds/common/u/images/themes/katy/ghosts/person/ghost_person_100x100_v1.png"
            link_url = driver.current_url
            lis.append({'details': d.encode("ascii"), 'image': i.encode("ascii", 'ignore'), 'Profile_link': link_url.encode("ascii", 'ignore'), 'name': n.encode("ascii", 'ignore')})
        else:
            ul = driver.find_elements_by_xpath('//div[@class="profile-card"]')
            for lic in ul:
                d1 = lic.find_element_by_xpath('.//div[@class="content"]').text  #
                d = d1.split("\n", 1)[1]
                n = d1.split("\n", 1)[0]
                i = lic.find_element_by_xpath('.//a/img').get_attribute('src')  #
                if not i:
                    i = lic.find_element_by_xpath('.//a/img').get_attribute('data-delayed-url')
                link_url = lic.find_element_by_xpath('.//a[@class="profile-img"]').get_attribute('href')
                lis.append({'details': d.encode("ascii", 'ignore'), 'image': i.encode("ascii", 'ignore'), 'Profile_link': link_url.encode("ascii", 'ignore'), 'name': n.encode("ascii", 'ignore')})
        driver.quit()
        return json.dumps(lis)

   # def chk_fun(self, nam):
   #     try:
   #         output = self.link(nam=nam)
   #     except:
   #         output = ""
   #         self.driver.quit()
   #     return output#
