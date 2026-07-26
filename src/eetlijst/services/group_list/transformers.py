from typing import Optional

from eetlijst.exceptions import EetlijstException
from eetlijst.generated.create_list_item import CreateListItem
from eetlijst.generated.create_many_list_items import CreateManyListItems
from eetlijst.generated.fragments import ItemFields
from eetlijst.generated.update_list_item import UpdateListItem


def transform_list_item(item: Optional[ItemFields]) -> ItemFields:
    if not item:
        raise EetlijstException("List item not found")

    return item


def transform_create_many_list_items(result: CreateManyListItems):
    if not result.insert_eetschema_list:
        raise EetlijstException("Failed to create list items")

    return [
        transform_list_item(item) for item in result.insert_eetschema_list.returning
    ]


def transform_create_list_item(result: CreateListItem):
    if not result.insert_eetschema_list_one:
        raise EetlijstException("Failed to create list item")

    return transform_list_item(result.insert_eetschema_list_one)


def transform_update_list_item(result: UpdateListItem):
    if not result.update_eetschema_list_by_pk:
        raise EetlijstException("Failed to update list item")

    return transform_list_item(result.update_eetschema_list_by_pk)
