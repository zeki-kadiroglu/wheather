"""Pydantic models for the API."""
from typing import Dict, List, Optional

from pydantic import BaseModel, Field


class QueryParameters(BaseModel):
    """Expected parameters that comes from user."""

    city: str = Field(
        None, title="city", description="city name is a necessary input"
    )
    filters: Optional[Dict]
    columns: List