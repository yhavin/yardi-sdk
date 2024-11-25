import os


class GetPropertyConfigurations:
    """Interface: Common Data."""
    def __init__(
        self,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE")
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetPropertyConfigurationsNewFromDate:
    """Interface: Common Data."""
    def __init__(
        self,
        DateCreated: str,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE")
    ):
        self.DateCreated = DateCreated
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetPropertyList:
    """Interface: Common Data."""
    def __init__(
        self,
        YardiPropertyId: str,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE")
    ):
        self.YardiPropertyId = YardiPropertyId
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetPropertyOptions:
    """Interface: Common Data."""
    def __init__(
        self,
        YardiPropertyId: str,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE")
    ):
        self.YardiPropertyId = YardiPropertyId
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetVendorOptions:
    """Interface: Common Data."""
    def __init__(
        self,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE")
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetResidents:
    """Interface: Common Data."""
    def __init__(
        self,
        YardiPropertyId: str,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
        MoveOut1: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.MoveOut1 = MoveOut1
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetResidentData_ByChargeCode:
    """Interface: Common Data."""
    def __init__(
        self,
        YardiPropertyId: str,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
        TenantCode: str = None,
        ChargeCode: str = None,
        FromDate: str = None,
        ToDate: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.TenantCode = TenantCode
        self.ChargeCode = ChargeCode
        self.FromDate = FromDate
        self.ToDate = ToDate
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetResidentFromRoommate:
    """Interface: Common Data."""
    def __init__(
        self,
        YardiPropertyId: str,
        IncludeLedger: bool,
        LedgerAsOfDate: str,
        IncludeLeaseCharges: bool,
        IncludeVehicleInfo: bool,
        IncludeRoommateData: bool,
        IncludeEmployerData: bool,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
        RoommateCode: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.IncludeLedger = IncludeLedger
        self.LedgerAsOfDate = LedgerAsOfDate
        self.IncludeLeaseCharges = IncludeLeaseCharges
        self.IncludeVehicleInfo = IncludeVehicleInfo
        self.IncludeRoommateData = IncludeRoommateData
        self.IncludeEmployerData = IncludeEmployerData
        self.RoommateCode = RoommateCode
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetResidentsByDate:
    """Interface: Common Data."""
    def __init__(
        self,
        YardiPropertyId: str,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
        Status: str = None,
        ModifiedSinceDate: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.Status = Status
        self.ModifiedSinceDate = ModifiedSinceDate
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetResidentsByStatus:
    """Interface: Common Data."""
    def __init__(
        self,
        YardiPropertyId: str,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
        Status: str = None,
        DateFrom: str = None,
        DateTo: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.Status = Status
        self.DateFrom = DateFrom
        self.DateTo = DateTo
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetResidentData:
    """Interface: Common Data."""
    def __init__(
        self,
        YardiPropertyId: str,
        IncludeLedger: bool,
        LedgerAsOfDate: str,
        IncludeLeaseCharges: bool,
        IncludeVehicleInfo: bool,
        IncludeRoommateData: bool,
        IncludeEmployerData: bool,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
        TenantCode: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.IncludeLedger = IncludeLedger
        self.LedgerAsOfDate = LedgerAsOfDate
        self.IncludeLeaseCharges = IncludeLeaseCharges
        self.IncludeVehicleInfo = IncludeVehicleInfo
        self.IncludeRoommateData = IncludeRoommateData
        self.IncludeEmployerData = IncludeEmployerData
        self.TenantCode = TenantCode
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetOccupants:
    """Interface: Common Data."""
    def __init__(
        self,
        YardiPropertyId: str,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
        TenantCode: str = None,
        UnitCode: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.TenantCode = TenantCode
        self.UnitCode = UnitCode
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class UpdateResidentData:
    """Interface: Common Data."""
    def __init__(
        self,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
        XmlDoc: str = None
    ):
        self.XmlDoc = XmlDoc
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class ImportTenantLeaseDocumentPDF:
    """Interface: Common Data."""
    def __init__(
        self,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
        DataBase: str = None,
        PropertyId: str = None,
        TenantCode: str = None,
        AttachmentType: str = None,
        Description: str = None,
        Attachment: str = None
    ):
        self.DataBase = DataBase
        self.PropertyId = PropertyId
        self.TenantCode = TenantCode
        self.AttachmentType = AttachmentType
        self.Description = Description
        self.Attachment = Attachment
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class ImportTenantLeaseDocumentExt:
    """Interface: Common Data."""
    def __init__(
        self,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
        DataBase: str = None,
        PropertyId: str = None,
        TenantCode: str = None,
        AttachmentType: str = None,
        Description: str = None,
        Attachment: str = None,
        FileExtension: str = None
    ):
        self.DataBase = DataBase
        self.PropertyId = PropertyId
        self.TenantCode = TenantCode
        self.AttachmentType = AttachmentType
        self.Description = Description
        self.Attachment = Attachment
        self.FileExtension = FileExtension
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetTenantLeaseDocuments_DateRange:
    """Interface: Common Data."""
    def __init__(
        self,
        YardiPropertyId: str,
        DateFrom: str,
        DateTo: str,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
        TenantCode: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.DateFrom = DateFrom
        self.DateTo = DateTo
        self.TenantCode = TenantCode
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetTenantLeaseDocuments:
    """Interface: Common Data."""
    def __init__(
        self,
        YardiPropertyId: str,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
        TenantCode: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.TenantCode = TenantCode
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetTenantDocument:
    """Interface: Common Data."""
    def __init__(
        self,
        YardiPropertyId: str,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
        TenantCode: str = None,
        FileName: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.TenantCode = TenantCode
        self.FileName = FileName
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetAttachmentTypes:
    """Interface: Common Data."""
    def __init__(
        self,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE")
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetPermissions:
    """Interface: Common Data."""
    def __init__(
        self,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE")
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetResidentsByUnit:
    """Interface: Common Data."""
    def __init__(
        self,
        YardiPropertyId: str,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
        UnitId: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.UnitId = UnitId
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetUserPropertyAccess:
    """Interface: Common Data."""
    def __init__(
        self,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE")
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetRentroll:
    """Interface: Common Data."""
    def __init__(
        self,
        YardiPropertyId: str,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
        UnitId: str = None,
        MoveIn: str = None,
        MoveOut: str = None,
        LeaseChgFrom: str = None,
        LeaseChgTo: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.UnitId = UnitId
        self.MoveIn = MoveIn
        self.MoveOut = MoveOut
        self.LeaseChgFrom = LeaseChgFrom
        self.LeaseChgTo = LeaseChgTo
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetTenantStatus:
    """Interface: Common Data."""
    def __init__(
        self,
        YardiPropertyId: str,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE")
    ):
        self.YardiPropertyId = YardiPropertyId
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetUnitInformation:
    """Interface: Common Data."""
    def __init__(
        self,
        YardiPropertyId: str,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE")
    ):
        self.YardiPropertyId = YardiPropertyId
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetCurrentUnitInformation:
    """Interface: Common Data."""
    def __init__(
        self,
        YardiPropertyId: str,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE")
    ):
        self.YardiPropertyId = YardiPropertyId
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetContacts:
    """Interface: Common Data."""
    def __init__(
        self,
        YardiPropertyId: str,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
        TenantCode: str = None,
        ContactRoleType: str = None,
        ContactRoleDescription: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.TenantCode = TenantCode
        self.ContactRoleType = ContactRoleType
        self.ContactRoleDescription = ContactRoleDescription
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetContactRoles:
    """Interface: Common Data."""
    def __init__(
        self,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
        ContactRoleType: str = None
    ):
        self.ContactRoleType = ContactRoleType
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetUnitTransferData:
    """Interface: Common Data."""
    def __init__(
        self,
        YardiPropertyId: str,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE")
    ):
        self.YardiPropertyId = YardiPropertyId
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetUnitTransferData_DateRange:
    """Interface: Common Data."""
    def __init__(
        self,
        YardiPropertyId: str,
        FromDate: str,
        ToDate: str,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE")
    ):
        self.YardiPropertyId = YardiPropertyId
        self.FromDate = FromDate
        self.ToDate = ToDate
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetSchedulers:
    """Interface: Common Data."""
    def __init__(
        self,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
        UpdatedDate: str = None
    ):
        self.UpdatedDate = UpdatedDate
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetRoommatePromotions:
    """Interface: Common Data."""
    def __init__(
        self,
        YardiPropertyId: str,
        MoveOutFrom: str,
        MoveOutTo: str,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE")
    ):
        self.YardiPropertyId = YardiPropertyId
        self.MoveOutFrom = MoveOutFrom
        self.MoveOutTo = MoveOutTo
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


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


