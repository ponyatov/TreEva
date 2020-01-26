# TreEva
## Eva port to object graph model / Python /

* following the interpreter design course:
    * **Essentials of Interpretation** (by) Dmitry Soshnikov
        * https://www.youtube.com/playlist?list=PLGNbPb3dQJ_4WT_m3aI3T2LRf2R_FKM2k
            * [Lecture 5](https://www.youtube.com/watch?v=MQYs7rFfQ-Q&list=PLGNbPb3dQJ_4WT_m3aI3T2LRf2R_FKM2k&index=5)

### goal: reimplement the Eva language in the **object graph** program representation

github: https://github.com/ponyatov/TreEva

Classical Lisp-like list evaluation language described in the "Essentials of
Interpretation" lecture course looks too weak for me. The list program
representation lacks the ability to store custom attributes for any code element
(see attribute grammar) in the form easy to read and use and limits the
execution to lambda evaluation only.  So I choose to use more OOP-friendly
directed **object graphs** as a program representation:
- every node is an @ref TreEva.Object "Object"
- objects refer to other objects by @ref TreEva.Object.slot "named" and @ref TreEva.Object.nest "ordered" references
- every object can be executed via
  - lambda-evaluation
    - every object is resposible for itself evaluation via `eval()` method call
      - @ref TreEva.Primitive type object evaluates to itself
      - object with nested elements applies evaluation recursively for all subgraph objects
      - the way the object evaluates its nested subgraphs is defined by its internal behavior
        which is the same for the class of these objects
  - *async message passing* and late dispatch (**actor model** = pure OOP)
