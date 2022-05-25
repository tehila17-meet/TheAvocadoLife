from typing import Union

from pyArango import connection

from arango_handler.arango_config import ArangoConfig
from arango_handler.errors.arango_connection_error import ArangoConnectionError


class ArangoConnector:
    @property
    def arango_connection(self) -> Union[connection.Connection, str]:
        try:
            return connection.Connection(arangoURL=ArangoConfig.ARANGO_HOST, username=ArangoConfig.USERNAME,
                                         password=ArangoConfig.PASSWORD)
        except Exception as e:
            raise ArangoConnectionError(e)
