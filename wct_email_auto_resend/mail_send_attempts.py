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

import base64
import logging
from email.utils import formataddr
from urlparse import urljoin

import psycopg2

from openerp import api, tools
from openerp import SUPERUSER_ID
from openerp.addons.base.ir.ir_mail_server import MailDeliveryException
from openerp import models, fields, _
from openerp.tools.safe_eval import safe_eval as eval
from openerp.tools.translate import _

_logger = logging.getLogger(__name__)


class mail_mail(models.Model):
    """ Model holding RFC2822 email messages to send. This model also provides
        facilities to queue and send new email messages.  """
    _inherit = 'mail.mail'

    attempt_send = fields.Integer(default=0,string='Sending Attempts', readonly=True)


    def write(self, cr, uid, ids, vals, context=None):
        if 'state' in vals:
            if vals['state'] == 'exception':
                default_attempt_send = self.pool.get('ir.config_parameter').get_param(cr, uid, 'mail_attempt_send', default=5, context=context)
                for mail in self.browse(cr, uid, ids):
                    if mail.attempt_send < int(default_attempt_send):
                        attempt_send = mail.attempt_send +1
                        vals['state'] = 'outgoing'
                        vals['attempt_send'] = attempt_send
        super(mail_mail,self).write(cr, uid, ids, vals, context)
