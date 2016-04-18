# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2010-today OpenERP SA (<http://www.openerp.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################


from openerp import api, tools
from openerp import models, fields, _



class mail_mail(models.Model):
    """ Model holding RFC2822 email messages to send. This model also provides
        facilities to queue and send new email messages.  """
    _inherit = 'mail.mail'

    attempt_send = fields.Integer(default=0,string='Sending Attempts', readonly=True)

    @api.constrains('state')
    def _onchange_state(self):
        default_attempt_send = self.env['ir.config_parameter'].get_param('mail_attempt_send', default=5)
        if self.state == 'exception':
            if self.attempt_send < int(default_attempt_send):
                self.attempt_send += 1
                self.state = 'outgoing'
