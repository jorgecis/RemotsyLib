Remotsy python library |Build Status| |Codacy Badge|
====================================================

`Remotsy <https://www.remotsy.com>`_ is an infrared blaster device, is cloud controlled,
this a Python library to control the Remotsy device via Rest API.

Installation
============

  $ pip install remotsylib

Example
========

.. code-block:: python

    from remotsylib.api import API

    if __name__ == "__main__":

        client = API()

        #Do the login and get the token
        token = client.login(args.username, args.password)

        #Get the list of the controls
        lst_ctl = client.list_controls()
        for ctl in lst_ctl:
            print "id %s Name %s" % (ctl["_id"], ctl['name'])


Authentication
==============

You can use your remotsy username and password, but for security is recomended to generate
a application password, logon in https://home.remotsy.com and use the option App Passwords.


Documentation API
-----------------

The API documentation and links to additional resources are available at
https://www.remotsy.com/help


.. |Build Status| image:: https://travis-ci.org/jorgecis/RemotsyLib.svg?branch=master
   :target: https://travis-ci.org/jorgecis/RemotsyLib
.. |Codacy Badge| image:: https://api.codacy.com/project/badge/Grade/79fb3255b464442983bb5b6b6fdecd98
   :target: https://app.codacy.com/app/jorgecis/RemotsyLib?utm_source=github.com&utm_medium=referral&utm_content=jorgecis/RemotsyLib&utm_campaign=Badge_Grade_Settings


