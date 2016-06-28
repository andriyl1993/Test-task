# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class Selenium:
	_driver = None

	def __init__(self, url):
		self._driver = webdriver.Firefox()
		self._driver.get(url)

	def open_elem(self, elem):
		if elem:
			return elem.click()
		else:
			return None

	def open_select_option(self, elem, value):
		select = Select(elem)
		return select.select_by_value(value)		

	def find_elements_by_class_name(self, elem, class_name):
		if not elem:
			elem = self._driver

		return elem.find_elements_by_class_name(class_name)

	def find_elem_xpath(self, elem, xpath):
		if not elem:
			elem = self._driver

		return elem.find_element_by_xpath(xpath)

	def find_elements_by_tag_name(self, elem, tag):
		if not elem:
			elem = self._driver

		return elem.find_elements_by_tag_name(tag)

	def get_elem_html(self, elem):
		return elem.get_attribute('innerHTML')