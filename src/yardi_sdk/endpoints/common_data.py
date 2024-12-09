import os


class GetPropertyConfigurations:
    """Interface: Common Data."""
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


class GetPropertyConfigurationsNewFromDate:
    """Interface: Common Data."""
    def __init__(
        self,
        DateCreated: str = None,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None
    ):
        self.DateCreated = DateCreated
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")


class GetPropertyList:
    """Interface: Common Data."""
    def __init__(
        self,
        YardiPropertyId: str = None,
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


class GetPropertyOptions:
    """Interface: Common Data."""
    def __init__(
        self,
        YardiPropertyId: str = None,
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


class GetVendorOptions:
    """Interface: Common Data."""
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


class GetResidents:
    """Interface: Common Data."""
    def __init__(
        self,
        YardiPropertyId: str = None,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        MoveOut1: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.MoveOut1 = MoveOut1


class GetResidentData_ByChargeCode:
    """Interface: Common Data."""
    def __init__(
        self,
        YardiPropertyId: str = None,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        TenantCode: str = None,
        ChargeCode: str = None,
        FromDate: str = None,
        ToDate: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.TenantCode = TenantCode
        self.ChargeCode = ChargeCode
        self.FromDate = FromDate
        self.ToDate = ToDate


class GetResidentFromRoommate:
    """Interface: Common Data."""
    def __init__(
        self,
        YardiPropertyId: str = None,
        IncludeLedger: bool = None,
        LedgerAsOfDate: str = None,
        IncludeLeaseCharges: bool = None,
        IncludeVehicleInfo: bool = None,
        IncludeRoommateData: bool = None,
        IncludeEmployerData: bool = None,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        RoommateCode: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.IncludeLedger = IncludeLedger
        self.LedgerAsOfDate = LedgerAsOfDate
        self.IncludeLeaseCharges = IncludeLeaseCharges
        self.IncludeVehicleInfo = IncludeVehicleInfo
        self.IncludeRoommateData = IncludeRoommateData
        self.IncludeEmployerData = IncludeEmployerData
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.RoommateCode = RoommateCode


class GetResidentsByDate:
    """Interface: Common Data."""
    def __init__(
        self,
        YardiPropertyId: str = None,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        Status: str = None,
        ModifiedSinceDate: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.Status = Status
        self.ModifiedSinceDate = ModifiedSinceDate


class GetResidentsByStatus:
    """Interface: Common Data."""
    def __init__(
        self,
        YardiPropertyId: str = None,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        Status: str = None,
        DateFrom: str = None,
        DateTo: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.Status = Status
        self.DateFrom = DateFrom
        self.DateTo = DateTo


class GetResidentData:
    """Interface: Common Data."""
    def __init__(
        self,
        YardiPropertyId: str = None,
        IncludeLedger: bool = None,
        LedgerAsOfDate: str = None,
        IncludeLeaseCharges: bool = None,
        IncludeVehicleInfo: bool = None,
        IncludeRoommateData: bool = None,
        IncludeEmployerData: bool = None,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        TenantCode: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.IncludeLedger = IncludeLedger
        self.LedgerAsOfDate = LedgerAsOfDate
        self.IncludeLeaseCharges = IncludeLeaseCharges
        self.IncludeVehicleInfo = IncludeVehicleInfo
        self.IncludeRoommateData = IncludeRoommateData
        self.IncludeEmployerData = IncludeEmployerData
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.TenantCode = TenantCode


class GetOccupants:
    """Interface: Common Data."""
    def __init__(
        self,
        YardiPropertyId: str = None,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        TenantCode: str = None,
        UnitCode: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.TenantCode = TenantCode
        self.UnitCode = UnitCode


class UpdateResidentData:
    """Interface: Common Data."""
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


class ImportTenantLeaseDocumentPDF:
    """Interface: Common Data."""
    def __init__(
        self,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        DataBase: str = None,
        PropertyId: str = None,
        TenantCode: str = None,
        AttachmentType: str = None,
        Description: str = None,
        Attachment: str = None
    ):
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.DataBase = DataBase
        self.PropertyId = PropertyId
        self.TenantCode = TenantCode
        self.AttachmentType = AttachmentType
        self.Description = Description
        self.Attachment = Attachment


class ImportTenantLeaseDocumentExt:
    """Interface: Common Data."""
    def __init__(
        self,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        DataBase: str = None,
        PropertyId: str = None,
        TenantCode: str = None,
        AttachmentType: str = None,
        Description: str = None,
        Attachment: str = None,
        FileExtension: str = None
    ):
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.DataBase = DataBase
        self.PropertyId = PropertyId
        self.TenantCode = TenantCode
        self.AttachmentType = AttachmentType
        self.Description = Description
        self.Attachment = Attachment
        self.FileExtension = FileExtension


class GetTenantLeaseDocuments_DateRange:
    """Interface: Common Data."""
    def __init__(
        self,
        YardiPropertyId: str = None,
        DateFrom: str = None,
        DateTo: str = None,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        TenantCode: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.DateFrom = DateFrom
        self.DateTo = DateTo
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.TenantCode = TenantCode


class GetTenantLeaseDocuments:
    """Interface: Common Data."""
    def __init__(
        self,
        YardiPropertyId: str = None,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        TenantCode: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.TenantCode = TenantCode


class GetTenantDocument:
    """Interface: Common Data."""
    def __init__(
        self,
        YardiPropertyId: str = None,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        TenantCode: str = None,
        FileName: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.TenantCode = TenantCode
        self.FileName = FileName


class GetAttachmentTypes:
    """Interface: Common Data."""
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


class GetPermissions:
    """Interface: Common Data."""
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


class GetResidentsByUnit:
    """Interface: Common Data."""
    def __init__(
        self,
        YardiPropertyId: str = None,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        UnitId: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.UnitId = UnitId


class GetUserPropertyAccess:
    """Interface: Common Data."""
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


class GetRentroll:
    """Interface: Common Data."""
    def __init__(
        self,
        YardiPropertyId: str = None,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        UnitId: str = None,
        MoveIn: str = None,
        MoveOut: str = None,
        LeaseChgFrom: str = None,
        LeaseChgTo: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.UnitId = UnitId
        self.MoveIn = MoveIn
        self.MoveOut = MoveOut
        self.LeaseChgFrom = LeaseChgFrom
        self.LeaseChgTo = LeaseChgTo


class GetTenantStatus:
    """Interface: Common Data."""
    def __init__(
        self,
        YardiPropertyId: str = None,
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


class GetUnitInformation:
    """Interface: Common Data."""
    def __init__(
        self,
        YardiPropertyId: str = None,
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


class GetCurrentUnitInformation:
    """Interface: Common Data."""
    def __init__(
        self,
        YardiPropertyId: str = None,
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


class GetContacts:
    """Interface: Common Data."""
    def __init__(
        self,
        YardiPropertyId: str = None,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        TenantCode: str = None,
        ContactRoleType: str = None,
        ContactRoleDescription: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.TenantCode = TenantCode
        self.ContactRoleType = ContactRoleType
        self.ContactRoleDescription = ContactRoleDescription


class GetContactRoles:
    """Interface: Common Data."""
    def __init__(
        self,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        ContactRoleType: str = None
    ):
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.ContactRoleType = ContactRoleType


class GetUnitTransferData:
    """Interface: Common Data."""
    def __init__(
        self,
        YardiPropertyId: str = None,
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


class GetUnitTransferData_DateRange:
    """Interface: Common Data."""
    def __init__(
        self,
        YardiPropertyId: str = None,
        FromDate: str = None,
        ToDate: str = None,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.FromDate = FromDate
        self.ToDate = ToDate
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")


class GetSchedulers:
    """Interface: Common Data."""
    def __init__(
        self,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        UpdatedDate: str = None
    ):
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.UpdatedDate = UpdatedDate


class GetRoommatePromotions:
    """Interface: Common Data."""
    def __init__(
        self,
        YardiPropertyId: str = None,
        MoveOutFrom: str = None,
        MoveOutTo: str = None,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.MoveOutFrom = MoveOutFrom
        self.MoveOutTo = MoveOutTo
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")


class GetVersionNumber:
    """Interface: Common Data."""
    def __init__(self):
        pass


class GetServerTime:
    """Interface: Common Data."""
    def __init__(self):
        pass


class Ping:
    """Interface: Common Data."""
    def __init__(self):
        pass


