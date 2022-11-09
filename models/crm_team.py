import logging

from odoo import fields, models, api


logger = logging.getLogger(__name__)


class CRMTeamExtend(models.Model):
    _inherit = "crm.team"

    products_category_ids = fields.Many2many(
        "product.category", string="Categories de produits vendus")

    @api.model
    def _name_search(self, name, args=None, operator="ilike", limit=100, name_get_uid=None):
        args = args or []

        domain = []

        # Get the connected user
        connected_user = self.env.user

        # Get all the sales teams
        sales_teams = self.env['crm.team'].search([("active", '=', True)])

        for team in sales_teams:
            if connected_user in team.member_ids:
                domain += [('id', '=', team.id)]

        return self._search(domain+args, limit=limit, access_rights_uid=name_get_uid)
