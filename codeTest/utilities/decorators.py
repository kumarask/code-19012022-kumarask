"""The module containes decorators functions.

    .. current module::
        - codeTest.utilities.decorators
"""

import functools
import os
import sqlite3

from os import path


def createDatabaseConnection(database):
    """Connect to a sqlite DB. Create the database if there isn't one yet. Open
    a connection to a sqlite DB. When a database is accessed by multiple connections,
    and one of the processes modifies the database, the sqlite databse is located until
    that trasaction is committed.

    Args:
        database(str with db. extension): if None, create database.

    Returns:
        sqlite3.connectionn. returns a connection object.
    """
    if not path.exists(path.dirname(database)):
        os.makedirs(path.dirname(database))

    connection = sqlite3.connect(database)
    return connection


def databaseConnection(path=None):
    """A decorator with parameter of path to connect respective database.

    Args:
        path(str): A name or path of the database & ends with .db extensions.

    Returns:
        dbConnection, returns a result of dbConnection function.
    """

    def dbConnection(function):
        """Decorator to re(open) a sqlite database connection when needed. A database
        connection must be open when we want to perform a database query but we are in
        one of the following situations:
            1) There is no connetion
            2) The connection is closed.

        Args:
            function(function): function which performs the databse query.

        Returns:
            wrapper, returns a result of wrapper function.
        """

        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            """Function to run input.

            Args:
                args(tuple): A positional arguments for given function.
                kwargs(dict): A keyword arguments for given function.

            Decorators:
                functools.wraps

            Returns:
                function, returns a result of actual function.
            """
            connection = kwargs.get("connection")
            if not connection:
                connection = createDatabaseConnection(path)

            kwargs["connection"] = connection
            return function(*args, **kwargs)

        return wrapper

    return dbConnection
