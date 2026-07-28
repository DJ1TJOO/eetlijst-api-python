from datetime import datetime
from typing import Annotated, Any, Optional

from pydantic import Field, PlainSerializer

from eetlijst_py.utils.scalars import serialize_datetime

from .base_model import BaseModel
from .enums import (
    ads_interaction_constraint,
    ads_interaction_update_column,
    cursor_ordering,
    eetschema_cook_points_import_constraint,
    eetschema_cook_points_import_update_column,
    eetschema_event_attendees_constraint,
    eetschema_event_attendees_update_column,
    eetschema_event_constraint,
    eetschema_event_select_column,
    eetschema_event_select_column_eetschema_event_aggregate_bool_exp_bool_and_arguments_columns,
    eetschema_event_select_column_eetschema_event_aggregate_bool_exp_bool_or_arguments_columns,
    eetschema_event_statistics_select_column,
    eetschema_event_update_column,
    eetschema_expense_constraint,
    eetschema_expense_distribution_constraint,
    eetschema_expense_distribution_update_column,
    eetschema_expense_select_column,
    eetschema_expense_select_column_eetschema_expense_aggregate_bool_exp_bool_and_arguments_columns,
    eetschema_expense_select_column_eetschema_expense_aggregate_bool_exp_bool_or_arguments_columns,
    eetschema_expense_update_column,
    eetschema_group_constraint,
    eetschema_group_update_column,
    eetschema_list_constraint,
    eetschema_list_update_column,
    eetschema_notification_constraint,
    eetschema_notification_update_column,
    eetschema_settlements_constraint,
    eetschema_settlements_update_column,
    eetschema_users_in_group_constraint,
    eetschema_users_in_group_update_column,
    order_by,
    recipe_review_constraint,
    recipe_review_select_column,
    recipe_review_update_column,
    recipes_constraint,
    recipes_select_column,
    recipes_select_column_recipes_aggregate_bool_exp_bool_and_arguments_columns,
    recipes_select_column_recipes_aggregate_bool_exp_bool_or_arguments_columns,
    recipes_update_column,
)


class Boolean_comparison_exp(BaseModel):
    """Boolean expression to compare columns of type "Boolean". All fields are combined with logical 'AND'."""

    eq: Optional[bool] = Field(alias="_eq", default=None)
    gt: Optional[bool] = Field(alias="_gt", default=None)
    gte: Optional[bool] = Field(alias="_gte", default=None)
    in_: Optional[list[bool]] = Field(alias="_in", default=None)
    is_null: Optional[bool] = Field(alias="_is_null", default=None)
    lt: Optional[bool] = Field(alias="_lt", default=None)
    lte: Optional[bool] = Field(alias="_lte", default=None)
    neq: Optional[bool] = Field(alias="_neq", default=None)
    nin: Optional[list[bool]] = Field(alias="_nin", default=None)


class Float_comparison_exp(BaseModel):
    """Boolean expression to compare columns of type "Float". All fields are combined with logical 'AND'."""

    eq: Optional[float] = Field(alias="_eq", default=None)
    gt: Optional[float] = Field(alias="_gt", default=None)
    gte: Optional[float] = Field(alias="_gte", default=None)
    in_: Optional[list[float]] = Field(alias="_in", default=None)
    is_null: Optional[bool] = Field(alias="_is_null", default=None)
    lt: Optional[float] = Field(alias="_lt", default=None)
    lte: Optional[float] = Field(alias="_lte", default=None)
    neq: Optional[float] = Field(alias="_neq", default=None)
    nin: Optional[list[float]] = Field(alias="_nin", default=None)


class Int_comparison_exp(BaseModel):
    """Boolean expression to compare columns of type "Int". All fields are combined with logical 'AND'."""

    eq: Optional[int] = Field(alias="_eq", default=None)
    gt: Optional[int] = Field(alias="_gt", default=None)
    gte: Optional[int] = Field(alias="_gte", default=None)
    in_: Optional[list[int]] = Field(alias="_in", default=None)
    is_null: Optional[bool] = Field(alias="_is_null", default=None)
    lt: Optional[int] = Field(alias="_lt", default=None)
    lte: Optional[int] = Field(alias="_lte", default=None)
    neq: Optional[int] = Field(alias="_neq", default=None)
    nin: Optional[list[int]] = Field(alias="_nin", default=None)


class SampleInput(BaseModel):
    app_id: str
    billable: Optional[bool] = None
    build: Optional[str] = None
    country_code: Optional[str] = None
    device_name: Optional[str] = Field(alias="deviceName", default=None)
    dialog_version: Optional[str] = Field(alias="dialogVersion", default=None)
    interaction_type: str
    model: str
    name_app: Optional[str] = Field(alias="nameApp", default=None)
    os: str
    os_version: Optional[str] = Field(alias="osVersion", default=None)
    package_name: Optional[str] = Field(alias="packageName", default=None)
    platform: str
    user_id: str
    version: Optional[str] = None


class String_array_comparison_exp(BaseModel):
    """Boolean expression to compare columns of type "String". All fields are combined with logical 'AND'."""

    contained_in: Optional[list[str]] = Field(alias="_contained_in", default=None)
    "is the array contained in the given array value"
    contains: Optional[list[str]] = Field(alias="_contains", default=None)
    "does the array contain the given value"
    eq: Optional[list[str]] = Field(alias="_eq", default=None)
    gt: Optional[list[str]] = Field(alias="_gt", default=None)
    gte: Optional[list[str]] = Field(alias="_gte", default=None)
    in_: Optional[list[list[str]]] = Field(alias="_in", default=None)
    is_null: Optional[bool] = Field(alias="_is_null", default=None)
    lt: Optional[list[str]] = Field(alias="_lt", default=None)
    lte: Optional[list[str]] = Field(alias="_lte", default=None)
    neq: Optional[list[str]] = Field(alias="_neq", default=None)
    nin: Optional[list[list[str]]] = Field(alias="_nin", default=None)


class String_comparison_exp(BaseModel):
    """Boolean expression to compare columns of type "String". All fields are combined with logical 'AND'."""

    eq: Optional[str] = Field(alias="_eq", default=None)
    gt: Optional[str] = Field(alias="_gt", default=None)
    gte: Optional[str] = Field(alias="_gte", default=None)
    ilike: Optional[str] = Field(alias="_ilike", default=None)
    "does the column match the given case-insensitive pattern"
    in_: Optional[list[str]] = Field(alias="_in", default=None)
    iregex: Optional[str] = Field(alias="_iregex", default=None)
    "does the column match the given POSIX regular expression, case insensitive"
    is_null: Optional[bool] = Field(alias="_is_null", default=None)
    like: Optional[str] = Field(alias="_like", default=None)
    "does the column match the given pattern"
    lt: Optional[str] = Field(alias="_lt", default=None)
    lte: Optional[str] = Field(alias="_lte", default=None)
    neq: Optional[str] = Field(alias="_neq", default=None)
    nilike: Optional[str] = Field(alias="_nilike", default=None)
    "does the column NOT match the given case-insensitive pattern"
    nin: Optional[list[str]] = Field(alias="_nin", default=None)
    niregex: Optional[str] = Field(alias="_niregex", default=None)
    "does the column NOT match the given POSIX regular expression, case insensitive"
    nlike: Optional[str] = Field(alias="_nlike", default=None)
    "does the column NOT match the given pattern"
    nregex: Optional[str] = Field(alias="_nregex", default=None)
    "does the column NOT match the given POSIX regular expression, case sensitive"
    nsimilar: Optional[str] = Field(alias="_nsimilar", default=None)
    "does the column NOT match the given SQL regular expression"
    regex: Optional[str] = Field(alias="_regex", default=None)
    "does the column match the given POSIX regular expression, case sensitive"
    similar: Optional[str] = Field(alias="_similar", default=None)
    "does the column match the given SQL regular expression"


class ads_ads_bool_exp(BaseModel):
    """Boolean expression to filter rows from the table "ads.ads". All fields are combined with a logical 'AND'."""

    and_: Optional[list["ads_ads_bool_exp"]] = Field(alias="_and", default=None)
    not_: Optional["ads_ads_bool_exp"] = Field(alias="_not", default=None)
    or_: Optional[list["ads_ads_bool_exp"]] = Field(alias="_or", default=None)
    ads_targetings: Optional["ads_ads_targeting_bool_exp"] = None
    btn_text: Optional["String_comparison_exp"] = None
    description: Optional["String_comparison_exp"] = None
    header: Optional["String_comparison_exp"] = None
    id: Optional["uuid_comparison_exp"] = None
    image_url: Optional["String_comparison_exp"] = None
    platform: Optional["String_comparison_exp"] = None
    target_user_type: Optional["String_comparison_exp"] = None
    url: Optional["String_comparison_exp"] = None


class ads_ads_order_by(BaseModel):
    """Ordering options when selecting data from "ads.ads"."""

    ads_targetings_aggregate: Optional["ads_ads_targeting_aggregate_order_by"] = None
    btn_text: Optional[order_by] = None
    description: Optional[order_by] = None
    header: Optional[order_by] = None
    id: Optional[order_by] = None
    image_url: Optional[order_by] = None
    platform: Optional[order_by] = None
    target_user_type: Optional[order_by] = None
    url: Optional[order_by] = None


class ads_ads_stream_cursor_input(BaseModel):
    '''Streaming cursor of the table "ads_ads"'''

    initial_value: "ads_ads_stream_cursor_value_input"
    "Stream column input with initial value"
    ordering: Optional[cursor_ordering] = None
    "cursor ordering"


class ads_ads_stream_cursor_value_input(BaseModel):
    """Initial value of the column from where the streaming should start"""

    btn_text: Optional[str] = None
    description: Optional[str] = None
    header: Optional[str] = None
    id: Optional[str] = None
    image_url: Optional[str] = None
    platform: Optional[str] = None
    target_user_type: Optional[str] = None
    url: Optional[str] = None


class ads_ads_targeting_aggregate_order_by(BaseModel):
    '''order by aggregate values of table "ads.ads_targeting"'''

    count: Optional[order_by] = None
    max: Optional["ads_ads_targeting_max_order_by"] = None
    min: Optional["ads_ads_targeting_min_order_by"] = None


class ads_ads_targeting_bool_exp(BaseModel):
    """Boolean expression to filter rows from the table "ads.ads_targeting". All fields are combined with a logical 'AND'."""

    and_: Optional[list["ads_ads_targeting_bool_exp"]] = Field(
        alias="_and", default=None
    )
    not_: Optional["ads_ads_targeting_bool_exp"] = Field(alias="_not", default=None)
    or_: Optional[list["ads_ads_targeting_bool_exp"]] = Field(alias="_or", default=None)
    ad: Optional["ads_ads_bool_exp"] = None
    ads_id: Optional["uuid_comparison_exp"] = None
    targeting: Optional["ads_targeting_bool_exp"] = None
    targeting_id: Optional["uuid_comparison_exp"] = None


class ads_ads_targeting_max_order_by(BaseModel):
    '''order by max() on columns of table "ads.ads_targeting"'''

    ads_id: Optional[order_by] = None
    targeting_id: Optional[order_by] = None


class ads_ads_targeting_min_order_by(BaseModel):
    '''order by min() on columns of table "ads.ads_targeting"'''

    ads_id: Optional[order_by] = None
    targeting_id: Optional[order_by] = None


class ads_ads_targeting_order_by(BaseModel):
    """Ordering options when selecting data from "ads.ads_targeting"."""

    ad: Optional["ads_ads_order_by"] = None
    ads_id: Optional[order_by] = None
    targeting: Optional["ads_targeting_order_by"] = None
    targeting_id: Optional[order_by] = None


class ads_ads_targeting_stream_cursor_input(BaseModel):
    '''Streaming cursor of the table "ads_ads_targeting"'''

    initial_value: "ads_ads_targeting_stream_cursor_value_input"
    "Stream column input with initial value"
    ordering: Optional[cursor_ordering] = None
    "cursor ordering"


class ads_ads_targeting_stream_cursor_value_input(BaseModel):
    """Initial value of the column from where the streaming should start"""

    ads_id: Optional[str] = None
    targeting_id: Optional[str] = None


class ads_interaction_bool_exp(BaseModel):
    """Boolean expression to filter rows from the table "ads.interaction". All fields are combined with a logical 'AND'."""

    and_: Optional[list["ads_interaction_bool_exp"]] = Field(alias="_and", default=None)
    not_: Optional["ads_interaction_bool_exp"] = Field(alias="_not", default=None)
    or_: Optional[list["ads_interaction_bool_exp"]] = Field(alias="_or", default=None)


class ads_interaction_insert_input(BaseModel):
    '''input type for inserting data into table "ads.interaction"'''

    i_pv_4: Optional[str] = Field(alias="IPv4", default=None)
    ad_id: Optional[str] = None
    billable: Optional[bool] = None
    build: Optional[str] = None
    city: Optional[str] = None
    country_code: Optional[str] = None
    country_name: Optional[str] = None
    device_name: Optional[str] = Field(alias="deviceName", default=None)
    device_id: Optional[str] = None
    dialog_version: Optional[Any] = None
    interaction_type: Optional[str] = None
    latitude: Optional[str] = None
    longitude: Optional[str] = None
    model: Optional[str] = None
    name_app: Optional[str] = Field(alias="nameApp", default=None)
    os: Optional[str] = None
    os_version: Optional[str] = Field(alias="osVersion", default=None)
    package_name: Optional[str] = Field(alias="packageName", default=None)
    platform: Optional[str] = None
    postal: Optional[str] = None
    state: Optional[str] = None
    version: Optional[str] = None


class ads_interaction_on_conflict(BaseModel):
    '''on_conflict condition type for table "ads.interaction"'''

    constraint: ads_interaction_constraint
    update_columns: list[ads_interaction_update_column] = Field(
        default_factory=lambda: []
    )
    where: Optional["ads_interaction_bool_exp"] = None


class ads_targeting_bool_exp(BaseModel):
    """Boolean expression to filter rows from the table "ads.targeting". All fields are combined with a logical 'AND'."""

    and_: Optional[list["ads_targeting_bool_exp"]] = Field(alias="_and", default=None)
    not_: Optional["ads_targeting_bool_exp"] = Field(alias="_not", default=None)
    or_: Optional[list["ads_targeting_bool_exp"]] = Field(alias="_or", default=None)
    ads_targetings: Optional["ads_ads_targeting_bool_exp"] = None
    city: Optional["String_comparison_exp"] = None
    id: Optional["uuid_comparison_exp"] = None


class ads_targeting_order_by(BaseModel):
    """Ordering options when selecting data from "ads.targeting"."""

    ads_targetings_aggregate: Optional["ads_ads_targeting_aggregate_order_by"] = None
    city: Optional[order_by] = None
    id: Optional[order_by] = None


class ads_targeting_stream_cursor_input(BaseModel):
    '''Streaming cursor of the table "ads_targeting"'''

    initial_value: "ads_targeting_stream_cursor_value_input"
    "Stream column input with initial value"
    ordering: Optional[cursor_ordering] = None
    "cursor ordering"


class ads_targeting_stream_cursor_value_input(BaseModel):
    """Initial value of the column from where the streaming should start"""

    city: Optional[str] = None
    id: Optional[str] = None


class bigint_comparison_exp(BaseModel):
    """Boolean expression to compare columns of type "bigint". All fields are combined with logical 'AND'."""

    eq: Optional[Any] = Field(alias="_eq", default=None)
    gt: Optional[Any] = Field(alias="_gt", default=None)
    gte: Optional[Any] = Field(alias="_gte", default=None)
    in_: Optional[list[Any]] = Field(alias="_in", default=None)
    is_null: Optional[bool] = Field(alias="_is_null", default=None)
    lt: Optional[Any] = Field(alias="_lt", default=None)
    lte: Optional[Any] = Field(alias="_lte", default=None)
    neq: Optional[Any] = Field(alias="_neq", default=None)
    nin: Optional[list[Any]] = Field(alias="_nin", default=None)


class eetschema_app_status_bool_exp(BaseModel):
    """Boolean expression to filter rows from the table "eetschema.app_status". All fields are combined with a logical 'AND'."""

    and_: Optional[list["eetschema_app_status_bool_exp"]] = Field(
        alias="_and", default=None
    )
    not_: Optional["eetschema_app_status_bool_exp"] = Field(alias="_not", default=None)
    or_: Optional[list["eetschema_app_status_bool_exp"]] = Field(
        alias="_or", default=None
    )
    beta_online: Optional["Boolean_comparison_exp"] = None
    created_at: Optional["timestamptz_comparison_exp"] = None
    id: Optional["uuid_comparison_exp"] = None
    updated_at: Optional["timestamptz_comparison_exp"] = None


class eetschema_app_status_order_by(BaseModel):
    """Ordering options when selecting data from "eetschema.app_status"."""

    beta_online: Optional[order_by] = None
    created_at: Optional[order_by] = None
    id: Optional[order_by] = None
    updated_at: Optional[order_by] = None


class eetschema_app_status_stream_cursor_input(BaseModel):
    '''Streaming cursor of the table "eetschema_app_status"'''

    initial_value: "eetschema_app_status_stream_cursor_value_input"
    "Stream column input with initial value"
    ordering: Optional[cursor_ordering] = None
    "cursor ordering"


class eetschema_app_status_stream_cursor_value_input(BaseModel):
    """Initial value of the column from where the streaming should start"""

    beta_online: Optional[bool] = None
    created_at: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = (
        None
    )
    id: Optional[str] = None
    updated_at: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = (
        None
    )


class eetschema_cook_points_import_aggregate_order_by(BaseModel):
    '''order by aggregate values of table "eetschema.cook_points_import"'''

    avg: Optional["eetschema_cook_points_import_avg_order_by"] = None
    count: Optional[order_by] = None
    max: Optional["eetschema_cook_points_import_max_order_by"] = None
    min: Optional["eetschema_cook_points_import_min_order_by"] = None
    stddev: Optional["eetschema_cook_points_import_stddev_order_by"] = None
    stddev_pop: Optional["eetschema_cook_points_import_stddev_pop_order_by"] = None
    stddev_samp: Optional["eetschema_cook_points_import_stddev_samp_order_by"] = None
    sum: Optional["eetschema_cook_points_import_sum_order_by"] = None
    var_pop: Optional["eetschema_cook_points_import_var_pop_order_by"] = None
    var_samp: Optional["eetschema_cook_points_import_var_samp_order_by"] = None
    variance: Optional["eetschema_cook_points_import_variance_order_by"] = None


class eetschema_cook_points_import_avg_order_by(BaseModel):
    '''order by avg() on columns of table "eetschema.cook_points_import"'''

    cook_points: Optional[order_by] = None


class eetschema_cook_points_import_bool_exp(BaseModel):
    """Boolean expression to filter rows from the table "eetschema.cook_points_import". All fields are combined with a logical 'AND'."""

    and_: Optional[list["eetschema_cook_points_import_bool_exp"]] = Field(
        alias="_and", default=None
    )
    not_: Optional["eetschema_cook_points_import_bool_exp"] = Field(
        alias="_not", default=None
    )
    or_: Optional[list["eetschema_cook_points_import_bool_exp"]] = Field(
        alias="_or", default=None
    )
    allowed_to_edit: Optional["Boolean_comparison_exp"] = None
    cook_points: Optional["Float_comparison_exp"] = None
    created_at: Optional["timestamptz_comparison_exp"] = None
    group: Optional["eetschema_group_bool_exp"] = None
    group_id: Optional["uuid_comparison_exp"] = None
    updated_at: Optional["timestamptz_comparison_exp"] = None
    user: Optional["eetschema_user_bool_exp"] = None
    user_id: Optional["String_comparison_exp"] = None
    user_in_group: Optional["eetschema_users_in_group_bool_exp"] = None


class eetschema_cook_points_import_inc_input(BaseModel):
    '''input type for incrementing numeric columns in table "eetschema.cook_points_import"'''

    cook_points: Optional[float] = None


class eetschema_cook_points_import_insert_input(BaseModel):
    '''input type for inserting data into table "eetschema.cook_points_import"'''

    cook_points: Optional[float] = None
    group: Optional["eetschema_group_obj_rel_insert_input"] = None
    group_id: Optional[str] = None
    user_id: Optional[str] = None
    user_in_group: Optional["eetschema_users_in_group_obj_rel_insert_input"] = None


class eetschema_cook_points_import_max_order_by(BaseModel):
    '''order by max() on columns of table "eetschema.cook_points_import"'''

    cook_points: Optional[order_by] = None
    created_at: Optional[order_by] = None
    group_id: Optional[order_by] = None
    updated_at: Optional[order_by] = None
    user_id: Optional[order_by] = None


class eetschema_cook_points_import_min_order_by(BaseModel):
    '''order by min() on columns of table "eetschema.cook_points_import"'''

    cook_points: Optional[order_by] = None
    created_at: Optional[order_by] = None
    group_id: Optional[order_by] = None
    updated_at: Optional[order_by] = None
    user_id: Optional[order_by] = None


class eetschema_cook_points_import_on_conflict(BaseModel):
    '''on_conflict condition type for table "eetschema.cook_points_import"'''

    constraint: eetschema_cook_points_import_constraint
    update_columns: list[eetschema_cook_points_import_update_column] = Field(
        default_factory=lambda: []
    )
    where: Optional["eetschema_cook_points_import_bool_exp"] = None


class eetschema_cook_points_import_order_by(BaseModel):
    """Ordering options when selecting data from "eetschema.cook_points_import"."""

    allowed_to_edit: Optional[order_by] = None
    cook_points: Optional[order_by] = None
    created_at: Optional[order_by] = None
    group: Optional["eetschema_group_order_by"] = None
    group_id: Optional[order_by] = None
    updated_at: Optional[order_by] = None
    user: Optional["eetschema_user_order_by"] = None
    user_id: Optional[order_by] = None
    user_in_group: Optional["eetschema_users_in_group_order_by"] = None


class eetschema_cook_points_import_pk_columns_input(BaseModel):
    """primary key columns input for table: eetschema.cook_points_import"""

    group_id: str
    user_id: str


class eetschema_cook_points_import_set_input(BaseModel):
    '''input type for updating data in table "eetschema.cook_points_import"'''

    cook_points: Optional[float] = None


class eetschema_cook_points_import_stddev_order_by(BaseModel):
    '''order by stddev() on columns of table "eetschema.cook_points_import"'''

    cook_points: Optional[order_by] = None


class eetschema_cook_points_import_stddev_pop_order_by(BaseModel):
    '''order by stddev_pop() on columns of table "eetschema.cook_points_import"'''

    cook_points: Optional[order_by] = None


class eetschema_cook_points_import_stddev_samp_order_by(BaseModel):
    '''order by stddev_samp() on columns of table "eetschema.cook_points_import"'''

    cook_points: Optional[order_by] = None


class eetschema_cook_points_import_stream_cursor_input(BaseModel):
    '''Streaming cursor of the table "eetschema_cook_points_import"'''

    initial_value: "eetschema_cook_points_import_stream_cursor_value_input"
    "Stream column input with initial value"
    ordering: Optional[cursor_ordering] = None
    "cursor ordering"


