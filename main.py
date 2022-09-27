import regex, logging
from github import Github
import numpy as np

sentence = 'This is a sample string'
x=bool(regex.search(r'is', sentence))
print(x)
