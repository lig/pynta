from string import Template

from mako.lookup import TemplateLookup

from .base import Renderer


class Mako(Renderer):

    settings_name = 'TEMPLATES_MAKO'

    class settings:
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
            directories=self.settings.directories,
            module_directory=self.settings.module_directory,
            filesystem_checks=self.settings.filesystem_checks,
            collection_size=self.settings.collection_size,
            format_exceptions=self.settings.format_exceptions,
            error_handler=self.settings.error_handler,
            disable_unicode=self.settings.disable_unicode,
            bytestring_passthrough=self.settings.bytestring_passthrough,
            output_encoding=self.settings.output_encoding,
            encoding_errors=self.settings.encoding_errors,
            cache_type=self.settings.cache_type,
            cache_dir=self.settings.cache_dir,
            cache_url=self.settings.cache_url,
            cache_enabled=self.settings.cache_url,
            modulename_callable=self.settings.modulename_callable,
            default_filters=self.settings.default_filters,
            buffer_filters=self.settings.buffer_filters,
            strict_undefined=self.settings.strict_undefined,
            imports=self.settings.imports,
            input_encoding=self.settings.input_encoding,
            preprocessor=self.settings.preprocessor)

    def render(self, data, action_name=None):

        if action_name and '$action' in self.settings.template:
            template = Template(self.settings.template).substitute(
                action=action_name)
        else:
            template = self.settings.template

        return self.template_lookup.get_template(template).render(**data)
