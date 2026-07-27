from enum import Enum


class AttendanceStatus(str, Enum):
    cook = "cook"
    eat_only = "eat_only"
    got_groceries = "got_groceries"
    not_attending = "not_attending"


class ads_ads_select_column(str, Enum):
    btn_text = "btn_text"
    description = "description"
    header = "header"
    id = "id"
    image_url = "image_url"
    platform = "platform"
    target_user_type = "target_user_type"
    url = "url"


class ads_ads_targeting_select_column(str, Enum):
    ads_id = "ads_id"
    targeting_id = "targeting_id"


class ads_interaction_constraint(str, Enum):
    interaction_pkey = "interaction_pkey"


class ads_interaction_update_column(str, Enum):
    _PLACEHOLDER = "_PLACEHOLDER"


class ads_targeting_select_column(str, Enum):
    city = "city"
    id = "id"


class cursor_ordering(str, Enum):
    ASC = "ASC"
    DESC = "DESC"


class eetschema_app_status_select_column(str, Enum):
    beta_online = "beta_online"
    created_at = "created_at"
    id = "id"
    updated_at = "updated_at"


class eetschema_cook_points_import_constraint(str, Enum):
    cook_points_import_pkey = "cook_points_import_pkey"


class eetschema_cook_points_import_select_column(str, Enum):
    allowed_to_edit = "allowed_to_edit"
    cook_points = "cook_points"
    created_at = "created_at"
    group_id = "group_id"
    updated_at = "updated_at"
    user_id = "user_id"


class eetschema_cook_points_import_update_column(str, Enum):
    cook_points = "cook_points"


class eetschema_event_attendees_constraint(str, Enum):
    event_attending_members_pkey = "event_attending_members_pkey"


class eetschema_event_attendees_select_column(str, Enum):
    comment = "comment"
    created_at = "created_at"
    event_id = "event_id"
    number_guests = "number_guests"
    status = "status"
    updated_at = "updated_at"
    user_changed_status = "user_changed_status"
    user_id = "user_id"


class eetschema_event_attendees_update_column(str, Enum):
    comment = "comment"
    number_guests = "number_guests"
    status = "status"
    updated_at = "updated_at"
    user_changed_status = "user_changed_status"
    user_id = "user_id"


class eetschema_event_attendees_view_select_column(str, Enum):
    active = "active"
    comment = "comment"
    event_id = "event_id"
    friday = "friday"
    group_id = "group_id"
    monday = "monday"
    number_guests = "number_guests"
    order = "order"
    saturday = "saturday"
    status = "status"
    sunday = "sunday"
    thursday = "thursday"
    tuesday = "tuesday"
    user_id = "user_id"
    wednesday = "wednesday"


class eetschema_event_constraint(str, Enum):
    event_pkey = "event_pkey"


class eetschema_event_select_column(str, Enum):
    changed_signup_time = "changed_signup_time"
    closed_by = "closed_by"
    created_at = "created_at"
    created_by = "created_by"
    description = "description"
    end_date = "end_date"
    expense_id = "expense_id"
    group_id = "group_id"
    id = "id"
    name = "name"
    open = "open"
    signup_deadline = "signup_deadline"
    start_date = "start_date"
    type_ = "type"
    updated_at = "updated_at"


class eetschema_event_select_column_eetschema_event_aggregate_bool_exp_bool_and_arguments_columns(
    str, Enum
):
    changed_signup_time = "changed_signup_time"
    open = "open"


class eetschema_event_select_column_eetschema_event_aggregate_bool_exp_bool_or_arguments_columns(
    str, Enum
):
    changed_signup_time = "changed_signup_time"
    open = "open"


class eetschema_event_statistics_old_import_select_column(str, Enum):
    event_start_date = "event_start_date"
    group_id = "group_id"
    num_cooked = "num_cooked"
    num_does_groceries = "num_does_groceries"
    num_eat_only = "num_eat_only"
    user_id = "user_id"


class eetschema_event_statistics_select_column(str, Enum):
    cook_points = "cook_points"
    event_id = "event_id"
    event_start_date = "event_start_date"
    group_id = "group_id"
    number_guests = "number_guests"
    status = "status"
    total_number_of_eaters = "total_number_of_eaters"
    user_id = "user_id"


class eetschema_event_update_column(str, Enum):
    changed_signup_time = "changed_signup_time"
    closed_by = "closed_by"
    description = "description"
    end_date = "end_date"
    name = "name"
    open = "open"
    signup_deadline = "signup_deadline"
    start_date = "start_date"


class eetschema_expense_constraint(str, Enum):
    expense_pkey = "expense_pkey"


class eetschema_expense_distribution_constraint(str, Enum):
    expense_distribution_pkey = "expense_distribution_pkey"


class eetschema_expense_distribution_select_column(str, Enum):
    count = "count"
    created_at = "created_at"
    expense_id = "expense_id"
    id = "id"
    payed_amount = "payed_amount"
    updated_at = "updated_at"
    user_id = "user_id"


