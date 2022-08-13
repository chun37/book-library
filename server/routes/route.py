from dataclasses import dataclass
from enum import Enum
from typing import Any, Callable, Dict, List, Optional, Sequence, Set, Type

from fastapi import params
from fastapi.datastructures import Default, DefaultPlaceholder
from fastapi.encoders import DictIntStrAny, SetIntStr
from fastapi.routing import APIRoute
from starlette.responses import JSONResponse, Response
from starlette.routing import BaseRoute


# pylint: disable=too-many-instance-attributes
@dataclass(frozen=True)
class Route:
    path: str
    endpoint: Callable[..., Any]
    response_model: Optional[Type[Any]] = None
    status_code: Optional[int] = None
    tags: Optional[List[str | Enum]] = None
    dependencies: Optional[Sequence[params.Depends]] = None
    summary: Optional[str] = None
    description: Optional[str] = None
    response_description: str = "Successful Response"
    responses: Optional[Dict[int | str, Dict[str, Any]]] = None
    deprecated: Optional[bool] = None
    methods: Optional[Set[str] | List[str]] = None
    operation_id: Optional[str] = None
    response_model_include: Optional[SetIntStr | DictIntStrAny] = None
    response_model_exclude: Optional[SetIntStr | DictIntStrAny] = None
    response_model_by_alias: bool = True
    response_model_exclude_unset: bool = False
    response_model_exclude_defaults: bool = False
    response_model_exclude_none: bool = False
    include_in_schema: bool = True
    response_class: Type[Response] | DefaultPlaceholder = Default(JSONResponse)
    name: Optional[str] = None
    route_class_override: Optional[Type[APIRoute]] = None
    callbacks: Optional[List[BaseRoute]] = None
    openapi_extra: Optional[Dict[str, Any]] = None
