## @file

## @defgroup core language core

## **base class** for all nodes forms a *class graph*
## @ingroup core
class Object:

    ## @param[in] V initializer value
    def __init__(self,V):

        ## element **label or scalar value** (string, number,..)
        self.val = V

        ## every object can have arbitrary **attributes** = slots
        self.slot = {}

        ## every object can have **nested elements** stored *in order*
        self.nest = []


    ## @name object graph dump

    ## @defgroup dump object graph dump
    ## @ingroup core
    ## @{

    ## @brief `print` callback
    ## @ingroup dump
    def __repr__(self): return self.dump()

    ## @brief full tree dump
    ## @ingroup dump
    ## @param[in] depth current recursion depth
    ## @param[in] prefix optional header prefix
    def dump(self,depth=0,prefix=''):
        tree = self._pad(depth) + self.head(prefix)
        return tree

    ## @brief short <T:V> header only
    ## @ingroup dump
    def head(self,prefix=''):
        return '%s<%s:%s> @%x' % (prefix, self.__class__.__name__.lower(), self._val(), id(self))

    ## @brief tree padding
    ## @ingroup dump
    def _pad(self,depth): return '\n' + '\t' * depth

    ## @brief represent `val` for dumps
    ## @ingroup dump
    def _val(self): return self.val


    ## @name evaluation
    
    ## @defgroup eval evaluation
    ## @ingroup core

    ## @brief evaluate a generic object graph
    ## @ingroup eval
    def eval(self,env=None): raise Error('not implemented')



## @brief System error = exception
## @ingroup core
class Error(Object,BaseException): pass



## @brief Environment
## @ingroup core
class Env(Object): pass

## @brief global Environment
## @ingroup core
glob = Env('global')


## @defgroup test test

## @brief prints empty `<object:Hello>` and @ref Error `(not implemented)` trace
## @ingroup test
def test_hello():
    hello = Object('Hello')
    print(hello) ; print(hello.eval())
# test_hello()


## @defgroup prim primitives
## @ingroup core

## @ingroup prim
class Primitive(Object):
    ## @brief the key property: any primitive evaluates to itself
    def eval(self,env=None): return self

## @ingroup prim
## @brief floating point number
class Number(Primitive): pass

## @ingroup prim
## @brief integer number
class Integer(Number): pass

## @ingroup prim
## @brief string
class String(Primitive): pass

## @ingroup prim
## @brief symbol (name of variable, method,..)
class Symbol(Primitive): pass
