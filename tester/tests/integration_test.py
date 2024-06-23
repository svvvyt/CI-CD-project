import unittest
import os
import requests


class IntegrationTest(unittest.TestCase):
    def __init__(self, method: str = "runTest") -> None:
        super().__init__(method)
        self.base_url = os.environ.get("BASE_URL", "http://app:5000")

    def test_endpoint_index_get(self):
        res = requests.get(self.base_url)
        self.assertEqual(res.status_code, 200)

    def test_endpoint_upload_get(self):
        res = requests.get(f'{self.base_url}/upload')
        self.assertEqual(res.status_code, 200)

    def test_endpoint_upload_post(self):
        with open('temp.txt', 'w') as f:
            f.write('Test file')

        files = {'file': open('temp.txt', 'rb')}
        res = requests.post(f'{self.base_url}/upload', files=files)

        os.remove('temp.txt')

        self.assertEqual(res.status_code, 200)

    def test_endpoint_download_get(self):
        res = requests.get(f'{self.base_url}/download/temp.txt')
        self.assertEqual(res.status_code, 404)

    def test_endpoint_files_get(self):
        res = requests.get(f'{self.base_url}/files')
        self.assertEqual(res.status_code, 200)

    def test_endpoint_to_files_get_redirect(self):
        res = requests.get(f'{self.base_url}/to_files')
        self.assertEqual(res.status_code, 200)

    def test_endpoint_success_get(self):
        res = requests.get(f'{self.base_url}/success/python')
        self.assertEqual(res.status_code, 200)

    def test_endpoint_increment_get_exception(self):
        self.assertRaises(
            requests.exceptions.TooManyRedirects,
            requests.get, f'{self.base_url}/increment/50'
        )

    def test_endpoint_check_even_get_on_even(self):
        res = requests.get(f'{self.base_url}/check_even/4')
        self.assertEqual(res.status_code, 200)

    def test_endpoint_check_even_get_on_odd(self):
        res = requests.get(f'{self.base_url}/check_even/3')
        self.assertEqual(res.status_code, 200)

    def test_endpoint_even_get_on_even(self):
        res = requests.get(f'{self.base_url}/even/4')
        self.assertEqual(res.status_code, 200)

    def test_endpoint_odd_get_on_odd(self):
        res = requests.get(f'{self.base_url}/odd/3')
        self.assertEqual(res.status_code, 200)

    def test_endpoint_login_post_good_creds(self):
        data = {'name': 'user', 'password': 'pass'}
        res = requests.post(f'{self.base_url}/login', data=data)
        self.assertEqual(res.status_code, 401)

    def test_endpoint_login_post_bad_creds(self):
        data = {'name': 'wrong_user', 'password': 'wrong_pass'}
        res = requests.post(f'{self.base_url}/login', data=data)
        self.assertEqual(res.status_code, 401)


if __name__ == '__main__':
    unittest.main()
