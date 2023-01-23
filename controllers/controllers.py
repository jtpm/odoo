# -*- coding: utf-8 -*-
# from odoo import http


# class Tes14(http.Controller):
#     @http.route('/tes14/tes14/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tes14/tes14/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tes14.listing', {
#             'root': '/tes14/tes14',
#             'objects': http.request.env['tes14.tes14'].search([]),
#         })

#     @http.route('/tes14/tes14/objects/<model("tes14.tes14"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tes14.object', {
#             'object': obj
#         })
