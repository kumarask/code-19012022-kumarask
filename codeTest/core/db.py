"""The Module is creating database interface methods.

    ..current module::
        - codeTest.core.db
"""
from codeTest import settings
from codeTest.utilities import decorators


@decorators.databaseConnection(path=settings.DATABASE_PATH)
def insertConfig(configuration, connection=None):
    """Function to insert the new configuration to the database.

    Args:
        configuration(str): A string of config data.

    Kwargs:
        connection(object): a sqlite database connection object.

    Decorators:
        databaseConnection(path="/var/cache/database.db")
    """
    sql = "INSERT INTO `dataPipeline` (teamName, roleName) VALUES (?, ?)"
    cursor = connection.cursor()
    cursor.execute(sql, configuration)
    connection.commit()


@decorators.databaseConnection(path=settings.DATABASE_PATH)
def getConfig(teamName=None, roleName=None, connection=None):
    """A Method to query a sql select command and returns a result.

    Kwargs:
        connection(object): a sqlite database connection object.
        teamName(str): fetch values from a specific teamname
        roleName(str): fetch values from a specific rolename

    Decorators:
        databaseConnection(path="/var/cache/database.db")

    Returns:
        dict, returns a list of values.
    """
    sql = "SELECT * FROM `dataPipeline`"
    if teamName and roleName:
        sql = """
            SELECT * FROM `dataPipeline` 
            WHERE teamName='{teamName}' AND roleName='{roleName}'
        """.format(teamName=teamName, roleName=roleName)
    elif teamName:
        sql = """
            SELECT roleName FROM `dataPipeline` 
            WHERE teamName='{teamName}'
        """.format(teamName=teamName)

    cursor = connection.execute(sql)
    result = cursor.fetchall()

    if not result:
        return list()

    return result


@decorators.databaseConnection(path=settings.DATABASE_PATH)
def createDatabaseTable(connection=None):
    """A Method to create database tables from given sql query.

    Kwargs:
        connection(object): a sqlite3 database connection object.

    Decorators:
        databaseConnection(path="/var/cache/database.db")

    Returns:
        created table.
    """
    sql = """
        CREATE TABLE IF NOT EXISTS `dataPipeline`(
            teamID INTEGER PRIMARY KEY AUTOINCREMENT,
            teamName VARCHAR NOT NULL,
            roleName varchar NOT NULL
        )
    """

    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT count(name) FROM sqlite_master
        WHERE type="table" AND name="dataPipeline"
    """
    )

    if cursor.fetchone()[0] != 1:
        cursor.execute(sql)
    connection.commit()
