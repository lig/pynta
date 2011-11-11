def settings_provider_factory(section_name):

    class SettingsProvider(type):

        def __new__(cls, name, bases, args):
            from pynta.conf import settings

            section_settings_name = args.get('%s_settings_name' % section_name)

            if section_settings_name:
                # Base I'm. Just project settings I need.
                section_settings = getattr(settings, section_settings_name, {})
            else:
                # find base settings name 
                section_bases = filter(
                    lambda base: hasattr(base,
                        '%s_settings_name' % section_name),
                    bases)

                if section_bases:
                    # we have settings
                    section_settings_name = getattr(section_bases[0],
                        '%s_settings_name' % section_name)
                    section_settings = getattr(settings, section_settings_name,
                        {})
                    # update section_settings with my args
                    section_settings.update(args)
                else:
                    section_settings = {}

            # update args with calculated settings
            args.update(section_settings)

            return type.__new__(cls, name, bases, args)

    return SettingsProvider
