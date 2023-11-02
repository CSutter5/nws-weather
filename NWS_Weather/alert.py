from datetime import datetime
from typing import List, Tuple

def check_if_none(value, return_value=0):
    """Returns 0 if the value is None

    Args:
        value: Any value you want to check to see if it is None
        return_value: The value to return if the value is None

    Returns:
        return_value if the value is None, otherwise the value 
    """
    if value == None:
        return return_value
    return value

class alert:
    
    polygon: List[Tuple[int, int]]
    
    id: str
    area_desc: str
    same_code: int
    ugc_code: str
    affected_zoned: List[str]
    
    sent: datetime
    effective: datetime
    onset: datetime
    expires: datetime
    ends: datetime
    
    status: str
    message_type: str
    category: str
    severity: str
    certainty: str
    urgency: str
    event: str
    
    headline: str
    description: str
    instruction: str
    response: str
    
    def __init__(self, data: dict):
        self.id        = data["properties"]["id"]
        self.area_desc = data["properties"]["areaDesc"]
        self.same_code = data["properties"]["geocode"]["SAME"]
        self.ugc_code  = data["properties"]["geocode"]["UGC"]
        self.affected_zoned = data["properties"]["affectedZones"]

        self.sent       = datetime.strptime(data["properties"]["sent"], "%Y-%m-%dT%H:%M:%S%z")
        self.effective  = datetime.strptime(data["properties"]["effective"], "%Y-%m-%dT%H:%M:%S%z")
        self.onset      = datetime.strptime(check_if_none(data["properties"]["onset"], "3000-12-31T23:59:59-08:00"), "%Y-%m-%dT%H:%M:%S%z")
        self.expires    = datetime.strptime(data["properties"]["expires"], "%Y-%m-%dT%H:%M:%S%z")
        self.ends       = datetime.strptime(check_if_none(data["properties"]["ends"], "3000-12-31T23:59:59-08:00"), "%Y-%m-%dT%H:%M:%S%z")
        
        self.status         = data["properties"]["status"]
        self.message_type   = data["properties"]["messageType"]
        self.category       = data["properties"]["category"]
        self.severity       = data["properties"]["severity"]
        self.certainty      = data["properties"]["certainty"]
        self.urgency        = data["properties"]["urgency"]
        self.event          = data["properties"]["event"]
        
        self.headline    = data["properties"]["headline"]
        self.description = data["properties"]["description"]
        self.instruction = data["properties"]["instruction"]
        self.response    = data["properties"]["response"]
        
    def __str__(self):
        return f"""Alert: {self.id}
Area Description: {self.area_desc}
SAME Code: {self.same_code}
UGC Code: {self.ugc_code}
Affected Zones: {self.affected_zoned}

Sent: {self.sent}
Effective: {self.effective}
Onset: {self.onset}
Expires: {self.expires}
Ends: {self.ends}

Status: {self.status}
Message Type: {self.message_type}
Category: {self.category}
Severity: {self.severity}
Certainty: {self.certainty}
Urgency: {self.urgency}
Event: {self.event}

Headline: {self.headline}
Description: {self.description}
Instruction: {self.instruction}
Response: {self.response}
"""