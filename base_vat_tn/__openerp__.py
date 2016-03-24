# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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
##############################################################################

{
    "name" : "Validateur de matricule fiscal - Tunisie",
    'version': '1.0',
    "author" : "WHITECAPE TECHNOLOGIES",
    "website": "http://www.whitecapetech.com",
    'category': 'Accounting & Finance',
    'description': """
Validateur de matricule fiscal - Tunisie.
============================================

Ce Module vous permettra de vérifier le numéro du matricule fiscal de vos clients et fournisseurs conformément à la loi tunisienne.
Ce module est validé par une cabinet d'expertise comptable.
    """,
    'depends': ['base_vat'],
    'data': ['base_vat_view.xml'],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
