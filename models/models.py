# -*- coding: utf-8 -*-

from odoo import models, fields, api

class route(models.Model):
    _name = 'routes.route'

    date = fields.Datetime(string='Fecha de creación', required=True, default=fields.datetime.now())
    client_ids = fields.Many2many('res.partner', string='Clientes', required=True)
    distance = fields.Char(string='Distancia recorrida')
    duration = fields.Char(string='Duración total')
    route_url = fields.Char(string='Dirección de Google Maps')
