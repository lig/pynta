from bson import ObjectId
from mongoengine import Document, StringField, DynamicField
from mongoengine.base import get_document, NotRegistered
from mongoengine.connection import (connect, get_db, disconnect,
    DEFAULT_CONNECTION_NAME)

from pynta.storage.base import Storage


class PyntaStorage(Document):

    meta = {
        'indexes': [{
            'fields': ('tag', 'key'),
            'unique': True,
        }],
    }

    tag = StringField(required=True)
    key = StringField(required=True)
    value = DynamicField(default=None)


class Mongoengine(Storage):

    settings_name = 'STORAGE_MONGOENGINE'

    class settings:
        alias = DEFAULT_CONNECTION_NAME
        host = 'localhost'
        port = 27017
        max_pool_size = 10
        tz_aware = False
        database = 'test'

    def __init__(self, *args, **kwargs):
        super(Mongoengine, self).__init__(*args, **kwargs)
        self.connection = connect(
            db=self.settings.database,
            alias=self.settings.alias,
            host=self.settings.host,
            port=self.settings.port,
            max_pool_size=self.settings.max_pool_size,
            tz_aware=self.settings.tz_aware)
        self.db = get_db(alias=self.settings.alias)

    def __del__(self):
        disconnect(alias=self.settings.alias)
        super(Mongoengine, self).__del__()

    def get(self, tag, key):
        doc = self._get_document(tag)

        if doc:
            obj = doc.objects.with_id(key)
        else:
            stored_obj = PyntaStorage.objects(tag=tag, key=str(key)).get()
            obj = stored_obj.value

        return obj

    def put(self, tag, key, obj):
        doc = self._get_document(tag)

        if doc:

            if isinstance(obj, dict):
                doc(pk=key, **obj).save()
            elif isinstance(obj, doc):
                obj.pk = key
                obj.save()
            else:
                raise Exception(
                    'Cannot save "%s" object with tag "%s" and key "%s"' %
                    (obj, tag, key))

        else:
            PyntaStorage(tag=tag, key=str(key), value=obj).save()

    def delete(self, tag, key):
        doc = self._get_document(tag)

        if doc:
            doc.objects(pk=key).delete()
        else:
            PyntaStorage.objects(tag=tag, key=str(key)).delete()

    def get_free_key(self, tag):
        return str(ObjectId())

    def get_dataset(self, tag):
        doc = self._get_document(tag)

        if doc:
            qs = doc.objects
        else:
            qs = PyntaStorage.objects(tag=tag)

        return qs

    def _get_document(self, tag):
        try:
            doc = get_document(tag)
        except NotRegistered:
            pass
        else:
            return doc
