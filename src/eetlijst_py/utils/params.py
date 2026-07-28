from typing import Any

from eetlijst_py.generated.base_model import BaseModel


def build_where[T: BaseModel](
    model_cls: type[T], where: T | None, **defaults: Any
) -> T:
    """Merges filter constraints into an existing model or instantiates a new one."""
    if where is not None:
        return where.model_copy(update=defaults)

    return model_cls(**defaults)


def default_order[T: BaseModel](order: list[T] | None, default_item: T) -> list[T]:
    """Returns the provided order list or falls back to a single default item."""
    return order or [default_item]
