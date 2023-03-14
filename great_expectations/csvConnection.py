from DataConnection import DataConnection

"""
Details required for creating batch request : 
datasource_name - datasource name created using the config parameters for specific data
data_connector_name - connector name used to create the datasource
data_asset_name - table or path name of the data

"""


# batch request for csv data
class CsvData(DataConnection):
    # @csvData - creating batch request for csv data connection
    @staticmethod
    def get_connection():
        # Creating batch request for snowflake connection
        batch_request2 = {
            "datasource_name": "taxi_datasource",
            "data_connector_name": "default_runtime_data_connector_name",
            "data_asset_name": "/Users/saisupriya/Desktop/OBE/gx_tutorials/data/yellow_tripdata_sample_2019-01.csv",
        }
        return batch_request2
