from datetime import datetime
from typing import Any, Optional

from .base_model import BaseModel


class AppStatusFields(BaseModel):
    id: str
    beta_online: bool
    updated_at: datetime


class AttendanceFields(BaseModel):
    created_at: datetime
    updated_at: datetime
    comment: Optional[str]
    number_guests: int
    status: str
    linked_event: "AttendanceFieldsLinkedEvent"
    user_in_group: Optional["AttendanceFieldsUserInGroup"]


class AttendanceFieldsLinkedEvent(BaseModel):
    id: str
    name: str


class AttendanceFieldsUserInGroup(BaseModel):
    order: Optional[int]
    user: "AttendanceFieldsUserInGroupUser"


class AttendanceFieldsUserInGroupUser(BaseModel):
    id: str
    name: str


class ExpenseFields(BaseModel):
    id: str
    event_id: Optional[str]
    settled_id: Optional[str]
    description: str
    payed_amount: int
    deleted: bool
    settlement_expense_id: Optional[str]
    expense_distributions: list["ExpenseFieldsExpenseDistributions"]
    payed_at: datetime
    payed_by: "ExpenseFieldsPayedBy"
    updated_at: datetime
    updated_by: Optional["ExpenseFieldsUpdatedBy"]


class ExpenseFieldsExpenseDistributions(BaseModel):
    id: str
    count: int
    payed_amount: int
    user: "ExpenseFieldsExpenseDistributionsUser"


class ExpenseFieldsExpenseDistributionsUser(BaseModel):
    id: str
    name: str


class ExpenseFieldsPayedBy(BaseModel):
    id: str
    name: str


class ExpenseFieldsUpdatedBy(BaseModel):
    id: str
    name: str


class EventFields(BaseModel):
    id: str
    group_id: str
    open: bool
    start_date: datetime
    closed_by: Optional[str]
    signup_deadline: Optional[datetime]
    changed_signup_time: bool
    name: str
    description: Optional[str]
    user: Optional["EventFieldsUser"]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    linked_expenses: Optional[list["EventFieldsLinkedExpenses"]] = None
    event_attendees: Optional[list["EventFieldsEventAttendees"]] = None


class EventFieldsUser(BaseModel):
    id: str
    name: str


class EventFieldsLinkedExpenses(ExpenseFields):
    pass


class EventFieldsEventAttendees(AttendanceFields):
    pass


class GroupFields(BaseModel):
    id: str
    name: str
    default_close_time: Optional[datetime]
    created_at: datetime
    created_at_eetlijst: Optional[datetime]
    statistics_start_date: Optional[datetime]
    statistics_end_date: Optional[datetime]
    invite_uuid: str
    invite_open: bool
    description: Optional[str]
    summary: list["GroupFieldsSummary"]


class GroupFieldsSummary(BaseModel):
    payed_total: Optional[Any]
    user_id: Optional[str]


class ListItemFields(BaseModel):
    active: bool
    checked: bool
    group_id: str
    id: str
    text: str
    recipe_id: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


class SettlementFields(BaseModel):
    id: str
    group_id: str
    created_at: datetime
    updated_at: datetime
    created_by: "SettlementFieldsCreatedBy"
    expenses_total: "SettlementFieldsExpensesTotal"
    adjustments_total: "SettlementFieldsAdjustmentsTotal"


class SettlementFieldsCreatedBy(BaseModel):
    id: str
    name: str


class SettlementFieldsExpensesTotal(BaseModel):
    aggregate: Optional["SettlementFieldsExpensesTotalAggregate"]


class SettlementFieldsExpensesTotalAggregate(BaseModel):
    sum: Optional["SettlementFieldsExpensesTotalAggregateSum"]


class SettlementFieldsExpensesTotalAggregateSum(BaseModel):
    payed_amount: Optional[int]


class SettlementFieldsAdjustmentsTotal(BaseModel):
    aggregate: Optional["SettlementFieldsAdjustmentsTotalAggregate"]


class SettlementFieldsAdjustmentsTotalAggregate(BaseModel):
    sum: Optional["SettlementFieldsAdjustmentsTotalAggregateSum"]


class SettlementFieldsAdjustmentsTotalAggregateSum(BaseModel):
    payed_amount: Optional[int]


class UserFields(BaseModel):
    id: str
    origin: Optional[str]
    name: str
    email: Optional[str]
    allergies: list[str]
    birthday: Optional[datetime]
    profile_image: Optional[str]
    order_of_buttom_bar: Optional[list[str]]
    wants_to_recieve_notifications: bool
    funnel_lead: Optional[list[str]]
    cook_points_imports: list["UserFieldsCookPointsImports"]


class UserFieldsCookPointsImports(BaseModel):
    group_id: str
    cook_points: float
    allowed_to_edit: bool


class UserFieldsPrivate(BaseModel):
    id: Optional[str]
    active: Optional[bool]
    origin: Optional[str]
    last_seen: Optional[datetime]
    name: Optional[str]
    email: Optional[str]
    address: Optional[str]
    phone_nr: Optional[str]
    bank_account: Optional[str]
    allergies: Optional[list[str]]
    birthday: Optional[datetime]
    profile_image: Optional[str]
    order_of_buttom_bar: Optional[list[str]]
    default_landingpage: Optional[str]
    wants_to_recieve_notifications: Optional[bool]
    is_color_blind: Optional[bool]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


class UserInGroupFields(BaseModel):
    active: bool
    order: Optional[int]
    start_holliday: Optional[datetime]
    end_holliday: Optional[datetime]
    monday: Optional[str]
    tuesday: Optional[str]
    wednesday: Optional[str]
    thursday: Optional[str]
    friday: Optional[str]
    saturday: Optional[str]
    sunday: Optional[str]
    user: "UserInGroupFieldsUser"


class UserInGroupFieldsUser(UserFields):
    pass


AppStatusFields.model_rebuild()
AttendanceFields.model_rebuild()
ExpenseFields.model_rebuild()
EventFields.model_rebuild()
GroupFields.model_rebuild()
ListItemFields.model_rebuild()
SettlementFields.model_rebuild()
UserFields.model_rebuild()
UserFieldsPrivate.model_rebuild()
UserInGroupFields.model_rebuild()
