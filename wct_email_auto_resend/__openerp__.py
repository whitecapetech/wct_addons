# -*- encoding: utf-8 -*-
##############################################################################
#    
#    Odoo, Open Source Management Solution
#
#    Author: Andrius Laukavičius. Copyright: JSC Boolit
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
    'name': "Email Auto-Resend",
    'version': '1.0',
    'summary': 'Resend failed emails automatically',
    'category': 'Mail',
    'description': """This module give you the possibility to configure the number of attempts to resend a failed email automatically.""",
    'author': 'WHITECAPE TECHNOLOGIES',
    'license': 'AGPL-3',
    'website': "www.whitecapetech.com",
    "depends" : ['base','mail'],
    'data': [
        'mail_send_attempts.xml'
    ],
    "images": [
		"images/wct_mail_auto_resend.png",
	],
    "installable": True
}
