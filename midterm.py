# -*- coding: utf-8 -*-
"""midterm.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pC7Y4JzWmvViT0MHIrqVAxdCsWWQ0iAH
"""

def file_length(file_name):
    file = open(file_name)
    contents = file.read()
    file.close()
    print(len(contents))