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


class DeviceDto(object):
    # pylint: disable=too-few-public-methods, too-many-instance-attributes

    """Device Data Transfer Object (DTO)."""

    def __init__(
            self, adid, battery_per, cpu, density, hardware_make,
            hardware_model, locale, orientation, orientation_deg, os_,
            os_version, resolution_x, resolution_y, time, token, tz_,
            user_agent):
        # pylint: disable=too-many-locals, too-many-arguments
        """Create an instance of DeviceDto."""
        self.adid = adid
        self.battery_per = battery_per
        self.cpu = cpu
        self.density = density
        self.hardware_make = hardware_make
        self.hardware_model = hardware_model
        self.locale = locale
        self.orientation = orientation
        self.orientation_deg = orientation_deg
        self.os_ = os_
        self.os_version = os_version
        self.resolution_x = resolution_x
        self.resolution_y = resolution_y
        self.time = time
        self.token = token
        self.tz_ = tz_
        self.user_agent = user_agent
