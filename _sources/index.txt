Welcome to pynta's documentation!
=================================

Pynta is web framework written in Python.

Contents:

.. toctree::
    :maxdepth: 2
    
    concepts
    install
    tutorial/index
    reference/index

Basic Principals
----------------

Pynta will always be:

* flexible
* scalable
* complex
* PEP-oriented
* on the edge


Goals
-----

* Provide tools for building low volume products.
* Allow developer to choose any abstraction level to work on.
* Support most of the popular technologies out of the box.
* Allow developer to easy add support for any desired technology.
* Be compatible with any future technology.


Main Features
-------------

* WSGI compatible on most levels (almost everything is WSGI app).
* Simple and powerful url mapping mechanism (regexes with host and url
  matching).
* One app could handle a number of urls for different actions.
* CRUD support out of the box (using actions mechanism). 
* Different storages support (relational and non-relational):
 - Anydbm,
 - MongoDB via pymongo,
 - (planned) Relational via SQLAlchemy,
 - (deprecated) MongoDB via MongoKIT,
 - (planned) MongoDB via MongoEngine.
* (planned) Forms processing support (storage integrated).
* Sessions support.
* (planned) Authentication support.
* (planned) Flexible logging mechanism.
* (planned) Generic administration interface.
* (planned) Stateful apps support.
* (planned) Server side interface toolkit (twitter's Bootstrap and jQuery
  integration).


Possible Features
-----------------

*These features are still subject for discuss*

* Authorization support (separated from authentication).
* Django apps support.
* Visual editor (using interface toolkit).


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
