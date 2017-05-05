Hemp
=====

Environment aware configuration and tools for `Fabric <http://www.fabfile.org>`_.

.. image:: https://img.shields.io/pypi/v/Hemp.svg?style=flat-square   :target: https://pypi.python.org/pypi/Hemp
.. image:: https://img.shields.io/pypi/l/Hemp.svg?style=flat-square   :target: https://pypi.python.org/pypi/Hemp
.. image:: https://img.shields.io/pypi/pyversions/Hemp.svg?style=flat-square   :target: https://pypi.python.org/pypi/Hemp
.. image:: https://img.shields.io/github/issues/Addvilz/hemp.svg?style=flat-square   :target: https://github.com/Addvilz/hemp/issues

Installation
------------

``pip install hemp``

What is Hemp
-------------

| Hemp is wrapper around `Fabric <http://www.fabfile.org>`_
 that gives Fabric some environmental awareness and allows for use of configuration
| files to set common or per-environment variables to be used in Fabric scripts.
| Hemp is considered stable and production ready. 
| It is used internally by `MobileCashout <https://github.com/mobilecashout>`_ and has been
| used to perform thousands of production deployments and uncountable amount of automation
| tasks across multitude of platforms without any issues so far.

Usage
-----

| Hemp executable wraps Fabric and performs some subtle alterations to
  how Fabric is loaded and executed, namely,
| loading default tasks and configuration files before Fabric execution.
| The command line interface is not any different than Fabric itself,
  so, running your tasks
| as usual and replacing ``fab`` with ``hemp`` should work out of the
  box.

Differences from Fabric
-----------------------

Fabfile location
~~~~~~~~~~~~~~~~

| By default, Fabric will load ``fabfile.py`` from current working
  directory or any of the parent directories.
| Hemp extends this functionality to include ``fabfile.py`` located in
  ``$HOME`` of the current user.

| This allows you to define your custom, shared utilties and tasks in
  one file, and use them without specifying the file
| location explicitly when using Hemp.

Hemp files
~~~~~~~~~~

| Hemp loads configuration from Hemp configuration files called
  ``hemp.yml``. They are loaded, by default, from ``$HOME``
| of the current user and current working directory.

| If ``hemp.yml`` if found both at home directory of the user and
  current working directory, both files are loaded and
| their contents merged recursively with contents of the ``hemp.yml``
  located in current working directory taking precedence.

Default stages
~~~~~~~~~~~~~~

| By default, specifying a stage requires stage config to be loaded
  before any other tasks are executed. It can be done
| by invoking hemp with one of the predefined stage tasks or a custom
  one, passing the name as an argument to ``on`` task.

Consider these samples:

``hemp development [task]``

``hemp on:development [task]``

will ultimately result in ``development`` stage to be used.

Sample environment configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: yaml

    hemp:
      environments:
        staging:
          roles:
            web: ['web0.host.com']
            db: ['web0.host.com']
        production:
          roles:
            web: ['web1.host.com', 'web2.host.com', 'web3.host.com', 'web4.host.com']
            db: ['web1.host.com']
        development:
          roles:
            web: ['web5.host.lan']
            db: ['web5.host.lan']
    # [...]

Loading the hosts and roledefs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| When invoked with one of the stage tasks or ``on`` task, Hemp will
  load appropriate configs to Fabric’s ``env`` dictionary.
| For example, loading ``staging`` stage will populate ``env`` with
  fallowing values:

.. code:: python

    env.hosts = ['web0.host.com']
    env.roledefs['web'] = ['web0.host.com']
    env.roledefs['db'] = ['web0.host.com']

Host and role definition merging
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| Instead of overwriting, Hemp will merge whatever values there are
  already located in ``env`` dictionary, both for hosts
| and role definitions.

Additional ``env`` settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~

All root keys of the ``hemp.yml`` file will be loaded into Fabric’s
``env`` dictionary. For example, having configuration like

.. code:: yaml

    hosts: ['a.com', 'b.com']
    hemp: [
        # ...
    ]

will result in ``env.hosts`` to be populated with ``a.com`` and
``b.com``

License
-------

Licensed under terms and conditions of Apache 2.0 license.

