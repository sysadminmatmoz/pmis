# -*- coding: utf-8 -*-
# © 2014-17 Eficent Business and IT Consulting Services S.L.
# © 2016 Matmoz d.o.o.
# Copyright 2017 Serpent Consulting Services Pvt. Ltd.
#   (<http://www.serpentcs.com>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'Analytic Account Cost Category',
    'version': '10.0.1.0.0',
    'summary': 'Adds the cost category to analytic accounts.',
    'author': 'Eficent, '
              'Project Expert Team',
    'website': 'http://project.expert',
    'category': 'Project Management',
    'license': 'AGPL-3',
    'depends': [
        'account',
        'analytic'
    ],
    'data': [
        'views/account_analytic_account_view.xml',
    ],
    'installable': True,
    'active': False,
}
