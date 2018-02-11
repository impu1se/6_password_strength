import password_strength
import unittest
import os


class FileTests(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		empty_file = open('empty_file.txt', 'w+')
		with open('top_password.txt', 'w+') as file:
			file.write('123qwerty\nqwerty1234')

	@classmethod
	def tearDownClass(cls):
		os.remove('empty_file.txt')

	def test_open_not_file(self):
		self.assertRaises(FileNotFoundError, password_strength.get_black_list, '')

	def test_open_empty_file(self):
		self.assertFalse(password_strength.get_black_list('empty_file.txt'))

	def test_open_not_empty_file(self):
		self.assertTrue(password_strength.get_black_list('top_password.txt'))


class PasswordTests(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.black_list = ['123qwerty', 'qwerty1234']
	
	def test_empty_password(self):
		self.assertEqual(password_strength.get_password_strength(' ', self.black_list), 0)

	def test_return_one_point(self):
		self.assertEqual(password_strength.get_password_strength('1', self.black_list), 1)

	def test_return_two_point(self):
		self.assertEqual(password_strength.get_password_strength('ABC1', self.black_list), 2)

	def test_return_three_point(self):
		self.assertEqual(password_strength.get_password_strength('abc123!', self.black_list), 3)	

	def test_return_four_point(self):
		self.assertEqual(password_strength.get_password_strength('Abc123!', self.black_list), 4)

	def	test_return_seven_point(self):
		self.assertEqual(password_strength.get_password_strength('Acc123!@', self.black_list), 7)

	def test_return_ten_point(self):
		self.assertEqual(password_strength.get_password_strength('Abcde12@#', self.black_list), 10)

	def test_return_password_in_black_list(self):
		self.assertEqual(password_strength.get_password_strength('123qwerty', self.black_list), 2)