class eetschema_cook_points_import_stream_cursor_value_input(BaseModel):
    """Initial value of the column from where the streaming should start"""

    allowed_to_edit: Optional[bool] = None
    cook_points: Optional[float] = None
    created_at: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = (
        None
    )
    group_id: Optional[str] = None
    updated_at: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = (
        None
    )
    user_id: Optional[str] = None


class eetschema_cook_points_import_sum_order_by(BaseModel):
    '''order by sum() on columns of table "eetschema.cook_points_import"'''

    cook_points: Optional[order_by] = None


class eetschema_cook_points_import_updates(BaseModel):
    inc: Optional["eetschema_cook_points_import_inc_input"] = Field(
        alias="_inc", default=None
    )
    "increments the numeric columns with given value of the filtered values"
    set_: Optional["eetschema_cook_points_import_set_input"] = Field(
        alias="_set", default=None
    )
    "sets the columns of the filtered rows to the given values"
    where: "eetschema_cook_points_import_bool_exp"
    "filter the rows which have to be updated"


class eetschema_cook_points_import_var_pop_order_by(BaseModel):
    '''order by var_pop() on columns of table "eetschema.cook_points_import"'''

    cook_points: Optional[order_by] = None


class eetschema_cook_points_import_var_samp_order_by(BaseModel):
    '''order by var_samp() on columns of table "eetschema.cook_points_import"'''

    cook_points: Optional[order_by] = None


class eetschema_cook_points_import_variance_order_by(BaseModel):
    '''order by variance() on columns of table "eetschema.cook_points_import"'''

    cook_points: Optional[order_by] = None


class eetschema_event_aggregate_bool_exp(BaseModel):
    bool_and: Optional["eetschema_event_aggregate_bool_exp_bool_and"] = None
    bool_or: Optional["eetschema_event_aggregate_bool_exp_bool_or"] = None
    count: Optional["eetschema_event_aggregate_bool_exp_count"] = None


class eetschema_event_aggregate_bool_exp_bool_and(BaseModel):
    arguments: eetschema_event_select_column_eetschema_event_aggregate_bool_exp_bool_and_arguments_columns
    distinct: Optional[bool] = None
    filter_: Optional["eetschema_event_bool_exp"] = Field(alias="filter", default=None)
    predicate: "Boolean_comparison_exp"


class eetschema_event_aggregate_bool_exp_bool_or(BaseModel):
    arguments: eetschema_event_select_column_eetschema_event_aggregate_bool_exp_bool_or_arguments_columns
    distinct: Optional[bool] = None
    filter_: Optional["eetschema_event_bool_exp"] = Field(alias="filter", default=None)
    predicate: "Boolean_comparison_exp"


class eetschema_event_aggregate_bool_exp_count(BaseModel):
    arguments: Optional[list[eetschema_event_select_column]] = None
    distinct: Optional[bool] = None
    filter_: Optional["eetschema_event_bool_exp"] = Field(alias="filter", default=None)
    predicate: "Int_comparison_exp"


class eetschema_event_aggregate_order_by(BaseModel):
    '''order by aggregate values of table "eetschema.event"'''

    count: Optional[order_by] = None
    max: Optional["eetschema_event_max_order_by"] = None
    min: Optional["eetschema_event_min_order_by"] = None


class eetschema_event_arr_rel_insert_input(BaseModel):
    '''input type for inserting array relation for remote table "eetschema.event"'''

    data: list["eetschema_event_insert_input"]
    on_conflict: Optional["eetschema_event_on_conflict"] = None
    "upsert condition"


class eetschema_event_attendees_aggregate_order_by(BaseModel):
    '''order by aggregate values of table "eetschema.event_attendees"'''

    avg: Optional["eetschema_event_attendees_avg_order_by"] = None
    count: Optional[order_by] = None
    max: Optional["eetschema_event_attendees_max_order_by"] = None
    min: Optional["eetschema_event_attendees_min_order_by"] = None
    stddev: Optional["eetschema_event_attendees_stddev_order_by"] = None
    stddev_pop: Optional["eetschema_event_attendees_stddev_pop_order_by"] = None
    stddev_samp: Optional["eetschema_event_attendees_stddev_samp_order_by"] = None
    sum: Optional["eetschema_event_attendees_sum_order_by"] = None
    var_pop: Optional["eetschema_event_attendees_var_pop_order_by"] = None
    var_samp: Optional["eetschema_event_attendees_var_samp_order_by"] = None
    variance: Optional["eetschema_event_attendees_variance_order_by"] = None


class eetschema_event_attendees_arr_rel_insert_input(BaseModel):
    '''input type for inserting array relation for remote table "eetschema.event_attendees"'''

    data: list["eetschema_event_attendees_insert_input"]
    on_conflict: Optional["eetschema_event_attendees_on_conflict"] = None
    "upsert condition"


class eetschema_event_attendees_avg_order_by(BaseModel):
    '''order by avg() on columns of table "eetschema.event_attendees"'''

    number_guests: Optional[order_by] = None


class eetschema_event_attendees_bool_exp(BaseModel):
    """Boolean expression to filter rows from the table "eetschema.event_attendees". All fields are combined with a logical 'AND'."""

    and_: Optional[list["eetschema_event_attendees_bool_exp"]] = Field(
        alias="_and", default=None
    )
    not_: Optional["eetschema_event_attendees_bool_exp"] = Field(
        alias="_not", default=None
    )
    or_: Optional[list["eetschema_event_attendees_bool_exp"]] = Field(
        alias="_or", default=None
    )
    attending_user: Optional["eetschema_user_bool_exp"] = None
    comment: Optional["String_comparison_exp"] = None
    created_at: Optional["timestamptz_comparison_exp"] = None
    event_id: Optional["uuid_comparison_exp"] = None
    linked_event: Optional["eetschema_event_bool_exp"] = None
    number_guests: Optional["Int_comparison_exp"] = None
    status: Optional["String_comparison_exp"] = None
    updated_at: Optional["timestamptz_comparison_exp"] = None
    user_changed_status: Optional["Boolean_comparison_exp"] = None
    user_id: Optional["String_comparison_exp"] = None
    user_in_group: Optional["eetschema_users_in_group_bool_exp"] = None


class eetschema_event_attendees_inc_input(BaseModel):
    '''input type for incrementing numeric columns in table "eetschema.event_attendees"'''

    number_guests: Optional[int] = None


class eetschema_event_attendees_insert_input(BaseModel):
    '''input type for inserting data into table "eetschema.event_attendees"'''

    comment: Optional[str] = None
    event_id: Optional[str] = None
    linked_event: Optional["eetschema_event_obj_rel_insert_input"] = None
    number_guests: Optional[int] = None
    status: Optional[str] = None
    user_changed_status: Optional[bool] = None
    user_id: Optional[str] = None
    user_in_group: Optional["eetschema_users_in_group_obj_rel_insert_input"] = None


class eetschema_event_attendees_max_order_by(BaseModel):
    '''order by max() on columns of table "eetschema.event_attendees"'''

    comment: Optional[order_by] = None
    created_at: Optional[order_by] = None
    event_id: Optional[order_by] = None
    number_guests: Optional[order_by] = None
    status: Optional[order_by] = None
    updated_at: Optional[order_by] = None
    user_id: Optional[order_by] = None


class eetschema_event_attendees_min_order_by(BaseModel):
    '''order by min() on columns of table "eetschema.event_attendees"'''

    comment: Optional[order_by] = None
    created_at: Optional[order_by] = None
    event_id: Optional[order_by] = None
    number_guests: Optional[order_by] = None
    status: Optional[order_by] = None
    updated_at: Optional[order_by] = None
    user_id: Optional[order_by] = None


class eetschema_event_attendees_on_conflict(BaseModel):
    '''on_conflict condition type for table "eetschema.event_attendees"'''

    constraint: eetschema_event_attendees_constraint
    update_columns: list[eetschema_event_attendees_update_column] = Field(
        default_factory=lambda: []
    )
    where: Optional["eetschema_event_attendees_bool_exp"] = None


class eetschema_event_attendees_order_by(BaseModel):
    """Ordering options when selecting data from "eetschema.event_attendees"."""

    attending_user: Optional["eetschema_user_order_by"] = None
    comment: Optional[order_by] = None
    created_at: Optional[order_by] = None
    event_id: Optional[order_by] = None
    linked_event: Optional["eetschema_event_order_by"] = None
    number_guests: Optional[order_by] = None
    status: Optional[order_by] = None
    updated_at: Optional[order_by] = None
    user_changed_status: Optional[order_by] = None
    user_id: Optional[order_by] = None
    user_in_group: Optional["eetschema_users_in_group_order_by"] = None


class eetschema_event_attendees_pk_columns_input(BaseModel):
    """primary key columns input for table: eetschema.event_attendees"""

    event_id: str
    user_id: str


class eetschema_event_attendees_set_input(BaseModel):
    '''input type for updating data in table "eetschema.event_attendees"'''

    comment: Optional[str] = None
    number_guests: Optional[int] = None
    status: Optional[str] = None
    updated_at: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = (
        None
    )
    user_changed_status: Optional[bool] = None
    user_id: Optional[str] = None


class eetschema_event_attendees_stddev_order_by(BaseModel):
    '''order by stddev() on columns of table "eetschema.event_attendees"'''

    number_guests: Optional[order_by] = None


class eetschema_event_attendees_stddev_pop_order_by(BaseModel):
    '''order by stddev_pop() on columns of table "eetschema.event_attendees"'''

    number_guests: Optional[order_by] = None


class eetschema_event_attendees_stddev_samp_order_by(BaseModel):
    '''order by stddev_samp() on columns of table "eetschema.event_attendees"'''

    number_guests: Optional[order_by] = None


class eetschema_event_attendees_stream_cursor_input(BaseModel):
    '''Streaming cursor of the table "eetschema_event_attendees"'''

    initial_value: "eetschema_event_attendees_stream_cursor_value_input"
    "Stream column input with initial value"
    ordering: Optional[cursor_ordering] = None
    "cursor ordering"


class eetschema_event_attendees_stream_cursor_value_input(BaseModel):
    """Initial value of the column from where the streaming should start"""

    comment: Optional[str] = None
    created_at: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = (
        None
    )
    event_id: Optional[str] = None
    number_guests: Optional[int] = None
    status: Optional[str] = None
    updated_at: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = (
        None
    )
    user_changed_status: Optional[bool] = None
    user_id: Optional[str] = None


class eetschema_event_attendees_sum_order_by(BaseModel):
    '''order by sum() on columns of table "eetschema.event_attendees"'''

    number_guests: Optional[order_by] = None


class eetschema_event_attendees_updates(BaseModel):
    inc: Optional["eetschema_event_attendees_inc_input"] = Field(
        alias="_inc", default=None
    )
    "increments the numeric columns with given value of the filtered values"
    set_: Optional["eetschema_event_attendees_set_input"] = Field(
        alias="_set", default=None
    )
    "sets the columns of the filtered rows to the given values"
    where: "eetschema_event_attendees_bool_exp"
    "filter the rows which have to be updated"


class eetschema_event_attendees_var_pop_order_by(BaseModel):
    '''order by var_pop() on columns of table "eetschema.event_attendees"'''

    number_guests: Optional[order_by] = None


class eetschema_event_attendees_var_samp_order_by(BaseModel):
    '''order by var_samp() on columns of table "eetschema.event_attendees"'''

    number_guests: Optional[order_by] = None


class eetschema_event_attendees_variance_order_by(BaseModel):
    '''order by variance() on columns of table "eetschema.event_attendees"'''

    number_guests: Optional[order_by] = None


class eetschema_event_attendees_view_aggregate_order_by(BaseModel):
    '''order by aggregate values of table "eetschema.event_attendees_view"'''

    avg: Optional["eetschema_event_attendees_view_avg_order_by"] = None
    count: Optional[order_by] = None
    max: Optional["eetschema_event_attendees_view_max_order_by"] = None
    min: Optional["eetschema_event_attendees_view_min_order_by"] = None
    stddev: Optional["eetschema_event_attendees_view_stddev_order_by"] = None
    stddev_pop: Optional["eetschema_event_attendees_view_stddev_pop_order_by"] = None
    stddev_samp: Optional["eetschema_event_attendees_view_stddev_samp_order_by"] = None
    sum: Optional["eetschema_event_attendees_view_sum_order_by"] = None
    var_pop: Optional["eetschema_event_attendees_view_var_pop_order_by"] = None
    var_samp: Optional["eetschema_event_attendees_view_var_samp_order_by"] = None
    variance: Optional["eetschema_event_attendees_view_variance_order_by"] = None


class eetschema_event_attendees_view_avg_order_by(BaseModel):
    '''order by avg() on columns of table "eetschema.event_attendees_view"'''

    number_guests: Optional[order_by] = None
    order: Optional[order_by] = None


class eetschema_event_attendees_view_bool_exp(BaseModel):
    """Boolean expression to filter rows from the table "eetschema.event_attendees_view". All fields are combined with a logical 'AND'."""

    and_: Optional[list["eetschema_event_attendees_view_bool_exp"]] = Field(
        alias="_and", default=None
    )
    not_: Optional["eetschema_event_attendees_view_bool_exp"] = Field(
        alias="_not", default=None
    )
    or_: Optional[list["eetschema_event_attendees_view_bool_exp"]] = Field(
        alias="_or", default=None
    )
    active: Optional["Boolean_comparison_exp"] = None
    comment: Optional["String_comparison_exp"] = None
    event: Optional["eetschema_event_bool_exp"] = None
    event_id: Optional["uuid_comparison_exp"] = None
    friday: Optional["String_comparison_exp"] = None
    group: Optional["eetschema_group_bool_exp"] = None
    group_id: Optional["uuid_comparison_exp"] = None
    monday: Optional["String_comparison_exp"] = None
    number_guests: Optional["Int_comparison_exp"] = None
    order: Optional["Int_comparison_exp"] = None
    saturday: Optional["String_comparison_exp"] = None
    status: Optional["String_comparison_exp"] = None
    sunday: Optional["String_comparison_exp"] = None
    thursday: Optional["String_comparison_exp"] = None
    tuesday: Optional["String_comparison_exp"] = None
    user: Optional["eetschema_user_bool_exp"] = None
    user_id: Optional["String_comparison_exp"] = None
    wednesday: Optional["String_comparison_exp"] = None


class eetschema_event_attendees_view_max_order_by(BaseModel):
    '''order by max() on columns of table "eetschema.event_attendees_view"'''

    comment: Optional[order_by] = None
    event_id: Optional[order_by] = None
    friday: Optional[order_by] = None
    group_id: Optional[order_by] = None
    monday: Optional[order_by] = None
    number_guests: Optional[order_by] = None
    order: Optional[order_by] = None
    saturday: Optional[order_by] = None
    status: Optional[order_by] = None
    sunday: Optional[order_by] = None
    thursday: Optional[order_by] = None
    tuesday: Optional[order_by] = None
    user_id: Optional[order_by] = None
    wednesday: Optional[order_by] = None


class eetschema_event_attendees_view_min_order_by(BaseModel):
    '''order by min() on columns of table "eetschema.event_attendees_view"'''

    comment: Optional[order_by] = None
    event_id: Optional[order_by] = None
    friday: Optional[order_by] = None
    group_id: Optional[order_by] = None
    monday: Optional[order_by] = None
    number_guests: Optional[order_by] = None
    order: Optional[order_by] = None
    saturday: Optional[order_by] = None
    status: Optional[order_by] = None
    sunday: Optional[order_by] = None
    thursday: Optional[order_by] = None
    tuesday: Optional[order_by] = None
    user_id: Optional[order_by] = None
    wednesday: Optional[order_by] = None


class eetschema_event_attendees_view_order_by(BaseModel):
    """Ordering options when selecting data from "eetschema.event_attendees_view"."""

    active: Optional[order_by] = None
    comment: Optional[order_by] = None
    event: Optional["eetschema_event_order_by"] = None
    event_id: Optional[order_by] = None
    friday: Optional[order_by] = None
    group: Optional["eetschema_group_order_by"] = None
    group_id: Optional[order_by] = None
    monday: Optional[order_by] = None
    number_guests: Optional[order_by] = None
    order: Optional[order_by] = None
    saturday: Optional[order_by] = None
    status: Optional[order_by] = None
    sunday: Optional[order_by] = None
    thursday: Optional[order_by] = None
    tuesday: Optional[order_by] = None
    user: Optional["eetschema_user_order_by"] = None
    user_id: Optional[order_by] = None
    wednesday: Optional[order_by] = None


class eetschema_event_attendees_view_stddev_order_by(BaseModel):
    '''order by stddev() on columns of table "eetschema.event_attendees_view"'''

    number_guests: Optional[order_by] = None
    order: Optional[order_by] = None


class eetschema_event_attendees_view_stddev_pop_order_by(BaseModel):
    '''order by stddev_pop() on columns of table "eetschema.event_attendees_view"'''

    number_guests: Optional[order_by] = None
    order: Optional[order_by] = None


class eetschema_event_attendees_view_stddev_samp_order_by(BaseModel):
    '''order by stddev_samp() on columns of table "eetschema.event_attendees_view"'''

    number_guests: Optional[order_by] = None
    order: Optional[order_by] = None


class eetschema_event_attendees_view_stream_cursor_input(BaseModel):
    '''Streaming cursor of the table "eetschema_event_attendees_view"'''

    initial_value: "eetschema_event_attendees_view_stream_cursor_value_input"
    "Stream column input with initial value"
    ordering: Optional[cursor_ordering] = None
    "cursor ordering"


class eetschema_event_attendees_view_stream_cursor_value_input(BaseModel):
    """Initial value of the column from where the streaming should start"""

    active: Optional[bool] = None
    comment: Optional[str] = None
    event_id: Optional[str] = None
    friday: Optional[str] = None
    group_id: Optional[str] = None
    monday: Optional[str] = None
    number_guests: Optional[int] = None
    order: Optional[int] = None
    saturday: Optional[str] = None
    status: Optional[str] = None
    sunday: Optional[str] = None
    thursday: Optional[str] = None
    tuesday: Optional[str] = None
    user_id: Optional[str] = None
    wednesday: Optional[str] = None


class eetschema_event_attendees_view_sum_order_by(BaseModel):
    '''order by sum() on columns of table "eetschema.event_attendees_view"'''

    number_guests: Optional[order_by] = None
    order: Optional[order_by] = None


class eetschema_event_attendees_view_var_pop_order_by(BaseModel):
    '''order by var_pop() on columns of table "eetschema.event_attendees_view"'''

    number_guests: Optional[order_by] = None
    order: Optional[order_by] = None


class eetschema_event_attendees_view_var_samp_order_by(BaseModel):
    '''order by var_samp() on columns of table "eetschema.event_attendees_view"'''

    number_guests: Optional[order_by] = None
    order: Optional[order_by] = None


class eetschema_event_attendees_view_variance_order_by(BaseModel):
    '''order by variance() on columns of table "eetschema.event_attendees_view"'''

    number_guests: Optional[order_by] = None
    order: Optional[order_by] = None


class eetschema_event_bool_exp(BaseModel):
    """Boolean expression to filter rows from the table "eetschema.event". All fields are combined with a logical 'AND'."""

    and_: Optional[list["eetschema_event_bool_exp"]] = Field(alias="_and", default=None)
    not_: Optional["eetschema_event_bool_exp"] = Field(alias="_not", default=None)
    or_: Optional[list["eetschema_event_bool_exp"]] = Field(alias="_or", default=None)
    changed_signup_time: Optional["Boolean_comparison_exp"] = None
    closed_by: Optional["String_comparison_exp"] = None
    created_at: Optional["timestamptz_comparison_exp"] = None
    created_by: Optional["String_comparison_exp"] = None
    description: Optional["String_comparison_exp"] = None
    end_date: Optional["timestamptz_comparison_exp"] = None
    event_attendees: Optional["eetschema_event_attendees_bool_exp"] = None
    event_attendees_all_users: Optional["eetschema_event_attendees_view_bool_exp"] = (
        None
    )
    expense_id: Optional["uuid_comparison_exp"] = None
    group_id: Optional["uuid_comparison_exp"] = None
    id: Optional["uuid_comparison_exp"] = None
    linked_expenses: Optional["eetschema_expense_bool_exp"] = None
    linked_expenses_aggregate: Optional["eetschema_expense_aggregate_bool_exp"] = None
    linked_group: Optional["eetschema_group_bool_exp"] = None
    name: Optional["String_comparison_exp"] = None
    open: Optional["Boolean_comparison_exp"] = None
    signup_deadline: Optional["timestamptz_comparison_exp"] = None
    start_date: Optional["timestamptz_comparison_exp"] = None
    type_: Optional["String_comparison_exp"] = Field(alias="type", default=None)
    updated_at: Optional["timestamptz_comparison_exp"] = None
    user: Optional["eetschema_user_bool_exp"] = None


class eetschema_event_insert_input(BaseModel):
    '''input type for inserting data into table "eetschema.event"'''

    closed_by: Optional[str] = None
    created_by: Optional[str] = None
    description: Optional[str] = None
    end_date: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = None
    event_attendees: Optional["eetschema_event_attendees_arr_rel_insert_input"] = None
    linked_expenses: Optional["eetschema_expense_arr_rel_insert_input"] = None
    linked_group: Optional["eetschema_group_obj_rel_insert_input"] = None
    name: Optional[str] = None
    open: Optional[bool] = None
    signup_deadline: Optional[
        Annotated[datetime, PlainSerializer(serialize_datetime)]
    ] = None
    start_date: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = (
        None
    )
    type_: Optional[str] = Field(alias="type", default=None)


class eetschema_event_max_order_by(BaseModel):
    '''order by max() on columns of table "eetschema.event"'''

    closed_by: Optional[order_by] = None
    created_at: Optional[order_by] = None
    created_by: Optional[order_by] = None
    description: Optional[order_by] = None
    end_date: Optional[order_by] = None
    expense_id: Optional[order_by] = None
    group_id: Optional[order_by] = None
    id: Optional[order_by] = None
    name: Optional[order_by] = None
    signup_deadline: Optional[order_by] = None
    start_date: Optional[order_by] = None
    type_: Optional[order_by] = Field(alias="type", default=None)
    updated_at: Optional[order_by] = None


class eetschema_event_min_order_by(BaseModel):
    '''order by min() on columns of table "eetschema.event"'''

    closed_by: Optional[order_by] = None
    created_at: Optional[order_by] = None
    created_by: Optional[order_by] = None
    description: Optional[order_by] = None
    end_date: Optional[order_by] = None
    expense_id: Optional[order_by] = None
    group_id: Optional[order_by] = None
    id: Optional[order_by] = None
    name: Optional[order_by] = None
    signup_deadline: Optional[order_by] = None
    start_date: Optional[order_by] = None
    type_: Optional[order_by] = Field(alias="type", default=None)
    updated_at: Optional[order_by] = None


