from django.test import TestCase

class ViewTestCase(TestCase):
    def text_index_load(self):
        """La carga del index es el apropiado"""
        response=self.client.get('your_server_ip:8000')
        self.assertEqual(response.status_code,00000)