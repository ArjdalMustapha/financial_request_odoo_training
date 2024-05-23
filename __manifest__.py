
{
    'name': 'Financial Request',
    'version': '1.0',
    'author': 'Arj Mu',
    'depends': ['base', 'project'],  
    'data': [
         'security/financial_request_security.xml',
        'security/ir.model.access.csv',
        'views/financial_request_views.xml',
        'views/financial_request_menus.xml',
    ],
    'installable': True,
    'application': True,
}