class eetschema_event_obj_rel_insert_input(BaseModel):
    '''input type for inserting object relation for remote table "eetschema.event"'''

    data: "eetschema_event_insert_input"
    on_conflict: Optional["eetschema_event_on_conflict"] = None
    "upsert condition"


class eetschema_event_on_conflict(BaseModel):
    '''on_conflict condition type for table "eetschema.event"'''

    constraint: eetschema_event_constraint
    update_columns: list[eetschema_event_update_column] = Field(
        default_factory=lambda: []
    )
    where: Optional["eetschema_event_bool_exp"] = None


class eetschema_event_order_by(BaseModel):
    """Ordering options when selecting data from "eetschema.event"."""

    changed_signup_time: Optional[order_by] = None
    closed_by: Optional[order_by] = None
    created_at: Optional[order_by] = None
    created_by: Optional[order_by] = None
    description: Optional[order_by] = None
    end_date: Optional[order_by] = None
    event_attendees_aggregate: Optional[
        "eetschema_event_attendees_aggregate_order_by"
    ] = None
    event_attendees_all_users_aggregate: Optional[
        "eetschema_event_attendees_view_aggregate_order_by"
    ] = None
    expense_id: Optional[order_by] = None
    group_id: Optional[order_by] = None
    id: Optional[order_by] = None
    linked_expenses_aggregate: Optional["eetschema_expense_aggregate_order_by"] = None
    linked_group: Optional["eetschema_group_order_by"] = None
    name: Optional[order_by] = None
    open: Optional[order_by] = None
    signup_deadline: Optional[order_by] = None
    start_date: Optional[order_by] = None
    type_: Optional[order_by] = Field(alias="type", default=None)
    updated_at: Optional[order_by] = None
    user: Optional["eetschema_user_order_by"] = None


class eetschema_event_pk_columns_input(BaseModel):
    """primary key columns input for table: eetschema.event"""

    id: str


class eetschema_event_set_input(BaseModel):
    '''input type for updating data in table "eetschema.event"'''

    changed_signup_time: Optional[bool] = None
    closed_by: Optional[str] = None
    description: Optional[str] = None
    end_date: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = None
    name: Optional[str] = None
    open: Optional[bool] = None
    signup_deadline: Optional[
        Annotated[datetime, PlainSerializer(serialize_datetime)]
    ] = None
    start_date: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = (
        None
    )


class eetschema_event_statistics_aggregate_bool_exp(BaseModel):
    count: Optional["eetschema_event_statistics_aggregate_bool_exp_count"] = None


class eetschema_event_statistics_aggregate_bool_exp_count(BaseModel):
    arguments: Optional[list[eetschema_event_statistics_select_column]] = None
    distinct: Optional[bool] = None
    filter_: Optional["eetschema_event_statistics_bool_exp"] = Field(
        alias="filter", default=None
    )
    predicate: "Int_comparison_exp"


class eetschema_event_statistics_aggregate_order_by(BaseModel):
    '''order by aggregate values of table "eetschema.event_statistics"'''

    avg: Optional["eetschema_event_statistics_avg_order_by"] = None
    count: Optional[order_by] = None
    max: Optional["eetschema_event_statistics_max_order_by"] = None
    min: Optional["eetschema_event_statistics_min_order_by"] = None
    stddev: Optional["eetschema_event_statistics_stddev_order_by"] = None
    stddev_pop: Optional["eetschema_event_statistics_stddev_pop_order_by"] = None
    stddev_samp: Optional["eetschema_event_statistics_stddev_samp_order_by"] = None
    sum: Optional["eetschema_event_statistics_sum_order_by"] = None
    var_pop: Optional["eetschema_event_statistics_var_pop_order_by"] = None
    var_samp: Optional["eetschema_event_statistics_var_samp_order_by"] = None
    variance: Optional["eetschema_event_statistics_variance_order_by"] = None


class eetschema_event_statistics_avg_order_by(BaseModel):
    '''order by avg() on columns of table "eetschema.event_statistics"'''

    cook_points: Optional[order_by] = None
    number_guests: Optional[order_by] = None
    total_number_of_eaters: Optional[order_by] = None


class eetschema_event_statistics_bool_exp(BaseModel):
    """Boolean expression to filter rows from the table "eetschema.event_statistics". All fields are combined with a logical 'AND'."""

    and_: Optional[list["eetschema_event_statistics_bool_exp"]] = Field(
        alias="_and", default=None
    )
    not_: Optional["eetschema_event_statistics_bool_exp"] = Field(
        alias="_not", default=None
    )
    or_: Optional[list["eetschema_event_statistics_bool_exp"]] = Field(
        alias="_or", default=None
    )
    cook_points: Optional["Float_comparison_exp"] = None
    event: Optional["eetschema_event_bool_exp"] = None
    event_id: Optional["uuid_comparison_exp"] = None
    event_start_date: Optional["timestamptz_comparison_exp"] = None
    group_id: Optional["uuid_comparison_exp"] = None
    number_guests: Optional["Int_comparison_exp"] = None
    status: Optional["String_comparison_exp"] = None
    total_number_of_eaters: Optional["Int_comparison_exp"] = None
    user: Optional["eetschema_user_bool_exp"] = None
    user_id: Optional["String_comparison_exp"] = None


class eetschema_event_statistics_max_order_by(BaseModel):
    '''order by max() on columns of table "eetschema.event_statistics"'''

    cook_points: Optional[order_by] = None
    event_id: Optional[order_by] = None
    event_start_date: Optional[order_by] = None
    group_id: Optional[order_by] = None
    number_guests: Optional[order_by] = None
    status: Optional[order_by] = None
    total_number_of_eaters: Optional[order_by] = None
    user_id: Optional[order_by] = None


class eetschema_event_statistics_min_order_by(BaseModel):
    '''order by min() on columns of table "eetschema.event_statistics"'''

    cook_points: Optional[order_by] = None
    event_id: Optional[order_by] = None
    event_start_date: Optional[order_by] = None
    group_id: Optional[order_by] = None
    number_guests: Optional[order_by] = None
    status: Optional[order_by] = None
    total_number_of_eaters: Optional[order_by] = None
    user_id: Optional[order_by] = None


class eetschema_event_statistics_old_import_aggregate_order_by(BaseModel):
    '''order by aggregate values of table "eetschema.event_statistics_old_import"'''

    avg: Optional["eetschema_event_statistics_old_import_avg_order_by"] = None
    count: Optional[order_by] = None
    max: Optional["eetschema_event_statistics_old_import_max_order_by"] = None
    min: Optional["eetschema_event_statistics_old_import_min_order_by"] = None
    stddev: Optional["eetschema_event_statistics_old_import_stddev_order_by"] = None
    stddev_pop: Optional[
        "eetschema_event_statistics_old_import_stddev_pop_order_by"
    ] = None
    stddev_samp: Optional[
        "eetschema_event_statistics_old_import_stddev_samp_order_by"
    ] = None
    sum: Optional["eetschema_event_statistics_old_import_sum_order_by"] = None
    var_pop: Optional["eetschema_event_statistics_old_import_var_pop_order_by"] = None
    var_samp: Optional["eetschema_event_statistics_old_import_var_samp_order_by"] = None
    variance: Optional["eetschema_event_statistics_old_import_variance_order_by"] = None


class eetschema_event_statistics_old_import_avg_order_by(BaseModel):
    '''order by avg() on columns of table "eetschema.event_statistics_old_import"'''

    num_cooked: Optional[order_by] = None
    num_does_groceries: Optional[order_by] = None
    num_eat_only: Optional[order_by] = None


class eetschema_event_statistics_old_import_bool_exp(BaseModel):
    """Boolean expression to filter rows from the table "eetschema.event_statistics_old_import". All fields are combined with a logical 'AND'."""

    and_: Optional[list["eetschema_event_statistics_old_import_bool_exp"]] = Field(
        alias="_and", default=None
    )
    not_: Optional["eetschema_event_statistics_old_import_bool_exp"] = Field(
        alias="_not", default=None
    )
    or_: Optional[list["eetschema_event_statistics_old_import_bool_exp"]] = Field(
        alias="_or", default=None
    )
    event_start_date: Optional["timestamptz_comparison_exp"] = None
    group: Optional["eetschema_group_bool_exp"] = None
    group_id: Optional["uuid_comparison_exp"] = None
    num_cooked: Optional["Int_comparison_exp"] = None
    num_does_groceries: Optional["Int_comparison_exp"] = None
    num_eat_only: Optional["Int_comparison_exp"] = None
    user: Optional["eetschema_user_bool_exp"] = None
    user_id: Optional["String_comparison_exp"] = None


class eetschema_event_statistics_old_import_max_order_by(BaseModel):
    '''order by max() on columns of table "eetschema.event_statistics_old_import"'''

    event_start_date: Optional[order_by] = None
    group_id: Optional[order_by] = None
    num_cooked: Optional[order_by] = None
    num_does_groceries: Optional[order_by] = None
    num_eat_only: Optional[order_by] = None
    user_id: Optional[order_by] = None


class eetschema_event_statistics_old_import_min_order_by(BaseModel):
    '''order by min() on columns of table "eetschema.event_statistics_old_import"'''

    event_start_date: Optional[order_by] = None
    group_id: Optional[order_by] = None
    num_cooked: Optional[order_by] = None
    num_does_groceries: Optional[order_by] = None
    num_eat_only: Optional[order_by] = None
    user_id: Optional[order_by] = None


class eetschema_event_statistics_old_import_order_by(BaseModel):
    """Ordering options when selecting data from "eetschema.event_statistics_old_import"."""

    event_start_date: Optional[order_by] = None
    group: Optional["eetschema_group_order_by"] = None
    group_id: Optional[order_by] = None
    num_cooked: Optional[order_by] = None
    num_does_groceries: Optional[order_by] = None
    num_eat_only: Optional[order_by] = None
    user: Optional["eetschema_user_order_by"] = None
    user_id: Optional[order_by] = None


class eetschema_event_statistics_old_import_stddev_order_by(BaseModel):
    '''order by stddev() on columns of table "eetschema.event_statistics_old_import"'''

    num_cooked: Optional[order_by] = None
    num_does_groceries: Optional[order_by] = None
    num_eat_only: Optional[order_by] = None


class eetschema_event_statistics_old_import_stddev_pop_order_by(BaseModel):
    '''order by stddev_pop() on columns of table "eetschema.event_statistics_old_import"'''

    num_cooked: Optional[order_by] = None
    num_does_groceries: Optional[order_by] = None
    num_eat_only: Optional[order_by] = None


class eetschema_event_statistics_old_import_stddev_samp_order_by(BaseModel):
    '''order by stddev_samp() on columns of table "eetschema.event_statistics_old_import"'''

    num_cooked: Optional[order_by] = None
    num_does_groceries: Optional[order_by] = None
    num_eat_only: Optional[order_by] = None


class eetschema_event_statistics_old_import_stream_cursor_input(BaseModel):
    '''Streaming cursor of the table "eetschema_event_statistics_old_import"'''

    initial_value: "eetschema_event_statistics_old_import_stream_cursor_value_input"
    "Stream column input with initial value"
    ordering: Optional[cursor_ordering] = None
    "cursor ordering"


class eetschema_event_statistics_old_import_stream_cursor_value_input(BaseModel):
    """Initial value of the column from where the streaming should start"""

    event_start_date: Optional[
        Annotated[datetime, PlainSerializer(serialize_datetime)]
    ] = None
    group_id: Optional[str] = None
    num_cooked: Optional[int] = None
    num_does_groceries: Optional[int] = None
    num_eat_only: Optional[int] = None
    user_id: Optional[str] = None


class eetschema_event_statistics_old_import_sum_order_by(BaseModel):
    '''order by sum() on columns of table "eetschema.event_statistics_old_import"'''

    num_cooked: Optional[order_by] = None
    num_does_groceries: Optional[order_by] = None
    num_eat_only: Optional[order_by] = None


class eetschema_event_statistics_old_import_var_pop_order_by(BaseModel):
    '''order by var_pop() on columns of table "eetschema.event_statistics_old_import"'''

    num_cooked: Optional[order_by] = None
    num_does_groceries: Optional[order_by] = None
    num_eat_only: Optional[order_by] = None


class eetschema_event_statistics_old_import_var_samp_order_by(BaseModel):
    '''order by var_samp() on columns of table "eetschema.event_statistics_old_import"'''

    num_cooked: Optional[order_by] = None
    num_does_groceries: Optional[order_by] = None
    num_eat_only: Optional[order_by] = None


class eetschema_event_statistics_old_import_variance_order_by(BaseModel):
    '''order by variance() on columns of table "eetschema.event_statistics_old_import"'''

    num_cooked: Optional[order_by] = None
    num_does_groceries: Optional[order_by] = None
    num_eat_only: Optional[order_by] = None


class eetschema_event_statistics_order_by(BaseModel):
    """Ordering options when selecting data from "eetschema.event_statistics"."""

    cook_points: Optional[order_by] = None
    event: Optional["eetschema_event_order_by"] = None
    event_id: Optional[order_by] = None
    event_start_date: Optional[order_by] = None
    group_id: Optional[order_by] = None
    number_guests: Optional[order_by] = None
    status: Optional[order_by] = None
    total_number_of_eaters: Optional[order_by] = None
    user: Optional["eetschema_user_order_by"] = None
    user_id: Optional[order_by] = None


class eetschema_event_statistics_stddev_order_by(BaseModel):
    '''order by stddev() on columns of table "eetschema.event_statistics"'''

    cook_points: Optional[order_by] = None
    number_guests: Optional[order_by] = None
    total_number_of_eaters: Optional[order_by] = None


class eetschema_event_statistics_stddev_pop_order_by(BaseModel):
    '''order by stddev_pop() on columns of table "eetschema.event_statistics"'''

    cook_points: Optional[order_by] = None
    number_guests: Optional[order_by] = None
    total_number_of_eaters: Optional[order_by] = None


class eetschema_event_statistics_stddev_samp_order_by(BaseModel):
    '''order by stddev_samp() on columns of table "eetschema.event_statistics"'''

    cook_points: Optional[order_by] = None
    number_guests: Optional[order_by] = None
    total_number_of_eaters: Optional[order_by] = None


class eetschema_event_statistics_stream_cursor_input(BaseModel):
    '''Streaming cursor of the table "eetschema_event_statistics"'''

    initial_value: "eetschema_event_statistics_stream_cursor_value_input"
    "Stream column input with initial value"
    ordering: Optional[cursor_ordering] = None
    "cursor ordering"


class eetschema_event_statistics_stream_cursor_value_input(BaseModel):
    """Initial value of the column from where the streaming should start"""

    cook_points: Optional[float] = None
    event_id: Optional[str] = None
    event_start_date: Optional[
        Annotated[datetime, PlainSerializer(serialize_datetime)]
    ] = None
    group_id: Optional[str] = None
    number_guests: Optional[int] = None
    status: Optional[str] = None
    total_number_of_eaters: Optional[int] = None
    user_id: Optional[str] = None


class eetschema_event_statistics_sum_order_by(BaseModel):
    '''order by sum() on columns of table "eetschema.event_statistics"'''

    cook_points: Optional[order_by] = None
    number_guests: Optional[order_by] = None
    total_number_of_eaters: Optional[order_by] = None


class eetschema_event_statistics_var_pop_order_by(BaseModel):
    '''order by var_pop() on columns of table "eetschema.event_statistics"'''

    cook_points: Optional[order_by] = None
    number_guests: Optional[order_by] = None
    total_number_of_eaters: Optional[order_by] = None


class eetschema_event_statistics_var_samp_order_by(BaseModel):
    '''order by var_samp() on columns of table "eetschema.event_statistics"'''

    cook_points: Optional[order_by] = None
    number_guests: Optional[order_by] = None
    total_number_of_eaters: Optional[order_by] = None


class eetschema_event_statistics_variance_order_by(BaseModel):
    '''order by variance() on columns of table "eetschema.event_statistics"'''

    cook_points: Optional[order_by] = None
    number_guests: Optional[order_by] = None
    total_number_of_eaters: Optional[order_by] = None


class eetschema_event_stream_cursor_input(BaseModel):
    '''Streaming cursor of the table "eetschema_event"'''

    initial_value: "eetschema_event_stream_cursor_value_input"
    "Stream column input with initial value"
    ordering: Optional[cursor_ordering] = None
    "cursor ordering"


class eetschema_event_stream_cursor_value_input(BaseModel):
    """Initial value of the column from where the streaming should start"""

    changed_signup_time: Optional[bool] = None
    closed_by: Optional[str] = None
    created_at: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = (
        None
    )
    created_by: Optional[str] = None
    description: Optional[str] = None
    end_date: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = None
    expense_id: Optional[str] = None
    group_id: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    open: Optional[bool] = None
    signup_deadline: Optional[
        Annotated[datetime, PlainSerializer(serialize_datetime)]
    ] = None
    start_date: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = (
        None
    )
    type_: Optional[str] = Field(alias="type", default=None)
    updated_at: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = (
        None
    )


class eetschema_event_updates(BaseModel):
    set_: Optional["eetschema_event_set_input"] = Field(alias="_set", default=None)
    "sets the columns of the filtered rows to the given values"
    where: "eetschema_event_bool_exp"
    "filter the rows which have to be updated"


class eetschema_expense_aggregate_bool_exp(BaseModel):
    bool_and: Optional["eetschema_expense_aggregate_bool_exp_bool_and"] = None
    bool_or: Optional["eetschema_expense_aggregate_bool_exp_bool_or"] = None
    count: Optional["eetschema_expense_aggregate_bool_exp_count"] = None


class eetschema_expense_aggregate_bool_exp_bool_and(BaseModel):
    arguments: eetschema_expense_select_column_eetschema_expense_aggregate_bool_exp_bool_and_arguments_columns
    distinct: Optional[bool] = None
    filter_: Optional["eetschema_expense_bool_exp"] = Field(
        alias="filter", default=None
    )
    predicate: "Boolean_comparison_exp"


class eetschema_expense_aggregate_bool_exp_bool_or(BaseModel):
    arguments: eetschema_expense_select_column_eetschema_expense_aggregate_bool_exp_bool_or_arguments_columns
    distinct: Optional[bool] = None
    filter_: Optional["eetschema_expense_bool_exp"] = Field(
        alias="filter", default=None
    )
    predicate: "Boolean_comparison_exp"


class eetschema_expense_aggregate_bool_exp_count(BaseModel):
    arguments: Optional[list[eetschema_expense_select_column]] = None
    distinct: Optional[bool] = None
    filter_: Optional["eetschema_expense_bool_exp"] = Field(
        alias="filter", default=None
    )
    predicate: "Int_comparison_exp"


class eetschema_expense_aggregate_order_by(BaseModel):
    '''order by aggregate values of table "eetschema.expense"'''

    avg: Optional["eetschema_expense_avg_order_by"] = None
    count: Optional[order_by] = None
    max: Optional["eetschema_expense_max_order_by"] = None
    min: Optional["eetschema_expense_min_order_by"] = None
    stddev: Optional["eetschema_expense_stddev_order_by"] = None
    stddev_pop: Optional["eetschema_expense_stddev_pop_order_by"] = None
    stddev_samp: Optional["eetschema_expense_stddev_samp_order_by"] = None
    sum: Optional["eetschema_expense_sum_order_by"] = None
    var_pop: Optional["eetschema_expense_var_pop_order_by"] = None
    var_samp: Optional["eetschema_expense_var_samp_order_by"] = None
    variance: Optional["eetschema_expense_variance_order_by"] = None


class eetschema_expense_arr_rel_insert_input(BaseModel):
    '''input type for inserting array relation for remote table "eetschema.expense"'''

    data: list["eetschema_expense_insert_input"]
    on_conflict: Optional["eetschema_expense_on_conflict"] = None
    "upsert condition"


class eetschema_expense_avg_order_by(BaseModel):
    '''order by avg() on columns of table "eetschema.expense"'''

    payed_amount: Optional[order_by] = None


class eetschema_expense_bool_exp(BaseModel):
    """Boolean expression to filter rows from the table "eetschema.expense". All fields are combined with a logical 'AND'."""

    and_: Optional[list["eetschema_expense_bool_exp"]] = Field(
        alias="_and", default=None
    )
    not_: Optional["eetschema_expense_bool_exp"] = Field(alias="_not", default=None)
    or_: Optional[list["eetschema_expense_bool_exp"]] = Field(alias="_or", default=None)
    created_at: Optional["timestamptz_comparison_exp"] = None
    deleted: Optional["Boolean_comparison_exp"] = None
    description: Optional["String_comparison_exp"] = None
    event_id: Optional["uuid_comparison_exp"] = None
    expense_distributions: Optional["eetschema_expense_distribution_bool_exp"] = None
    group: Optional["eetschema_group_bool_exp"] = None
    group_id: Optional["uuid_comparison_exp"] = None
    id: Optional["uuid_comparison_exp"] = None
    issued_by: Optional["String_comparison_exp"] = None
    linked_event: Optional["eetschema_event_bool_exp"] = None
    payed_amount: Optional["Int_comparison_exp"] = None
    payed_at: Optional["timestamptz_comparison_exp"] = None
    payed_by: Optional["String_comparison_exp"] = None
    payed_by_user: Optional["eetschema_user_bool_exp"] = None
    settled_id: Optional["uuid_comparison_exp"] = None
    settlement: Optional["eetschema_settlements_bool_exp"] = None
    settlement_expense_id: Optional["uuid_comparison_exp"] = None
    updated_by_user: Optional["eetschema_user_bool_exp"] = Field(
        alias="updatedByUser", default=None
    )
    updated_at: Optional["timestamptz_comparison_exp"] = None
    updated_by: Optional["String_comparison_exp"] = None
    user: Optional["eetschema_user_bool_exp"] = None


class eetschema_expense_distribution_aggregate_order_by(BaseModel):
    '''order by aggregate values of table "eetschema.expense_distribution"'''

    avg: Optional["eetschema_expense_distribution_avg_order_by"] = None
    count: Optional[order_by] = None
    max: Optional["eetschema_expense_distribution_max_order_by"] = None
    min: Optional["eetschema_expense_distribution_min_order_by"] = None
    stddev: Optional["eetschema_expense_distribution_stddev_order_by"] = None
    stddev_pop: Optional["eetschema_expense_distribution_stddev_pop_order_by"] = None
    stddev_samp: Optional["eetschema_expense_distribution_stddev_samp_order_by"] = None
    sum: Optional["eetschema_expense_distribution_sum_order_by"] = None
    var_pop: Optional["eetschema_expense_distribution_var_pop_order_by"] = None
    var_samp: Optional["eetschema_expense_distribution_var_samp_order_by"] = None
    variance: Optional["eetschema_expense_distribution_variance_order_by"] = None


class eetschema_expense_distribution_arr_rel_insert_input(BaseModel):
    '''input type for inserting array relation for remote table "eetschema.expense_distribution"'''

    data: list["eetschema_expense_distribution_insert_input"]
    on_conflict: Optional["eetschema_expense_distribution_on_conflict"] = None
    "upsert condition"


