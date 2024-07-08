from odoo import models, fields


class slide_slide(models.Model):
    _inherit = 'slide.slide'
    _description = 'Custom Slide'

    local_video_id = fields.Many2one('ir.attachment', string="Local Video", required=False)
