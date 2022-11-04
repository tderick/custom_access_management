# -*- coding: utf-8 -*-
# from odoo import http


# class CustomAccessManagement(http.Controller):
#     @http.route('/custom_access_management/custom_access_management/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_access_management/custom_access_management/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_access_management.listing', {
#             'root': '/custom_access_management/custom_access_management',
#             'objects': http.request.env['custom_access_management.custom_access_management'].search([]),
#         })

#     @http.route('/custom_access_management/custom_access_management/objects/<model("custom_access_management.custom_access_management"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_access_management.object', {
#             'object': obj
#         })
