from django.core.exceptions import MultipleObjectsReturned
from django.db.models import QuerySet, Prefetch
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from main.models import LocomotivePart
from main.serializers import LocomotivePartSerializer
from main.utils.functions import xls_to_json


def prefetch_locomotive_parts(depth: int) -> QuerySet:
    if depth == 0:
        return LocomotivePart.objects.all()
    return LocomotivePart.objects.prefetch_related(
        Prefetch(lookup='children', queryset=prefetch_locomotive_parts(depth - 1)))


def start_import_data_from_file(request):
    parents = [
        ('PJ350200000', 'Схема тепловоза'),
        ('PJ350170000', 'Система воздухопровода'),
        ('PJ350150000', 'Схема тележки')
    ]

    for schema_id, russian_name in parents:
        LocomotivePart.objects.create(
            schema_id=schema_id,
            russian_name=russian_name
        )

    data = xls_to_json()
    for row in data:
        try:
            parent, _ = LocomotivePart.objects.get_or_create(
                schema_id=row['parent_id'].strip()
            )
        except MultipleObjectsReturned:
            print(row['parent_id'].strip())
            parent = LocomotivePart.objects.filter(
                schema_id=row['parent_id']
            ).first()

        LocomotivePart.objects.create(
            parent=parent,
            schema_id=row['schema_id'].strip(),
            russian_name=row['rus'].strip() if row['rus'] is not None else None,
            chinese_name=row['china'].strip() if row['china'] is not None else None,
            quantity=str(row['quantity']).strip(),
            description=row['description'].strip() if row['description'] is not None else None
        )

    return HttpResponse("import completed.")


def tree_view(request):
    def build(node):
        children = LocomotivePart.objects.filter(parent=node)
        tree = {'node': node, 'children': []}
        for child in children:
            tree['children'].append(build(child))
        return tree

    root_nodes = LocomotivePart.objects.filter(parent=None, schema_id__in=['PJ350200000', 'PJ350170000', 'PJ350150000'])

    tree_data = []

    for node in root_nodes:
        tree_data.append(build(node))

    return render(request, 'tree.html', {'tree_data': tree_data})


@api_view(('GET',))
@permission_classes((AllowAny,))
def json_tree(request):
    queryset = LocomotivePart.objects.filter(parent_id=None).prefetch_related(
        Prefetch(lookup='children', queryset=prefetch_locomotive_parts(5))
    )
    serializer_context = {'request': request}
    serializer = LocomotivePartSerializer(queryset, many=True, context=serializer_context)
    parents = ['PJ350200000', 'PJ350170000', 'PJ350150000']
    result = [dictionary for dictionary in serializer.data if dictionary.get('schema_id') in parents]
    return Response(result)
