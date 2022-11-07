import logging

from odoo import fields, models, api


logger = logging.getLogger(__name__)


class CRMLeadExtend(models.Model):
    _inherit = "crm.lead"

    @api.model
    def search_read(self, domain=None, fields=None, offset=0, limit=None, order=None):

        logger.critical(domain)

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

        res = super(CRMLeadExtend, self).search_read(
            domain, fields, offset, limit, order)

        return res
