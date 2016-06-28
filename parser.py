import requests
from bs4 import BeautifulSoup

from _selenium import Selenium

def get_request(url, **kwargs):
	return requests.get(url, data=kwargs)


def post_request(url, **kwargs):
	return requests.post(url, params=kwargs)


def bs_find_all_regions(html):	
	soup = BeautifulSoup(html, 'html.parser')

	regions_html = soup.find("select", {"name": "ctl00$ContentPlaceHolder1$ddlOblast"}).findAll("option")
	regions = []
	for region in regions_html:
		if region.get("value"):
			regions.append({
				"value": region.get("value"),
				"name": region.get_text(),
			})
	return regions


def bs_parse_options(html):
	soup = BeautifulSoup(html, 'html.parser')

	html_arr = soup.findAll("option")
	res = []
	for elem in html_arr:
		if elem.get("value"):
			res.append({
				"value": elem.get("value"),
				"name": elem.get_text(),
			})
	return res


if __name__ == "__main__":
	request_url = "http://services.ukrposhta.com/postindex_new/default.aspx"
	html = get_request(request_url).text
	regions = bs_find_all_regions(html)
		
	s = Selenium(request_url)

	elem = s.find_elements_by_class_name(None, "ih1")[1]
	val = s.open_elem(elem)

	region_selector = "//select[contains(@name, 'ctl00$ContentPlaceHolder1$ddlOblast')]"
	elem_region = s.find_elem_xpath(None, )
	s.open_elem(elem_region)

	for region in regions:
		s.open_select_option(elem_region, region.get("value"))

		district_selector = "//select[contains(@name, 'ctl00$ContentPlaceHolder1$ddlRegion')]"

		elem_district = s.find_elem_xpath(None, district_selector)
		s.open_elem(elem_district)
		html = s.get_elem_html(elem_district)
		region["districts"] = bs_parse_options(html)

		for district in region["districts"]:
			option_town = s.find_elem_xpath(elem_district, '//option[@value="' + district.get("value") + '"]')
			s.open_elem(option_town)

			city_selector = "//select[contains(@name, 'ctl00$ContentPlaceHolder1$ddlCity')]"

			elem_district = s.find_elem_xpath(None, city_selector)
			html = s.get_elem_html(elem_district)
			district["towns"] = bs_parse_options(html)

			for town in district["towns"]:
				### parse table with indexes
				pass

	print regions