from typing import List

from consts import EntryConsts, ArangoConsts


def check_arango_connectivity(arango_handler):
    connection_status = arango_handler.arango_connection
    return connection_status if ArangoConsts.ARANGO_CONNECTION_ERROR in str(connection_status) else 1


def remove_sent_entries(session, db_name) -> None:
    sent_entries = session.query(db_name).filter_by(sentToDestination=EntryConsts.SENT_TO_DESTINATION_STATUS).all()
    for sent_entry in sent_entries:
        session.delete(sent_entry)
        session.commit()


def listify_data(data: str) -> List:
    return str(data).split()
