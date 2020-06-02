[![Build Status](https://travis-ci.com/AlbertUlysses/Kanye_the_Wrapper.svg?branch=master)](https://travis-ci.com/AlbertUlysses/Kanye_the_Wrapper)
# Kanye the Python Wrapper
This is a wrapper for kanye.rest - a Free REST API for random Kanye West quotes by Andrew Jazbec.
Thank You [Andrew!](https://github.com/ajzbc)

* Wraps GET requests found here -> [https://kanye.rest/](https://kanye.rest/)

# Version
# TODO: look into versioning for PIP

# Dependencies
None

# Usage
### The Wrapper

There is one class that you need to import, and one main method for the wrapper. The class is Kanye and the method is west(), below is an example of running the wrapper in the Python interpreter:
```
>>> from kanye_the_wrapper import Kanye
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
>>> from kanye_the_wrapper import Kanye
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
{1: 'My greatest pain in life is that I will never be able to see myself perform live.', 2: 'Style is genderless', 3: 'Only free thinkers', 4: "People always say that you can't please everybody. I think that's a cop-out. Why not attempt it? Cause think of all the people that you will please if you try.", 5: 'The world is our family', 6: "If I don't scream, if I don't say something then no one's going to say anything."}
>>> example.bound_2(3)
'The dictionary can save 3 quotes.'
>>> example.heard_em_say()
{1: "If I don't scream, if I don't say something then no one's going to say anything.", 2: "If I don't scream, if I don't say something then no one's going to say anything.", 3: "If I don't scream, if I don't say something then no one's going to say anything."}
>>> 
```

## Current TODO: 

* Look into changing how to save to dictionary, use heapq.
* Write unit tests.
