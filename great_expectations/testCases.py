import unittest
import snowflakeConnection
import csvConnection


class TestCount(unittest.TestCase):
    def test_connection_Snowflake(self):
        print(snowflakeConnection.SnowflakeData.get_connection())
        self.assertIsNotNone(snowflakeConnection.SnowflakeData.get_connection())

    def test_connection_CSV(self):
        print(csvConnection.CsvData.get_connection())
        self.assertIsNotNone(csvConnection.CsvData.get_connection())


if __name__ == '__main__':
    unittest.main()
