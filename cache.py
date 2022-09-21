'''
The Cache class caches data, with a delegate to get missing data
'''

from fileinput import filename
import json

class Cache:
	def __init__(self, getAction):
		self.getAction = getAction
		self.data = {}
	
	def __getitem__(self, key):
		if key not in self.data:
			value = self.getAction(key)
			self.data[key] = value
			return value
		return self.data[key]
	
	def __setitem__(self, key, newvalue):
		self.data[key] = newvalue
	
	def has(self, key):
		return key in self.data
	
	def __contains__(self, key):
		return key in self.data


class JsonCache(Cache):
	def __init__(self, getAction, filename):
		super().__init__(getAction)
		self.filename = filename
	
	def __getitem__(self, key):
		if not isinstance(key, str):
			raise RuntimeError('Keys need to be strings!')
		return super().__getitem__(key)
	
	def __setitem__(self, key, newvalue):
		if not isinstance(key, str):
			raise RuntimeError('Keys need to be strings!')
		return super().__setitem__(key, newvalue)
	
	def load(self):
		with open(self.filename, 'r') as json_file:
			self.data = json.load(json_file)
	
	def save(self):
		with open(self.filename, 'w') as json_file:
			json.dump(self.data, json_file)

#------------------------------------------------------------------------------------------

import unittest, pathlib, os

class CacheTests(unittest.TestCase):
	GetCallCount = 0
	GetDelegateReturn = '123'

	@staticmethod
	def GetDelegate(key):
		CacheTests.GetCallCount += 1
		return CacheTests.GetDelegateReturn
	
	def setUp(self):
		CacheTests.GetCallCount = 0

	def test_get_once_action_called(self):
		cache = Cache(CacheTests.GetDelegate)
		result = cache[123]
		self.assertEqual('123', result)
		self.assertEqual(1, CacheTests.GetCallCount)

	def test_get_multiple_action_called(self):
		cache = Cache(CacheTests.GetDelegate)
		result = [ cache[123] for _ in range(10) ]
		self.assertTrue(all(x == '123' for x in result))
		self.assertEqual(1, CacheTests.GetCallCount)

	def test_set_multiple_action_not_called(self):
		cache = Cache(CacheTests.GetDelegate)
		for i in range(10):
			cache[i] = i
		self.assertEqual(0, CacheTests.GetCallCount)
		self.assertTrue(all([cache[i] == i for i in range(10)]))
		self.assertEqual(0, CacheTests.GetCallCount)
	
	def test_has_check(self):
		cache = Cache(CacheTests.GetDelegate)
		cache[123] = '123'
		self.assertTrue(cache.has(123))
		self.assertTrue(123 in cache)
		self.assertFalse(cache.has('abc'))
		self.assertFalse('abc' in cache)


class JsonCacheTests(CacheTests):
	JsonFilename = os.path.join(pathlib.Path(__file__).parent.resolve(), 'test_output.json')

	def test_save_load(self):
		jsoncache1 = JsonCache(CacheTests.GetDelegate, self.JsonFilename)
		jsoncache1['123'] = '123'
		jsoncache1['abc'] = 'abc'
		jsoncache1.save()

		jsoncache2 = JsonCache(CacheTests.GetDelegate, self.JsonFilename)
		jsoncache2.load()
		self.assertTrue('123' in jsoncache2)
		self.assertEqual('123', jsoncache2['123'])
		self.assertTrue('abc' in jsoncache2)
		self.assertEqual('abc', jsoncache2['abc'])
	
	def test_get_set_nonstring(self):
		jsoncache = JsonCache(CacheTests.GetDelegate, self.JsonFilename)
		with self.assertRaises(RuntimeError):
			jsoncache[123] = 123
		
		with self.assertRaises(RuntimeError):
			jsoncache[1.1] = 123




if __name__ == "__main__":
	unittest.main()
