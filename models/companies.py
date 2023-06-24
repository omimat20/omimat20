from odoo import models, fields

class Companies(models.Model):

    _name = 'companies'
    _description = 'Companies Management'

    name = fields.Char(string='Name')
    icon = fields.Binary(string='Icone')