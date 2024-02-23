from django.urls import path

from . import views

urlpatterns = [
    path('reports/new-register/<int:id>',
         views.new_register, name='new-register'),
    path('add-report/<int:id>', views.add_report, name='add-report'),
    path('add-project', views.add_project, name='add-project'),
    path('reports/details/<int:id>', views.details, name='details'),
    path('delete/<int:id>', views.delete),
    path('finish/<int:id>', views.finish),

    path('reports/details/analyzed/documentation/<int:id>',
         views.analyzed_documentation, name='analyzed_documentation'),

    path('reports/details/analyzed/material-list/<int:id>',
         views.analyzed_material_list, name='analyzed_materialList'),

    path('reports/details/analyzed/price/<int:id>',
         views.analyzed_price, name='analyzed_price'),

    path('reports/details/analyzed/layout/<int:id>',
         views.analyzed_layout, name='analyzed_layout'),

    path('reports/details/analyzed/network/<int:id>',
         views.analyzed_network, name='analyzed_network'),

    path('reports/details/analyzed/tecnical-offer/<int:id>',
         views.analyzed_tecnical_offer, name='analyzed_tecnical_offer'),

    path('reports/details/analyzed/commercial-offer/<int:id>',
         views.analyzed_commercial_offer, name='analyzed_commercial_offer'),

    path('reports/details/to-analyze/documentation/<int:id>',
         views.to_analyze_documentation),

    path('reports/details/to-analyze/material-list/<int:id>',
         views.to_analyze_material_list),

    path('reports/details/to-analyze/price/<int:id>',
         views.to_analyze_price),

    path('reports/details/to-analyze/layout/<int:id>',
         views.to_analyze_layout),

    path('reports/details/to-analyze/network/<int:id>',
         views.to_analyze_network),

    path('reports/details/to-analyze/tecnical-offer/<int:id>',
         views.to_analyze_tecnical_offer),

    path('reports/details/to-analyze/commercial-offer/<int:id>',
         views.to_analyze_commercial_offer),

]
