from pynta.apps import PyntaApp
from pynta.apps.decorators import require_method
from pynta.core.paginator import Paginator
from pynta.storage.base import Storage


class CRUDApp(PyntaApp):
    """
    Provide full CRUD (Create, Read, Update, Delete) interface for any data set
    via five actions: `_create`, `_list`, `_detail`, `_update`, `_delete`.
    """

    urls = (
        (r'^(?P<_action>(create|list))/$', 'self', {}),
        (r'^(?P<slug>\w+)/(?P<_action>(detail|update|delete))/$', 'self', {}),
    )

    object_name = 'object'
    storage = Storage
    list_page_size = 20


    def create_object(self, object_data):
        object_id = self.storage.get_free_key(self.object_name)
        self.storage.put(self.object_name, object_id, object_data)
        return self.storage.get(self.object_name, object_id)


    def get_dataset(self):
        return self.storage.get_dataset(self.object_name)


    def get_object(self, object_id):
        return self.storage.get(self.object_name, object_id)


    def update_object(self, object_id, object_data):
        self.storage.put(self.object_name, object_id, object_data)
        return self.storage.get(self.object_name, object_id)


    def delete_object(self, object_id):
        self.storage.delete(self.object_name, object_id)


    @require_method('POST')
    def do_create(self):
        obj = self.create_object(self.request.POST)
        return {self.object_name: obj}


    def do_list(self):
        dataset = self.get_dataset()
        paginator = Paginator(dataset, self.list_page_size)
        page = paginator.get_page(self.request.GET.get('page', 1))
        return {'%s_list' % self.object_name: page}


    def do_detail(self, slug):
        obj = self.get_object(slug)
        return {self.object_name: obj}


    @require_method('POST')
    def do_update(self, slug):
        obj = self.update_object(slug, self.request.POST)
        return {self.object_name: obj}


    @require_method('POST')
    def do_delete(self, slug):
        self.delete_object(slug)
        return {}
