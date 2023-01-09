# -*- coding: utf-8 -*-
{
    'name': 'GIOT Config',
    'version': '16.0.1.0.0',
    'summary': 'Application for giot management',
    'description': """
        This module contain all application to connect to giot device.
        This module needs airflow application to work properly.
        In the future, stand alone will be supported.
    """,
    'author': 'Mcimam',
    'data': [
        'security/ir.model.access.csv',
        'views/device_view.xml',
        'views/log_view.xml',
        'views/cmd_view.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'AGPL-3',
}
