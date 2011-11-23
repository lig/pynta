from pynta.apps import PyntaApp


class CRUDApp(PyntaApp):
    """
    Provide full CRUD (Create, Read, Update, Delete) interface for any data set
    via five actions: `_create`, `_list`, `_detail`, `_update`, `_delete`.
    """

    urls = (
        (r'^(?P<_action>(create|list))/$', 'self', {}),
        (r'^(?P<slug>\w+)/(?P<_action>(detail|update|delete))/$', 'self', {}),
    )
