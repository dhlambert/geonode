from django.contrib.auth import get_user_model
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import Client
from django.urls import reverse

from geonode.services.utils import test_resource_table_status
from . import enumerations, forms

from selenium import webdriver
# from selenium.webdriver.chrome.webdriver import WebDriver
# from webdriver_manager.chrome import ChromeDriverManager


class WmsServiceHarvestingTestCase(StaticLiveServerTestCase):
    selenium = None

    @classmethod
    def setUpClass(self):
        super(WmsServiceHarvestingTestCase, self).setUpClass()

        try:
            self.client = Client()
            UserModel = get_user_model()
            self.user = UserModel.objects.create_user(username='test', password='test@123', first_name='ather',
                                                     last_name='ashraf', is_staff=True,
                                                     is_active=True, is_superuser=False)
            self.user.save()
            self.client.login(username='test', password='test@123')
            self.cookie = self.client.cookies['sessionid']
            self.selenium = webdriver.Firefox()
            self.selenium.implicitly_wait(10)
            self.selenium.get(self.live_server_url + '/')
            self.selenium.add_cookie({'name': 'sessionid', 'value': self.cookie.value, 'secure': False, 'path': '/'})
            self.selenium.refresh()
            reg_url = reverse('register_service')
            self.client.get(reg_url)

            url = 'https://demo.geo-solutions.it/geoserver/ows?service=wms&version=1.3.0&request=GetCapabilities'
            service_type = enumerations.WMS
            form_data = {
                'url': url,
                'type': service_type
            }
            forms.CreateServiceForm(form_data)

            response = self.client.post(reverse('register_service'), data=form_data)
            self.selenium.get(self.live_server_url + response.url)
            self.selenium.refresh()
        except Exception as e:
            msg = str(e)
            print(msg)

    @classmethod
    def tearDownClass(self):
        if self.selenium:
            self.selenium.quit()
            super(WmsServiceHarvestingTestCase, self).tearDownClass()

    def test_harvest_resources(self):
        if self.selenium:
            table = self.selenium.find_element_by_id('resource_table')
            test_resource_table_status(self, table, False)

            self.selenium.find_element_by_id('id-filter').send_keys('atlantis:roads')
            self.selenium.find_element_by_id('btn-id-filter').click()
            test_resource_table_status(self, table, True)

            self.selenium.find_element_by_id('name-filter').send_keys('landmarks')
            self.selenium.find_element_by_id('btn-name-filter').click()
            test_resource_table_status(self, table, True)

            self.selenium.find_element_by_id('desc-filter').send_keys('None')
            self.selenium.find_element_by_id('btn-desc-filter').click()
            test_resource_table_status(self, table, True)

            self.selenium.find_element_by_id('desc-filter').send_keys('')
            self.selenium.find_element_by_id('btn-desc-filter').click()
            test_resource_table_status(self, table, True)

            self.selenium.find_element_by_id('btnClearFilter').click()
            test_resource_table_status(self, table, False)
            self.selenium.find_element_by_id('id-filter').send_keys('atlantis:tiger_roads_tiger_roads')

            # self.selenium.find_element_by_id('btn-id-filter').click()
            # self.selenium.find_element_by_id('option_atlantis:tiger_roads_tiger_roads').click()
            # self.selenium.find_element_by_tag_name('form').submit()
