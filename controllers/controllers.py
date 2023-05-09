# -*- coding: utf-8 -*-
# from odoo import http


# class PlanesnetHelpdesk(http.Controller):
#     @http.route('/planesnet_helpdesk/planesnet_helpdesk/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/planesnet_helpdesk/planesnet_helpdesk/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('planesnet_helpdesk.listing', {
#             'root': '/planesnet_helpdesk/planesnet_helpdesk',
#             'objects': http.request.env['planesnet_helpdesk.planesnet_helpdesk'].search([]),
#         })

#     @http.route('/planesnet_helpdesk/planesnet_helpdesk/objects/<model("planesnet_helpdesk.planesnet_helpdesk"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('planesnet_helpdesk.object', {
#             'object': obj
#         })
