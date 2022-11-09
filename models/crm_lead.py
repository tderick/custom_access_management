import logging

from odoo import fields, models, api


logger = logging.getLogger(__name__)


class CRMLeadExtend(models.Model):
    _inherit = "crm.lead"

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
                # if the connected user is not a team member and is the person who create the opportunity of is the saleperson of the opportunity
                domain += ['|', ("create_uid", '=', connected_user.id),
                           ("user_id", '=', connected_user.id)]

        res = super(CRMLeadExtend, self).search_read(
            domain, fields, offset, limit, order)

        return res

    @api.model
    def read_group(self, domain, fields, groupby, offset=0, limit=None, orderby=False, lazy=True):
        # Get the connected user
        connected_user = self.env.user

        # Get all the sales teams
        sales_teams = self.env['crm.team'].search([("active", '=', True)])

        for team in sales_teams:

            # Test if the connected user is a Team Lead
            if connected_user in team.member_ids and connected_user == team.user_id:
                domain += [("user_id", 'in',
                            [user.id for user in team.member_ids])]
            elif connected_user in team.member_ids:
                domain += [("user_id", '=', connected_user.id)]

        res = super(CRMLeadExtend, self).read_group(
            domain, fields, groupby, offset=offset, limit=limit, orderby=orderby, lazy=lazy)
        return res
