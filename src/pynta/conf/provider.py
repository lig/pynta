class SettingsProvider(type):

    def __new__(cls, name, bases, args):
        from pynta.conf import settings

        settings_name = args.get('settings_name')

        if settings_name:
            # Base I'm. Just this project settings I need.
            class_settings = getattr(settings, settings_name, {})
        else:
            # find settings for all bases
            class_bases = filter(lambda base: hasattr(base, 'settings_name'),
                bases)

            class_settings = {}
            for class_base in class_bases:
                settings_name = getattr(class_base, 'settings_name')
                section_settings = getattr(settings, settings_name, {})
                class_settings.update(section_settings)
            # update class_settings with my args
            class_settings.update(args)

        # update args with calculated settings
        args.update(class_settings)

        return type.__new__(cls, name, bases, args)
