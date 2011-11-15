class SettingsProvider(type):
    """
    Provider for various settings sections. Allows embedding of section based
    settings slices depending on templates, storage or any other settings
    depended classes connected to app class.
    """
    handle_settings = ()

    def __new__(cls, name, bases, args):
        from pynta.conf import settings

        # for all handled settings we will take defaults from provided class,
        # apply project settings on it, apply resolved app settings and then
        # instantiate appropriated app settings properties

        new_class = type.__new__(cls, name, bases, args)

        for section_name in cls.handle_settings:

            if hasattr(new_class, section_name):
                # defaults
                section_class = getattr(new_class, section_name)
                section_class_name = '%s_settings' % section_name
                section_settings = getattr(section_class,
                    section_class_name).__dict__

                # project settings
                settings_name = section_class.settings_name
                project_settings = getattr(settings, settings_name, {})
                section_settings.update(project_settings)

                # app class settings
                class_settings = getattr(new_class, section_class_name, {})
                class_settings = class_settings and class_settings.__dict__
                section_settings.update(class_settings)

                # sanitize and store section settings
                app_settings = {}
                for key in section_settings:
                    if not key.startswith('_'):
                        app_settings[key] = section_settings[key]
                del section_settings

                # attach settings to app as property
                setattr(new_class, section_class_name,
                    type(section_class_name, (), app_settings)())

        return new_class
