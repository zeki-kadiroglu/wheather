"""Pydantic models for the API."""
from typing import Dict, List, Optional

from fastapi import Query
from pydantic import BaseModel, Field


class CurrentTemperatures(BaseModel):
    """Expected parameters that comes from user."""

    city: str = Field(
         title="city", description="city name is a necessary input"
    )
    date: Optional[str] = None
    temperature_type: str
    days: Optional[int] = Field(None, lt=7)
