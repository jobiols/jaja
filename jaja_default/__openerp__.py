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
    'version': '8.0.0.1.0',
    'author': 'jeo Software',
    'maintainer': 'jorge.obiols@gmail.com',
    'website': 'www.jeo-soft.com.ar',
    'license': 'AGPL-3',

    'category': 'Extra Tools',    'summary': 'Customización Cotillon JAJA',
    'description': """

.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

.. image:: https://codeclimate.com/github/jobiols/jaja/badges/gpa.svg
   :target: https://codeclimate.com/github/jobiols/jaja
   :alt: Code Climate

===========================
Customización Cotillon JAJA
===========================

Este módulo fue escrito para desarrollar la customización básica de Cotillon JAJA
""",
    'depends': [
        # base modules for standard instance
        # ----------------------------------
        'base',
        'l10n_ar_base',  # modulo base para localización argentina
        'base_vat_unique',  # evita que duplique cuit
        #        'base_vat_unique_parent',  # evita que duplique cuit en multicompañia
        'disable_openerp_online',  # elimina referencias a odoo online
        'account_cancel',  # Muestra el check en los diarios que permite cancelar asientos
        'hide_product_variants',  # oculta las variantes
        'invoice_order_by_id',  # ordena facturas ultima arriba
        #        'account_invoice_tax_wizard',  # agrega menu add_taxes para cargar percepciones
        #        'sale_order_recalculate_prices',  # agrega boton para recalcular precios
        #        'account_journal_sequence'         # agrega un campo de secuencia en el diario para elegirlos
        #        'account_statement_move_import'    # agrega boton de importar aputnes en extractos bancarios
        #        'l10n_ar_aeroo_sale',  # dependencia requerida
        #        'l10n_ar_aeroo_purchase',  # dependencia requerida
        #        'l10n_ar_aeroo_einvoice',  # dependencia requerida
        #        'l10n_ar_aeroo_stock',  # dependencia requerida
        #        'po_custom_reports',  # dependencia requerida
        'account_journal_sequence', #Adds sequence field on account journal and it is going to be considered when choosing journals in differents models.

        # customized modules for jaja instance
        # ------------------------------------

        'stock_available', # Stock available to promise

    ],
    'external_dependencies': {
        'python': [],
    },

    # always loaded
    'data': [
        'views/sale_view.xml',
        'views/sale_workflow.xml'
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
