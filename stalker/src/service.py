import datetime
import uuid

class Generator:

    def getTimestamp():
        return datetime.datetime.now()

    def getUid():
        return uuid.uuid4()
