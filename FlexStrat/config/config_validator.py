from typing import Dict, List, Optional
from pydantic import BaseModel, Field

class SourceConfig(BaseModel):
    src: List[str] = Field(..., min_length=1)
    hierarchy: Optional[List[str]] = Field(default_factory=list)

class ModuleConfig(BaseModel):
    api: SourceConfig
    indicator: SourceConfig
    scripts: SourceConfig
    visualizer: SourceConfig

