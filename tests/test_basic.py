import unittest
import os
from crypto_utils import encrypt_data, decrypt_data

class TestCryptoUtils(unittest.TestCase):

    def test_encrypt_decrypt(self):
        original = b"this is a secret message"
        encrypted = encrypt_data(original)
        decrypted = decrypt_data(encrypted)

        self.assertNotEqual(original, encrypted)
        self.assertEqual(original, decrypted)

    def test_encrypt_returns_bytes(self):
        data = b"test"
        encrypted = encrypt_data(data)
        self.assertIsInstance(encrypted, bytes)


class TestUsersFile(unittest.TestCase):

    def test_users_file_exists(self):
        self.assertTrue(os.path.exists("users.txt"))


if __name__ == "__main__":
    unittest.main()
