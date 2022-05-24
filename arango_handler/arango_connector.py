from pyArango import connection
from arango_handler.arango_config import ArangoConfig
from arango_handler.consts import ArangoErrorMessages
from typing import Union


class ArangoConnector:

    @property
    def arango_connection(self) -> Union[connection.Connection, str]:
        try:
            return connection.Connection(arangoURL=ArangoConfig.ARANGO_HOST, username=ArangoConfig.USERNAME,
                                         password=ArangoConfig.PASSWORD)
        except Exception as e:
            return f"{e} - {ArangoErrorMessages.ARANGO_CONNECTION_ERROR}"
