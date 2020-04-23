"""Models for currents API."""
# pylint: disable=no-name-in-module
from typing import List

from pydantic import BaseModel, Field


class DataItem(BaseModel):
    """Data Schema."""

    station: str = Field(..., title="Title")
    name: str = Field(..., title="Title")
    county: str = Field(..., title="Title")
    state: str = Field(..., title="Title")
    network: str = Field(..., title="Title")
    local_date: str = Field(..., title="Title")
    snow: str = Field(..., title="Title")
    snowd: str = Field(..., title="Title")
    snoww: str = Field(..., title="Title")
    utc_valid: str = Field(..., title="Title")
    local_valid: str = Field(..., title="Title")
    tmpf: str = Field(..., title="Title")
    max_tmpf: str = Field(..., title="Title")
    min_tmpf: str = Field(..., title="Title")
    dwpf: str = Field(..., title="Title")
    relh: str = Field(..., title="Title")
    vsby: str = Field(..., title="Title")
    sknt: str = Field(..., title="Title")
    drct: str = Field(..., title="Title")
    c1smv: str = Field(..., title="Title")
    c2smv: str = Field(..., title="Title")
    c3smv: str = Field(..., title="Title")
    c4smv: str = Field(..., title="Title")
    c5smv: str = Field(..., title="Title")
    c1tmpf: str = Field(..., title="Title")
    c2tmpf: str = Field(..., title="Title")
    c3tmpf: str = Field(..., title="Title")
    c4tmpf: str = Field(..., title="Title")
    c5tmpf: str = Field(..., title="Title")
    ob_pday: str = Field(..., title="Title")
    ob_pmonth: str = Field(..., title="Title")
    s_pmonth: str = Field(..., title="Title")
    max_sknt: str = Field(..., title="Title")
    max_gust: str = Field(..., title="Title")
    gust: str = Field(..., title="Title")
    mslp: str = Field(..., title="Title")
    pres: str = Field(..., title="Title")
    scond0: str = Field(..., title="Title")
    scond1: str = Field(..., title="Title")
    scond2: str = Field(..., title="Title")
    scond3: str = Field(..., title="Title")
    srad: str = Field(..., title="Title")
    tsf0: str = Field(..., title="Title")
    tsf1: str = Field(..., title="Title")
    tsf2: str = Field(..., title="Title")
    tsf3: str = Field(..., title="Title")
    rwis_subf: str = Field(..., title="Title")
    raw: str = Field(..., title="Title")
    phour: str = Field(..., title="Title")
    feel: str = Field(..., title="Title")
    ice_accretion_1hr: str = Field(..., title="Title")
    ice_accretion_3hr: str = Field(..., title="Title")
    ice_accretion_6hr: str = Field(..., title="Title")
    skyl1: str = Field(..., title="Title")
    skyc1: str = Field(..., title="Title")
    skyl2: str = Field(..., title="Title")
    skyc2: str = Field(..., title="Title")
    skyl3: str = Field(..., title="Title")
    skyc3: str = Field(..., title="Title")
    skyl4: str = Field(..., title="Title")
    skyc4: str = Field(..., title="Title")
    alti: str = Field(..., title="Title")
    wxcodes: str = Field(..., title="Title")
    utc_max_gust_ts: str = Field(..., title="Title")
    local_max_gust_ts: str = Field(..., title="Title")
    utc_max_sknt_ts: str = Field(..., title="Title")
    local_max_sknt_ts: str = Field(..., title="Title")
    lon: str = Field(..., title="Title")
    lat: str = Field(..., title="Title")
    pday: str = Field(..., title="Title")


class RootSchema(BaseModel):
    """The schema used by this service."""

    data: List[DataItem]
