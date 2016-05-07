# -*- encoding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution
#    This module copyright (C) 2016 jeo Software#    (www.jeo-soft.com.ar).#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'jaja_default',
    'version': '8.0.1.0.0',
    'author': 'jeo Software',
    'maintainer': 'jorge.obiols@gmail.com',
    'website': 'www.jeo-soft.com.ar',
    'license': 'AGPL-3',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml # noqa
    # for the full list
    'category': 'Extra Tools',    'summary': 'Customización Cotillon JAJA',
    'description': """
.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

===========================
Customización Cotillon JAJA
===========================

Este módulo fue escrito para desarrollar la customización básica de Cotillon JAJA
""",

    # any module necessary for this one to work correctly
    'depends': [
    ],
    'external_dependencies': {
        'python': [],
    },

    # always loaded
    'data': [
    ],
    # only loaded in demonstration mode
    'demo': [
    ],

    'installable': True,
    # Install this module automatically if all dependency have been previously
    # and independently installed.  Used for synergetic or glue modules.
    'auto_install': False,
    'application': True,
}
