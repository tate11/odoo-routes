# -*- coding: utf-8 -*-
from odoo import http

class Routes(http.Controller):
    @http.route('/routes/routes/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/routes/routes/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('routes.listing', {
            'root': '/routes/routes',
            'objects': http.request.env['routes.routes'].search([]),
        })

    @http.route('/routes/routes/objects/<model("routes.routes"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('routes.object', {
            'object': obj
        })

    @http.route('/routes/all/', auth='public', website=True)
    def all_routes(self):
        all = http.request.env['routes.routes'].search([])

        return http.request.render('routes.all_routes', {'routes': all})

    # @http.route('/routes/create/', auth='public', website=True)
    # def create_route(self):
    #     '''Test.'''

    #     # Create tuples for Many2many relationship.
    #     # Each client is a tuple of (4, client_id),
    #     # `4` means `add existing record to the relationship`
    #     # www.odoo.com/documentation/11.0/reference/orm.html#model-reference
    #     contacts = [(4, c.id) for c in http.request.env['res.partner'].search([])]

    #     new_route = {
    #         'distance': '10 km',
    #         'duration': '2 min',
    #         'url': 'maps.google.com',
    #         'client_ids': contacts,
    #     }

    #     http.request.env['routes.routes'].create(new_route)

    #     return http.request.render('routes.all_routes', {'routes': all})    