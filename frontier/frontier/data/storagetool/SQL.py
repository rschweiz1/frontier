# Header
# RunMe>>> C:\Python36\Lib\idlelib\idle.bat -r "$(FULL_CURRENT_PATH)"
# mydb = cDatabase(user='test',password='password',database='testdb')
# mydb.createtb('testtb',[('name','varchar(255)'),('value','int')])

import mysql.connector

class cDatabase(object):
    """Class to Interface with MariaDB Server
    """
    def __init__(self, **kwargs):
        """Constructor for cDatabase

        Note:
            Connects to MySQL Server and initializes Cursor object

        Args:
            user (string):      Username used to authenticate with MySQL server
            password (string):  Password to authenticate with MySQL server
            host (string):      Host name or IP address of MySQL server
            port (int):         TCP/IP port for the MySQL server
            database (string):  Database name to use when connecting to MySQL server

            autocommit (bool):  Whether to autocommit transactions
            time_zone (string): Set time zone session variable (e.g. '+10:00' or '-6:00' or 'Europe/Helsinki' or 'US/Eastern')
            get_warn (bool):    Whether to fetch warnings
            raise_warn (bool):  Whether to raise an exception on warnings
            use_pure (bool):    Use pure Pythonif True and try C extensions if False
        """

        self.user       = kwargs.get('user')
        self.password   = kwargs.get('password')
        self.host       = kwargs.get('host')
        self.port       = kwargs.get('port', 3306)
        self.database   = kwargs.get('database')

        self.time_zone  = kwargs.get('time_zone', '-5:00')
        self.autocommit = kwargs.get('autocommit', False)
        self.get_warn   = kwargs.get('get_warnings', False)
        self.raise_warn = kwargs.get('raise_on_warnings', False)
        self.use_pure   = kwargs.get('use_pure', True)

        # Connection to MySQL Server
        self._connect = mysql.connector.connect(
                            user        = self.user,
                            password    = self.password,
                            host        = self.host,
                            port        = self.port,
                            database    = self.database,
                            time_zone   = self.time_zone,
                            autocommit  = self.autocommit,
                            get_warnings = self.get_warn,
                            raise_on_warnings = self.raise_warn,
                            use_pure    = self.use_pure)

        # Cursor is the object that communicates with MySQL Server
        self._cursor = self._connect.cursor(buffered=True)

    ####################  Connection Commands ####################
    def __enter__(self):
        """Allows implementation of class using "with" statement
        """
        return self

    def __exit__(self):
        """Terminates MySQL database connection object
        """
        self.commit()
        self.connection.close()

    @property
    def connection(self):
        """Getter of MySQL connection object
        """
        return self._connect


    def connection_id(self):
        """Return Connection ID
        """
        return self.connection.connection_id

    @property
    def cursor(self):
        """Getter of MySQL cursor object
        """
        return self._cursor

    @cursor.setter
    def cursor(self, buffered=True):
        self._cursor = self._connect.cursor(buffered=buffered)

    @cursor.deleter
    def cursor(self, buffered=True):
        self.cursor.close()
        del self._cursor

    def clearcursor(self):
        """Empty Cursor results
        Note:
            Doesn't throw error like fetchall()
        Returns:
            List of rows in query result
        """
        rowList=[]
        for row in self.cursor:
            rowList.append(row)
        return rowList

    ####################  Basic SQL Commands ####################
    def commit(self):
        """Commit MySQL transactions
        """
        self.connection.commit()

    def rollback(self):
        """Undo all MySQL transactions from current transactions

        Note:
            Autocommit option makes this operation impossible
        """
        self.connection.rollback()

    def execute(self, sqlFormula, params=None):
        """Execute a prepared SQL statement

        Args:
            sqlFormula (string):    SQL formula sent using cursor object to open connection
            params (tuple):         Additional parameters

        Returns:
            Boolean True if statement succeeds in executing
        """
        try:
            self.cursor.execute(sqlFormula, params or ())
            return True
        except:
            return False

    def fetchall(self):
        """Fetch all rows of query result

        Note:
            Throws an exception if there are no query results

        Returns:
            List of tuples
        """
        return self.cursor.fetchall()

    def fetchone(self):
        """Fetch first query result

        Returns:
            Tuple with most recent query result
        """
        return self.cursor.fetchone()

    def rows(self):
        """Return rowcount of query result
        """
        return self.cursor.rowcount

    def query(self, sqlFormula, params=None):
        """Execute a prepared SQL statement

        Args:
            sqlFormula (string):    SQL formula sent using cursor object to open connection
            params (tuple):         Additional parameters

        Returns:
            List of tuples generated by executed query
        """

        self.execute(sqlFormula, params or ())
        return self.fetchall()

    ####################  Database Commands ####################
    def createdb(self, database_name):
        """Create Database

        Args:
            database_name (string): Name for new database
        """
        if not self.finddb(database_name):
            sqlFormula = 'CREATE DATABASE {db};'.format(db=database_name)
            self.execute(sqlFormula)
            print('Created Database "{db}"'.format(db=database_name))

    def dropdb(self, database_name):
        """Delete Database

        Args:
            database_name (string): Name of database to delete
        """
        if self.finddb(database_name):
            sqlFormula = 'DROP DATABASE {db};'.format(db=database_name)
            self.execute(sqlFormula)
            print('Dropped Database "{db}"'.format(db=database_name))

    @property
    def activedb(self):
        """Getter of active database of current connection
        """
        return self.database

    @activedb.setter
    def activedb(self, database_name):
        self.database = database_name

    def finddb(self, database_name):
        """Find Database

        Args:
            database_name (string): Name of database to find

        Returns:
            Boolean True if database found else False
        """
        self.showdb(verbose=False)
        for db in self.cursor:
            if database_name == db[0]:
                return True
        return False

    def showdb(self, verbose=True):
        """Show all Databases

        Note:
            Console print all databases on server
        """
        sqlFormula = 'SHOW DATABASES;'
        self.execute(sqlFormula)
        if verbose:
            for db in self.cursor:
                print(db[0])

    ####################  Table Commands ####################
    def createtb(self, table_name, columns, **kwargs):
        """Create Table in Database

        Args:
            table_name (string):        Name of new table
            columns (List of Tuples):   Column and column datatype specification
                Tuple Syntax:   ("Column_Name", "Datatype(size)")
                Example List:   [("col1","varchar(255)"), ("col2","int")]

            database (string):          Name of database to use (default active database)
            schema (string):            Name of MySQL schema to use
        """
        if not self.findtb(table_name):
            database_name = kwargs.get('database', self.activedb)
            schema_name   = kwargs.get('schema')

            # Unpack Columns Tuples ("Column_Name", "DataType(size)")
            # columnList = ''
            # for item in columns:
                # if type(item) == tuple:
                    # column_name = column[0]; datatype = column[1]
                    # columnList += '{name} {data}, '.format(name=column_name,data=datatype)
            # columnList=columnList.strip(' ').strip(',')
            columnString = ', '.join([' '.join(col) for col in columns])

            # Specify schema_name and Database for new table
            if schema_name:
                table_name='{schema}.{table}'.format(schema=schema_name,table=table_name)
            if database_name and self.finddb(database_name):
                table_name='{db}.{tb}'.format(db=database_name,tb=table_name)

            # Generate and execute SQL command
            sqlFormula = 'CREATE TABLE {name}({list});'.format(name=table_name, list=columnString)
            self.execute(sqlFormula)
            print('Created Table "{tb}" in Database "{db}"'.format(tb=table_name,db=database_name))
        else:
            print('Table "{tb}" already exists in Database "{db}"'.format(tb=table_name,db=database_name))

    def droptb(self, table_name):
        """Delete Table in Active Database

        Args:
            table_name (string):    Name of table to delete
        """
        if self.findtb(table_name):
            sqlFormula = 'DROP TABLE {name};'.format(name=table_name)
            self.execute(sqlFormula)
            print('Dropped Table "{tb}"'.format(tb=table_name))

    def truncatetb(self, table_name):
        pass

    def renametb(self, table_name, column_name, new_table_name):
        pass

    def findtb(self, table_name):
        """Find Table in Active Database

        Args:
            table_name (string):    Name of table to find
        """
        self.showtb(verbose=False)
        for tb in self.cursor:
            if table_name == tb[0]:
                return True
        return False

    def showtb(self, verbose=True):
        """Show all Tables in Active Database

        Note:
            Console Print all tables in active database
        """
        sqlFormula = 'SHOW TABLES;'
        self.execute(sqlFormula)
        if verbose:
            for tb in self.cursor:
                print(tb)

    #################### Table Index Commands ####################
    def createind(self, table_name, column_name, index_name):
        """Create new Table Index

        Args:
            table_name (string):    Name of table
            column_name (string):   Name of column in table
            index_name (string):    Name of index created for table-column
        """
        if self.findtb(table_name):
            sqlFormula = 'CREATE INDEX {ind} ON {tb}({col});'.format(ind=index_name,tb=table_name,col=column_name)
            self.execute(sqlFormula)
            print('Added Index "{ind}" for Column "{col}" in Table "{tb}"'.format(ind=index_name,tb=table_name,col=column_name))

    def showind(self, table_name):
        """Show all Indixes in Table

        Note:
            Console Print all indixes in specific table

        Args:
            table_name (string):    Name of table
        """
        if self.findtb(table_name):
            sqlFormula = 'SHOW INDEXES FROM {tb};'.format(tb=table_name)
            self.execute(sqlFormula)
            for ind in self.cursor:
                print(ind)

    def desctb(self, table_name):
        pass

    #################### Table Data Commands ####################
    def addcol(self, table_name, column_name, datatype):
        pass

    def dropcol(self, table_name, column_name, datatype):
        pass

    def modcol(self, table_name, column_name, datatype):
        pass


    def insertrecord(self, table_name, columns, values):
        pass

    def insertrecords(self, table_name, columns, values):
        pass

    #################### Query Commands ####################
    def querytb(self, table_name, columns, **kwargs):
        pass
