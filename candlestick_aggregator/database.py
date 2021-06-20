import mysql.connector
from retry import retry

config = {"user": "root", "password": "", "host": "mariadb_1", "database": "crypto_candles"}


class Database(object):
    @retry()
    def __init__(self):
        """
        Connects to the database and initialize it, creating a schema
        with an empty table. If the schema or table is already present,
        only the connection is established.
        """
        self.conn = mysql.connector.connect(
            user=config["user"], password=config["password"], host=config["host"]
        )
        self.cursor = self.conn.cursor()
        self.initialize_db()

    def __del__(self):
        """
        Closes the database connection once the object no longer exists
        """
        self.cursor.close()
        self.conn.close()

    def insert(self, candle: dict) -> None:
        """Method that inserts data into the 'candle_data' table.

        Args:
            candle (dict): Information about the candlestick. Created by the fetch_last_candle
            method of the CandlestickAPI class.
        """

        sql = (
            "INSERT INTO `crypto_candles`.`candle_data` "
            "(`coin_name`, `candle_period`, `datetime`, `open`, `high`, `low`, `close`) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s);"
        )

        values = (
            candle["currency_pair"],
            candle["period"],
            candle["date"],
            candle["open"],
            candle["high"],
            candle["low"],
            candle["close"],
        )

        try:
            self.cursor.execute(sql, values)
            self.conn.commit()
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)

    def initialize_db(self):
        """
        Creates the database schema and table if they don't exist
        """
        create_schema_query = "CREATE SCHEMA IF NOT EXISTS " + config["database"]
        create_table_query = (
            "CREATE TABLE IF NOT EXISTS " + config["database"] + ".`candle_data` ("
            "`id` INT NOT NULL AUTO_INCREMENT,"
            "`coin_name` VARCHAR(45) NULL,"
            "`candle_period` VARCHAR(45) NULL,"
            "`datetime` DATETIME NULL,"
            "`open` DOUBLE NULL,"
            "`high` DOUBLE NULL,"
            "`low` DOUBLE NULL,"
            "`close` DOUBLE NULL,"
            "PRIMARY KEY (`id`),"
            "UNIQUE INDEX `cripto_id_UNIQUE` (`id` ASC) VISIBLE)"
            "DEFAULT CHARACTER SET = utf8"
        )

        try:
            self.cursor.execute(create_schema_query)
            self.cursor.execute(create_table_query)
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)
