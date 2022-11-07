import logging

from odoo import fields, models, api


logger = logging.getLogger(__name__)


class Menu(models.Model):
    _inherit = 'ir.ui.menu'

    @api.model
    def _visible_menu_ids(self, debug=False):
        menus = super(Menu, self)._visible_menu_ids(debug)

        # get menu item id
        employee_item_id = self.env.ref('hr.menu_hr_root').id
        leave_item_id = self.env.ref('hr_holidays.menu_hr_holidays_root').id
        expense_item_id = self.env.ref('hr_expense.menu_hr_expense_root').id
        email_maketing_item_id = self.env.ref(
            'mass_mailing.mass_mailing_menu_root').id

        # Get the list of users groups
        user_groups = self.env.user.groups_id

        if self.env['res.groups'].with_context(lang='fr_FR').search_count([('name', 'like', 'Commercial Externe')]) >= 1:
            external_salesperson_group = self.env['res.groups'].with_context(lang='fr_FR').search(
                [('name', 'like', 'Commercial Externe')])

            if external_salesperson_group in user_groups:
                if employee_item_id:
                    menus.discard(employee_item_id)
                if leave_item_id:
                    menus.discard(leave_item_id)
                if expense_item_id:
                    menus.discard(expense_item_id)
                if email_maketing_item_id:
                    menus.discard(email_maketing_item_id)

        return menus