class eetschema_expense_distribution_avg_order_by(BaseModel):
    '''order by avg() on columns of table "eetschema.expense_distribution"'''

    count: Optional[order_by] = None
    payed_amount: Optional[order_by] = None


class eetschema_expense_distribution_bool_exp(BaseModel):
    """Boolean expression to filter rows from the table "eetschema.expense_distribution". All fields are combined with a logical 'AND'."""

    and_: Optional[list["eetschema_expense_distribution_bool_exp"]] = Field(
        alias="_and", default=None
    )
    not_: Optional["eetschema_expense_distribution_bool_exp"] = Field(
        alias="_not", default=None
    )
    or_: Optional[list["eetschema_expense_distribution_bool_exp"]] = Field(
        alias="_or", default=None
    )
    count: Optional["Int_comparison_exp"] = None
    created_at: Optional["timestamptz_comparison_exp"] = None
    expense_id: Optional["uuid_comparison_exp"] = None
    expense_origin: Optional["eetschema_expense_bool_exp"] = None
    id: Optional["uuid_comparison_exp"] = None
    payed_amount: Optional["Int_comparison_exp"] = None
    updated_at: Optional["timestamptz_comparison_exp"] = None
    user: Optional["eetschema_user_bool_exp"] = None
    user_id: Optional["String_comparison_exp"] = None


class eetschema_expense_distribution_inc_input(BaseModel):
    '''input type for incrementing numeric columns in table "eetschema.expense_distribution"'''

    count: Optional[int] = None
    payed_amount: Optional[int] = None


class eetschema_expense_distribution_insert_input(BaseModel):
    '''input type for inserting data into table "eetschema.expense_distribution"'''

    count: Optional[int] = None
    created_at: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = (
        None
    )
    expense_id: Optional[str] = None
    expense_origin: Optional["eetschema_expense_obj_rel_insert_input"] = None
    id: Optional[str] = None
    payed_amount: Optional[int] = None
    updated_at: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = (
        None
    )
    user_id: Optional[str] = None


class eetschema_expense_distribution_max_order_by(BaseModel):
    '''order by max() on columns of table "eetschema.expense_distribution"'''

    count: Optional[order_by] = None
    created_at: Optional[order_by] = None
    expense_id: Optional[order_by] = None
    id: Optional[order_by] = None
    payed_amount: Optional[order_by] = None
    updated_at: Optional[order_by] = None
    user_id: Optional[order_by] = None


class eetschema_expense_distribution_min_order_by(BaseModel):
    '''order by min() on columns of table "eetschema.expense_distribution"'''

    count: Optional[order_by] = None
    created_at: Optional[order_by] = None
    expense_id: Optional[order_by] = None
    id: Optional[order_by] = None
    payed_amount: Optional[order_by] = None
    updated_at: Optional[order_by] = None
    user_id: Optional[order_by] = None


class eetschema_expense_distribution_on_conflict(BaseModel):
    '''on_conflict condition type for table "eetschema.expense_distribution"'''

    constraint: eetschema_expense_distribution_constraint
    update_columns: list[eetschema_expense_distribution_update_column] = Field(
        default_factory=lambda: []
    )
    where: Optional["eetschema_expense_distribution_bool_exp"] = None


class eetschema_expense_distribution_order_by(BaseModel):
    """Ordering options when selecting data from "eetschema.expense_distribution"."""

    count: Optional[order_by] = None
    created_at: Optional[order_by] = None
    expense_id: Optional[order_by] = None
    expense_origin: Optional["eetschema_expense_order_by"] = None
    id: Optional[order_by] = None
    payed_amount: Optional[order_by] = None
    updated_at: Optional[order_by] = None
    user: Optional["eetschema_user_order_by"] = None
    user_id: Optional[order_by] = None


class eetschema_expense_distribution_pk_columns_input(BaseModel):
    """primary key columns input for table: eetschema.expense_distribution"""

    id: str


class eetschema_expense_distribution_set_input(BaseModel):
    '''input type for updating data in table "eetschema.expense_distribution"'''

    count: Optional[int] = None
    created_at: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = (
        None
    )
    expense_id: Optional[str] = None
    id: Optional[str] = None
    payed_amount: Optional[int] = None
    updated_at: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = (
        None
    )
    user_id: Optional[str] = None


class eetschema_expense_distribution_stddev_order_by(BaseModel):
    '''order by stddev() on columns of table "eetschema.expense_distribution"'''

    count: Optional[order_by] = None
    payed_amount: Optional[order_by] = None


class eetschema_expense_distribution_stddev_pop_order_by(BaseModel):
    '''order by stddev_pop() on columns of table "eetschema.expense_distribution"'''

    count: Optional[order_by] = None
    payed_amount: Optional[order_by] = None


class eetschema_expense_distribution_stddev_samp_order_by(BaseModel):
    '''order by stddev_samp() on columns of table "eetschema.expense_distribution"'''

    count: Optional[order_by] = None
    payed_amount: Optional[order_by] = None


class eetschema_expense_distribution_stream_cursor_input(BaseModel):
    '''Streaming cursor of the table "eetschema_expense_distribution"'''

    initial_value: "eetschema_expense_distribution_stream_cursor_value_input"
    "Stream column input with initial value"
    ordering: Optional[cursor_ordering] = None
    "cursor ordering"


class eetschema_expense_distribution_stream_cursor_value_input(BaseModel):
    """Initial value of the column from where the streaming should start"""

    count: Optional[int] = None
    created_at: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = (
        None
    )
    expense_id: Optional[str] = None
    id: Optional[str] = None
    payed_amount: Optional[int] = None
    updated_at: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = (
        None
    )
    user_id: Optional[str] = None


class eetschema_expense_distribution_sum_order_by(BaseModel):
    '''order by sum() on columns of table "eetschema.expense_distribution"'''

    count: Optional[order_by] = None
    payed_amount: Optional[order_by] = None


class eetschema_expense_distribution_updates(BaseModel):
    inc: Optional["eetschema_expense_distribution_inc_input"] = Field(
        alias="_inc", default=None
    )
    "increments the numeric columns with given value of the filtered values"
    set_: Optional["eetschema_expense_distribution_set_input"] = Field(
        alias="_set", default=None
    )
    "sets the columns of the filtered rows to the given values"
    where: "eetschema_expense_distribution_bool_exp"
    "filter the rows which have to be updated"


class eetschema_expense_distribution_var_pop_order_by(BaseModel):
    '''order by var_pop() on columns of table "eetschema.expense_distribution"'''

    count: Optional[order_by] = None
    payed_amount: Optional[order_by] = None


class eetschema_expense_distribution_var_samp_order_by(BaseModel):
    '''order by var_samp() on columns of table "eetschema.expense_distribution"'''

    count: Optional[order_by] = None
    payed_amount: Optional[order_by] = None


class eetschema_expense_distribution_variance_order_by(BaseModel):
    '''order by variance() on columns of table "eetschema.expense_distribution"'''

    count: Optional[order_by] = None
    payed_amount: Optional[order_by] = None


class eetschema_expense_eetlijst_import_bool_exp(BaseModel):
    """Boolean expression to filter rows from the table "eetschema.expense_eetlijst_import". All fields are combined with a logical 'AND'."""

    and_: Optional[list["eetschema_expense_eetlijst_import_bool_exp"]] = Field(
        alias="_and", default=None
    )
    not_: Optional["eetschema_expense_eetlijst_import_bool_exp"] = Field(
        alias="_not", default=None
    )
    or_: Optional[list["eetschema_expense_eetlijst_import_bool_exp"]] = Field(
        alias="_or", default=None
    )
    group: Optional["eetschema_group_bool_exp"] = None
    group_id: Optional["uuid_comparison_exp"] = None
    payed_amount: Optional["Int_comparison_exp"] = None


class eetschema_expense_eetlijst_import_order_by(BaseModel):
    """Ordering options when selecting data from "eetschema.expense_eetlijst_import"."""

    group: Optional["eetschema_group_order_by"] = None
    group_id: Optional[order_by] = None
    payed_amount: Optional[order_by] = None


class eetschema_expense_eetlijst_import_stream_cursor_input(BaseModel):
    '''Streaming cursor of the table "eetschema_expense_eetlijst_import"'''

    initial_value: "eetschema_expense_eetlijst_import_stream_cursor_value_input"
    "Stream column input with initial value"
    ordering: Optional[cursor_ordering] = None
    "cursor ordering"


class eetschema_expense_eetlijst_import_stream_cursor_value_input(BaseModel):
    """Initial value of the column from where the streaming should start"""

    group_id: Optional[str] = None
    payed_amount: Optional[int] = None


class eetschema_expense_inc_input(BaseModel):
    '''input type for incrementing numeric columns in table "eetschema.expense"'''

    payed_amount: Optional[int] = None


class eetschema_expense_insert_input(BaseModel):
    '''input type for inserting data into table "eetschema.expense"'''

    deleted: Optional[bool] = None
    description: Optional[str] = None
    event_id: Optional[str] = None
    expense_distributions: Optional[
        "eetschema_expense_distribution_arr_rel_insert_input"
    ] = None
    group: Optional["eetschema_group_obj_rel_insert_input"] = None
    group_id: Optional[str] = None
    linked_event: Optional["eetschema_event_obj_rel_insert_input"] = None
    payed_amount: Optional[int] = None
    payed_at: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = None
    payed_by: Optional[str] = None
    settlement: Optional["eetschema_settlements_obj_rel_insert_input"] = None
    settlement_expense_id: Optional[str] = None
    updated_by: Optional[str] = None


class eetschema_expense_max_order_by(BaseModel):
    '''order by max() on columns of table "eetschema.expense"'''

    created_at: Optional[order_by] = None
    description: Optional[order_by] = None
    event_id: Optional[order_by] = None
    group_id: Optional[order_by] = None
    id: Optional[order_by] = None
    issued_by: Optional[order_by] = None
    payed_amount: Optional[order_by] = None
    payed_at: Optional[order_by] = None
    payed_by: Optional[order_by] = None
    settled_id: Optional[order_by] = None
    settlement_expense_id: Optional[order_by] = None
    updated_at: Optional[order_by] = None
    updated_by: Optional[order_by] = None


class eetschema_expense_min_order_by(BaseModel):
    '''order by min() on columns of table "eetschema.expense"'''

    created_at: Optional[order_by] = None
    description: Optional[order_by] = None
    event_id: Optional[order_by] = None
    group_id: Optional[order_by] = None
    id: Optional[order_by] = None
    issued_by: Optional[order_by] = None
    payed_amount: Optional[order_by] = None
    payed_at: Optional[order_by] = None
    payed_by: Optional[order_by] = None
    settled_id: Optional[order_by] = None
    settlement_expense_id: Optional[order_by] = None
    updated_at: Optional[order_by] = None
    updated_by: Optional[order_by] = None


class eetschema_expense_obj_rel_insert_input(BaseModel):
    '''input type for inserting object relation for remote table "eetschema.expense"'''

    data: "eetschema_expense_insert_input"
    on_conflict: Optional["eetschema_expense_on_conflict"] = None
    "upsert condition"


class eetschema_expense_on_conflict(BaseModel):
    '''on_conflict condition type for table "eetschema.expense"'''

    constraint: eetschema_expense_constraint
    update_columns: list[eetschema_expense_update_column] = Field(
        default_factory=lambda: []
    )
    where: Optional["eetschema_expense_bool_exp"] = None


class eetschema_expense_order_by(BaseModel):
    """Ordering options when selecting data from "eetschema.expense"."""

    created_at: Optional[order_by] = None
    deleted: Optional[order_by] = None
    description: Optional[order_by] = None
    event_id: Optional[order_by] = None
    expense_distributions_aggregate: Optional[
        "eetschema_expense_distribution_aggregate_order_by"
    ] = None
    group: Optional["eetschema_group_order_by"] = None
    group_id: Optional[order_by] = None
    id: Optional[order_by] = None
    issued_by: Optional[order_by] = None
    linked_event: Optional["eetschema_event_order_by"] = None
    payed_amount: Optional[order_by] = None
    payed_at: Optional[order_by] = None
    payed_by: Optional[order_by] = None
    payed_by_user: Optional["eetschema_user_order_by"] = None
    settled_id: Optional[order_by] = None
    settlement: Optional["eetschema_settlements_order_by"] = None
    settlement_expense_id: Optional[order_by] = None
    updated_by_user: Optional["eetschema_user_order_by"] = Field(
        alias="updatedByUser", default=None
    )
    updated_at: Optional[order_by] = None
    updated_by: Optional[order_by] = None
    user: Optional["eetschema_user_order_by"] = None


class eetschema_expense_pk_columns_input(BaseModel):
    """primary key columns input for table: eetschema.expense"""

    id: str


class eetschema_expense_set_input(BaseModel):
    '''input type for updating data in table "eetschema.expense"'''

    deleted: Optional[bool] = None
    description: Optional[str] = None
    issued_by: Optional[str] = None
    payed_amount: Optional[int] = None
    payed_at: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = None
    payed_by: Optional[str] = None
    settled_id: Optional[str] = None
    settlement_expense_id: Optional[str] = None
    updated_by: Optional[str] = None


class eetschema_expense_stddev_order_by(BaseModel):
    '''order by stddev() on columns of table "eetschema.expense"'''

    payed_amount: Optional[order_by] = None


class eetschema_expense_stddev_pop_order_by(BaseModel):
    '''order by stddev_pop() on columns of table "eetschema.expense"'''

    payed_amount: Optional[order_by] = None


class eetschema_expense_stddev_samp_order_by(BaseModel):
    '''order by stddev_samp() on columns of table "eetschema.expense"'''

    payed_amount: Optional[order_by] = None


class eetschema_expense_stream_cursor_input(BaseModel):
    '''Streaming cursor of the table "eetschema_expense"'''

    initial_value: "eetschema_expense_stream_cursor_value_input"
    "Stream column input with initial value"
    ordering: Optional[cursor_ordering] = None
    "cursor ordering"


class eetschema_expense_stream_cursor_value_input(BaseModel):
    """Initial value of the column from where the streaming should start"""

    created_at: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = (
        None
    )
    deleted: Optional[bool] = None
    description: Optional[str] = None
    event_id: Optional[str] = None
    group_id: Optional[str] = None
    id: Optional[str] = None
    issued_by: Optional[str] = None
    payed_amount: Optional[int] = None
    payed_at: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = None
    payed_by: Optional[str] = None
    settled_id: Optional[str] = None
    settlement_expense_id: Optional[str] = None
    updated_at: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = (
        None
    )
    updated_by: Optional[str] = None


class eetschema_expense_sum_order_by(BaseModel):
    '''order by sum() on columns of table "eetschema.expense"'''

    payed_amount: Optional[order_by] = None


class eetschema_expense_updates(BaseModel):
    inc: Optional["eetschema_expense_inc_input"] = Field(alias="_inc", default=None)
    "increments the numeric columns with given value of the filtered values"
    set_: Optional["eetschema_expense_set_input"] = Field(alias="_set", default=None)
    "sets the columns of the filtered rows to the given values"
    where: "eetschema_expense_bool_exp"
    "filter the rows which have to be updated"


class eetschema_expense_var_pop_order_by(BaseModel):
    '''order by var_pop() on columns of table "eetschema.expense"'''

    payed_amount: Optional[order_by] = None


class eetschema_expense_var_samp_order_by(BaseModel):
    '''order by var_samp() on columns of table "eetschema.expense"'''

    payed_amount: Optional[order_by] = None


class eetschema_expense_variance_order_by(BaseModel):
    '''order by variance() on columns of table "eetschema.expense"'''

    payed_amount: Optional[order_by] = None


class eetschema_group_aggregate_order_by(BaseModel):
    '''order by aggregate values of table "eetschema.group"'''

    avg: Optional["eetschema_group_avg_order_by"] = None
    count: Optional[order_by] = None
    max: Optional["eetschema_group_max_order_by"] = None
    min: Optional["eetschema_group_min_order_by"] = None
    stddev: Optional["eetschema_group_stddev_order_by"] = None
    stddev_pop: Optional["eetschema_group_stddev_pop_order_by"] = None
    stddev_samp: Optional["eetschema_group_stddev_samp_order_by"] = None
    sum: Optional["eetschema_group_sum_order_by"] = None
    var_pop: Optional["eetschema_group_var_pop_order_by"] = None
    var_samp: Optional["eetschema_group_var_samp_order_by"] = None
    variance: Optional["eetschema_group_variance_order_by"] = None


class eetschema_group_avg_order_by(BaseModel):
    '''order by avg() on columns of table "eetschema.group"'''

    pincode: Optional[order_by] = None


class eetschema_group_bool_exp(BaseModel):
    """Boolean expression to filter rows from the table "eetschema.group". All fields are combined with a logical 'AND'."""

    and_: Optional[list["eetschema_group_bool_exp"]] = Field(alias="_and", default=None)
    not_: Optional["eetschema_group_bool_exp"] = Field(alias="_not", default=None)
    or_: Optional[list["eetschema_group_bool_exp"]] = Field(alias="_or", default=None)
    active: Optional["Boolean_comparison_exp"] = None
    address: Optional["String_comparison_exp"] = None
    beta: Optional["Boolean_comparison_exp"] = None
    city: Optional["String_comparison_exp"] = None
    created_at: Optional["timestamptz_comparison_exp"] = None
    created_at_eetlijst: Optional["timestamptz_comparison_exp"] = None
    default_close_time: Optional["timestamptz_comparison_exp"] = None
    default_status: Optional["uuid_comparison_exp"] = None
    description: Optional["String_comparison_exp"] = None
    email: Optional["String_comparison_exp"] = None
    events: Optional["eetschema_event_bool_exp"] = None
    events_aggregate: Optional["eetschema_event_aggregate_bool_exp"] = None
    expense_eetlijst_import: Optional["eetschema_expense_eetlijst_import_bool_exp"] = (
        None
    )
    expenses: Optional["eetschema_expense_bool_exp"] = None
    expenses_aggregate: Optional["eetschema_expense_aggregate_bool_exp"] = None
    id: Optional["uuid_comparison_exp"] = None
    invite_open: Optional["Boolean_comparison_exp"] = None
    invite_uuid: Optional["uuid_comparison_exp"] = None
    lists: Optional["eetschema_list_bool_exp"] = None
    login_name: Optional["String_comparison_exp"] = None
    name: Optional["String_comparison_exp"] = None
    pincode: Optional["Int_comparison_exp"] = None
    statistics_end_date: Optional["timestamptz_comparison_exp"] = None
    statistics_start_date: Optional["timestamptz_comparison_exp"] = None
    summary: Optional["eetschema_group_summary_bool_exp"] = None
    updated_at: Optional["timestamptz_comparison_exp"] = None
    users_in_groups: Optional["eetschema_users_in_group_bool_exp"] = None


class eetschema_group_insert_input(BaseModel):
    '''input type for inserting data into table "eetschema.group"'''

    description: Optional[str] = None
    email: Optional[str] = None
    events: Optional["eetschema_event_arr_rel_insert_input"] = None
    expenses: Optional["eetschema_expense_arr_rel_insert_input"] = None
    lists: Optional["eetschema_list_arr_rel_insert_input"] = None
    name: Optional[str] = None
    statistics_end_date: Optional[
        Annotated[datetime, PlainSerializer(serialize_datetime)]
    ] = None
    statistics_start_date: Optional[
        Annotated[datetime, PlainSerializer(serialize_datetime)]
    ] = None
    users_in_groups: Optional["eetschema_users_in_group_arr_rel_insert_input"] = None


class eetschema_group_invite_bool_exp(BaseModel):
    """Boolean expression to filter rows from the table "eetschema.group_invite". All fields are combined with a logical 'AND'."""

    and_: Optional[list["eetschema_group_invite_bool_exp"]] = Field(
        alias="_and", default=None
    )
    not_: Optional["eetschema_group_invite_bool_exp"] = Field(
        alias="_not", default=None
    )
    or_: Optional[list["eetschema_group_invite_bool_exp"]] = Field(
        alias="_or", default=None
    )
    id: Optional["uuid_comparison_exp"] = None
    invite_uuid: Optional["uuid_comparison_exp"] = None


class eetschema_group_invite_order_by(BaseModel):
    """Ordering options when selecting data from "eetschema.group_invite"."""

    id: Optional[order_by] = None
    invite_uuid: Optional[order_by] = None


class eetschema_group_invite_stream_cursor_input(BaseModel):
    '''Streaming cursor of the table "eetschema_group_invite"'''

    initial_value: "eetschema_group_invite_stream_cursor_value_input"
    "Stream column input with initial value"
    ordering: Optional[cursor_ordering] = None
    "cursor ordering"


class eetschema_group_invite_stream_cursor_value_input(BaseModel):
    """Initial value of the column from where the streaming should start"""

    id: Optional[str] = None
    invite_uuid: Optional[str] = None


class eetschema_group_max_order_by(BaseModel):
    '''order by max() on columns of table "eetschema.group"'''

    address: Optional[order_by] = None
    city: Optional[order_by] = None
    created_at: Optional[order_by] = None
    created_at_eetlijst: Optional[order_by] = None
    default_close_time: Optional[order_by] = None
    default_status: Optional[order_by] = None
    description: Optional[order_by] = None
    email: Optional[order_by] = None
    id: Optional[order_by] = None
    invite_uuid: Optional[order_by] = None
    login_name: Optional[order_by] = None
    name: Optional[order_by] = None
    pincode: Optional[order_by] = None
    statistics_end_date: Optional[order_by] = None
    statistics_start_date: Optional[order_by] = None
    updated_at: Optional[order_by] = None


class eetschema_group_min_order_by(BaseModel):
    '''order by min() on columns of table "eetschema.group"'''

    address: Optional[order_by] = None
    city: Optional[order_by] = None
    created_at: Optional[order_by] = None
    created_at_eetlijst: Optional[order_by] = None
    default_close_time: Optional[order_by] = None
    default_status: Optional[order_by] = None
    description: Optional[order_by] = None
    email: Optional[order_by] = None
    id: Optional[order_by] = None
    invite_uuid: Optional[order_by] = None
    login_name: Optional[order_by] = None
    name: Optional[order_by] = None
    pincode: Optional[order_by] = None
    statistics_end_date: Optional[order_by] = None
    statistics_start_date: Optional[order_by] = None
    updated_at: Optional[order_by] = None


class eetschema_group_obj_rel_insert_input(BaseModel):
    '''input type for inserting object relation for remote table "eetschema.group"'''

    data: "eetschema_group_insert_input"
    on_conflict: Optional["eetschema_group_on_conflict"] = None
    "upsert condition"


class eetschema_group_on_conflict(BaseModel):
    '''on_conflict condition type for table "eetschema.group"'''

    constraint: eetschema_group_constraint
    update_columns: list[eetschema_group_update_column] = Field(
        default_factory=lambda: []
    )
    where: Optional["eetschema_group_bool_exp"] = None