class eetschema_expense_distribution_update_column(str, Enum):
    count = "count"
    created_at = "created_at"
    expense_id = "expense_id"
    id = "id"
    payed_amount = "payed_amount"
    updated_at = "updated_at"
    user_id = "user_id"


class eetschema_expense_eetlijst_import_select_column(str, Enum):
    group_id = "group_id"
    payed_amount = "payed_amount"


class eetschema_expense_select_column(str, Enum):
    created_at = "created_at"
    deleted = "deleted"
    description = "description"
    event_id = "event_id"
    group_id = "group_id"
    id = "id"
    issued_by = "issued_by"
    payed_amount = "payed_amount"
    payed_at = "payed_at"
    payed_by = "payed_by"
    settled_id = "settled_id"
    settlement_expense_id = "settlement_expense_id"
    updated_at = "updated_at"
    updated_by = "updated_by"


class eetschema_expense_select_column_eetschema_expense_aggregate_bool_exp_bool_and_arguments_columns(
    str, Enum
):
    deleted = "deleted"


class eetschema_expense_select_column_eetschema_expense_aggregate_bool_exp_bool_or_arguments_columns(
    str, Enum
):
    deleted = "deleted"


class eetschema_expense_update_column(str, Enum):
    deleted = "deleted"
    description = "description"
    issued_by = "issued_by"
    payed_amount = "payed_amount"
    payed_at = "payed_at"
    payed_by = "payed_by"
    settled_id = "settled_id"
    settlement_expense_id = "settlement_expense_id"
    updated_by = "updated_by"


class eetschema_group_constraint(str, Enum):
    group_login_name_key = "group_login_name_key"
    group_pkey = "group_pkey"


class eetschema_group_invite_select_column(str, Enum):
    id = "id"
    invite_uuid = "invite_uuid"


class eetschema_group_select_column(str, Enum):
    active = "active"
    address = "address"
    beta = "beta"
    city = "city"
    created_at = "created_at"
    created_at_eetlijst = "created_at_eetlijst"
    default_close_time = "default_close_time"
    default_status = "default_status"
    description = "description"
    email = "email"
    id = "id"
    invite_open = "invite_open"
    invite_uuid = "invite_uuid"
    login_name = "login_name"
    name = "name"
    pincode = "pincode"
    statistics_end_date = "statistics_end_date"
    statistics_start_date = "statistics_start_date"
    updated_at = "updated_at"


class eetschema_group_statistics_2_select_column(str, Enum):
    cook_points = "cook_points"
    group_id = "group_id"
    minus_points = "minus_points"
    num_cooked = "num_cooked"
    num_eat = "num_eat"
    num_groceries = "num_groceries"
    num_not_attended = "num_not_attended"
    number_guests = "number_guests"
    user_id = "user_id"


class eetschema_group_statistics_select_column(str, Enum):
    count = "count"
    group_id = "group_id"
    number_guests = "number_guests"
    status = "status"
    user_id = "user_id"


class eetschema_group_summary_select_column(str, Enum):
    group_id = "group_id"
    payed_total = "payed_total"
    user_id = "user_id"


class eetschema_group_update_column(str, Enum):
    beta = "beta"
    default_close_time = "default_close_time"
    description = "description"
    invite_uuid = "invite_uuid"
    name = "name"
    statistics_end_date = "statistics_end_date"
    statistics_start_date = "statistics_start_date"


class eetschema_list_constraint(str, Enum):
    list_pkey = "list_pkey"


class eetschema_list_select_column(str, Enum):
    active = "active"
    checked = "checked"
    created_at = "created_at"
    group_id = "group_id"
    id = "id"
    recipe_id = "recipe_id"
    text = "text"
    updated_at = "updated_at"


class eetschema_list_update_column(str, Enum):
    active = "active"
    checked = "checked"
    group_id = "group_id"
    recipe_id = "recipe_id"
    text = "text"


class eetschema_notification_constraint(str, Enum):
    notification_device_token_key = "notification_device_token_key"
    notifications_pkey = "notifications_pkey"


class eetschema_notification_logs_select_column(str, Enum):
    body = "body"
    created_at = "created_at"
    data = "data"
    device_token = "device_token"
    id = "id"
    opened_by_user = "opened_by_user"
    send_by = "send_by"
    title = "title"
    updated_at = "updated_at"
    user_id = "user_id"


class eetschema_notification_select_column(str, Enum):
    Timestamp = "Timestamp"
    body = "body"
    created_at = "created_at"
    device = "device"
    device_token = "device_token"
    id = "id"
    platform = "platform"
    title = "title"
    updated_at = "updated_at"
    user_id = "user_id"
    wants_to_recieve = "wants_to_recieve"


