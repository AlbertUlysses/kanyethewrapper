[![Build Status](https://travis-ci.com/AlbertUlysses/kanyethewrapper.svg?branch=master)](https://travis-ci.com/AlbertUlysses/kanyethewrapper)
[![codecov](https://codecov.io/gh/AlbertUlysses/kanyethewrapper/branch/master/graph/badge.svg)](https://codecov.io/gh/AlbertUlysses/kanyethewrapper)

# Kanye the Python Wrapper
This is a wrapper for kanye.rest - a Free REST API for random Kanye West quotes by Andrew Jazbec.
Thank You [Andrew!](https://github.com/ajzbc)

* Wraps GET requests found here -> [https://kanye.rest/](https://kanye.rest/)

# Version
TODO: look into versioning for PIP

# Dependencies
None

# Usage
### The Wrapper

There is one class that you need to import, and one main method for the wrapper. The class is Kanye and the method is west(), below is an example of running the wrapper in the Python interpreter:
```
>>> from kanyethewrapper import Kanye
>>> example = Kanye()
>>> print(example.west())
I want the world to be better! All I want is positive! All I want is dopeness!
>>> 
```
The method returns type string. 
Generating a random quote can be enough in most cases. 
There is another built in functionality for saving quotes, which you can read in the next section.

### Saving Quotes

If you like a quote and want to access it later, there are two steps you need to take. 
First you need run the `watch_the_throne()` method. 
This method saves the last quote that the API called. 
If the `west()` method was not called, then you'll receive an error. 
To see the saved quote, run the `heard_em_say()` method. 
This will return a dictionary with all saved quotes. 
If you called the method without saving a quote first, then you'll receive an error. 
Below is an example of this with the Python Interpreter. 

```
>>> from kanyethewrapper import Kanye
>>> example = Kanye()
>>> example.west()
'My greatest pain in life is that I will never be able to see myself perform live.'
>>> example.watch_the_throne()
'Quote Saved'
>>> example.heard_em_say()
{1: 'My greatest pain in life is that I will never be able to see myself perform live.'}
>>> 
```

### Dictionary Size

The number of quotes saved defaults to five. 
You can change this to any number you like using the `bound_2()` method. 
This method takes one argument, an integer that will serve as the new dictionary size. 
Below is an example of what it looks like to increase the dictionary size from five to ten. 


```
>>> example.bound_2(10)
'The dictionary can save 10 quotes.'
>>> 
```  

If you want to decrease the dictionary size, then the dictionary removes the last saved quotes that meet the bound. 
See below for an example.

```
>>> example.heard_em_say()
{1: "We all self-conscious. I'm just the first to admit it.", 
2: 'I want the world to be better! All I want is positive! All I want is dopeness!', 
3: "Today is the best day ever and tomorrow's going to be even better", 
4: 'Only free thinkers', 
5: "Truth is my goal. Controversy is my gym. I'll do a hundred reps of controversy for a 6 pack of truth"}
>>> example.bound_2(3)
'The dictionary can save 3 quotes.'
>>> example.heard_em_say()
{1: "We all self-conscious. I'm just the first to admit it.", 
2: 'I want the world to be better! All I want is positive! All I want is dopeness!', 
3: "Today is the best day ever and tomorrow's going to be even better"}
>>> 

```

## Current TODO: 

* Write unit tests.
