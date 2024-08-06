from odoo import models, fields, Command


# from addons import account

class accounting_estate(models.Model):
    _description = "Module connects estate module with Accounting"

    _inherit = "estate.property"

    def sold_action(self):
        partner_id = self.buyer_id
        self.env['account.move'].create({
            'move_type': 'out_invoice',
            'partner_id': partner_id.id,
            #'journal_id': self.journal_id.id,
            'invoice_line_ids': [
                Command.create(
                    {'name': 'Property Price', 'price_unit': self.selling_price, 'quantity': 1}
                ),
                Command.create(
                    {'name': 'Comission', 'price_unit': (self.selling_price * 6) / 100.0, 'quantity': 1}
                ),
                Command.create(
                    {'name': 'Administrative Fees', 'price_unit': 100.0, 'quantity': 1}
                )
            ]
        })

        print("7a7a")
        return super().sold_action()
