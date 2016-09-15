# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------------
#
#    Copyright (C) 2016  jeo Software  (http://www.jeo-soft.com.ar)
#    All Rights Reserved.
#
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
# -----------------------------------------------------------------------------------
from openerp import models, fields


class sale_order(models.Model):
    _inherit = 'sale.order'

    state = fields.Selection([
        ('draft', 'Draft Quotation'),

        ('to_pack', 'Para embalar'),
        ('packing', 'Armando paquete'),
        ('packed', 'Embalado'),
        ('modified', 'Modificado'),
        ('dispatched', 'Despachado'),
        ('delivered', 'Entregado'),
        ('in_transit', 'En transito'),
        ('on_arrival', 'En destino'),

        ('sent', 'Quotation Sent'),
        ('cancel', 'Cancelled'),
        ('waiting_date', 'Waiting Schedule'),
        ('progress', 'Sales Order'),
        ('manual', 'Sale to Invoice'),
        ('shipping_except', 'Shipping Exception'),
        ('invoice_except', 'Invoice Exception'),
        ('done', 'Done'),
    ], 'Status', readonly=True, copy=False, help="Gives the status of the quotation or sales order.\
              \nThe exception status is automatically set when a cancel operation occurs \
              in the invoice validation (Invoice Exception) or in the picking list process (Shipping Exception).\nThe 'Waiting Schedule' status is set when the invoice is confirmed\
               but waiting for the scheduler to run on the order date.", select=True)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
