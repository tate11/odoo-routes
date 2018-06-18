# -*- coding: utf-8 -*-

from odoo import models, fields, api

class routes(models.Model):
    _name = 'routes.routes'

    date = fields.Date(string='Fecha de creación', required=True, default=fields.datetime.now())
    client_ids = fields.Many2many('res.partner', string='Clientes', required=True)
    distance = fields.Char(string='Distancia recorrida', required=True)
    duration = fields.Char(string='Duración total', required=True)
    url = fields.Char(string='Dirección de Google Maps',required=True)
