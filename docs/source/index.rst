.. mercadolibre.py documentation master file, created by
   sphinx-quickstart on Tue Mar 18 19:38:48 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to mercadolibre.py's documentation!
===========================================

Python awesome client for MercadoLibre REST API.


Installation and setup:
^^^^^^^^^^^^^^^^^^^^^^^


You can install mercadolibre.py using Pypi::

    $ pip install mercadolibre

Or just clone github repository and install it from source code, like this::

    $ git clone git@github.com:martinzugnoni/mercadolibre.py.git
    $ cd mercadolibre.py/
    $ easy_install .

Basic usage:
^^^^^^^^^^^^

Use it as simple as::

    ml = api.login(APP_ID, APP_SECRET)
    ml.authenticate(CODE, REDIRECT_URL)
    print ml.access_token
    >>> YOUR_ACCESS_TOKEN

    # post a new item
    item_data = {
        'title': 'This is a fake item',
        'price': 123.45,
        ...
    }
    ml.create_item(data=item_data)
    >>> ITEM_ID

.. toctree::
   :maxdepth: 2



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

