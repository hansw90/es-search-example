from datetime import datetime

def defaultconverter(self, o):
        if isinstance(o, datetime):
            return o.isoformat()

def del_none(d):
    
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
    return d  # For convenience