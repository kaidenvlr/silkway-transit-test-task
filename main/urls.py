from django.urls import path

from main.views import start_import_data_from_file, tree_view, json_tree

urlpatterns = [
    path('import/', start_import_data_from_file, name='import'),
    path('tree/', tree_view, name='tree-view'),
    path('json-tree/', json_tree, name='json-tree')
]
