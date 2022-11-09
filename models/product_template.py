import logging

from odoo import fields, models, api


logger = logging.getLogger(__name__)


class ProductExtend(models.Model):
    _inherit = "product.template"

    @api.model
    def search_read(self, domain=None, fields=None, offset=0, limit=None, order=None):

        # Get the connected user
        connected_user = self.env.user

        # Get all the sales teams
        sales_teams = self.env['crm.team'].search([("active", '=', True)])

        for team in sales_teams:
            if connected_user in team.member_ids:
                domain += [("categ_id", 'in',
                            [cat.id for cat in team.products_category_ids])]

        res = super(ProductExtend, self).search_read(
            domain, fields, offset, limit, order)

        return res

    @api.model
    def read_group(self, domain, fields, groupby, offset=0, limit=None, orderby=False, lazy=True):
        # Get the connected user
        connected_user = self.env.user

        # Get all the sales teams
        sales_teams = self.env['crm.team'].search([("active", '=', True)])

        for team in sales_teams:

            for team in sales_teams:
                if connected_user in team.member_ids:
                    domain += [("categ_id", 'in',
                                [cat.id for cat in team.products_category_ids])]

        res = super(ProductExtend, self).read_group(
            domain, fields, groupby, offset=offset, limit=limit, orderby=orderby, lazy=lazy)
        return res
