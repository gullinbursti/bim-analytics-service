"""Selfieclub event endpoint Member Data Transfer Objects (DTO)."""


class MemberDto(object):
    # Simple DTO.  pylint: disable=too-few-public-methods

    """Member Data Transfer Object (DTO)."""

    def __init__(self, id_, name, cohort_date, cohort_week):
        """Create an instance of MemberDto."""
        self.id_ = id_
        self.name = name
        self.cohort_date = cohort_date
        self.cohort_week = cohort_week
