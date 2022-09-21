'''
The Cache class caches data, with a delegate to get missing data
'''

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

#------------------------------------------------------------------------------------------

import unittest

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


if __name__ == "__main__":
	unittest.main()
