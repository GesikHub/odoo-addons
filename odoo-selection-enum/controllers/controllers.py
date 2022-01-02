# -*- coding: utf-8 -*-
from odoo import http

# class Odoo-selection-enum(http.Controller):
#     @http.route('/odoo-selection-enum/odoo-selection-enum/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo-selection-enum/odoo-selection-enum/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo-selection-enum.listing', {
#             'root': '/odoo-selection-enum/odoo-selection-enum',
#             'objects': http.request.env['odoo-selection-enum.odoo-selection-enum'].search([]),
#         })

#     @http.route('/odoo-selection-enum/odoo-selection-enum/objects/<model("odoo-selection-enum.odoo-selection-enum"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo-selection-enum.object', {
#             'object': obj
#         })