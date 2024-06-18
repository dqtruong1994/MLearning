from odoo import models, fields

class res_users(models.Model):
    _inherit = 'res.users'
    _description = 'Custom Users'

    know_as = fields.Char()
