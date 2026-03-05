# 20260302_Synchrn_Python

## Prior Reading
* Compiled  vs Interpreted languages
* Base datatype (Noe, Bool, int, float, Decimal, Fraction)
* Mutability (Mutable vs Immutable; Adv.s of Immutability)
* Collection (Strings, Lists, Sets, Tuples, Dictionaries, FrozenSets, NamedTuples)
* Comprehensions

## Future Reading
* Function overloading using 'multipledispatch' module
* Generator & Iterator (iter(), next() methods)
* Lambdas (Annonymous function)
* Utilitiy functions (Map, Filter, Reduce)
* [Python Docs](https://docs.python.org/3.11/)
* ['open' method (builtins)](https://docs.python.org/3.11/library/functions.html#open)

## Notes
* Virtual Environment (venv module)
    * Create env - `py -m venv <env_folder_name>`
    * Activate the env
        * CommandPrompt - `<env_folder_name>\Scripts\activate.bat`
        * PowerShell - `<env_folder_name>\Scripts\activate.ps1`
        * Bash - `source <env_folder_name>\Scripts\activate`
    * Deactivate - `deactivate`
    * Package manager - `pip / pip3`
        * List all packages - `pip list` OR  `py -m pip list`
        * Upgrade pip - `py -m pip install pip --upgrade`
        * Install packages - `pip install numpy`
        * Remove package - `pip remove numpy`
        * Get modules and versions in req file format - `pip freeze`
            * `pip freeze > fix_req.txt`
    * [Exception Hierarchy](https://docs.python.org/3.11/library/exceptions.html#exception-hierarchy)
    * [HTTP Requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods)
    * [HTTP Responses](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status)
    