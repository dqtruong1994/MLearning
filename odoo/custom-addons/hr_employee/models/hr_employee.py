from odoo import models, fields


class hr_employee(models.Model):
    _inherit = 'hr.employee'
    _description = 'Custom hr employee'

    know_as = fields.Char()
