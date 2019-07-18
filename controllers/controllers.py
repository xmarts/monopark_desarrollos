# -*- coding: utf-8 -*-
from odoo import http

# class DesarrollosMonopark(http.Controller):
#     @http.route('/desarrollos_monopark/desarrollos_monopark/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/desarrollos_monopark/desarrollos_monopark/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('desarrollos_monopark.listing', {
#             'root': '/desarrollos_monopark/desarrollos_monopark',
#             'objects': http.request.env['desarrollos_monopark.desarrollos_monopark'].search([]),
#         })

#     @http.route('/desarrollos_monopark/desarrollos_monopark/objects/<model("desarrollos_monopark.desarrollos_monopark"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('desarrollos_monopark.object', {
#             'object': obj
#         })