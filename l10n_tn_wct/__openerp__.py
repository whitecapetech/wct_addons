# -*- encoding: utf-8 -*-

{
    'name' : 'Tunisia - Accounting 9.0',
    'version' : '1.0',
    'author' : 'WHITECAPE TECHNOLOGIES',
    'website': 'http://www.whitecapetech.com',
    'summary': 'Manage Chart of Accounts and Taxes template for companies in Tunisia with odoo 9',
    'category' : 'Localization/Account Charts',
    'description': """
This is the base module to manage Chart of Accounts and Taxes template for companies in Tunisia.
=================================================================================================
Ce Module charge le modèle du plan de comptes standard Tunisien et permet de générer les états
comptables aux normes tunisiennes.""",

    'depends': ['base_iban', 'account', 'base_vat'],
    'init_xml' : [],
    'data': [
        'tn_pcg_taxes.xml',
        'plan_comptable_general.xml',
        'tn_tax.xml',
        'tn_fiscal_templates.xml',
        'account_chart_template.yml',
    ],
    'images': [
		'images/wct_tn.png',
        ],
    'test': [],
    'demo_xml' : [],
    'active': True,
    'installable': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
