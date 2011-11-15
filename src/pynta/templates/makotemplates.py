from mako.lookup import TemplateLookup

from base import Renderer


class Mako(Renderer):

    settings_name = 'TEMPLATES_MAKO'

    class templates_settings:
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
            directories = self.templates_settings.directories,
            module_directory = self.templates_settings.module_directory,
            filesystem_checks = self.templates_settings.filesystem_checks,
            collection_size = self.templates_settings.collection_size,
            format_exceptions = self.templates_settings.format_exceptions,
            error_handler = self.templates_settings.error_handler,
            disable_unicode = self.templates_settings.disable_unicode,
            bytestring_passthrough = \
                self.templates_settings.bytestring_passthrough,
            output_encoding = self.templates_settings.output_encoding,
            encoding_errors = self.templates_settings.encoding_errors,
            cache_type = self.templates_settings.cache_type,
            cache_dir = self.templates_settings.cache_dir,
            cache_url = self.templates_settings.cache_url,
            cache_enabled = self.templates_settings.cache_url,
            modulename_callable = self.templates_settings.modulename_callable,
            default_filters = self.templates_settings.default_filters,
            buffer_filters = self.templates_settings.buffer_filters,
            strict_undefined = self.templates_settings.strict_undefined,
            imports = self.templates_settings.imports,
            input_encoding = self.templates_settings.input_encoding,
            preprocessor = self.templates_settings.preprocessor)


    def render(self, data):
        return self.template_lookup.get_template(self.template).render(**data)
