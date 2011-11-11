from mako.lookup import TemplateLookup

from base import RendererMixin


class Mako(RendererMixin):
    renderer_settings_name = 'TEMPLATES_MAKO'

    directories = None
    module_directory = None
    filesystem_checks = True
    collection_size = -1
    format_exceptions = False
    error_handler = None
    disable_unicode = False
    bytestring_passthrough = False
    output_encoding = None
    encoding_errors = 'strict'
    cache_type = None
    cache_dir = None
    cache_url = None
    cache_enabled = True
    modulename_callable = None
    default_filters = None
    buffer_filters = ()
    strict_undefined = False
    imports = None
    input_encoding = None
    preprocessor = None

    template = None


    def __init__(self, *args, **kwargs):
        super(Mako, self).__init__(*args, **kwargs)
        self.template_lookup = TemplateLookup(
            directories=self.directories,
            module_directory=self.module_directory,
            filesystem_checks=self.filesystem_checks,
            collection_size=self.collection_size,
            format_exceptions=self.format_exceptions,
            error_handler=self.error_handler,
            disable_unicode=self.disable_unicode,
            bytestring_passthrough=self.bytestring_passthrough,
            output_encoding=self.output_encoding,
            encoding_errors=self.encoding_errors,
            cache_type=self.cache_type,
            cache_dir=self.cache_dir,
            cache_url=self.cache_url,
            cache_enabled=self.cache_url,
            modulename_callable=self.modulename_callable,
            default_filters=self.default_filters,
            buffer_filters=self.buffer_filters,
            strict_undefined=self.strict_undefined,
            imports=self.imports,
            input_encoding=self.input_encoding,
            preprocessor=self.preprocessor)


    def render(self, data):
        return self.template_lookup.get_template(self.template).render(**data)
