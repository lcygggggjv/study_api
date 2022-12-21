
import pathlib


class config:


    # login_file=r'D:\Python_EAM_API\EAM\test_case\tc_cases.xlsx'

    login_file=r'/Users/lcy/PycharmProjects/study_api/EAM/test_case/tc_cases.xlsx'

    log=r'D:\Python_EAM_API\EAM\logger_log\log.txt'

    config_file=pathlib.Path(__file__).absolute().parent   #当前文件目录的父级 就是config

    eam_dir=config_file.parent   #config的父级，就是EAM项目的目录

    root_dir=eam_dir.parent   #eam的父级，就是根目录，一般可直接再项目目录，拼接即可
    login_file=root_dir / eam_dir / 'test_case' / 'tc_cases.xlsx'

    #mac地址
    file_dir=r'/Users/lcy/PycharmProjects/study_api/EAM/test_case/tc_cases.xlsx'

    log = root_dir / eam_dir / 'logger_log' / 'log.txt'

    tc_host='https://test2.teletraan.io/graphql/?login'

    tc_sit_host='https://teamsit.teletraan.io/graphql/?login'

    sit_tentcode='cr7'
    sit_account='eam115'
    sit_password='teletraan'