class eetschema_group_order_by(BaseModel):
    """Ordering options when selecting data from "eetschema.group"."""

    active: Optional[order_by] = None
    address: Optional[order_by] = None
    beta: Optional[order_by] = None
    city: Optional[order_by] = None
    created_at: Optional[order_by] = None
    created_at_eetlijst: Optional[order_by] = None
    default_close_time: Optional[order_by] = None
    default_status: Optional[order_by] = None
    description: Optional[order_by] = None
    email: Optional[order_by] = None
    events_aggregate: Optional["eetschema_event_aggregate_order_by"] = None
    expense_eetlijst_import: Optional["eetschema_expense_eetlijst_import_order_by"] = (
        None
    )
    expenses_aggregate: Optional["eetschema_expense_aggregate_order_by"] = None
    id: Optional[order_by] = None
    invite_open: Optional[order_by] = None
    invite_uuid: Optional[order_by] = None
    lists_aggregate: Optional["eetschema_list_aggregate_order_by"] = None
    login_name: Optional[order_by] = None
    name: Optional[order_by] = None
    pincode: Optional[order_by] = None
    statistics_end_date: Optional[order_by] = None
    statistics_start_date: Optional[order_by] = None
    summary_aggregate: Optional["eetschema_group_summary_aggregate_order_by"] = None
    updated_at: Optional[order_by] = None
    users_in_groups_aggregate: Optional[
        "eetschema_users_in_group_aggregate_order_by"
    ] = None


class eetschema_group_pk_columns_input(BaseModel):
    """primary key columns input for table: eetschema.group"""

    id: str


class eetschema_group_set_input(BaseModel):
    '''input type for updating data in table "eetschema.group"'''

    beta: Optional[bool] = None
    default_close_time: Optional[
        Annotated[datetime, PlainSerializer(serialize_datetime)]
    ] = None
    description: Optional[str] = None
    invite_uuid: Optional[str] = None
    name: Optional[str] = None
    statistics_end_date: Optional[
        Annotated[datetime, PlainSerializer(serialize_datetime)]
    ] = None
    statistics_start_date: Optional[
        Annotated[datetime, PlainSerializer(serialize_datetime)]
    ] = None


class eetschema_group_statistics_2_aggregate_order_by(BaseModel):
    '''order by aggregate values of table "eetschema.group_statistics_2"'''

    avg: Optional["eetschema_group_statistics_2_avg_order_by"] = None
    count: Optional[order_by] = None
    max: Optional["eetschema_group_statistics_2_max_order_by"] = None
    min: Optional["eetschema_group_statistics_2_min_order_by"] = None
    stddev: Optional["eetschema_group_statistics_2_stddev_order_by"] = None
    stddev_pop: Optional["eetschema_group_statistics_2_stddev_pop_order_by"] = None
    stddev_samp: Optional["eetschema_group_statistics_2_stddev_samp_order_by"] = None
    sum: Optional["eetschema_group_statistics_2_sum_order_by"] = None
    var_pop: Optional["eetschema_group_statistics_2_var_pop_order_by"] = None
    var_samp: Optional["eetschema_group_statistics_2_var_samp_order_by"] = None
    variance: Optional["eetschema_group_statistics_2_variance_order_by"] = None


class eetschema_group_statistics_2_avg_order_by(BaseModel):
    '''order by avg() on columns of table "eetschema.group_statistics_2"'''

    cook_points: Optional[order_by] = None
    minus_points: Optional[order_by] = None
    num_cooked: Optional[order_by] = None
    num_eat: Optional[order_by] = None
    num_groceries: Optional[order_by] = None
    num_not_attended: Optional[order_by] = None
    number_guests: Optional[order_by] = None


class eetschema_group_statistics_2_bool_exp(BaseModel):
    """Boolean expression to filter rows from the table "eetschema.group_statistics_2". All fields are combined with a logical 'AND'."""

    and_: Optional[list["eetschema_group_statistics_2_bool_exp"]] = Field(
        alias="_and", default=None
    )
    not_: Optional["eetschema_group_statistics_2_bool_exp"] = Field(
        alias="_not", default=None
    )
    or_: Optional[list["eetschema_group_statistics_2_bool_exp"]] = Field(
        alias="_or", default=None
    )
    cook_points: Optional["Float_comparison_exp"] = None
    group: Optional["eetschema_group_bool_exp"] = None
    group_id: Optional["uuid_comparison_exp"] = None
    minus_points: Optional["bigint_comparison_exp"] = None
    num_cooked: Optional["numeric_comparison_exp"] = None
    num_eat: Optional["numeric_comparison_exp"] = None
    num_groceries: Optional["numeric_comparison_exp"] = None
    num_not_attended: Optional["numeric_comparison_exp"] = None
    number_guests: Optional["bigint_comparison_exp"] = None
    user: Optional["eetschema_user_bool_exp"] = None
    user_id: Optional["String_comparison_exp"] = None


class eetschema_group_statistics_2_max_order_by(BaseModel):
    '''order by max() on columns of table "eetschema.group_statistics_2"'''

    cook_points: Optional[order_by] = None
    group_id: Optional[order_by] = None
    minus_points: Optional[order_by] = None
    num_cooked: Optional[order_by] = None
    num_eat: Optional[order_by] = None
    num_groceries: Optional[order_by] = None
    num_not_attended: Optional[order_by] = None
    number_guests: Optional[order_by] = None
    user_id: Optional[order_by] = None


class eetschema_group_statistics_2_min_order_by(BaseModel):
    '''order by min() on columns of table "eetschema.group_statistics_2"'''

    cook_points: Optional[order_by] = None
    group_id: Optional[order_by] = None
    minus_points: Optional[order_by] = None
    num_cooked: Optional[order_by] = None
    num_eat: Optional[order_by] = None
    num_groceries: Optional[order_by] = None
    num_not_attended: Optional[order_by] = None
    number_guests: Optional[order_by] = None
    user_id: Optional[order_by] = None


class eetschema_group_statistics_2_order_by(BaseModel):
    """Ordering options when selecting data from "eetschema.group_statistics_2"."""

    cook_points: Optional[order_by] = None
    group: Optional["eetschema_group_order_by"] = None
    group_id: Optional[order_by] = None
    minus_points: Optional[order_by] = None
    num_cooked: Optional[order_by] = None
    num_eat: Optional[order_by] = None
    num_groceries: Optional[order_by] = None
    num_not_attended: Optional[order_by] = None
    number_guests: Optional[order_by] = None
    user: Optional["eetschema_user_order_by"] = None
    user_id: Optional[order_by] = None


class eetschema_group_statistics_2_stddev_order_by(BaseModel):
    '''order by stddev() on columns of table "eetschema.group_statistics_2"'''

    cook_points: Optional[order_by] = None
    minus_points: Optional[order_by] = None
    num_cooked: Optional[order_by] = None
    num_eat: Optional[order_by] = None
    num_groceries: Optional[order_by] = None
    num_not_attended: Optional[order_by] = None
    number_guests: Optional[order_by] = None


class eetschema_group_statistics_2_stddev_pop_order_by(BaseModel):
    '''order by stddev_pop() on columns of table "eetschema.group_statistics_2"'''

    cook_points: Optional[order_by] = None
    minus_points: Optional[order_by] = None
    num_cooked: Optional[order_by] = None
    num_eat: Optional[order_by] = None
    num_groceries: Optional[order_by] = None
    num_not_attended: Optional[order_by] = None
    number_guests: Optional[order_by] = None


class eetschema_group_statistics_2_stddev_samp_order_by(BaseModel):
    '''order by stddev_samp() on columns of table "eetschema.group_statistics_2"'''

    cook_points: Optional[order_by] = None
    minus_points: Optional[order_by] = None
    num_cooked: Optional[order_by] = None
    num_eat: Optional[order_by] = None
    num_groceries: Optional[order_by] = None
    num_not_attended: Optional[order_by] = None
    number_guests: Optional[order_by] = None


class eetschema_group_statistics_2_stream_cursor_input(BaseModel):
    '''Streaming cursor of the table "eetschema_group_statistics_2"'''

    initial_value: "eetschema_group_statistics_2_stream_cursor_value_input"
    "Stream column input with initial value"
    ordering: Optional[cursor_ordering] = None
    "cursor ordering"


class eetschema_group_statistics_2_stream_cursor_value_input(BaseModel):
    """Initial value of the column from where the streaming should start"""

    cook_points: Optional[float] = None
    group_id: Optional[str] = None
    minus_points: Optional[Any] = None
    num_cooked: Optional[Any] = None
    num_eat: Optional[Any] = None
    num_groceries: Optional[Any] = None
    num_not_attended: Optional[Any] = None
    number_guests: Optional[Any] = None
    user_id: Optional[str] = None


class eetschema_group_statistics_2_sum_order_by(BaseModel):
    '''order by sum() on columns of table "eetschema.group_statistics_2"'''

    cook_points: Optional[order_by] = None
    minus_points: Optional[order_by] = None
    num_cooked: Optional[order_by] = None
    num_eat: Optional[order_by] = None
    num_groceries: Optional[order_by] = None
    num_not_attended: Optional[order_by] = None
    number_guests: Optional[order_by] = None


class eetschema_group_statistics_2_var_pop_order_by(BaseModel):
    '''order by var_pop() on columns of table "eetschema.group_statistics_2"'''

    cook_points: Optional[order_by] = None
    minus_points: Optional[order_by] = None
    num_cooked: Optional[order_by] = None
    num_eat: Optional[order_by] = None
    num_groceries: Optional[order_by] = None
    num_not_attended: Optional[order_by] = None
    number_guests: Optional[order_by] = None


class eetschema_group_statistics_2_var_samp_order_by(BaseModel):
    '''order by var_samp() on columns of table "eetschema.group_statistics_2"'''

    cook_points: Optional[order_by] = None
    minus_points: Optional[order_by] = None
    num_cooked: Optional[order_by] = None
    num_eat: Optional[order_by] = None
    num_groceries: Optional[order_by] = None
    num_not_attended: Optional[order_by] = None
    number_guests: Optional[order_by] = None


class eetschema_group_statistics_2_variance_order_by(BaseModel):
    '''order by variance() on columns of table "eetschema.group_statistics_2"'''

    cook_points: Optional[order_by] = None
    minus_points: Optional[order_by] = None
    num_cooked: Optional[order_by] = None
    num_eat: Optional[order_by] = None
    num_groceries: Optional[order_by] = None
    num_not_attended: Optional[order_by] = None
    number_guests: Optional[order_by] = None


class eetschema_group_statistics_bool_exp(BaseModel):
    """Boolean expression to filter rows from the table "eetschema.group_statistics". All fields are combined with a logical 'AND'."""

    and_: Optional[list["eetschema_group_statistics_bool_exp"]] = Field(
        alias="_and", default=None
    )
    not_: Optional["eetschema_group_statistics_bool_exp"] = Field(
        alias="_not", default=None
    )
    or_: Optional[list["eetschema_group_statistics_bool_exp"]] = Field(
        alias="_or", default=None
    )
    count: Optional["bigint_comparison_exp"] = None
    group_id: Optional["uuid_comparison_exp"] = None
    linked_group: Optional["eetschema_group_bool_exp"] = None
    number_guests: Optional["bigint_comparison_exp"] = None
    status: Optional["String_comparison_exp"] = None
    user: Optional["eetschema_user_bool_exp"] = None
    user_id: Optional["String_comparison_exp"] = None


class eetschema_group_statistics_order_by(BaseModel):
    """Ordering options when selecting data from "eetschema.group_statistics"."""

    count: Optional[order_by] = None
    group_id: Optional[order_by] = None
    linked_group: Optional["eetschema_group_order_by"] = None
    number_guests: Optional[order_by] = None
    status: Optional[order_by] = None
    user: Optional["eetschema_user_order_by"] = None
    user_id: Optional[order_by] = None


class eetschema_group_statistics_stream_cursor_input(BaseModel):
    '''Streaming cursor of the table "eetschema_group_statistics"'''

    initial_value: "eetschema_group_statistics_stream_cursor_value_input"
    "Stream column input with initial value"
    ordering: Optional[cursor_ordering] = None
    "cursor ordering"


class eetschema_group_statistics_stream_cursor_value_input(BaseModel):
    """Initial value of the column from where the streaming should start"""

    count: Optional[Any] = None
    group_id: Optional[str] = None
    number_guests: Optional[Any] = None
    status: Optional[str] = None
    user_id: Optional[str] = None


class eetschema_group_stddev_order_by(BaseModel):
    '''order by stddev() on columns of table "eetschema.group"'''

    pincode: Optional[order_by] = None


class eetschema_group_stddev_pop_order_by(BaseModel):
    '''order by stddev_pop() on columns of table "eetschema.group"'''

    pincode: Optional[order_by] = None


class eetschema_group_stddev_samp_order_by(BaseModel):
    '''order by stddev_samp() on columns of table "eetschema.group"'''

    pincode: Optional[order_by] = None


class eetschema_group_stream_cursor_input(BaseModel):
    '''Streaming cursor of the table "eetschema_group"'''

    initial_value: "eetschema_group_stream_cursor_value_input"
    "Stream column input with initial value"
    ordering: Optional[cursor_ordering] = None
    "cursor ordering"


class eetschema_group_stream_cursor_value_input(BaseModel):
    """Initial value of the column from where the streaming should start"""

    active: Optional[bool] = None
    address: Optional[str] = None
    beta: Optional[bool] = None
    city: Optional[str] = None
    created_at: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = (
        None
    )
    created_at_eetlijst: Optional[
        Annotated[datetime, PlainSerializer(serialize_datetime)]
    ] = None
    default_close_time: Optional[
        Annotated[datetime, PlainSerializer(serialize_datetime)]
    ] = None
    default_status: Optional[str] = None
    description: Optional[str] = None
    email: Optional[str] = None
    id: Optional[str] = None
    invite_open: Optional[bool] = None
    invite_uuid: Optional[str] = None
    login_name: Optional[str] = None
    name: Optional[str] = None
    pincode: Optional[int] = None
    statistics_end_date: Optional[
        Annotated[datetime, PlainSerializer(serialize_datetime)]
    ] = None
    statistics_start_date: Optional[
        Annotated[datetime, PlainSerializer(serialize_datetime)]
    ] = None
    updated_at: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = (
        None
    )


class eetschema_group_sum_order_by(BaseModel):
    '''order by sum() on columns of table "eetschema.group"'''

    pincode: Optional[order_by] = None


class eetschema_group_summary_aggregate_order_by(BaseModel):
    '''order by aggregate values of table "eetschema.group_summary"'''

    avg: Optional["eetschema_group_summary_avg_order_by"] = None
    count: Optional[order_by] = None
    max: Optional["eetschema_group_summary_max_order_by"] = None
    min: Optional["eetschema_group_summary_min_order_by"] = None
    stddev: Optional["eetschema_group_summary_stddev_order_by"] = None
    stddev_pop: Optional["eetschema_group_summary_stddev_pop_order_by"] = None
    stddev_samp: Optional["eetschema_group_summary_stddev_samp_order_by"] = None
    sum: Optional["eetschema_group_summary_sum_order_by"] = None
    var_pop: Optional["eetschema_group_summary_var_pop_order_by"] = None
    var_samp: Optional["eetschema_group_summary_var_samp_order_by"] = None
    variance: Optional["eetschema_group_summary_variance_order_by"] = None


class eetschema_group_summary_avg_order_by(BaseModel):
    '''order by avg() on columns of table "eetschema.group_summary"'''

    payed_total: Optional[order_by] = None


class eetschema_group_summary_bool_exp(BaseModel):
    """Boolean expression to filter rows from the table "eetschema.group_summary". All fields are combined with a logical 'AND'."""

    and_: Optional[list["eetschema_group_summary_bool_exp"]] = Field(
        alias="_and", default=None
    )
    not_: Optional["eetschema_group_summary_bool_exp"] = Field(
        alias="_not", default=None
    )
    or_: Optional[list["eetschema_group_summary_bool_exp"]] = Field(
        alias="_or", default=None
    )
    group: Optional["eetschema_group_bool_exp"] = None
    group_id: Optional["uuid_comparison_exp"] = None
    payed_total: Optional["bigint_comparison_exp"] = None
    user: Optional["eetschema_user_bool_exp"] = None
    user_id: Optional["String_comparison_exp"] = None


class eetschema_group_summary_max_order_by(BaseModel):
    '''order by max() on columns of table "eetschema.group_summary"'''

    group_id: Optional[order_by] = None
    payed_total: Optional[order_by] = None
    user_id: Optional[order_by] = None


class eetschema_group_summary_min_order_by(BaseModel):
    '''order by min() on columns of table "eetschema.group_summary"'''

    group_id: Optional[order_by] = None
    payed_total: Optional[order_by] = None
    user_id: Optional[order_by] = None


class eetschema_group_summary_order_by(BaseModel):
    """Ordering options when selecting data from "eetschema.group_summary"."""

    group: Optional["eetschema_group_order_by"] = None
    group_id: Optional[order_by] = None
    payed_total: Optional[order_by] = None
    user: Optional["eetschema_user_order_by"] = None
    user_id: Optional[order_by] = None


class eetschema_group_summary_stddev_order_by(BaseModel):
    '''order by stddev() on columns of table "eetschema.group_summary"'''

    payed_total: Optional[order_by] = None


class eetschema_group_summary_stddev_pop_order_by(BaseModel):
    '''order by stddev_pop() on columns of table "eetschema.group_summary"'''

    payed_total: Optional[order_by] = None


class eetschema_group_summary_stddev_samp_order_by(BaseModel):
    '''order by stddev_samp() on columns of table "eetschema.group_summary"'''

    payed_total: Optional[order_by] = None


class eetschema_group_summary_stream_cursor_input(BaseModel):
    '''Streaming cursor of the table "eetschema_group_summary"'''

    initial_value: "eetschema_group_summary_stream_cursor_value_input"
    "Stream column input with initial value"
    ordering: Optional[cursor_ordering] = None
    "cursor ordering"


class eetschema_group_summary_stream_cursor_value_input(BaseModel):
    """Initial value of the column from where the streaming should start"""

    group_id: Optional[str] = None
    payed_total: Optional[Any] = None
    user_id: Optional[str] = None


class eetschema_group_summary_sum_order_by(BaseModel):
    '''order by sum() on columns of table "eetschema.group_summary"'''

    payed_total: Optional[order_by] = None


class eetschema_group_summary_var_pop_order_by(BaseModel):
    '''order by var_pop() on columns of table "eetschema.group_summary"'''

    payed_total: Optional[order_by] = None


class eetschema_group_summary_var_samp_order_by(BaseModel):
    '''order by var_samp() on columns of table "eetschema.group_summary"'''

    payed_total: Optional[order_by] = None


class eetschema_group_summary_variance_order_by(BaseModel):
    '''order by variance() on columns of table "eetschema.group_summary"'''

    payed_total: Optional[order_by] = None


class eetschema_group_updates(BaseModel):
    set_: Optional["eetschema_group_set_input"] = Field(alias="_set", default=None)
    "sets the columns of the filtered rows to the given values"
    where: "eetschema_group_bool_exp"
    "filter the rows which have to be updated"


class eetschema_group_var_pop_order_by(BaseModel):
    '''order by var_pop() on columns of table "eetschema.group"'''

    pincode: Optional[order_by] = None


class eetschema_group_var_samp_order_by(BaseModel):
    '''order by var_samp() on columns of table "eetschema.group"'''

    pincode: Optional[order_by] = None


class eetschema_group_variance_order_by(BaseModel):
    '''order by variance() on columns of table "eetschema.group"'''

    pincode: Optional[order_by] = None


class eetschema_list_aggregate_order_by(BaseModel):
    '''order by aggregate values of table "eetschema.list"'''

    count: Optional[order_by] = None
    max: Optional["eetschema_list_max_order_by"] = None
    min: Optional["eetschema_list_min_order_by"] = None


class eetschema_list_arr_rel_insert_input(BaseModel):
    '''input type for inserting array relation for remote table "eetschema.list"'''

    data: list["eetschema_list_insert_input"]
    on_conflict: Optional["eetschema_list_on_conflict"] = None
    "upsert condition"


class eetschema_list_bool_exp(BaseModel):
    """Boolean expression to filter rows from the table "eetschema.list". All fields are combined with a logical 'AND'."""

    and_: Optional[list["eetschema_list_bool_exp"]] = Field(alias="_and", default=None)
    not_: Optional["eetschema_list_bool_exp"] = Field(alias="_not", default=None)
    or_: Optional[list["eetschema_list_bool_exp"]] = Field(alias="_or", default=None)
    active: Optional["Boolean_comparison_exp"] = None
    checked: Optional["Boolean_comparison_exp"] = None
    created_at: Optional["timestamptz_comparison_exp"] = None
    group_id: Optional["uuid_comparison_exp"] = None
    id: Optional["uuid_comparison_exp"] = None
    linked_group: Optional["eetschema_group_bool_exp"] = None
    recipe_id: Optional["uuid_comparison_exp"] = None
    text: Optional["String_comparison_exp"] = None
    updated_at: Optional["timestamptz_comparison_exp"] = None


class eetschema_list_insert_input(BaseModel):
    '''input type for inserting data into table "eetschema.list"'''

    active: Optional[bool] = None
    checked: Optional[bool] = None
    group_id: Optional[str] = None
    linked_group: Optional["eetschema_group_obj_rel_insert_input"] = None
    recipe_id: Optional[str] = None
    text: Optional[str] = None


class eetschema_list_max_order_by(BaseModel):
    '''order by max() on columns of table "eetschema.list"'''

    created_at: Optional[order_by] = None
    group_id: Optional[order_by] = None
    id: Optional[order_by] = None
    recipe_id: Optional[order_by] = None
    text: Optional[order_by] = None
    updated_at: Optional[order_by] = None


class eetschema_list_min_order_by(BaseModel):
    '''order by min() on columns of table "eetschema.list"'''

    created_at: Optional[order_by] = None
    group_id: Optional[order_by] = None
    id: Optional[order_by] = None
    recipe_id: Optional[order_by] = None
    text: Optional[order_by] = None
    updated_at: Optional[order_by] = None


class eetschema_list_on_conflict(BaseModel):
    '''on_conflict condition type for table "eetschema.list"'''

    constraint: eetschema_list_constraint
    update_columns: list[eetschema_list_update_column] = Field(
        default_factory=lambda: []
    )
    where: Optional["eetschema_list_bool_exp"] = None


class eetschema_list_order_by(BaseModel):
    """Ordering options when selecting data from "eetschema.list"."""

    active: Optional[order_by] = None
    checked: Optional[order_by] = None
    created_at: Optional[order_by] = None
    group_id: Optional[order_by] = None
    id: Optional[order_by] = None
    linked_group: Optional["eetschema_group_order_by"] = None
    recipe_id: Optional[order_by] = None
    text: Optional[order_by] = None
    updated_at: Optional[order_by] = None


class eetschema_list_pk_columns_input(BaseModel):
    """primary key columns input for table: eetschema.list"""

    id: str


