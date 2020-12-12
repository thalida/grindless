Docs Styleguide
================================

inline markup
-------------------------
one asterisk: *text* for emphasis (italics),

two asterisks: **text** for strong emphasis (boldface), and

backquotes: ``text`` for code samples.

----

lists
-----------------------------
* This is a bulleted list.
* It has two items, the second
  item uses two lines.

1. This is a numbered list.
2. It has two items too.

#. This is a numbered list.
#. It has two items too.

* this is
* a list

  * with a nested list
  * and some subitems

* and here the parent list continues

----


defintions
------------------------------
term (up to a line of text)
   Definition of the term, which must be indented

   and can even consist of multiple paragraphs

next term
   Description.

----

line blocks
-----------------------------
| These lines are
| broken exactly like in
| the source file.

----

literal blocks
-------------------------------
This is a normal text paragraph. The next paragraph is a code sample::

   It is not processed in any way, except
   that the indentation is removed.

   It can span multiple lines.

This is a normal text paragraph again.

----

sidebar
---------------------------
.. sidebar:: Optional Sidebar Title
   :subtitle: Optional Sidebar Subtitle

   Subsequent indented lines comprise
   the body of the sidebar, and are
   interpreted as body elements.

----

pull-quote
-----------------------------------
.. pull-quote::

   No matter where you go, there you are.

   -- Buckaroo Banzai

----

tables
--------------------------------

basic
^^^^^^^^^^^^^^^^^^^^
.. table:: Truth table for "not"
   :widths: auto

   =====  =====
     A    not A
   =====  =====
   False  True
   True   False
   =====  =====

list-table
^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table:: Frozen Delights!
   :widths: 15 10 30
   :header-rows: 1

   * - Treat
     - Quantity
     - Description
   * - Albatross
     - 2.99
     - On a stick!
   * - Crunchy Frog
     - 1.49
     - If we took the bones out, it wouldn't be
       crunchy, now would it?
   * - Gannet Ripple
     - 1.99
     - On a stick!

----

centered
------------------------------------
.. centered:: LICENSE AGREEMENT

----

hlist
----------------------------------------
.. hlist::
   :columns: 3

   * A list of
   * short items
   * that should be
   * displayed
   * horizontally

----

doctest
---------------------------
This is an ordinary paragraph.

>>> print 'this is a Doctest block'
this is a Doctest block

The following is a literal block::

    >>> This is not recognized as a doctest block by
    reStructuredText.  It *will* be recognized by the doctest
    module, though!

----

codeblock
--------------------------------------------
.. code-block:: python
   :emphasize-lines: 3,5

   def some_function():
       interesting = False
       print 'This line is highlighted.'
       print 'This one is not...'
       print '...but this one is.'

.. code-block:: python
   :caption: this.py
   :name: this-py

   print 'Explicit is better than implicit.'

----

gloassary
------------------------------------------------
.. glossary::

   environment
      A structure where information about all documents under the root is
      saved, and used for cross-referencing.  The environment is pickled
      after the parsing stage, so that successive runs only need to read
      and parse new and changed documents.

   source directory
      The directory which, including its subdirectories, contains all
      source files for one Sphinx project.

.. glossary::

   term 1
   term 2
      Definition of both terms.


.. glossary::

   term 3 : A
   term 4 : B
      Definition of both terms.

----

admonitions
-------------------
.. ATTENTION::
    ATTENTION: Beware killer rabbits!

.. CAUTION::
    CAUTION: Beware killer rabbits!

.. WARNING::
    WARNING: Beware killer rabbits!

.. DANGER::
    DANGER: Beware killer rabbits!

.. ERROR::
    ERROR: Beware killer rabbits!

.. HINT::
    HINT: Beware killer rabbits!

.. IMPORTANT::
    IMPORTANT: Beware killer rabbits!

.. TIP::
    TIP: Beware killer rabbits!

.. NOTE::
    NOTE: Beware killer rabbits!

.. note::
   This function is not suitable for sending spam e-mails.
   
.. seealso::

   Module :py:mod:`zipfile`
      Documentation of the :py:mod:`zipfile` standard module.

   `GNU tar manual, Basic Tar Format <http://link>`_
      Documentation for tar archive files, including GNU tar extensions.

.. ADMONITION::
    ADMONITION: Beware killer rabbits!
    STUFF EHRE?

    AND MORE?

    
