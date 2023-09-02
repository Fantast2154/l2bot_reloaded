from user_props.personal_settings import PersonalSettings
import warnings


class PersonalSettingsBlank:
    permission_to_host = False
    l2window_name_login = ''
    l2window_name_game = ''

    l2window_name = 'Asterios'

    logins = []
    passwords = []
    names = []
    rb_names = []

    default_logins_observer = []
    default_passwords_observer = []
    default_names_observer = []
    default_rb_names_observer = []

    # default_logins = ['nnFantast2154q']
    # default_passwords = ['Km0G46x18YL5']
    # default_names = ['ШавермаНаМорском']
    # default_rb_names = ['longhorn_golkonda']

    default_logins_farmer = []
    default_passwords_farmer = []
    default_names_farmer = []
    default_rb_names_farmer = []

    # default_logins = ['f43705329']
    # default_passwords = ['AA5931593aa']
    # default_names = ['Инженер']
    # default_rb_names = ['1']

    asterios_ip = ''
    pytesseract_path = ''
    launcher_path = ''

    moscow_server_restart_time = ''
    timezone = ''
    relaunch_windows_time = 0  # in minutes
    basic_number_of_windows = 0
    program_timer = 0  # the program will be erased after that time

    package_network_interface = ''
    package_asterios_ip_prefix = '51.'

    def __init__(self):
        self_attributes_list = list(PersonalSettingsBlank.__dict__.keys())
        personal_settings_attributes_list = list(PersonalSettings.__dict__.keys())

        difference = set(self_attributes_list).symmetric_difference(set(personal_settings_attributes_list))

        personal_settings_dict = PersonalSettings.__dict__

        for attribute in self_attributes_list:

            if attribute.startswith('__'):
                continue
            try:
                setattr(self, attribute, personal_settings_dict[attribute])
            except KeyError as ke:
                warnings.warn(f'Settings blank were changed! Difference: {ke}')

        if difference:
            warnings.warn(f'Personal settings are different! Check: {difference} attribute')


if __name__ == '__main__':
    p = PersonalSettingsBlank()