class eetschema_list_set_input(BaseModel):
    '''input type for updating data in table "eetschema.list"'''

    active: Optional[bool] = None
    checked: Optional[bool] = None
    group_id: Optional[str] = None
    recipe_id: Optional[str] = None
    text: Optional[str] = None


class eetschema_list_stream_cursor_input(BaseModel):
    '''Streaming cursor of the table "eetschema_list"'''

    initial_value: "eetschema_list_stream_cursor_value_input"
    "Stream column input with initial value"
    ordering: Optional[cursor_ordering] = None
    "cursor ordering"


class eetschema_list_stream_cursor_value_input(BaseModel):
    """Initial value of the column from where the streaming should start"""

    active: Optional[bool] = None
    checked: Optional[bool] = None
    created_at: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = (
        None
    )
    group_id: Optional[str] = None
    id: Optional[str] = None
    recipe_id: Optional[str] = None
    text: Optional[str] = None
    updated_at: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = (
        None
    )


class eetschema_list_updates(BaseModel):
    set_: Optional["eetschema_list_set_input"] = Field(alias="_set", default=None)
    "sets the columns of the filtered rows to the given values"
    where: "eetschema_list_bool_exp"
    "filter the rows which have to be updated"


class eetschema_notification_aggregate_order_by(BaseModel):
    '''order by aggregate values of table "eetschema.notification"'''

    count: Optional[order_by] = None
    max: Optional["eetschema_notification_max_order_by"] = None
    min: Optional["eetschema_notification_min_order_by"] = None


class eetschema_notification_bool_exp(BaseModel):
    """Boolean expression to filter rows from the table "eetschema.notification". All fields are combined with a logical 'AND'."""

    timestamp: Optional["timestamptz_comparison_exp"] = Field(
        alias="Timestamp", default=None
    )
    and_: Optional[list["eetschema_notification_bool_exp"]] = Field(
        alias="_and", default=None
    )
    not_: Optional["eetschema_notification_bool_exp"] = Field(
        alias="_not", default=None
    )
    or_: Optional[list["eetschema_notification_bool_exp"]] = Field(
        alias="_or", default=None
    )
    body: Optional["String_comparison_exp"] = None
    created_at: Optional["timestamptz_comparison_exp"] = None
    device: Optional["String_comparison_exp"] = None
    device_token: Optional["String_comparison_exp"] = None
    id: Optional["uuid_comparison_exp"] = None
    platform: Optional["String_comparison_exp"] = None
    title: Optional["String_comparison_exp"] = None
    updated_at: Optional["timestamptz_comparison_exp"] = None
    user: Optional["eetschema_user_bool_exp"] = None
    user_id: Optional["String_comparison_exp"] = None
    wants_to_recieve: Optional["Boolean_comparison_exp"] = None


class eetschema_notification_insert_input(BaseModel):
    '''input type for inserting data into table "eetschema.notification"'''

    timestamp: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = (
        Field(alias="Timestamp", default=None)
    )
    body: Optional[str] = None
    device: Optional[str] = None
    device_token: Optional[str] = None
    id: Optional[str] = None
    platform: Optional[str] = None
    title: Optional[str] = None
    wants_to_recieve: Optional[bool] = None


class eetschema_notification_logs_aggregate_order_by(BaseModel):
    '''order by aggregate values of table "eetschema.notification_logs"'''

    count: Optional[order_by] = None
    max: Optional["eetschema_notification_logs_max_order_by"] = None
    min: Optional["eetschema_notification_logs_min_order_by"] = None


class eetschema_notification_logs_bool_exp(BaseModel):
    """Boolean expression to filter rows from the table "eetschema.notification_logs". All fields are combined with a logical 'AND'."""

    and_: Optional[list["eetschema_notification_logs_bool_exp"]] = Field(
        alias="_and", default=None
    )
    not_: Optional["eetschema_notification_logs_bool_exp"] = Field(
        alias="_not", default=None
    )
    or_: Optional[list["eetschema_notification_logs_bool_exp"]] = Field(
        alias="_or", default=None
    )
    body: Optional["String_comparison_exp"] = None
    created_at: Optional["timestamptz_comparison_exp"] = None
    data: Optional["json_comparison_exp"] = None
    device_token: Optional["String_comparison_exp"] = None
    id: Optional["uuid_comparison_exp"] = None
    opened_by_user: Optional["Boolean_comparison_exp"] = None
    send_by: Optional["String_comparison_exp"] = None
    title: Optional["String_comparison_exp"] = None
    updated_at: Optional["timestamptz_comparison_exp"] = None
    user: Optional["eetschema_user_bool_exp"] = None
    user_id: Optional["String_comparison_exp"] = None


class eetschema_notification_logs_max_order_by(BaseModel):
    '''order by max() on columns of table "eetschema.notification_logs"'''

    body: Optional[order_by] = None
    created_at: Optional[order_by] = None
    device_token: Optional[order_by] = None
    id: Optional[order_by] = None
    send_by: Optional[order_by] = None
    title: Optional[order_by] = None
    updated_at: Optional[order_by] = None
    user_id: Optional[order_by] = None


class eetschema_notification_logs_min_order_by(BaseModel):
    '''order by min() on columns of table "eetschema.notification_logs"'''

    body: Optional[order_by] = None
    created_at: Optional[order_by] = None
    device_token: Optional[order_by] = None
    id: Optional[order_by] = None
    send_by: Optional[order_by] = None
    title: Optional[order_by] = None
    updated_at: Optional[order_by] = None
    user_id: Optional[order_by] = None


class eetschema_notification_logs_order_by(BaseModel):
    """Ordering options when selecting data from "eetschema.notification_logs"."""

    body: Optional[order_by] = None
    created_at: Optional[order_by] = None
    data: Optional[order_by] = None
    device_token: Optional[order_by] = None
    id: Optional[order_by] = None
    opened_by_user: Optional[order_by] = None
    send_by: Optional[order_by] = None
    title: Optional[order_by] = None
    updated_at: Optional[order_by] = None
    user: Optional["eetschema_user_order_by"] = None
    user_id: Optional[order_by] = None


class eetschema_notification_logs_pk_columns_input(BaseModel):
    """primary key columns input for table: eetschema.notification_logs"""

    id: str


class eetschema_notification_logs_set_input(BaseModel):
    '''input type for updating data in table "eetschema.notification_logs"'''

    opened_by_user: Optional[bool] = None


class eetschema_notification_logs_stream_cursor_input(BaseModel):
    '''Streaming cursor of the table "eetschema_notification_logs"'''

    initial_value: "eetschema_notification_logs_stream_cursor_value_input"
    "Stream column input with initial value"
    ordering: Optional[cursor_ordering] = None
    "cursor ordering"


class eetschema_notification_logs_stream_cursor_value_input(BaseModel):
    """Initial value of the column from where the streaming should start"""

    body: Optional[str] = None
    created_at: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = (
        None
    )
    data: Optional[Any] = None
    device_token: Optional[str] = None
    id: Optional[str] = None
    opened_by_user: Optional[bool] = None
    send_by: Optional[str] = None
    title: Optional[str] = None
    updated_at: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = (
        None
    )
    user_id: Optional[str] = None


class eetschema_notification_logs_updates(BaseModel):
    set_: Optional["eetschema_notification_logs_set_input"] = Field(
        alias="_set", default=None
    )
    "sets the columns of the filtered rows to the given values"
    where: "eetschema_notification_logs_bool_exp"
    "filter the rows which have to be updated"


class eetschema_notification_max_order_by(BaseModel):
    '''order by max() on columns of table "eetschema.notification"'''

    timestamp: Optional[order_by] = Field(alias="Timestamp", default=None)
    body: Optional[order_by] = None
    created_at: Optional[order_by] = None
    device: Optional[order_by] = None
    device_token: Optional[order_by] = None
    id: Optional[order_by] = None
    platform: Optional[order_by] = None
    title: Optional[order_by] = None
    updated_at: Optional[order_by] = None
    user_id: Optional[order_by] = None


class eetschema_notification_min_order_by(BaseModel):
    '''order by min() on columns of table "eetschema.notification"'''

    timestamp: Optional[order_by] = Field(alias="Timestamp", default=None)
    body: Optional[order_by] = None
    created_at: Optional[order_by] = None
    device: Optional[order_by] = None
    device_token: Optional[order_by] = None
    id: Optional[order_by] = None
    platform: Optional[order_by] = None
    title: Optional[order_by] = None
    updated_at: Optional[order_by] = None
    user_id: Optional[order_by] = None


class eetschema_notification_on_conflict(BaseModel):
    '''on_conflict condition type for table "eetschema.notification"'''

    constraint: eetschema_notification_constraint
    update_columns: list[eetschema_notification_update_column] = Field(
        default_factory=lambda: []
    )
    where: Optional["eetschema_notification_bool_exp"] = None


class eetschema_notification_order_by(BaseModel):
    """Ordering options when selecting data from "eetschema.notification"."""

    timestamp: Optional[order_by] = Field(alias="Timestamp", default=None)
    body: Optional[order_by] = None
    created_at: Optional[order_by] = None
    device: Optional[order_by] = None
    device_token: Optional[order_by] = None
    id: Optional[order_by] = None
    platform: Optional[order_by] = None
    title: Optional[order_by] = None
    updated_at: Optional[order_by] = None
    user: Optional["eetschema_user_order_by"] = None
    user_id: Optional[order_by] = None
    wants_to_recieve: Optional[order_by] = None


class eetschema_notification_pk_columns_input(BaseModel):
    """primary key columns input for table: eetschema.notification"""

    device_token: str


class eetschema_notification_set_input(BaseModel):
    '''input type for updating data in table "eetschema.notification"'''

    body: Optional[str] = None
    device: Optional[str] = None
    device_token: Optional[str] = None
    id: Optional[str] = None
    platform: Optional[str] = None
    title: Optional[str] = None
    wants_to_recieve: Optional[bool] = None


class eetschema_notification_stream_cursor_input(BaseModel):
    '''Streaming cursor of the table "eetschema_notification"'''

    initial_value: "eetschema_notification_stream_cursor_value_input"
    "Stream column input with initial value"
    ordering: Optional[cursor_ordering] = None
    "cursor ordering"


class eetschema_notification_stream_cursor_value_input(BaseModel):
    """Initial value of the column from where the streaming should start"""

    timestamp: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = (
        Field(alias="Timestamp", default=None)
    )
    body: Optional[str] = None
    created_at: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = (
        None
    )
    device: Optional[str] = None
    device_token: Optional[str] = None
    id: Optional[str] = None
    platform: Optional[str] = None
    title: Optional[str] = None
    updated_at: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = (
        None
    )
    user_id: Optional[str] = None
    wants_to_recieve: Optional[bool] = None


class eetschema_notification_updates(BaseModel):
    set_: Optional["eetschema_notification_set_input"] = Field(
        alias="_set", default=None
    )
    "sets the columns of the filtered rows to the given values"
    where: "eetschema_notification_bool_exp"
    "filter the rows which have to be updated"


class eetschema_settlements_aggregate_order_by(BaseModel):
    '''order by aggregate values of table "eetschema.settlements"'''

    count: Optional[order_by] = None
    max: Optional["eetschema_settlements_max_order_by"] = None
    min: Optional["eetschema_settlements_min_order_by"] = None


class eetschema_settlements_bool_exp(BaseModel):
    """Boolean expression to filter rows from the table "eetschema.settlements". All fields are combined with a logical 'AND'."""

    and_: Optional[list["eetschema_settlements_bool_exp"]] = Field(
        alias="_and", default=None
    )
    not_: Optional["eetschema_settlements_bool_exp"] = Field(alias="_not", default=None)
    or_: Optional[list["eetschema_settlements_bool_exp"]] = Field(
        alias="_or", default=None
    )
    created_at: Optional["timestamptz_comparison_exp"] = None
    created_by: Optional["String_comparison_exp"] = None
    expenses: Optional["eetschema_expense_bool_exp"] = None
    expenses_aggregate: Optional["eetschema_expense_aggregate_bool_exp"] = None
    group: Optional["eetschema_group_bool_exp"] = None
    group_id: Optional["uuid_comparison_exp"] = None
    id: Optional["uuid_comparison_exp"] = None
    updated_at: Optional["timestamptz_comparison_exp"] = None
    user: Optional["eetschema_user_bool_exp"] = None


class eetschema_settlements_insert_input(BaseModel):
    '''input type for inserting data into table "eetschema.settlements"'''

    expenses: Optional["eetschema_expense_arr_rel_insert_input"] = None
    group: Optional["eetschema_group_obj_rel_insert_input"] = None
    group_id: Optional[str] = None


class eetschema_settlements_max_order_by(BaseModel):
    '''order by max() on columns of table "eetschema.settlements"'''

    created_at: Optional[order_by] = None
    created_by: Optional[order_by] = None
    group_id: Optional[order_by] = None
    id: Optional[order_by] = None
    updated_at: Optional[order_by] = None


class eetschema_settlements_min_order_by(BaseModel):
    '''order by min() on columns of table "eetschema.settlements"'''

    created_at: Optional[order_by] = None
    created_by: Optional[order_by] = None
    group_id: Optional[order_by] = None
    id: Optional[order_by] = None
    updated_at: Optional[order_by] = None


class eetschema_settlements_obj_rel_insert_input(BaseModel):
    '''input type for inserting object relation for remote table "eetschema.settlements"'''

    data: "eetschema_settlements_insert_input"
    on_conflict: Optional["eetschema_settlements_on_conflict"] = None
    "upsert condition"


class eetschema_settlements_on_conflict(BaseModel):
    '''on_conflict condition type for table "eetschema.settlements"'''

    constraint: eetschema_settlements_constraint
    update_columns: list[eetschema_settlements_update_column] = Field(
        default_factory=lambda: []
    )
    where: Optional["eetschema_settlements_bool_exp"] = None


class eetschema_settlements_order_by(BaseModel):
    """Ordering options when selecting data from "eetschema.settlements"."""

    created_at: Optional[order_by] = None
    created_by: Optional[order_by] = None
    expenses_aggregate: Optional["eetschema_expense_aggregate_order_by"] = None
    group: Optional["eetschema_group_order_by"] = None
    group_id: Optional[order_by] = None
    id: Optional[order_by] = None
    updated_at: Optional[order_by] = None
    user: Optional["eetschema_user_order_by"] = None


class eetschema_settlements_stream_cursor_input(BaseModel):
    '''Streaming cursor of the table "eetschema_settlements"'''

    initial_value: "eetschema_settlements_stream_cursor_value_input"
    "Stream column input with initial value"
    ordering: Optional[cursor_ordering] = None
    "cursor ordering"


class eetschema_settlements_stream_cursor_value_input(BaseModel):
    """Initial value of the column from where the streaming should start"""

    created_at: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = (
        None
    )
    created_by: Optional[str] = None
    group_id: Optional[str] = None
    id: Optional[str] = None
    updated_at: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = (
        None
    )


class eetschema_user_bool_exp(BaseModel):
    """Boolean expression to filter rows from the table "eetschema.user". All fields are combined with a logical 'AND'."""

    and_: Optional[list["eetschema_user_bool_exp"]] = Field(alias="_and", default=None)
    not_: Optional["eetschema_user_bool_exp"] = Field(alias="_not", default=None)
    or_: Optional[list["eetschema_user_bool_exp"]] = Field(alias="_or", default=None)
    alias: Optional["String_comparison_exp"] = None
    allergies: Optional["String_array_comparison_exp"] = None
    birthday: Optional["timestamptz_comparison_exp"] = None
    cook_points_imports: Optional["eetschema_cook_points_import_bool_exp"] = None
    default_language: Optional["String_comparison_exp"] = None
    email: Optional["String_comparison_exp"] = None
    event_attendees: Optional["eetschema_event_attendees_bool_exp"] = None
    event_statistics: Optional["eetschema_event_statistics_bool_exp"] = None
    event_statistics_aggregate: Optional[
        "eetschema_event_statistics_aggregate_bool_exp"
    ] = None
    event_statistics_old_imports: Optional[
        "eetschema_event_statistics_old_import_bool_exp"
    ] = None
    events: Optional["eetschema_event_bool_exp"] = None
    events_aggregate: Optional["eetschema_event_aggregate_bool_exp"] = None
    expense_distributions: Optional["eetschema_expense_distribution_bool_exp"] = None
    expenses: Optional["eetschema_expense_bool_exp"] = None
    expenses_by_payed_by: Optional["eetschema_expense_bool_exp"] = Field(
        alias="expensesByPayedBy", default=None
    )
    expenses_by_payed_by_aggregate: Optional["eetschema_expense_aggregate_bool_exp"] = (
        Field(alias="expensesByPayedBy_aggregate", default=None)
    )
    expenses_by_updated_by: Optional["eetschema_expense_bool_exp"] = Field(
        alias="expensesByUpdatedBy", default=None
    )
    expenses_by_updated_by_aggregate: Optional[
        "eetschema_expense_aggregate_bool_exp"
    ] = Field(alias="expensesByUpdatedBy_aggregate", default=None)
    expenses_aggregate: Optional["eetschema_expense_aggregate_bool_exp"] = None
    funnel_lead: Optional["String_array_comparison_exp"] = None
    groups: Optional["eetschema_group_bool_exp"] = None
    id: Optional["String_comparison_exp"] = None
    name: Optional["String_comparison_exp"] = None
    notification_logs: Optional["eetschema_notification_logs_bool_exp"] = None
    notifications: Optional["eetschema_notification_bool_exp"] = None
    order_of_buttom_bar: Optional["String_array_comparison_exp"] = None
    origin: Optional["String_comparison_exp"] = None
    profile_image: Optional["String_comparison_exp"] = None
    reason_to_remove_account_selection: Optional["String_array_comparison_exp"] = None
    reason_to_remove_account_selection_all_options: Optional[
        "String_array_comparison_exp"
    ] = None
    reason_to_remove_account_text: Optional["String_comparison_exp"] = None
    recipe_reviews: Optional["recipe_review_bool_exp"] = None
    recipe_reviews_aggregate: Optional["recipe_review_aggregate_bool_exp"] = None
    recipes: Optional["recipes_bool_exp"] = None
    recipes_aggregate: Optional["recipes_aggregate_bool_exp"] = None
    settlements: Optional["eetschema_settlements_bool_exp"] = None
    user_private_info: Optional["eetschema_user_private_bool_exp"] = None
    users_in_groups: Optional["eetschema_users_in_group_bool_exp"] = None
    wants_to_recieve_notifications: Optional["Boolean_comparison_exp"] = None


class eetschema_user_order_by(BaseModel):
    """Ordering options when selecting data from "eetschema.user"."""

    alias: Optional[order_by] = None
    allergies: Optional[order_by] = None
    birthday: Optional[order_by] = None
    cook_points_imports_aggregate: Optional[
        "eetschema_cook_points_import_aggregate_order_by"
    ] = None
    default_language: Optional[order_by] = None
    email: Optional[order_by] = None
    event_attendees_aggregate: Optional[
        "eetschema_event_attendees_aggregate_order_by"
    ] = None
    event_statistics_aggregate: Optional[
        "eetschema_event_statistics_aggregate_order_by"
    ] = None
    event_statistics_old_imports_aggregate: Optional[
        "eetschema_event_statistics_old_import_aggregate_order_by"
    ] = None
    events_aggregate: Optional["eetschema_event_aggregate_order_by"] = None
    expense_distributions_aggregate: Optional[
        "eetschema_expense_distribution_aggregate_order_by"
    ] = None
    expenses_by_payed_by_aggregate: Optional["eetschema_expense_aggregate_order_by"] = (
        Field(alias="expensesByPayedBy_aggregate", default=None)
    )
    expenses_by_updated_by_aggregate: Optional[
        "eetschema_expense_aggregate_order_by"
    ] = Field(alias="expensesByUpdatedBy_aggregate", default=None)
    expenses_aggregate: Optional["eetschema_expense_aggregate_order_by"] = None
    funnel_lead: Optional[order_by] = None
    groups_aggregate: Optional["eetschema_group_aggregate_order_by"] = None
    id: Optional[order_by] = None
    name: Optional[order_by] = None
    notification_logs_aggregate: Optional[
        "eetschema_notification_logs_aggregate_order_by"
    ] = None
    notifications_aggregate: Optional["eetschema_notification_aggregate_order_by"] = (
        None
    )
    order_of_buttom_bar: Optional[order_by] = None
    origin: Optional[order_by] = None
    profile_image: Optional[order_by] = None
    reason_to_remove_account_selection: Optional[order_by] = None
    reason_to_remove_account_selection_all_options: Optional[order_by] = None
    reason_to_remove_account_text: Optional[order_by] = None
    recipe_reviews_aggregate: Optional["recipe_review_aggregate_order_by"] = None
    recipes_aggregate: Optional["recipes_aggregate_order_by"] = None
    settlements_aggregate: Optional["eetschema_settlements_aggregate_order_by"] = None
    user_private_info: Optional["eetschema_user_private_order_by"] = None
    users_in_groups_aggregate: Optional[
        "eetschema_users_in_group_aggregate_order_by"
    ] = None
    wants_to_recieve_notifications: Optional[order_by] = None


class eetschema_user_pk_columns_input(BaseModel):
    """primary key columns input for table: eetschema.user"""

    id: str


class eetschema_user_private_bool_exp(BaseModel):
    """Boolean expression to filter rows from the table "eetschema.user_private". All fields are combined with a logical 'AND'."""

    and_: Optional[list["eetschema_user_private_bool_exp"]] = Field(
        alias="_and", default=None
    )
    not_: Optional["eetschema_user_private_bool_exp"] = Field(
        alias="_not", default=None
    )
    or_: Optional[list["eetschema_user_private_bool_exp"]] = Field(
        alias="_or", default=None
    )
    active: Optional["Boolean_comparison_exp"] = None
    address: Optional["String_comparison_exp"] = None
    alias: Optional["String_comparison_exp"] = None
    allergies: Optional["String_array_comparison_exp"] = None
    bank_account: Optional["String_comparison_exp"] = None
    birthday: Optional["timestamptz_comparison_exp"] = None
    created_at: Optional["timestamptz_comparison_exp"] = None
    default_landingpage: Optional["String_comparison_exp"] = None
    email: Optional["String_comparison_exp"] = None
    id: Optional["String_comparison_exp"] = None
    is_color_blind: Optional["Boolean_comparison_exp"] = None
    last_seen: Optional["timestamptz_comparison_exp"] = None
    name: Optional["String_comparison_exp"] = None
    old_id: Optional["String_comparison_exp"] = None
    order_of_buttom_bar: Optional["String_array_comparison_exp"] = None
    origin: Optional["String_comparison_exp"] = None
    phone_nr: Optional["String_comparison_exp"] = None
    profile_image: Optional["String_comparison_exp"] = None
    updated_at: Optional["timestamptz_comparison_exp"] = None
    wants_to_recieve_notifications: Optional["Boolean_comparison_exp"] = None


