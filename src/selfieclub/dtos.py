"""Selfieclub event endpoint Member Data Transfer Objects (DTO)."""


class MemberDto(object):
    # Simple DTO.  pylint: disable=too-few-public-methods

    """Member Data Transfer Object (DTO)."""

    def __init__(self, identifier, name, cohort_date, cohort_week):
        """Create an instance of MemberDto."""
        self.identifier = identifier
        self.name = name
        self.cohort_date = cohort_date
        self.cohort_week = cohort_week


class DeviceDto(object):
    # pylint: disable=too-few-public-methods, too-many-instance-attributes

    """Device Data Transfer Object (DTO)."""

    def __init__(
            self, adid, battery_per, cpu, pixel_density, hardware_make,
            hardware_model, locale, orientation, orientation_deg, platform,
            platform_version, resolution_x, resolution_y, time, timezone,
            user_agent):
        # pylint: disable=too-many-locals, too-many-arguments
        """Create an instance of DeviceDto."""
        self.adid = adid
        self.battery_per = battery_per
        self.cpu = cpu
        self.pixel_density = pixel_density
        self.hardware_make = hardware_make
        self.hardware_model = hardware_model
        self.locale = locale
        self.orientation = orientation
        self.orientation_deg = orientation_deg
        self.platform = platform
        self.platform_version = platform_version
        self.resolution_x = resolution_x
        self.resolution_y = resolution_y
        self.time = time
        self.timezone = timezone
        self.user_agent = user_agent
