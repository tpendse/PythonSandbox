# PythonSandbox
This repo is a collection for python scripts I have created as a part of other work

<br/>

---
## Cache
Cache aims to save data in save data locally, with a get delegate to fetch missing data

Use the `Cache` class to 

```python
from cache import Cache

def getDelegate(key):
	# Time consuming fetch data here ...
	return value

cache = Cache(getDelegate)

# Get for the first time - delegate invoked
value = cache[123]

# Get again - delegate not called, cached data returned instead
value = cache[123]

# Get a different key - delegate called for new key
value = cache['abc']

# Get again - delegate not called, cached data returned instead
value = cache['abc']
```

Run the `Cache` tests by running the script from command line
```Batchfile
python cache.py
```

## JsonCache
`JsonCache` Extends the `Cache` class to store and retrieve data to and from a JSON file

Works exactly like `Cache` however, since JSON cannot store non-string keys adding the additional restriction that get & set keys have to be strings. Specifically, `str` types

<br/>

---
## Karpekar Number
This script attempts to recreate [karpekar's number](https://en.wikipedia.org/wiki/6174_(number)) :

The logic is:
1. Take any four-digit number, using at least two different digits (leading zeros are allowed).
2. Arrange the digits in descending and then in ascending order to get two four-digit numbers, adding leading zeros if necessary.
3. Subtract the smaller number from the bigger number.
4. Go back to step 2 and repeat.

Eventually you will reach kaprekar's number => 6174

The entry criteria for this to work are:
1. Input is atleast a four digit number - if less than 4, zeros padded missing digits 
2. If there are atleast two different digits. For example, the number `9999` is disqualified since number of unique digits is 1

Running the script generates a random 4 digit number that fit the input criteria then process till Karpekar's constant is reached. This is repeated for 10 different times

Run the script to generate output,
```Batchfile
python karpekar.py
-------------------------------
Input is: 7314
Found Kaprekars Constant in 7 iterations
-------------------------------
Input is: 97
Found Kaprekars Constant in 3 iterations
-------------------------------
Input is: 6086
Found Kaprekars Constant in 6 iterations
-------------------------------
Input is: 224
Found Kaprekars Constant in 4 iterations
-------------------------------
Input is: 66
Found Kaprekars Constant in 4 iterations
-------------------------------
Input is: 419
Found Kaprekars Constant in 3 iterations
-------------------------------
Input is: 75
Found Kaprekars Constant in 5 iterations
-------------------------------
Input is: 7850
Found Kaprekars Constant in 6 iterations
-------------------------------
Input is: 501
Found Kaprekars Constant in 7 iterations
-------------------------------
Input is: 6944
Found Kaprekars Constant in 7 iterations
```
<br/>

---
## FormatJson

* This script aims to format a json elements to be more pretty
* It replaces long leading spaces to tabs
* It formats json objects into prettier version, by aligning all key value start/end positions
* For example, 
```json
{
    "name": "something",
    "somethinglong": "somethingelse",
	"child" : {
		"child1" : 123,
		"childkey_2" : "abc"
	}
}
```
is formatted to,
```json
{
	"name"          : "something",
	"somethinglong" : "somethingelse",
	"child" : {
		"child1"     : 123,
		"childkey_2" : "abc"
	}
}
```