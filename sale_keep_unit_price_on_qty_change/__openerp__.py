# -*- coding: utf-8 -*-
##############################################################################
#
#     Copyright (C) 2016 Opener B.V (<https://opener.am>)
#                        Openworx (<https://openworx.nl>)
#
#     License: AGPL V3
#
#     You should have received a copy of the
#     GNU Affero General Public License
#     along with inactive_session_timeout.
#     If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'On sale order lines, keep unit price when the quantity changes',
    'author': "Opener B.V.",
    'website': "https://opener.am",
    'category': 'Sale',
    'version': '8.0.1.0.0',
    'license': 'AGPL-3',
    'depends': [
        'sale',
        'web_context_tunnel',
    ],
    'data': [
        'views/sale_order.xml',
    ]
}
