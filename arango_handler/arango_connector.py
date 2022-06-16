from typing import Union

from pyArango import connection

from arango_handler.arango_config import ArangoConfig
from arango_handler.consts import ArangoErrorMessages

class ArangoConnector:

    @staticmethod
    def initiate_arango_connection() -> Union[connection.Connection, str]:
        try:
            return connection.Connection(arangoURL=ArangoConfig.ARANGO_HOST, username=ArangoConfig.USERNAME,
                                         password=ArangoConfig.PASSWORD)
        except Exception as e:
            return ArangoErrorMessages.ARANGO_CONNECTION_ERROR.format(error_reason=e)



