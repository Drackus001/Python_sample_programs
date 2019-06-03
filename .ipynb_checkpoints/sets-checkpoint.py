{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Help on set object:\n",
      "\n",
      "class set(object)\n",
      " |  set() -> new empty set object\n",
      " |  set(iterable) -> new set object\n",
      " |  \n",
      " |  Build an unordered collection of unique elements.\n",
      " |  \n",
      " |  Methods defined here:\n",
      " |  \n",
      " |  __and__(self, value, /)\n",
      " |      Return self&value.\n",
      " |  \n",
      " |  __contains__(...)\n",
      " |      x.__contains__(y) <==> y in x.\n",
      " |  \n",
      " |  __eq__(self, value, /)\n",
      " |      Return self==value.\n",
      " |  \n",
      " |  __ge__(self, value, /)\n",
      " |      Return self>=value.\n",
      " |  \n",
      " |  __getattribute__(self, name, /)\n",
      " |      Return getattr(self, name).\n",
      " |  \n",
      " |  __gt__(self, value, /)\n",
      " |      Return self>value.\n",
      " |  \n",
      " |  __iand__(self, value, /)\n",
      " |      Return self&=value.\n",
      " |  \n",
      " |  __init__(self, /, *args, **kwargs)\n",
      " |      Initialize self.  See help(type(self)) for accurate signature.\n",
      " |  \n",
      " |  __ior__(self, value, /)\n",
      " |      Return self|=value.\n",
      " |  \n",
      " |  __isub__(self, value, /)\n",
      " |      Return self-=value.\n",
      " |  \n",
      " |  __iter__(self, /)\n",
      " |      Implement iter(self).\n",
      " |  \n",
      " |  __ixor__(self, value, /)\n",
      " |      Return self^=value.\n",
      " |  \n",
      " |  __le__(self, value, /)\n",
      " |      Return self<=value.\n",
      " |  \n",
      " |  __len__(self, /)\n",
      " |      Return len(self).\n",
      " |  \n",
      " |  __lt__(self, value, /)\n",
      " |      Return self<value.\n",
      " |  \n",
      " |  __ne__(self, value, /)\n",
      " |      Return self!=value.\n",
      " |  \n",
      " |  __or__(self, value, /)\n",
      " |      Return self|value.\n",
      " |  \n",
      " |  __rand__(self, value, /)\n",
      " |      Return value&self.\n",
      " |  \n",
      " |  __reduce__(...)\n",
      " |      Return state information for pickling.\n",
      " |  \n",
      " |  __repr__(self, /)\n",
      " |      Return repr(self).\n",
      " |  \n",
      " |  __ror__(self, value, /)\n",
      " |      Return value|self.\n",
      " |  \n",
      " |  __rsub__(self, value, /)\n",
      " |      Return value-self.\n",
      " |  \n",
      " |  __rxor__(self, value, /)\n",
      " |      Return value^self.\n",
      " |  \n",
      " |  __sizeof__(...)\n",
      " |      S.__sizeof__() -> size of S in memory, in bytes\n",
      " |  \n",
      " |  __sub__(self, value, /)\n",
      " |      Return self-value.\n",
      " |  \n",
      " |  __xor__(self, value, /)\n",
      " |      Return self^value.\n",
      " |  \n",
      " |  add(...)\n",
      " |      Add an element to a set.\n",
      " |      \n",
      " |      This has no effect if the element is already present.\n",
      " |  \n",
      " |  clear(...)\n",
      " |      Remove all elements from this set.\n",
      " |  \n",
      " |  copy(...)\n",
      " |      Return a shallow copy of a set.\n",
      " |  \n",
      " |  difference(...)\n",
      " |      Return the difference of two or more sets as a new set.\n",
      " |      \n",
      " |      (i.e. all elements that are in this set but not the others.)\n",
      " |  \n",
      " |  difference_update(...)\n",
      " |      Remove all elements of another set from this set.\n",
      " |  \n",
      " |  discard(...)\n",
      " |      Remove an element from a set if it is a member.\n",
      " |      \n",
      " |      If the element is not a member, do nothing.\n",
      " |  \n",
      " |  intersection(...)\n",
      " |      Return the intersection of two sets as a new set.\n",
      " |      \n",
      " |      (i.e. all elements that are in both sets.)\n",
      " |  \n",
      " |  intersection_update(...)\n",
      " |      Update a set with the intersection of itself and another.\n",
      " |  \n",
      " |  isdisjoint(...)\n",
      " |      Return True if two sets have a null intersection.\n",
      " |  \n",
      " |  issubset(...)\n",
      " |      Report whether another set contains this set.\n",
      " |  \n",
      " |  issuperset(...)\n",
      " |      Report whether this set contains another set.\n",
      " |  \n",
      " |  pop(...)\n",
      " |      Remove and return an arbitrary set element.\n",
      " |      Raises KeyError if the set is empty.\n",
      " |  \n",
      " |  remove(...)\n",
      " |      Remove an element from a set; it must be a member.\n",
      " |      \n",
      " |      If the element is not a member, raise a KeyError.\n",
      " |  \n",
      " |  symmetric_difference(...)\n",
      " |      Return the symmetric difference of two sets as a new set.\n",
      " |      \n",
      " |      (i.e. all elements that are in exactly one of the sets.)\n",
      " |  \n",
      " |  symmetric_difference_update(...)\n",
      " |      Update a set with the symmetric difference of itself and another.\n",
      " |  \n",
      " |  union(...)\n",
      " |      Return the union of sets as a new set.\n",
      " |      \n",
      " |      (i.e. all elements that are in either set.)\n",
      " |  \n",
      " |  update(...)\n",
      " |      Update a set with the union of itself and others.\n",
      " |  \n",
      " |  ----------------------------------------------------------------------\n",
      " |  Static methods defined here:\n",
      " |  \n",
      " |  __new__(*args, **kwargs) from builtins.type\n",
      " |      Create and return a new object.  See help(type) for accurate signature.\n",
      " |  \n",
      " |  ----------------------------------------------------------------------\n",
      " |  Data and other attributes defined here:\n",
      " |  \n",
      " |  __hash__ = None\n",
      "\n"
     ]
    }
   ],
   "source": [
    "example = set()\n",
    "#set is a odered type list which can store multiple type elements into it.\n",
    "help(example)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "example.add(3) #int value added"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "example.add(True) #bool value added"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "example.add(\"My String\") #string value added"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "example.add(3.142015145) #float value added"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{3, 3.142015145, 'My String', True}"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "example #shows sets elements in sorted order"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "example.add(15)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{15, 3, 3.142015145, 'My String', True}"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "example #shows sets elements in order"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "example.add(3) #nothings happen (set don't have any duplicate value)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{15, 3, 3.142015145, 'My String', True}"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "example #shows sets elements in sorted order"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "#example2 = set(5,True,2.454) \n",
    "#TypeError: set expected at most 1 arguments, got 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "example2 = set([5,True,2.454]) #correct way of initialization of set"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{True, 2.454, 5}"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "example2 #shows sets elements in sorted order"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "#integers 1 - 10\n",
    "odds = set([1, 3, 5, 7, 9])\n",
    "evens = set([2, 4, 6, 8, 10])\n",
    "primes = set([2, 3, 5, 7])\n",
    "compisites = set([4, 6, 8, 9, 10])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "odds.union(evens)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "evens.union(odds)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1, 3, 5, 7, 9}"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "odds"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{2, 4, 6, 8, 10}"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "evens"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{3, 5, 7}"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "odds.intersection(primes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "set()"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "evens.intersection(odds)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "2 in primes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "3 not in evens"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['__and__',\n",
       " '__class__',\n",
       " '__contains__',\n",
       " '__delattr__',\n",
       " '__dir__',\n",
       " '__doc__',\n",
       " '__eq__',\n",
       " '__format__',\n",
       " '__ge__',\n",
       " '__getattribute__',\n",
       " '__gt__',\n",
       " '__hash__',\n",
       " '__iand__',\n",
       " '__init__',\n",
       " '__init_subclass__',\n",
       " '__ior__',\n",
       " '__isub__',\n",
       " '__iter__',\n",
       " '__ixor__',\n",
       " '__le__',\n",
       " '__len__',\n",
       " '__lt__',\n",
       " '__ne__',\n",
       " '__new__',\n",
       " '__or__',\n",
       " '__rand__',\n",
       " '__reduce__',\n",
       " '__reduce_ex__',\n",
       " '__repr__',\n",
       " '__ror__',\n",
       " '__rsub__',\n",
       " '__rxor__',\n",
       " '__setattr__',\n",
       " '__sizeof__',\n",
       " '__str__',\n",
       " '__sub__',\n",
       " '__subclasshook__',\n",
       " '__xor__',\n",
       " 'add',\n",
       " 'clear',\n",
       " 'copy',\n",
       " 'difference',\n",
       " 'difference_update',\n",
       " 'discard',\n",
       " 'intersection',\n",
       " 'intersection_update',\n",
       " 'isdisjoint',\n",
       " 'issubset',\n",
       " 'issuperset',\n",
       " 'pop',\n",
       " 'remove',\n",
       " 'symmetric_difference',\n",
       " 'symmetric_difference_update',\n",
       " 'union',\n",
       " 'update']"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dir(evens)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
