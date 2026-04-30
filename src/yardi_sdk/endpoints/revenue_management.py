import os


class GetPropertyConfigurations:
    """Interface: Revenue Management."""
    def __init__(
        self,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None
    ):
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")


class GetProperty_Login:
    """Interface: Revenue Management."""
    def __init__(
        self,
        YardiPropertyId: str,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")


class GetRawProperty_Login:
    """Interface: Revenue Management."""
    def __init__(
        self,
        YardiPropertyId: str,
        IncludeUnitSection: bool,
        IncludeChargeSection: bool,
        IncludeLeaseSection: bool,
        IncludeGuestCardSection: bool,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.IncludeUnitSection = IncludeUnitSection
        self.IncludeChargeSection = IncludeChargeSection
        self.IncludeLeaseSection = IncludeLeaseSection
        self.IncludeGuestCardSection = IncludeGuestCardSection
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")


class GetProperty_Params_Login:
    """Interface: Revenue Management."""
    def __init__(
        self,
        YardiPropertyId: str,
        IncludeCommunitySection: bool,
        IncludeUnitTypeSection: bool,
        IncludeUnitSection: bool,
        IncludeAmenitySection: bool,
        IncludeChargeSection: bool,
        ChargesBySummary: bool,
        NumDaysChargeHistory: str,
        IncludeIncomeCodeSection: bool,
        IncludeLeaseSection: bool,
        NumDaysLeaseHistory: str,
        IncludeGuestCardSection: bool,
        NumDaysGuestCardHistory: str,
        ShowAllGuestCards: bool,
        IncludeAllUnits: bool,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.IncludeCommunitySection = IncludeCommunitySection
        self.IncludeUnitTypeSection = IncludeUnitTypeSection
        self.IncludeUnitSection = IncludeUnitSection
        self.IncludeAmenitySection = IncludeAmenitySection
        self.IncludeChargeSection = IncludeChargeSection
        self.ChargesBySummary = ChargesBySummary
        self.NumDaysChargeHistory = NumDaysChargeHistory
        self.IncludeIncomeCodeSection = IncludeIncomeCodeSection
        self.IncludeLeaseSection = IncludeLeaseSection
        self.NumDaysLeaseHistory = NumDaysLeaseHistory
        self.IncludeGuestCardSection = IncludeGuestCardSection
        self.NumDaysGuestCardHistory = NumDaysGuestCardHistory
        self.ShowAllGuestCards = ShowAllGuestCards
        self.IncludeAllUnits = IncludeAllUnits
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")


class ImportRM_Login:
    """Interface: Revenue Management."""
    def __init__(
        self,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        XmlDoc: str = None
    ):
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.XmlDoc = XmlDoc


class ImportMR_Login:
    """Interface: Revenue Management."""
    def __init__(
        self,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        XmlDoc: str = None
    ):
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.XmlDoc = XmlDoc


class GetVersionNumber_Str:
    """Interface: Revenue Management."""
    def __init__(self):
        pass


class GetVersionNumber:
    """Interface: Revenue Management."""
    def __init__(self):
        pass


class Ping:
    """Interface: Revenue Management."""
    def __init__(self):
        pass


