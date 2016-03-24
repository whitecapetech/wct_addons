# -*- encoding: utf-8 -*-

{
    "name" : "Tunisia - Accounting",
    "version" : "1.0",
    "author" : "WHITECAPETECH : Sami RJIBA",
    "website": "http://www.whitecapetech.com",
    "category" : "Localization/Account Charts",
    "description": """
This is the base module to manage Chart of Accounts and Taxes template for companies in Tunisia.
=================================================================================================
Ce Module charge le modèle du plan de comptes standard Tunisien et permet de générer les états
comptables aux normes tunisiennes.""",

    "depends" : ['base','account'],
    "init_xml" : [],
    "data" : [
        'plan_comptable_general.xml',
        'tn_pcg_taxes.xml',
        'tn_tax.xml',
		'l10n_tn_wizard.xml',
        'security/ir.model.access.csv',
		     ],
    "test": [],
    "demo_xml" : [],
    "active": True,
    "installable": True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
