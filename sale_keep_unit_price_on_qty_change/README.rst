.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
    :alt: License: AGPL-3

In sale orders, keep unit price on quantity change
==================================================
As the Odoo price list mechanism supports varying prices for different
quantities, a change in quantity on a sale order line will normally overwrite
a manually adjusted unit price with the applicable price for the new quantity.

This module prevents that behaviour. That means that this module is not
compatible with a business process that relies on bulk discount or any other
price differentiation against different product quantities.

.. image:: /sale_keep_unit_price_on_qty_change/static/description/opener.png
    :width: 25 %
    :alt: Opener B.V.

`Opener B.V. <https://opener.am>`_
*Business solutions driven by open source collaboration*

