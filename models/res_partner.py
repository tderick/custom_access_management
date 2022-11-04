import logging

from odoo import fields, models, api


logger = logging.getLogger(__name__)


class PartnerExtend(models.Model):
    _inherit = "res.partner"

    @api.model
    def search_read(self, domain=None, fields=None, offset=0, limit=None, order=None):

        # Get the list of users groups
        user_groups = self.env.user.groups_id
        salesperson_group = self.env['res.groups'].with_context(lang='en_US').search(
            [('name', 'like', 'Salesperson')])

        if salesperson_group in user_groups:
            domain += [("create_uid", '=', self.env.user.id)]

        res = super(PartnerExtend, self).search_read(
            domain, fields, offset, limit, order)

        return res
