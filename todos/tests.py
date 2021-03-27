from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import FirefoxOptions

class ToDoTest(LiveServerTestCase):
	def setUp(self):
		opt = FirefoxOptions()
		opt.add_argument("--headless")
		self.selenium = webdriver.Firefox(service_log_path = "./geckodriver.log",options=opt)
		super(ToDoTest,self).setUp()

	def tearDown(self):
		self.selenium.quit()
		super(ToDoTest,self).tearDown()

	def test_todo(self):
		selenium = self.selenium
		selenium.get("http://localhost:8000/todos/add")
		title = selenium.find_element_by_id("title")
		desc = selenium.find_element_by_id("text")
		submit = selenium.find_element_by_id("submit")

		title.send_keys("New Title")
		desc.send_keys("New Description")
		submit.click() 

