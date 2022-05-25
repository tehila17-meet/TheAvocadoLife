from typing import List

from consts import EntryConsts, ArangoConsts


def check_arango_connectivity(arango_handler):
    return False if arango_handler.arango_connection == ArangoConsts.ARANGO_CONNECTION_ERROR else True


def remove_added_entries(session, db_name: str) -> None:
    added_entries = session.query(db_name).filter_by(sentToDestination=EntryConsts.SENT_TO_DESTINATION_STATUS).all()
    for added_entry in added_entries:
        session.delete(added_entry)
        session.commit()


def listify_data(data: str) -> List:
    return str(data).split()
