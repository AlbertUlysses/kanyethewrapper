# Kanye the Python Wrapper
This is a wrapper for kanye.rest - a Free REST API for random Kanye West quotes by Andrew Jazbec.
Thank You [Andrew!](https://github.com/ajzbc)

* Wraps GET requests found here -> [https://kanye.rest/](https://kanye.rest/)

# Version
1.0 Initial release - Kanye as a service, continued

1.1 refactor code to remove dependencies outside of the Python standard library.

# Dependencies
None

# Usage

There is only one class you need to import and only one method you need to invoke, just like there is only one **Kanye West**.
The class is `Kanye` 
The method is `west()`
Below is an example of running the wrapper in the Python interpreter:

```
>>> from kanye_the_wrapper import Kanye
>>> random = Kanye()
>>> print(random.west())
I want the world to be better! All I want is positive! All I want is dopeness!
>>> 
```

The method returns type string.

## Current TODO: 

* add requirements.txt file

