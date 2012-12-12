Concepts
========

It is usually a kind of deal for framework developer between end application 
flexibility and interoperability when planning framework restrictions, project 
structure agreements, embedded features, etc.

Pynta is not trying to keep balancing frankly. it is flixible as much as it 
possible to be. You are able to plug anything on almost any level of 
abstraction or seamlessly connect to any other framework or use any desired 
storage or whatever technology you want.

But Pynta is not microframework. It has several abstractions that allow it to 
be flexible. There are interfaces that allow one to develop his own components 
to rapidly implement any imaginable feature.


Components
----------

Pynta consits of the following logical components:

* Configuration
* Application base
* Storage
* Templates
* URLs resolver

Each of the components (except for urls resolver for now) is built on an 
abstract class or like application base (`PyntaApp` class) is the basis for the 
developer to design his project. Abstract classes stand for interface that 
developer could implement to allow using of any storage, template engine, etc.


Configuration
`````````````

#TODO


Application base
````````````````

#TODO


Storage
```````

#TODO


Templates
`````````

#TODO


URLs resolver
`````````````

#TODO
