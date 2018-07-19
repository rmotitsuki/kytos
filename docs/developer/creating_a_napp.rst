************************
How to develop your NApp
************************

To create your own NApp you will need to use the `kytos` command provider by
`kytos-utils` package. This package is already installed in your system if you
setup your develop environment.

To see the `kytos` helper you must run the following command to display the
helper in the command line.

.. code-block:: shell

  (kytos-environment)$ kytos -h
  kytos - The kytos command line.

  Usage: kytos [-c <file>|--config <file>] <command> [<args>...]
         kytos [-v|--version]
         kytos [-h|--help]

  Options:
    -c <file>, --config <file>    Load config file [default: ~/.kytosrc]
    -h, --help                    Show this screen.
    -v, --version                 Show version.

  The most commonly used kytos commands are:
     napps      Create, list, enable, install (and other actions) NApps.
     server     Start, Stop your Kytos Controller (Kytos)
     web        Manage the Web User Interface

  See 'kytos <command> -h|--help' for more information on a specific command.


In this section we will use the command `kytos napps` to handle your own NApp.

Create your NApp
================

To create your NApp you need to use your napp-server name and insert some NApp
information. Using the following command you will create a basic structure.


.. code-block:: shell

  (kytos-environment)$ kytos napps create
  --------------------------------------------------------------
  Welcome to the bootstrap process of your NApp.
  --------------------------------------------------------------
  In order to answer both the username and the napp name,
  You must follow this naming rules:
  - name starts with a letter
  - name contains only letters, numbers or underscores
  - at least three characters
  --------------------------------------------------------------

  Please, insert your NApps Server username: <username>
  Please, insert your NApp name: <napp name>
  Please, insert a brief description for your NApp [optional]: <brief description>

  Congratulations! Your NApp have been bootstrapped!
  Now you can go to the directory tutorial/helloworld and begin to code your NApp.
  Have fun!

After that a folder with `username` will be created and inside that we have
your NApp folder.

Understanding the NApp structure
--------------------------------

After created your NApp we have the basic NApp structure.

.. code-block:: shell

   <username>/
   ├── __init__.py
   └── <napp_name>/
       ├── __init__.py
       ├── kytos.json
       ├── main.py
       ├── README.rst
       ├── settings.py
       └── ui/
           ├── k-action-menu
           ├── k-info-panel
           ├── k-toolbar
           └── README.rst


- **kytos.json**: This file contains your NApp’s metadata.
- **settings.py**: Main settings parameters of your NApp.
- **main.py**: Main source code of your NApp.
- **README.rst**: Main description and information about your NApp.
- **ui**: Folder with components to be displayed in the Kytos UI
- **ui/README.rst**: A file with a brief description of your NApp components.

How to document your API Rest
=============================







How to register yourself in the NApps respository
=================================================

To publish your NApp in the `Napps server <https://napps.kytos.io/>`_ you need
to self register.Tto do that the tool `kytos` has a command
line to make the registration. Below we have the steps to make the
registration.

First of all use the command below and pass the your user information.

.. code-block:: shell

  (kytos-environment)$ kytos users register
  --------------------------------------------------------------
  Welcome to the user registration process.
  --------------------------------------------------------------
  To continue you must fill the following fields.
  Insert the field using the pattern below:
    - start with letter
    - insert only numbers and letters
  Username (Required): <username>
  Insert the field using the pattern below:
    - insert only letters
  First Name (Required): <first name>
  Insert the field using the pattern below:
    - insert only letters
  Last Name: <last name>
  Insert the field using the pattern below:
    - insert only the caracters: [letters, numbers, _, %, &, -, $]
    - must be at least 6 characters
  Password (Required): <password>
  Confirm your password: <password confirmation>
  Insert the field using the pattern below:
    - follow the format: <login>@<domain>
      e.g. john@test.com
  Email (Required): <email>
  Insert the field using the pattern below:
    - insert only numbers
  Phone: <phone>
  Insert the field using the pattern below:
    - insert only letters
  City: <city>
  Insert the field using the pattern below:
    - insert only letters
  State: <state>
  Insert the field using the pattern below:
    - insert only letters
  Country: <country>
  User successfully created.

- **username**: Username is the identifier in the server.
- **first name**: The first name information.
- **last name**: The last name information.
- **password**: The password used to make changes in the server
- **password confirmation**: The password confirmation.
- **email**: Email to confirm the registration in the server.
- **phone**: Phone number information.This field is optional.
- **city**: City name information.This field is optional.
- **state**: State information.This field is optional.
- **country**: Country information. This field is optional.

After created you can't use your user yet.You need to confirm your
registration process in the email box passed.
After that you can upload yours NApps.

How to upload your NApp in the NApps repository
===============================================


How the events works
====================


Events that are generated by Kytos
==================================

In the Kytos project we have a list of events generated by kytos. You can read
the section :doc:`./listened_events` to know more about events generated by
kytos.

The kytos events are divided in some categories, below a list of all
categories is displayed.

.. toctree::
   :maxdepth: 3

   listened_events