class eetschema_user_private_insert_input(BaseModel):
    '''input type for inserting data into table "eetschema.user_private"'''

    active: Optional[bool] = None
    address: Optional[str] = None
    alias: Optional[str] = None
    allergies: Optional[list[str]] = None
    bank_account: Optional[str] = None
    default_landingpage: Optional[str] = None
    email: Optional[str] = None
    is_color_blind: Optional[bool] = None
    name: Optional[str] = None
    phone_nr: Optional[str] = None
    profile_image: Optional[str] = None
    wants_to_recieve_notifications: Optional[bool] = None


class eetschema_user_private_order_by(BaseModel):
    """Ordering options when selecting data from "eetschema.user_private"."""

    active: Optional[order_by] = None
    address: Optional[order_by] = None
    alias: Optional[order_by] = None
    allergies: Optional[order_by] = None
    bank_account: Optional[order_by] = None
    birthday: Optional[order_by] = None
    created_at: Optional[order_by] = None
    default_landingpage: Optional[order_by] = None
    email: Optional[order_by] = None
    id: Optional[order_by] = None
    is_color_blind: Optional[order_by] = None
    last_seen: Optional[order_by] = None
    name: Optional[order_by] = None
    old_id: Optional[order_by] = None
    order_of_buttom_bar: Optional[order_by] = None
    origin: Optional[order_by] = None
    phone_nr: Optional[order_by] = None
    profile_image: Optional[order_by] = None
    updated_at: Optional[order_by] = None
    wants_to_recieve_notifications: Optional[order_by] = None


class eetschema_user_private_set_input(BaseModel):
    '''input type for updating data in table "eetschema.user_private"'''

    active: Optional[bool] = None
    address: Optional[str] = None
    alias: Optional[str] = None
    allergies: Optional[list[str]] = None
    bank_account: Optional[str] = None
    default_landingpage: Optional[str] = None
    email: Optional[str] = None
    is_color_blind: Optional[bool] = None
    name: Optional[str] = None
    old_id: Optional[str] = None
    order_of_buttom_bar: Optional[list[str]] = None
    origin: Optional[str] = None
    phone_nr: Optional[str] = None
    profile_image: Optional[str] = None
    wants_to_recieve_notifications: Optional[bool] = None


class eetschema_user_private_stream_cursor_input(BaseModel):
    '''Streaming cursor of the table "eetschema_user_private"'''

    initial_value: "eetschema_user_private_stream_cursor_value_input"
    "Stream column input with initial value"
    ordering: Optional[cursor_ordering] = None
    "cursor ordering"


class eetschema_user_private_stream_cursor_value_input(BaseModel):
    """Initial value of the column from where the streaming should start"""

    active: Optional[bool] = None
    address: Optional[str] = None
    alias: Optional[str] = None
    allergies: Optional[list[str]] = None
    bank_account: Optional[str] = None
    birthday: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = None
    created_at: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = (
        None
    )
    default_landingpage: Optional[str] = None
    email: Optional[str] = None
    id: Optional[str] = None
    is_color_blind: Optional[bool] = None
    last_seen: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = None
    name: Optional[str] = None
    old_id: Optional[str] = None
    order_of_buttom_bar: Optional[list[str]] = None
    origin: Optional[str] = None
    phone_nr: Optional[str] = None
    profile_image: Optional[str] = None
    updated_at: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = (
        None
    )
    wants_to_recieve_notifications: Optional[bool] = None


class eetschema_user_private_updates(BaseModel):
    set_: Optional["eetschema_user_private_set_input"] = Field(
        alias="_set", default=None
    )
    "sets the columns of the filtered rows to the given values"
    where: "eetschema_user_private_bool_exp"
    "filter the rows which have to be updated"


class eetschema_user_set_input(BaseModel):
    '''input type for updating data in table "eetschema.user"'''

    active: Optional[bool] = None
    address: Optional[str] = None
    alias: Optional[str] = None
    allergies: Optional[list[str]] = None
    bank_account: Optional[str] = None
    birthday: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = None
    default_landingpage: Optional[str] = None
    default_language: Optional[str] = None
    default_screen: Optional[str] = None
    funnel_lead: Optional[list[str]] = None
    is_color_blind: Optional[bool] = None
    name: Optional[str] = None
    order_of_buttom_bar: Optional[list[str]] = None
    phone_nr: Optional[str] = None
    profile_image: Optional[str] = None
    reason_to_remove_account_selection: Optional[list[str]] = None
    reason_to_remove_account_selection_all_options: Optional[list[str]] = None
    reason_to_remove_account_text: Optional[str] = None
    wants_to_recieve_notifications: Optional[bool] = None


class eetschema_user_stream_cursor_input(BaseModel):
    '''Streaming cursor of the table "eetschema_user"'''

    initial_value: "eetschema_user_stream_cursor_value_input"
    "Stream column input with initial value"
    ordering: Optional[cursor_ordering] = None
    "cursor ordering"


class eetschema_user_stream_cursor_value_input(BaseModel):
    """Initial value of the column from where the streaming should start"""

    alias: Optional[str] = None
    allergies: Optional[list[str]] = None
    birthday: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = None
    default_language: Optional[str] = None
    email: Optional[str] = None
    funnel_lead: Optional[list[str]] = None
    id: Optional[str] = None
    name: Optional[str] = None
    order_of_buttom_bar: Optional[list[str]] = None
    origin: Optional[str] = None
    profile_image: Optional[str] = None
    reason_to_remove_account_selection: Optional[list[str]] = None
    reason_to_remove_account_selection_all_options: Optional[list[str]] = None
    reason_to_remove_account_text: Optional[str] = None
    wants_to_recieve_notifications: Optional[bool] = None


class eetschema_user_updates(BaseModel):
    set_: Optional["eetschema_user_set_input"] = Field(alias="_set", default=None)
    "sets the columns of the filtered rows to the given values"
    where: "eetschema_user_bool_exp"
    "filter the rows which have to be updated"


class eetschema_users_in_group_aggregate_order_by(BaseModel):
    '''order by aggregate values of table "eetschema.users_in_group"'''

    avg: Optional["eetschema_users_in_group_avg_order_by"] = None
    count: Optional[order_by] = None
    max: Optional["eetschema_users_in_group_max_order_by"] = None
    min: Optional["eetschema_users_in_group_min_order_by"] = None
    stddev: Optional["eetschema_users_in_group_stddev_order_by"] = None
    stddev_pop: Optional["eetschema_users_in_group_stddev_pop_order_by"] = None
    stddev_samp: Optional["eetschema_users_in_group_stddev_samp_order_by"] = None
    sum: Optional["eetschema_users_in_group_sum_order_by"] = None
    var_pop: Optional["eetschema_users_in_group_var_pop_order_by"] = None
    var_samp: Optional["eetschema_users_in_group_var_samp_order_by"] = None
    variance: Optional["eetschema_users_in_group_variance_order_by"] = None


class eetschema_users_in_group_arr_rel_insert_input(BaseModel):
    '''input type for inserting array relation for remote table "eetschema.users_in_group"'''

    data: list["eetschema_users_in_group_insert_input"]
    on_conflict: Optional["eetschema_users_in_group_on_conflict"] = None
    "upsert condition"


class eetschema_users_in_group_avg_order_by(BaseModel):
    '''order by avg() on columns of table "eetschema.users_in_group"'''

    order: Optional[order_by] = None


class eetschema_users_in_group_bool_exp(BaseModel):
    """Boolean expression to filter rows from the table "eetschema.users_in_group". All fields are combined with a logical 'AND'."""

    and_: Optional[list["eetschema_users_in_group_bool_exp"]] = Field(
        alias="_and", default=None
    )
    not_: Optional["eetschema_users_in_group_bool_exp"] = Field(
        alias="_not", default=None
    )
    or_: Optional[list["eetschema_users_in_group_bool_exp"]] = Field(
        alias="_or", default=None
    )
    active: Optional["Boolean_comparison_exp"] = None
    end_holliday: Optional["timestamptz_comparison_exp"] = None
    event: Optional["eetschema_event_bool_exp"] = None
    event_id: Optional["uuid_comparison_exp"] = None
    friday: Optional["String_comparison_exp"] = None
    group: Optional["eetschema_group_bool_exp"] = None
    group_id: Optional["uuid_comparison_exp"] = None
    group_stats_2: Optional["eetschema_group_statistics_2_bool_exp"] = None
    monday: Optional["String_comparison_exp"] = None
    order: Optional["Int_comparison_exp"] = None
    saturday: Optional["String_comparison_exp"] = None
    start_holliday: Optional["timestamptz_comparison_exp"] = None
    sunday: Optional["String_comparison_exp"] = None
    thursday: Optional["String_comparison_exp"] = None
    tuesday: Optional["String_comparison_exp"] = None
    user: Optional["eetschema_user_bool_exp"] = None
    user_id: Optional["String_comparison_exp"] = None
    wednesday: Optional["String_comparison_exp"] = None


class eetschema_users_in_group_inc_input(BaseModel):
    '''input type for incrementing numeric columns in table "eetschema.users_in_group"'''

    order: Optional[int] = None


class eetschema_users_in_group_insert_input(BaseModel):
    '''input type for inserting data into table "eetschema.users_in_group"'''

    active: Optional[bool] = None
    event: Optional["eetschema_event_obj_rel_insert_input"] = None
    event_id: Optional[str] = None
    group: Optional["eetschema_group_obj_rel_insert_input"] = None
    group_id: Optional[str] = None
    order: Optional[int] = None
    user_id: Optional[str] = None


class eetschema_users_in_group_max_order_by(BaseModel):
    '''order by max() on columns of table "eetschema.users_in_group"'''

    end_holliday: Optional[order_by] = None
    event_id: Optional[order_by] = None
    friday: Optional[order_by] = None
    group_id: Optional[order_by] = None
    monday: Optional[order_by] = None
    order: Optional[order_by] = None
    saturday: Optional[order_by] = None
    start_holliday: Optional[order_by] = None
    sunday: Optional[order_by] = None
    thursday: Optional[order_by] = None
    tuesday: Optional[order_by] = None
    user_id: Optional[order_by] = None
    wednesday: Optional[order_by] = None


class eetschema_users_in_group_min_order_by(BaseModel):
    '''order by min() on columns of table "eetschema.users_in_group"'''

    end_holliday: Optional[order_by] = None
    event_id: Optional[order_by] = None
    friday: Optional[order_by] = None
    group_id: Optional[order_by] = None
    monday: Optional[order_by] = None
    order: Optional[order_by] = None
    saturday: Optional[order_by] = None
    start_holliday: Optional[order_by] = None
    sunday: Optional[order_by] = None
    thursday: Optional[order_by] = None
    tuesday: Optional[order_by] = None
    user_id: Optional[order_by] = None
    wednesday: Optional[order_by] = None


class eetschema_users_in_group_obj_rel_insert_input(BaseModel):
    '''input type for inserting object relation for remote table "eetschema.users_in_group"'''

    data: "eetschema_users_in_group_insert_input"
    on_conflict: Optional["eetschema_users_in_group_on_conflict"] = None
    "upsert condition"


class eetschema_users_in_group_on_conflict(BaseModel):
    '''on_conflict condition type for table "eetschema.users_in_group"'''

    constraint: eetschema_users_in_group_constraint
    update_columns: list[eetschema_users_in_group_update_column] = Field(
        default_factory=lambda: []
    )
    where: Optional["eetschema_users_in_group_bool_exp"] = None


class eetschema_users_in_group_order_by(BaseModel):
    """Ordering options when selecting data from "eetschema.users_in_group"."""

    active: Optional[order_by] = None
    end_holliday: Optional[order_by] = None
    event: Optional["eetschema_event_order_by"] = None
    event_id: Optional[order_by] = None
    friday: Optional[order_by] = None
    group: Optional["eetschema_group_order_by"] = None
    group_id: Optional[order_by] = None
    group_stats_2_aggregate: Optional[
        "eetschema_group_statistics_2_aggregate_order_by"
    ] = None
    monday: Optional[order_by] = None
    order: Optional[order_by] = None
    saturday: Optional[order_by] = None
    start_holliday: Optional[order_by] = None
    sunday: Optional[order_by] = None
    thursday: Optional[order_by] = None
    tuesday: Optional[order_by] = None
    user: Optional["eetschema_user_order_by"] = None
    user_id: Optional[order_by] = None
    wednesday: Optional[order_by] = None


class eetschema_users_in_group_pk_columns_input(BaseModel):
    """primary key columns input for table: eetschema.users_in_group"""

    group_id: str
    user_id: str


class eetschema_users_in_group_set_input(BaseModel):
    '''input type for updating data in table "eetschema.users_in_group"'''

    active: Optional[bool] = None
    end_holliday: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = (
        None
    )
    friday: Optional[str] = None
    monday: Optional[str] = None
    order: Optional[int] = None
    saturday: Optional[str] = None
    start_holliday: Optional[
        Annotated[datetime, PlainSerializer(serialize_datetime)]
    ] = None
    sunday: Optional[str] = None
    thursday: Optional[str] = None
    tuesday: Optional[str] = None
    wednesday: Optional[str] = None


class eetschema_users_in_group_stddev_order_by(BaseModel):
    '''order by stddev() on columns of table "eetschema.users_in_group"'''

    order: Optional[order_by] = None


class eetschema_users_in_group_stddev_pop_order_by(BaseModel):
    '''order by stddev_pop() on columns of table "eetschema.users_in_group"'''

    order: Optional[order_by] = None


class eetschema_users_in_group_stddev_samp_order_by(BaseModel):
    '''order by stddev_samp() on columns of table "eetschema.users_in_group"'''

    order: Optional[order_by] = None


class eetschema_users_in_group_stream_cursor_input(BaseModel):
    '''Streaming cursor of the table "eetschema_users_in_group"'''

    initial_value: "eetschema_users_in_group_stream_cursor_value_input"
    "Stream column input with initial value"
    ordering: Optional[cursor_ordering] = None
    "cursor ordering"


class eetschema_users_in_group_stream_cursor_value_input(BaseModel):
    """Initial value of the column from where the streaming should start"""

    active: Optional[bool] = None
    end_holliday: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = (
        None
    )
    event_id: Optional[str] = None
    friday: Optional[str] = None
    group_id: Optional[str] = None
    monday: Optional[str] = None
    order: Optional[int] = None
    saturday: Optional[str] = None
    start_holliday: Optional[
        Annotated[datetime, PlainSerializer(serialize_datetime)]
    ] = None
    sunday: Optional[str] = None
    thursday: Optional[str] = None
    tuesday: Optional[str] = None
    user_id: Optional[str] = None
    wednesday: Optional[str] = None


class eetschema_users_in_group_sum_order_by(BaseModel):
    '''order by sum() on columns of table "eetschema.users_in_group"'''

    order: Optional[order_by] = None


class eetschema_users_in_group_updates(BaseModel):
    inc: Optional["eetschema_users_in_group_inc_input"] = Field(
        alias="_inc", default=None
    )
    "increments the numeric columns with given value of the filtered values"
    set_: Optional["eetschema_users_in_group_set_input"] = Field(
        alias="_set", default=None
    )
    "sets the columns of the filtered rows to the given values"
    where: "eetschema_users_in_group_bool_exp"
    "filter the rows which have to be updated"


class eetschema_users_in_group_var_pop_order_by(BaseModel):
    '''order by var_pop() on columns of table "eetschema.users_in_group"'''

    order: Optional[order_by] = None


class eetschema_users_in_group_var_samp_order_by(BaseModel):
    '''order by var_samp() on columns of table "eetschema.users_in_group"'''

    order: Optional[order_by] = None


class eetschema_users_in_group_variance_order_by(BaseModel):
    '''order by variance() on columns of table "eetschema.users_in_group"'''

    order: Optional[order_by] = None


class json_comparison_exp(BaseModel):
    """Boolean expression to compare columns of type "json". All fields are combined with logical 'AND'."""

    eq: Optional[Any] = Field(alias="_eq", default=None)
    gt: Optional[Any] = Field(alias="_gt", default=None)
    gte: Optional[Any] = Field(alias="_gte", default=None)
    in_: Optional[list[Any]] = Field(alias="_in", default=None)
    is_null: Optional[bool] = Field(alias="_is_null", default=None)
    lt: Optional[Any] = Field(alias="_lt", default=None)
    lte: Optional[Any] = Field(alias="_lte", default=None)
    neq: Optional[Any] = Field(alias="_neq", default=None)
    nin: Optional[list[Any]] = Field(alias="_nin", default=None)


class numeric_comparison_exp(BaseModel):
    """Boolean expression to compare columns of type "numeric". All fields are combined with logical 'AND'."""

    eq: Optional[Any] = Field(alias="_eq", default=None)
    gt: Optional[Any] = Field(alias="_gt", default=None)
    gte: Optional[Any] = Field(alias="_gte", default=None)
    in_: Optional[list[Any]] = Field(alias="_in", default=None)
    is_null: Optional[bool] = Field(alias="_is_null", default=None)
    lt: Optional[Any] = Field(alias="_lt", default=None)
    lte: Optional[Any] = Field(alias="_lte", default=None)
    neq: Optional[Any] = Field(alias="_neq", default=None)
    nin: Optional[list[Any]] = Field(alias="_nin", default=None)


class recipe_review_aggregate_bool_exp(BaseModel):
    count: Optional["recipe_review_aggregate_bool_exp_count"] = None


class recipe_review_aggregate_bool_exp_count(BaseModel):
    arguments: Optional[list[recipe_review_select_column]] = None
    distinct: Optional[bool] = None
    filter_: Optional["recipe_review_bool_exp"] = Field(alias="filter", default=None)
    predicate: "Int_comparison_exp"


class recipe_review_aggregate_order_by(BaseModel):
    '''order by aggregate values of table "recipe_review"'''

    avg: Optional["recipe_review_avg_order_by"] = None
    count: Optional[order_by] = None
    max: Optional["recipe_review_max_order_by"] = None
    min: Optional["recipe_review_min_order_by"] = None
    stddev: Optional["recipe_review_stddev_order_by"] = None
    stddev_pop: Optional["recipe_review_stddev_pop_order_by"] = None
    stddev_samp: Optional["recipe_review_stddev_samp_order_by"] = None
    sum: Optional["recipe_review_sum_order_by"] = None
    var_pop: Optional["recipe_review_var_pop_order_by"] = None
    var_samp: Optional["recipe_review_var_samp_order_by"] = None
    variance: Optional["recipe_review_variance_order_by"] = None


class recipe_review_arr_rel_insert_input(BaseModel):
    '''input type for inserting array relation for remote table "recipe_review"'''

    data: list["recipe_review_insert_input"]
    on_conflict: Optional["recipe_review_on_conflict"] = None
    "upsert condition"


class recipe_review_avg_order_by(BaseModel):
    '''order by avg() on columns of table "recipe_review"'''

    rating: Optional[order_by] = None


class recipe_review_bool_exp(BaseModel):
    """Boolean expression to filter rows from the table "recipe_review". All fields are combined with a logical 'AND'."""

    and_: Optional[list["recipe_review_bool_exp"]] = Field(alias="_and", default=None)
    not_: Optional["recipe_review_bool_exp"] = Field(alias="_not", default=None)
    or_: Optional[list["recipe_review_bool_exp"]] = Field(alias="_or", default=None)
    rating: Optional["Int_comparison_exp"] = None
    recipe: Optional["recipes_bool_exp"] = None
    user: Optional["eetschema_user_bool_exp"] = None
    user_id: Optional["String_comparison_exp"] = None


class recipe_review_inc_input(BaseModel):
    '''input type for incrementing numeric columns in table "recipe_review"'''

    rating: Optional[int] = None


class recipe_review_insert_input(BaseModel):
    '''input type for inserting data into table "recipe_review"'''

    active: Optional[bool] = None
    description: Optional[str] = None
    rating: Optional[int] = None
    recipe: Optional["recipes_obj_rel_insert_input"] = None
    recipe_id: Optional[str] = None


class recipe_review_max_order_by(BaseModel):
    '''order by max() on columns of table "recipe_review"'''

    rating: Optional[order_by] = None
    user_id: Optional[order_by] = None


class recipe_review_min_order_by(BaseModel):
    '''order by min() on columns of table "recipe_review"'''

    rating: Optional[order_by] = None
    user_id: Optional[order_by] = None


class recipe_review_on_conflict(BaseModel):
    '''on_conflict condition type for table "recipe_review"'''

    constraint: recipe_review_constraint
    update_columns: list[recipe_review_update_column] = Field(
        default_factory=lambda: []
    )
    where: Optional["recipe_review_bool_exp"] = None


class recipe_review_order_by(BaseModel):
    """Ordering options when selecting data from "recipe_review"."""

    rating: Optional[order_by] = None
    recipe: Optional["recipes_order_by"] = None
    user: Optional["eetschema_user_order_by"] = None
    user_id: Optional[order_by] = None


class recipe_review_set_input(BaseModel):
    '''input type for updating data in table "recipe_review"'''

    rating: Optional[int] = None


class recipe_review_stddev_order_by(BaseModel):
    '''order by stddev() on columns of table "recipe_review"'''

    rating: Optional[order_by] = None


class recipe_review_stddev_pop_order_by(BaseModel):
    '''order by stddev_pop() on columns of table "recipe_review"'''

    rating: Optional[order_by] = None


class recipe_review_stddev_samp_order_by(BaseModel):
    '''order by stddev_samp() on columns of table "recipe_review"'''

    rating: Optional[order_by] = None


class recipe_review_stream_cursor_input(BaseModel):
    '''Streaming cursor of the table "recipe_review"'''

    initial_value: "recipe_review_stream_cursor_value_input"
    "Stream column input with initial value"
    ordering: Optional[cursor_ordering] = None
    "cursor ordering"


class recipe_review_stream_cursor_value_input(BaseModel):
    """Initial value of the column from where the streaming should start"""

    rating: Optional[int] = None
    user_id: Optional[str] = None


class recipe_review_sum_order_by(BaseModel):
    '''order by sum() on columns of table "recipe_review"'''

    rating: Optional[order_by] = None


class recipe_review_updates(BaseModel):
    inc: Optional["recipe_review_inc_input"] = Field(alias="_inc", default=None)
    "increments the numeric columns with given value of the filtered values"
    set_: Optional["recipe_review_set_input"] = Field(alias="_set", default=None)
    "sets the columns of the filtered rows to the given values"
    where: "recipe_review_bool_exp"
    "filter the rows which have to be updated"


class recipe_review_var_pop_order_by(BaseModel):
    '''order by var_pop() on columns of table "recipe_review"'''

    rating: Optional[order_by] = None


class recipe_review_var_samp_order_by(BaseModel):
    '''order by var_samp() on columns of table "recipe_review"'''

    rating: Optional[order_by] = None


class recipe_review_variance_order_by(BaseModel):
    '''order by variance() on columns of table "recipe_review"'''

    rating: Optional[order_by] = None


class recipes_aggregate_bool_exp(BaseModel):
    bool_and: Optional["recipes_aggregate_bool_exp_bool_and"] = None
    bool_or: Optional["recipes_aggregate_bool_exp_bool_or"] = None
    count: Optional["recipes_aggregate_bool_exp_count"] = None


