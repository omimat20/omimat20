from odoo import models, fields

class CarStore(models.Model):

    _name = 'car.store'
    _description = 'car store'

    name = fields.Char(string='Name')
    year = fields.Date(string='Year')
    companies_id = fields.Many2one('companies',string='companies')
    count = fields.Integer(string='Count')