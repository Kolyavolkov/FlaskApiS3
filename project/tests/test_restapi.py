from restapi import __version__
from restapi import app
import unittest
from io import BytesIO


def test_version():
    assert __version__ == "0.1.0"


class BasicTestCase(unittest.TestCase):
    def test_home(self):
        tester = app.test_client(self)
        response = tester.get("/api", content_type="html/text")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'{\n    "hello": "world"\n}\n')

    def test_buckets(self):
        tester = app.test_client(self)
        response = tester.get("/api/buckets", content_type="html/text")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b"bucket" in response.data)

    def test_write_access(self):
        app_client = app.test_client()
        response = app_client.post(
            "/api/upload",
            buffered=True,
            content_type="multipart/form-data",
            data={
                "bucket": "volkovsssbucket",
                "user": "TEST",
                "file": (BytesIO(b"test contents"), "test.jpg"),
            },
        )
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
