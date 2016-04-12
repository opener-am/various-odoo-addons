# coding: utf-8
from openerp import api, models


class SaleOrderLine(models.Model):

    @api.multi
    def product_id_change(
            self, pricelist, product, qty=0,
            uom=False, qty_uos=0, uos=False, name='', partner_id=False,
            lang=False, update_tax=True, date_order=False, packaging=False,
            fiscal_position=False, flag=False):
        """ Keep price unit depending on the context """
        res = super(self, SaleOrderLine).product_id_change(
            pricelist, product, qty=qty, uom=uom, qty_uos=qty_uos, uos=uos,
            name=name, partner_id=partner_id, lang=lang, update_tax=update_tax,
            date_order=date_order, packaging=packaging,
            fiscal_position=fiscal_position, flag=flag)
        if self.env.context.get('keep_price_unit'):
            if res.get('value') and 'price_unit' in res['value']:
                del res['value']['price_unit']
        return res
