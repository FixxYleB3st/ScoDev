from django.test import SimpleTestCase

from django.urls import resolve, reverse
from index.views import index, index_log
from about.views import index as about
from contact.views import index as contact
from sellers.views import index as sellers
from login.views import register, loginPage, logoutUser

class TestUrls(SimpleTestCase):
	def test_home_url(self):
		url = reverse('home')
		self.assertEquals(resolve(url).func, index)
	def test_home_log_url(self):
		url = reverse('home_log')
		self.assertEquals(resolve(url).func, index_log) 

	def test_about_url(self):
		url = reverse('about')
		self.assertEquals(resolve(url).func, about) 

	def test_contact_url(self):
		url = reverse('contact')
		self.assertEquals(resolve(url).func, contact)

	def test_sellers_url(self):
		url = reverse('sellers')
		self.assertEquals(resolve(url).func, sellers)  

	def test_signin_url(self):
		url = reverse('register')
		self.assertEquals(resolve(url).func, register)