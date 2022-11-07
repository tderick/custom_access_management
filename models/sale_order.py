import logging

from odoo import fields, models, api


logger = logging.getLogger(__name__)


class SaleOrderExtend(models.Model):
    _inherit = "sale.order"

    @api.model
    def search_read(self, domain=None, fields=None, offset=0, limit=None, order=None):

        # Get the connected user
        connected_user = self.env.user

        # Get all the sales teams
        sales_teams = self.env['crm.team'].search([("active", '=', True)])

        for team in sales_teams:

            # Test if the connected user is a Team Lead
            if connected_user in team.member_ids and connected_user == team.user_id:
                domain += [("create_uid", 'in',
                            [user.id for user in team.member_ids])]
            elif connected_user in team.member_ids:
                domain += [("create_uid", '=', connected_user.id)]

        res = super(SaleOrderExtend, self).search_read(
            domain, fields, offset, limit, order)

        return res

    @api.model
    def _name_search(self, name, args=None, operator="ilike", limit=100, name_get_uid=None):
        args = args or []

        domain = []

        # Get the connected user
        connected_user = self.env.user

        # Get all the sales teams
        sales_teams = self.env['crm.team'].search([("active", '=', True)])

        for team in sales_teams:

            # Test if the connected user is a Team Lead
            if connected_user in team.member_ids and connected_user == team.user_id:
                domain += [("create_uid", 'in',
                            [user.id for user in team.member_ids])]
            elif connected_user in team.member_ids:
                domain += [("create_uid", '=', connected_user.id)]

        return self._search(domain+args, limit=limit, access_rights_uid=name_get_uid)
