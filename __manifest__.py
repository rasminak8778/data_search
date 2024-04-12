{
    'name': 'Data Search',
    'version': '17.0.1.0.0',
    'description': '',
    'category': 'Sales/Data_Search',
    'summary': 'Search content from any searchable fields of any model through this Search bar',
    'installable': True,
    'application': True,
    'depends': [
        'base',
        'sale_management',
        'purchase'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/search_data_views.xml',
        'views/search_data_menu.xml',

    ]
}