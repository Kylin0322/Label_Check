#!/usr/bin/python
# -*- coding: UTF-8 -*-
import configparser
import os

G_config_path = ""
G_config_file_name = "config.ini"


class config():

    def __init__(self) -> None:
        self.c1 = configparser.ConfigParser()

    def get_default_setting(self):
        '''设置 Default setting
            Input: None
            Output: configparser.ConfigParser()
        '''
        config = configparser.ConfigParser()
        config['Path'] = {}
        config['Path']['file_save_path'] = r"C:\Label_picture"
        config['Path']['file_backup_path'] = r"\\CNHUAM0HPFILE01\hpte\Label_Backup"

        config['Setting'] = {}
        config['Setting']['backup_picture'] = "1"
        config['Setting']['camera_index'] = "0"
        config['Setting']['Database_path'] = "C:\sqlite3"
        config['Setting']['Database_name'] = "FIN_Process_check"
        config['Setting']['Database_user'] = "user"
        config['Setting']['Database_password'] = "user"
        config['Setting']['port'] = "4"
        config['Setting']['bytesize'] = "8"
        config['Setting']['stopbits'] = "1"
        config['Setting']['baudrate'] = "9600"
        config['Setting']['timeout'] = "1"
        config['Setting']['timeout'] = "1"

        config['AutoUpgrade'] = {}
        config['AutoUpgrade']['g_upgrade_flag'] = "No"
        config['AutoUpgrade']['g_upgrade_method'] = "File_Server"
        config['AutoUpgrade']['g_upgrade_server'] = r"\\CNHUAM0HPFILE01\HP_Data\HP_TE\software\Label_Check"
        config['AutoUpgrade']['g_upgrade_ftp_address'] = ""
        config['AutoUpgrade']['g_upgrade_ftp_username'] = ""
        config['AutoUpgrade']['g_upgrade_ftp_password'] = ""

        return config

    def create_config_file(self, Config_File_Name):
        ''' create configuration file on root path
        '''
        # self.c1 = configparser.ConfigParser()
        self.c1 = self.get_default_setting()

        with open(Config_File_Name, 'w') as configfile:
            self.c1.write(configfile, False)

    def get_config_file(self):
        ''' read config data from G_config_file_name, it will create a default if file not exist

            input:G_config_file_name
            output:self.c1
        '''
        # check config file exist
        Config_File_Name = os.path.join(os.getcwd(), G_config_file_name)
        if not os.path.isfile(Config_File_Name):
            # make config file if not present
            self.create_config_file(Config_File_Name)

            # make file name and path
        self.c1.read(Config_File_Name)

        # compare programming default setting and ini file
        self.check_default_item()

    def save_config_file(self):
        '''save current configration to file.
        '''
        # check config file exist
        Config_File_Name = os.path.join(os.getcwd(), G_config_file_name)
        with open(Config_File_Name, 'w') as configfile:
            self.c1.write(configfile, False)

    def add_item_to_config_file(self, section, key, value):
        '''add on item to config file and save to configration to file.

            input:section, key, value,G_config_file_name
            output:file G_config_file_name
        '''
        # check config file exist
        Config_File_Name = os.path.join(os.getcwd(), G_config_file_name)
        # self.c1 = get_config_file()
        self.c1[section][key] = value
        with open(Config_File_Name, 'w') as configfile:
            self.c1.write(configfile, False)

    def list_out_all_in_config(self):
        ''' list out all in config a
            input: Config
            output
        '''
        for i in self.c1:
            print('[' + i + ']')
            for j in self.c1[i]:
                print(j + "=" + self.c1[i].get(j))

    def merge_config_file(config_1, config_2):
        ''' Merge config_1's item to config_2
            Input: config_1  （configparser.ConfigParser()
            Output: config_2
        '''
        config_1_sections = config_1.sections()
        config_2_sections = config_2.sections()

        for i in config_1:
            # print('[' + i + ']')
            if (not i in config_2_sections) and (i != "DEFAULT"):
                # add section to config_2
                config_2.add_section(i)
            keys = config_2[i].keys()

            for j in config_1[i]:
                if (not j in keys):
                    # add key to config_2
                    config_2[i][j] = config_1[i].get(j)
        return config_2

    def check_default_item(self):
        ''' 检测配置文件中默认设置是否相同，程序配置比Ini中新，则插入新的Section和Value对
            Input:
            Output:
        '''
        changed = False
        # print("c2:===============")
        c2 = self.get_default_setting()

        # 获取sections
        file_sections = self.c1.sections()
        default_sections = c2.sections()

        # 比较Default section 和 File的Section是否不同，如果不同则在 file 中插入
        for i in default_sections:
            if not i in file_sections:
                self.c1[i] = {}
                changed = True

        # 比较Default keys 和 File的keys是否不同，如果不同则在 file 中插入
        for i in default_sections:
            #获取keys in section
            key_value = self.c1.items(i)
            file_keys_value = []
            for ii in key_value:
                file_keys_value.append(ii[0])

            key_value = c2.items(i)
            default_keys_value = []
            for ii in key_value:
                default_keys_value.append(ii[0])

            # 比较 keys
            for ii in default_keys_value:
                if not ii in file_keys_value:
                    self.c1[i][ii] = c2[i].get(ii)
                    changed = True
                    pass

        if changed:
            # 保存文件
            self.save_config_file()
            pass


if __name__ == '__main__':
    print("---- standard test data -------------")
    # get config file
    config = config()
    config.get_config_file()

    # print config file
    # config.list_out_all_in_config()

    # print('---------------- read out key ----------')
    # T = int(config['Setting'].get('G_refresh_time').split(' ')[0])
    # print(T)
    # T = int(config['Setting'].get('G_fail_log_keep_time').split(' ')[0])
    # print(T)

    # # save config file
    # if config.c1['AutoUpgrade'].get('g_upgrade_flag') == "No":
    #     config.c1['AutoUpgrade']['g_upgrade_flag'] = "Yes"
    # else:
    #     config.c1['AutoUpgrade']['g_upgrade_flag'] = "No"

    # config.save_config_file()
