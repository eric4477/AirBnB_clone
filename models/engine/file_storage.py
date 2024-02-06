#!/usr/bin/python3
""" Convert the dictionary representation in python to a JSON string.
	and JSON to a dictionary representation
"""

class FileStorage():
	""" Serializes instances to a JSON file and deserializes JSON file to instances.
	Private class attributes:
		__file_path: string - path to the JSON file (ex: file.json)
		__objects: dictionary - empty but will store all objects by <class name>.id
		(ex: to store a BaseModel object with id=12121212, the key will be BaseModel.12121212)
	Public instance methods:
		all(self): returns the dictionary __objects
		new(self, obj): sets in __objects the obj with key <obj class name>.id
		save(self): serializes __objects to the JSON file (path: __file_path)
		reload(self): deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ;
		  otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
	"""
	__file_path = ""
	__objects = {}
	
