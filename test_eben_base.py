#!/usr/bin/python3
"""
	Test
"""

from models.base_model import BaseModel
from datetime import datetime

def main():
	user = BaseModel(created_at="1999-08-04T12:56:14.419225")
	print(user)
#	print(datetime.now().isoformat())

if __name__ == "__main__":
	main()
