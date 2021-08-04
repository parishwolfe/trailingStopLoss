
from app import app
import unittest


class FlaskTest(unittest.TestCase):
    #Test Settings with no paramaters    
    def test_settings(self):
        tester = app.test_client(self)
        response = tester.post('/settings')
        self.assertEqual(response.status_code, 200)

    #Test Settings with invalid minute
    def test_settings_invalid_minute(self):
        tester = app.test_client(self)
        response = tester.post('/settings?minute=62')
        self.assertEqual(response.status_code, 400)

    #Test Settings with valid minute
    def test_settings_valid_minute(self):
        tester = app.test_client(self)
        response = tester.post('/settings?minute=30')
        self.assertEqual(response.status_code, 200)
    
    #Test Settings with invalid hour
    def test_settings_invalid_hour(self):
        tester = app.test_client(self)
        response = tester.post('/settings?hour=0')
        self.assertEqual(response.status_code, 400)

    #Test Settings with valid hour
    def test_settings_valid_hour(self):
        tester = app.test_client(self)
        response = tester.post('/settings?hour=12')
        self.assertEqual(response.status_code, 200)

    #Test Settings with invalid day
    def test_settings_invalid_day(self):
        tester = app.test_client(self)
        response = tester.post('/settings?day=32')
        self.assertEqual(response.status_code, 400)

    #Test Settings with valid day
    def test_settings_valid_day(self):
        tester = app.test_client(self)
        response = tester.post('/settings?day=1')
        self.assertEqual(response.status_code, 200)

    #Test add stock
    def test_add_stock(self):
        tester = app.test_client(self)
        response = tester.post('/add?ticker=UPRO&percent=20')
        self.assertEqual(response.status_code, 200)

    #test remove stock
    def test_remove_stock(self):
        tester = app.test_client(self)
        response = tester.post('/add?ticker=UPRO&percent=20')
        self.assertEqual(response.status_code, 200)
        response = tester.post('/rm?ticker=UPRO')
        self.assertEqual(response.status_code, 200)

    def test_list_stock(self):
        tester = app.test_client(self)
        response = tester.post('/add?ticker=UPRO&percent=20')
        self.assertEqual(response.status_code, 200)
        response = tester.get("/ls")
        self.assertEqual(response.status_code, 200)

    
if __name__ == '__main__':
    unittest.main()