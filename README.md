[![Build Status](https://travis-ci.com/AlbertUlysses/Kanye_the_Wrapper.svg?branch=master)](https://travis-ci.com/AlbertUlysses/Kanye_the_Wrapper)
# Kanye the Python Wrapper
This is a wrapper for kanye.rest - a Free REST API for random Kanye West quotes by Andrew Jazbec.
Thank You [Andrew!](https://github.com/ajzbc)

* Wraps GET requests found here -> [https://kanye.rest/](https://kanye.rest/)

# Version
#TODO: look into versioning for PIP

# Dependencies
None

# Usage
## The Wrapper

There is one class that you need to import, and one main method for the wrapper. The class is Kanye and the method is west(), below is an example of running the wrapper in the Python interpreter:
```
>>> from kanye_the_wrapper import Kanye
>>> example = Kanye()
>>> print(example.west())
I want the world to be better! All I want is positive! All I want is dopeness!
>>> 
```

The method returns type string.
Generating a random quote can be enough in most cases. In which case you can stop reading here. 

## Saving Quotes

Saving quotes is the second functionality built into the package. There are several methods and steps necessary to save quotes into the dictionary. 
If you liked a quote and want to return to it, you can now use the `heard_em_say` method.

The method keeps a list of the last 5 quotes and you can call this list by running: 
`example.heard_em_say()`. 
If you run this method before calling a random quote, you'll get a fun error message.

## Current TODO: 

* Look into changing how to save to dictionary, use heapq.
* Update Readme for function explanation.
* Write unit tests.
