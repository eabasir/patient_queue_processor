from enum import Enum

class PATIENT_STATUS(Enum):
    WAITING = 'waiting'
    BEDRID = 'bedrid'
    DISCHARGE = 'discharge'
    REVISIT = 'revisit'