class recipes_aggregate_bool_exp_bool_and(BaseModel):
    arguments: (
        recipes_select_column_recipes_aggregate_bool_exp_bool_and_arguments_columns
    )
    distinct: Optional[bool] = None
    filter_: Optional["recipes_bool_exp"] = Field(alias="filter", default=None)
    predicate: "Boolean_comparison_exp"


class recipes_aggregate_bool_exp_bool_or(BaseModel):
    arguments: (
        recipes_select_column_recipes_aggregate_bool_exp_bool_or_arguments_columns
    )
    distinct: Optional[bool] = None
    filter_: Optional["recipes_bool_exp"] = Field(alias="filter", default=None)
    predicate: "Boolean_comparison_exp"


class recipes_aggregate_bool_exp_count(BaseModel):
    arguments: Optional[list[recipes_select_column]] = None
    distinct: Optional[bool] = None
    filter_: Optional["recipes_bool_exp"] = Field(alias="filter", default=None)
    predicate: "Int_comparison_exp"


class recipes_aggregate_order_by(BaseModel):
    '''order by aggregate values of table "recipes"'''

    avg: Optional["recipes_avg_order_by"] = None
    count: Optional[order_by] = None
    max: Optional["recipes_max_order_by"] = None
    min: Optional["recipes_min_order_by"] = None
    stddev: Optional["recipes_stddev_order_by"] = None
    stddev_pop: Optional["recipes_stddev_pop_order_by"] = None
    stddev_samp: Optional["recipes_stddev_samp_order_by"] = None
    sum: Optional["recipes_sum_order_by"] = None
    var_pop: Optional["recipes_var_pop_order_by"] = None
    var_samp: Optional["recipes_var_samp_order_by"] = None
    variance: Optional["recipes_variance_order_by"] = None


class recipes_avg_order_by(BaseModel):
    '''order by avg() on columns of table "recipes"'''

    cook_time: Optional[order_by] = None
    prep_time: Optional[order_by] = None
    servings: Optional[order_by] = None
    total_time: Optional[order_by] = None


class recipes_bool_exp(BaseModel):
    """Boolean expression to filter rows from the table "recipes". All fields are combined with a logical 'AND'."""

    and_: Optional[list["recipes_bool_exp"]] = Field(alias="_and", default=None)
    not_: Optional["recipes_bool_exp"] = Field(alias="_not", default=None)
    or_: Optional[list["recipes_bool_exp"]] = Field(alias="_or", default=None)
    cook_time: Optional["Int_comparison_exp"] = None
    course_category: Optional["String_comparison_exp"] = None
    created_at: Optional["timestamptz_comparison_exp"] = None
    description: Optional["String_comparison_exp"] = None
    id: Optional["uuid_comparison_exp"] = None
    image_url: Optional["String_comparison_exp"] = None
    ingredients: Optional["String_array_comparison_exp"] = None
    instructions: Optional["String_array_comparison_exp"] = None
    is_deleted: Optional["Boolean_comparison_exp"] = None
    is_shared: Optional["Boolean_comparison_exp"] = None
    language: Optional["String_comparison_exp"] = None
    original_host: Optional["String_comparison_exp"] = None
    original_url: Optional["String_comparison_exp"] = None
    owner_id: Optional["String_comparison_exp"] = None
    prep_time: Optional["Int_comparison_exp"] = None
    recipe_reviews: Optional["recipe_review_bool_exp"] = None
    recipe_reviews_aggregate: Optional["recipe_review_aggregate_bool_exp"] = None
    servings: Optional["Int_comparison_exp"] = None
    title: Optional["String_comparison_exp"] = None
    total_time: Optional["Int_comparison_exp"] = None
    updated_at: Optional["timestamptz_comparison_exp"] = None
    user: Optional["eetschema_user_bool_exp"] = None


class recipes_inc_input(BaseModel):
    '''input type for incrementing numeric columns in table "recipes"'''

    cook_time: Optional[int] = None
    prep_time: Optional[int] = None
    servings: Optional[int] = None
    total_time: Optional[int] = None


class recipes_insert_input(BaseModel):
    '''input type for inserting data into table "recipes"'''

    cook_time: Optional[int] = None
    course_category: Optional[str] = None
    description: Optional[str] = None
    id: Optional[str] = None
    image_url: Optional[str] = None
    ingredients: Optional[list[str]] = None
    instructions: Optional[list[str]] = None
    language: Optional[str] = None
    original_host: Optional[str] = None
    prep_time: Optional[int] = None
    recipe_reviews: Optional["recipe_review_arr_rel_insert_input"] = None
    servings: Optional[int] = None
    title: Optional[str] = None
    total_time: Optional[int] = None


class recipes_max_order_by(BaseModel):
    '''order by max() on columns of table "recipes"'''

    cook_time: Optional[order_by] = None
    course_category: Optional[order_by] = None
    created_at: Optional[order_by] = None
    description: Optional[order_by] = None
    id: Optional[order_by] = None
    image_url: Optional[order_by] = None
    ingredients: Optional[order_by] = None
    instructions: Optional[order_by] = None
    language: Optional[order_by] = None
    original_host: Optional[order_by] = None
    original_url: Optional[order_by] = None
    owner_id: Optional[order_by] = None
    prep_time: Optional[order_by] = None
    servings: Optional[order_by] = None
    title: Optional[order_by] = None
    total_time: Optional[order_by] = None
    updated_at: Optional[order_by] = None


class recipes_min_order_by(BaseModel):
    '''order by min() on columns of table "recipes"'''

    cook_time: Optional[order_by] = None
    course_category: Optional[order_by] = None
    created_at: Optional[order_by] = None
    description: Optional[order_by] = None
    id: Optional[order_by] = None
    image_url: Optional[order_by] = None
    ingredients: Optional[order_by] = None
    instructions: Optional[order_by] = None
    language: Optional[order_by] = None
    original_host: Optional[order_by] = None
    original_url: Optional[order_by] = None
    owner_id: Optional[order_by] = None
    prep_time: Optional[order_by] = None
    servings: Optional[order_by] = None
    title: Optional[order_by] = None
    total_time: Optional[order_by] = None
    updated_at: Optional[order_by] = None


class recipes_obj_rel_insert_input(BaseModel):
    '''input type for inserting object relation for remote table "recipes"'''

    data: "recipes_insert_input"
    on_conflict: Optional["recipes_on_conflict"] = None
    "upsert condition"


class recipes_on_conflict(BaseModel):
    '''on_conflict condition type for table "recipes"'''

    constraint: recipes_constraint
    update_columns: list[recipes_update_column] = Field(default_factory=lambda: [])
    where: Optional["recipes_bool_exp"] = None


class recipes_order_by(BaseModel):
    """Ordering options when selecting data from "recipes"."""

    cook_time: Optional[order_by] = None
    course_category: Optional[order_by] = None
    created_at: Optional[order_by] = None
    description: Optional[order_by] = None
    id: Optional[order_by] = None
    image_url: Optional[order_by] = None
    ingredients: Optional[order_by] = None
    instructions: Optional[order_by] = None
    is_deleted: Optional[order_by] = None
    is_shared: Optional[order_by] = None
    language: Optional[order_by] = None
    original_host: Optional[order_by] = None
    original_url: Optional[order_by] = None
    owner_id: Optional[order_by] = None
    prep_time: Optional[order_by] = None
    recipe_reviews_aggregate: Optional["recipe_review_aggregate_order_by"] = None
    servings: Optional[order_by] = None
    title: Optional[order_by] = None
    total_time: Optional[order_by] = None
    updated_at: Optional[order_by] = None
    user: Optional["eetschema_user_order_by"] = None


class recipes_pk_columns_input(BaseModel):
    """primary key columns input for table: recipes"""

    id: str


class recipes_set_input(BaseModel):
    '''input type for updating data in table "recipes"'''

    cook_time: Optional[int] = None
    course_category: Optional[str] = None
    description: Optional[str] = None
    image_url: Optional[str] = None
    ingredients: Optional[list[str]] = None
    instructions: Optional[list[str]] = None
    is_deleted: Optional[bool] = None
    is_shared: Optional[bool] = None
    language: Optional[str] = None
    original_host: Optional[str] = None
    prep_time: Optional[int] = None
    servings: Optional[int] = None
    title: Optional[str] = None
    total_time: Optional[int] = None


class recipes_stddev_order_by(BaseModel):
    '''order by stddev() on columns of table "recipes"'''

    cook_time: Optional[order_by] = None
    prep_time: Optional[order_by] = None
    servings: Optional[order_by] = None
    total_time: Optional[order_by] = None


class recipes_stddev_pop_order_by(BaseModel):
    '''order by stddev_pop() on columns of table "recipes"'''

    cook_time: Optional[order_by] = None
    prep_time: Optional[order_by] = None
    servings: Optional[order_by] = None
    total_time: Optional[order_by] = None


class recipes_stddev_samp_order_by(BaseModel):
    '''order by stddev_samp() on columns of table "recipes"'''

    cook_time: Optional[order_by] = None
    prep_time: Optional[order_by] = None
    servings: Optional[order_by] = None
    total_time: Optional[order_by] = None


class recipes_stream_cursor_input(BaseModel):
    '''Streaming cursor of the table "recipes"'''

    initial_value: "recipes_stream_cursor_value_input"
    "Stream column input with initial value"
    ordering: Optional[cursor_ordering] = None
    "cursor ordering"


class recipes_stream_cursor_value_input(BaseModel):
    """Initial value of the column from where the streaming should start"""

    cook_time: Optional[int] = None
    course_category: Optional[str] = None
    created_at: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = (
        None
    )
    description: Optional[str] = None
    id: Optional[str] = None
    image_url: Optional[str] = None
    ingredients: Optional[list[str]] = None
    instructions: Optional[list[str]] = None
    is_deleted: Optional[bool] = None
    is_shared: Optional[bool] = None
    language: Optional[str] = None
    original_host: Optional[str] = None
    original_url: Optional[str] = None
    owner_id: Optional[str] = None
    prep_time: Optional[int] = None
    servings: Optional[int] = None
    title: Optional[str] = None
    total_time: Optional[int] = None
    updated_at: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = (
        None
    )


class recipes_sum_order_by(BaseModel):
    '''order by sum() on columns of table "recipes"'''

    cook_time: Optional[order_by] = None
    prep_time: Optional[order_by] = None
    servings: Optional[order_by] = None
    total_time: Optional[order_by] = None


class recipes_updates(BaseModel):
    inc: Optional["recipes_inc_input"] = Field(alias="_inc", default=None)
    "increments the numeric columns with given value of the filtered values"
    set_: Optional["recipes_set_input"] = Field(alias="_set", default=None)
    "sets the columns of the filtered rows to the given values"
    where: "recipes_bool_exp"
    "filter the rows which have to be updated"


class recipes_var_pop_order_by(BaseModel):
    '''order by var_pop() on columns of table "recipes"'''

    cook_time: Optional[order_by] = None
    prep_time: Optional[order_by] = None
    servings: Optional[order_by] = None
    total_time: Optional[order_by] = None


class recipes_var_samp_order_by(BaseModel):
    '''order by var_samp() on columns of table "recipes"'''

    cook_time: Optional[order_by] = None
    prep_time: Optional[order_by] = None
    servings: Optional[order_by] = None
    total_time: Optional[order_by] = None


class recipes_variance_order_by(BaseModel):
    '''order by variance() on columns of table "recipes"'''

    cook_time: Optional[order_by] = None
    prep_time: Optional[order_by] = None
    servings: Optional[order_by] = None
    total_time: Optional[order_by] = None


class timestamptz_comparison_exp(BaseModel):
    """Boolean expression to compare columns of type "timestamptz". All fields are combined with logical 'AND'."""

    eq: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = Field(
        alias="_eq", default=None
    )
    gt: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = Field(
        alias="_gt", default=None
    )
    gte: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = Field(
        alias="_gte", default=None
    )
    in_: Optional[list[Annotated[datetime, PlainSerializer(serialize_datetime)]]] = (
        Field(alias="_in", default=None)
    )
    is_null: Optional[bool] = Field(alias="_is_null", default=None)
    lt: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = Field(
        alias="_lt", default=None
    )
    lte: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = Field(
        alias="_lte", default=None
    )
    neq: Optional[Annotated[datetime, PlainSerializer(serialize_datetime)]] = Field(
        alias="_neq", default=None
    )
    nin: Optional[list[Annotated[datetime, PlainSerializer(serialize_datetime)]]] = (
        Field(alias="_nin", default=None)
    )


class uuid_comparison_exp(BaseModel):
    """Boolean expression to compare columns of type "uuid". All fields are combined with logical 'AND'."""

    eq: Optional[str] = Field(alias="_eq", default=None)
    gt: Optional[str] = Field(alias="_gt", default=None)
    gte: Optional[str] = Field(alias="_gte", default=None)
    in_: Optional[list[str]] = Field(alias="_in", default=None)
    is_null: Optional[bool] = Field(alias="_is_null", default=None)
    lt: Optional[str] = Field(alias="_lt", default=None)
    lte: Optional[str] = Field(alias="_lte", default=None)
    neq: Optional[str] = Field(alias="_neq", default=None)
    nin: Optional[list[str]] = Field(alias="_nin", default=None)


ads_ads_bool_exp.model_rebuild()
ads_ads_order_by.model_rebuild()
ads_ads_stream_cursor_input.model_rebuild()
ads_ads_targeting_aggregate_order_by.model_rebuild()
ads_ads_targeting_bool_exp.model_rebuild()
ads_ads_targeting_order_by.model_rebuild()
ads_ads_targeting_stream_cursor_input.model_rebuild()
ads_interaction_bool_exp.model_rebuild()
ads_interaction_on_conflict.model_rebuild()
ads_targeting_bool_exp.model_rebuild()
ads_targeting_order_by.model_rebuild()
ads_targeting_stream_cursor_input.model_rebuild()
eetschema_app_status_bool_exp.model_rebuild()
eetschema_app_status_stream_cursor_input.model_rebuild()
eetschema_cook_points_import_aggregate_order_by.model_rebuild()
eetschema_cook_points_import_bool_exp.model_rebuild()
eetschema_cook_points_import_insert_input.model_rebuild()
eetschema_cook_points_import_on_conflict.model_rebuild()
eetschema_cook_points_import_order_by.model_rebuild()
eetschema_cook_points_import_stream_cursor_input.model_rebuild()
eetschema_cook_points_import_updates.model_rebuild()
eetschema_event_aggregate_bool_exp.model_rebuild()
eetschema_event_aggregate_bool_exp_bool_and.model_rebuild()
eetschema_event_aggregate_bool_exp_bool_or.model_rebuild()
eetschema_event_aggregate_bool_exp_count.model_rebuild()
eetschema_event_aggregate_order_by.model_rebuild()
eetschema_event_arr_rel_insert_input.model_rebuild()
eetschema_event_attendees_aggregate_order_by.model_rebuild()
eetschema_event_attendees_arr_rel_insert_input.model_rebuild()
eetschema_event_attendees_bool_exp.model_rebuild()
eetschema_event_attendees_insert_input.model_rebuild()
eetschema_event_attendees_on_conflict.model_rebuild()
eetschema_event_attendees_order_by.model_rebuild()
eetschema_event_attendees_stream_cursor_input.model_rebuild()
eetschema_event_attendees_updates.model_rebuild()
eetschema_event_attendees_view_aggregate_order_by.model_rebuild()
eetschema_event_attendees_view_bool_exp.model_rebuild()
eetschema_event_attendees_view_order_by.model_rebuild()
eetschema_event_attendees_view_stream_cursor_input.model_rebuild()
eetschema_event_bool_exp.model_rebuild()
eetschema_event_insert_input.model_rebuild()
eetschema_event_obj_rel_insert_input.model_rebuild()
eetschema_event_on_conflict.model_rebuild()
eetschema_event_order_by.model_rebuild()
eetschema_event_statistics_aggregate_bool_exp.model_rebuild()
eetschema_event_statistics_aggregate_bool_exp_count.model_rebuild()
eetschema_event_statistics_aggregate_order_by.model_rebuild()
eetschema_event_statistics_bool_exp.model_rebuild()
eetschema_event_statistics_old_import_aggregate_order_by.model_rebuild()
eetschema_event_statistics_old_import_bool_exp.model_rebuild()
eetschema_event_statistics_old_import_order_by.model_rebuild()
eetschema_event_statistics_old_import_stream_cursor_input.model_rebuild()
eetschema_event_statistics_order_by.model_rebuild()
eetschema_event_statistics_stream_cursor_input.model_rebuild()
eetschema_event_stream_cursor_input.model_rebuild()
eetschema_event_updates.model_rebuild()
eetschema_expense_aggregate_bool_exp.model_rebuild()
eetschema_expense_aggregate_bool_exp_bool_and.model_rebuild()
eetschema_expense_aggregate_bool_exp_bool_or.model_rebuild()
eetschema_expense_aggregate_bool_exp_count.model_rebuild()
eetschema_expense_aggregate_order_by.model_rebuild()
eetschema_expense_arr_rel_insert_input.model_rebuild()
eetschema_expense_bool_exp.model_rebuild()
eetschema_expense_distribution_aggregate_order_by.model_rebuild()
eetschema_expense_distribution_arr_rel_insert_input.model_rebuild()
eetschema_expense_distribution_bool_exp.model_rebuild()
eetschema_expense_distribution_insert_input.model_rebuild()
eetschema_expense_distribution_on_conflict.model_rebuild()
eetschema_expense_distribution_order_by.model_rebuild()
eetschema_expense_distribution_stream_cursor_input.model_rebuild()
eetschema_expense_distribution_updates.model_rebuild()
eetschema_expense_eetlijst_import_bool_exp.model_rebuild()
eetschema_expense_eetlijst_import_order_by.model_rebuild()
eetschema_expense_eetlijst_import_stream_cursor_input.model_rebuild()
eetschema_expense_insert_input.model_rebuild()
eetschema_expense_obj_rel_insert_input.model_rebuild()
eetschema_expense_on_conflict.model_rebuild()
eetschema_expense_order_by.model_rebuild()
eetschema_expense_stream_cursor_input.model_rebuild()
eetschema_expense_updates.model_rebuild()
eetschema_group_aggregate_order_by.model_rebuild()
eetschema_group_bool_exp.model_rebuild()
eetschema_group_insert_input.model_rebuild()
eetschema_group_invite_bool_exp.model_rebuild()
eetschema_group_invite_stream_cursor_input.model_rebuild()
eetschema_group_obj_rel_insert_input.model_rebuild()
eetschema_group_on_conflict.model_rebuild()
eetschema_group_order_by.model_rebuild()
eetschema_group_statistics_2_aggregate_order_by.model_rebuild()
eetschema_group_statistics_2_bool_exp.model_rebuild()
eetschema_group_statistics_2_order_by.model_rebuild()
eetschema_group_statistics_2_stream_cursor_input.model_rebuild()
eetschema_group_statistics_bool_exp.model_rebuild()
eetschema_group_statistics_order_by.model_rebuild()
eetschema_group_statistics_stream_cursor_input.model_rebuild()
eetschema_group_stream_cursor_input.model_rebuild()
eetschema_group_summary_aggregate_order_by.model_rebuild()
eetschema_group_summary_bool_exp.model_rebuild()
eetschema_group_summary_order_by.model_rebuild()
eetschema_group_summary_stream_cursor_input.model_rebuild()
eetschema_group_updates.model_rebuild()
eetschema_list_aggregate_order_by.model_rebuild()
eetschema_list_arr_rel_insert_input.model_rebuild()
eetschema_list_bool_exp.model_rebuild()
eetschema_list_insert_input.model_rebuild()
eetschema_list_on_conflict.model_rebuild()
eetschema_list_order_by.model_rebuild()
eetschema_list_stream_cursor_input.model_rebuild()
eetschema_list_updates.model_rebuild()
eetschema_notification_aggregate_order_by.model_rebuild()
eetschema_notification_bool_exp.model_rebuild()
eetschema_notification_logs_aggregate_order_by.model_rebuild()
eetschema_notification_logs_bool_exp.model_rebuild()
eetschema_notification_logs_order_by.model_rebuild()
eetschema_notification_logs_stream_cursor_input.model_rebuild()
eetschema_notification_logs_updates.model_rebuild()
eetschema_notification_on_conflict.model_rebuild()
eetschema_notification_order_by.model_rebuild()
eetschema_notification_stream_cursor_input.model_rebuild()
eetschema_notification_updates.model_rebuild()
eetschema_settlements_aggregate_order_by.model_rebuild()
eetschema_settlements_bool_exp.model_rebuild()
eetschema_settlements_insert_input.model_rebuild()
eetschema_settlements_obj_rel_insert_input.model_rebuild()
eetschema_settlements_on_conflict.model_rebuild()
eetschema_settlements_order_by.model_rebuild()
eetschema_settlements_stream_cursor_input.model_rebuild()
eetschema_user_bool_exp.model_rebuild()
eetschema_user_order_by.model_rebuild()
eetschema_user_private_bool_exp.model_rebuild()
eetschema_user_private_stream_cursor_input.model_rebuild()
eetschema_user_private_updates.model_rebuild()
eetschema_user_stream_cursor_input.model_rebuild()
eetschema_user_updates.model_rebuild()
eetschema_users_in_group_aggregate_order_by.model_rebuild()
eetschema_users_in_group_arr_rel_insert_input.model_rebuild()
eetschema_users_in_group_bool_exp.model_rebuild()
eetschema_users_in_group_insert_input.model_rebuild()
eetschema_users_in_group_obj_rel_insert_input.model_rebuild()
eetschema_users_in_group_on_conflict.model_rebuild()
eetschema_users_in_group_order_by.model_rebuild()
eetschema_users_in_group_stream_cursor_input.model_rebuild()
eetschema_users_in_group_updates.model_rebuild()
recipe_review_aggregate_bool_exp.model_rebuild()
recipe_review_aggregate_bool_exp_count.model_rebuild()
recipe_review_aggregate_order_by.model_rebuild()
recipe_review_arr_rel_insert_input.model_rebuild()
recipe_review_bool_exp.model_rebuild()
recipe_review_insert_input.model_rebuild()
recipe_review_on_conflict.model_rebuild()
recipe_review_order_by.model_rebuild()
recipe_review_stream_cursor_input.model_rebuild()
recipe_review_updates.model_rebuild()
recipes_aggregate_bool_exp.model_rebuild()
recipes_aggregate_bool_exp_bool_and.model_rebuild()
recipes_aggregate_bool_exp_bool_or.model_rebuild()
recipes_aggregate_bool_exp_count.model_rebuild()
recipes_aggregate_order_by.model_rebuild()
recipes_bool_exp.model_rebuild()
recipes_insert_input.model_rebuild()
recipes_obj_rel_insert_input.model_rebuild()
recipes_on_conflict.model_rebuild()
recipes_order_by.model_rebuild()
recipes_stream_cursor_input.model_rebuild()
recipes_updates.model_rebuild()