class eetschema_notification_update_column(str, Enum):
    body = "body"
    device = "device"
    device_token = "device_token"
    id = "id"
    platform = "platform"
    title = "title"
    wants_to_recieve = "wants_to_recieve"


class eetschema_settlements_constraint(str, Enum):
    settlements_pkey = "settlements_pkey"


class eetschema_settlements_select_column(str, Enum):
    created_at = "created_at"
    created_by = "created_by"
    group_id = "group_id"
    id = "id"
    updated_at = "updated_at"


class eetschema_settlements_update_column(str, Enum):
    _PLACEHOLDER = "_PLACEHOLDER"


class eetschema_user_private_select_column(str, Enum):
    active = "active"
    address = "address"
    alias = "alias"
    allergies = "allergies"
    bank_account = "bank_account"
    birthday = "birthday"
    created_at = "created_at"
    default_landingpage = "default_landingpage"
    email = "email"
    id = "id"
    is_color_blind = "is_color_blind"
    last_seen = "last_seen"
    name = "name"
    old_id = "old_id"
    order_of_buttom_bar = "order_of_buttom_bar"
    origin = "origin"
    phone_nr = "phone_nr"
    profile_image = "profile_image"
    updated_at = "updated_at"
    wants_to_recieve_notifications = "wants_to_recieve_notifications"


class eetschema_user_select_column(str, Enum):
    alias = "alias"
    allergies = "allergies"
    birthday = "birthday"
    default_language = "default_language"
    email = "email"
    funnel_lead = "funnel_lead"
    id = "id"
    name = "name"
    order_of_buttom_bar = "order_of_buttom_bar"
    origin = "origin"
    profile_image = "profile_image"
    reason_to_remove_account_selection = "reason_to_remove_account_selection"
    reason_to_remove_account_selection_all_options = (
        "reason_to_remove_account_selection_all_options"
    )
    reason_to_remove_account_text = "reason_to_remove_account_text"
    wants_to_recieve_notifications = "wants_to_recieve_notifications"


class eetschema_users_in_group_constraint(str, Enum):
    users_in_group_pkey = "users_in_group_pkey"


class eetschema_users_in_group_select_column(str, Enum):
    active = "active"
    end_holliday = "end_holliday"
    event_id = "event_id"
    friday = "friday"
    group_id = "group_id"
    monday = "monday"
    order = "order"
    saturday = "saturday"
    start_holliday = "start_holliday"
    sunday = "sunday"
    thursday = "thursday"
    tuesday = "tuesday"
    user_id = "user_id"
    wednesday = "wednesday"


class eetschema_users_in_group_update_column(str, Enum):
    active = "active"
    end_holliday = "end_holliday"
    friday = "friday"
    monday = "monday"
    order = "order"
    saturday = "saturday"
    start_holliday = "start_holliday"
    sunday = "sunday"
    thursday = "thursday"
    tuesday = "tuesday"
    wednesday = "wednesday"


class order_by(str, Enum):
    asc = "asc"
    asc_nulls_first = "asc_nulls_first"
    asc_nulls_last = "asc_nulls_last"
    desc = "desc"
    desc_nulls_first = "desc_nulls_first"
    desc_nulls_last = "desc_nulls_last"


class recipe_review_constraint(str, Enum):
    recipe_review_pkey = "recipe_review_pkey"


class recipe_review_select_column(str, Enum):
    rating = "rating"
    user_id = "user_id"


class recipe_review_update_column(str, Enum):
    rating = "rating"


class recipes_constraint(str, Enum):
    recipes_pkey = "recipes_pkey"


class recipes_select_column(str, Enum):
    cook_time = "cook_time"
    course_category = "course_category"
    created_at = "created_at"
    description = "description"
    id = "id"
    image_url = "image_url"
    ingredients = "ingredients"
    instructions = "instructions"
    is_deleted = "is_deleted"
    is_shared = "is_shared"
    language = "language"
    original_host = "original_host"
    original_url = "original_url"
    owner_id = "owner_id"
    prep_time = "prep_time"
    servings = "servings"
    title = "title"
    total_time = "total_time"
    updated_at = "updated_at"


class recipes_select_column_recipes_aggregate_bool_exp_bool_and_arguments_columns(
    str, Enum
):
    is_deleted = "is_deleted"
    is_shared = "is_shared"


class recipes_select_column_recipes_aggregate_bool_exp_bool_or_arguments_columns(
    str, Enum
):
    is_deleted = "is_deleted"
    is_shared = "is_shared"


class recipes_update_column(str, Enum):
    cook_time = "cook_time"
    course_category = "course_category"
    description = "description"
    image_url = "image_url"
    ingredients = "ingredients"
    instructions = "instructions"
    is_deleted = "is_deleted"
    is_shared = "is_shared"
    language = "language"
    original_host = "original_host"
    prep_time = "prep_time"
    servings = "servings"
    title = "title"
    total_time = "total_time"
