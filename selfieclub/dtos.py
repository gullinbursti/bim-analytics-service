"""Selfieclub event endpoint User Data Transfer Objects (DTO)."""


class UserDto(object):
    # Simple DTO.  pylint: disable=too-few-public-methods

    """User Data Transfer Object (DTO)."""

    def __init__(self, id_, name, cohort_date, cohort_week):
        """Create an instance of UserDto."""
        self.id_ = id_
        self.name = name
        self.cohort_date = cohort_date
        self.cohort_week = cohort_week
