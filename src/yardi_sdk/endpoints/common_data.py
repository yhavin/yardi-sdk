class GetPropertyConfigurations:
    """Interface: Common Data."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        InterfaceEntity: str,
        InterfaceLicense: str
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
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        InterfaceEntity: str,
        InterfaceLicense: str,
        DateCreated: str
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.DateCreated = DateCreated


class GetPropertyList:
    """Interface: Common Data."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        InterfaceEntity: str,
        InterfaceLicense: str,
        YardiPropertyId: str
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.YardiPropertyId = YardiPropertyId


class GetPropertyOptions:
    """Interface: Common Data."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        InterfaceEntity: str,
        InterfaceLicense: str,
        YardiPropertyId: str
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.YardiPropertyId = YardiPropertyId


class GetVendorOptions:
    """Interface: Common Data."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        InterfaceEntity: str,
        InterfaceLicense: str
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
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        InterfaceEntity: str,
        InterfaceLicense: str,
        YardiPropertyId: str,
        MoveOut1: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.YardiPropertyId = YardiPropertyId
        self.MoveOut1 = MoveOut1


class GetResidentData_ByChargeCode:
    """Interface: Common Data."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        InterfaceEntity: str,
        InterfaceLicense: str,
        YardiPropertyId: str,
        TenantCode: str = None,
        ChargeCode: str = None,
        FromDate: str = None,
        ToDate: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.YardiPropertyId = YardiPropertyId
        self.TenantCode = TenantCode
        self.ChargeCode = ChargeCode
        self.FromDate = FromDate
        self.ToDate = ToDate


class GetResidentFromRoommate:
    """Interface: Common Data."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        InterfaceEntity: str,
        InterfaceLicense: str,
        YardiPropertyId: str,
        IncludeLedger: bool,
        LedgerAsOfDate: str,
        IncludeLeaseCharges: bool,
        IncludeVehicleInfo: bool,
        IncludeRoommateData: bool,
        IncludeEmployerData: bool,
        RoommateCode: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.YardiPropertyId = YardiPropertyId
        self.IncludeLedger = IncludeLedger
        self.LedgerAsOfDate = LedgerAsOfDate
        self.IncludeLeaseCharges = IncludeLeaseCharges
        self.IncludeVehicleInfo = IncludeVehicleInfo
        self.IncludeRoommateData = IncludeRoommateData
        self.IncludeEmployerData = IncludeEmployerData
        self.RoommateCode = RoommateCode


class GetResidentsByDate:
    """Interface: Common Data."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        InterfaceEntity: str,
        InterfaceLicense: str,
        YardiPropertyId: str,
        Status: str = None,
        ModifiedSinceDate: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.YardiPropertyId = YardiPropertyId
        self.Status = Status
        self.ModifiedSinceDate = ModifiedSinceDate


class GetResidentsByStatus:
    """Interface: Common Data."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        InterfaceEntity: str,
        InterfaceLicense: str,
        YardiPropertyId: str,
        Status: str = None,
        DateFrom: str = None,
        DateTo: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.YardiPropertyId = YardiPropertyId
        self.Status = Status
        self.DateFrom = DateFrom
        self.DateTo = DateTo


class GetResidentData:
    """Interface: Common Data."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        InterfaceEntity: str,
        InterfaceLicense: str,
        YardiPropertyId: str,
        IncludeLedger: bool,
        LedgerAsOfDate: str,
        IncludeLeaseCharges: bool,
        IncludeVehicleInfo: bool,
        IncludeRoommateData: bool,
        IncludeEmployerData: bool,
        TenantCode: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.YardiPropertyId = YardiPropertyId
        self.IncludeLedger = IncludeLedger
        self.LedgerAsOfDate = LedgerAsOfDate
        self.IncludeLeaseCharges = IncludeLeaseCharges
        self.IncludeVehicleInfo = IncludeVehicleInfo
        self.IncludeRoommateData = IncludeRoommateData
        self.IncludeEmployerData = IncludeEmployerData
        self.TenantCode = TenantCode


class GetOccupants:
    """Interface: Common Data."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        InterfaceEntity: str,
        InterfaceLicense: str,
        YardiPropertyId: str,
        TenantCode: str = None,
        UnitCode: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.YardiPropertyId = YardiPropertyId
        self.TenantCode = TenantCode
        self.UnitCode = UnitCode


class UpdateResidentData:
    """Interface: Common Data."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        InterfaceEntity: str,
        InterfaceLicense: str,
        XmlDoc: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.XmlDoc = XmlDoc


class ImportTenantLeaseDocumentPDF:
    """Interface: Common Data."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Platform: str,
        InterfaceEntity: str,
        InterfaceLicense: str,
        DataBase: str = None,
        PropertyId: str = None,
        TenantCode: str = None,
        AttachmentType: str = None,
        Description: str = None,
        Attachment: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
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
        UserName: str,
        Password: str,
        ServerName: str,
        Platform: str,
        InterfaceEntity: str,
        InterfaceLicense: str,
        DataBase: str = None,
        PropertyId: str = None,
        TenantCode: str = None,
        AttachmentType: str = None,
        Description: str = None,
        Attachment: str = None,
        FileExtension: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
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
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        YardiPropertyId: str,
        InterfaceEntity: str,
        InterfaceLicense: str,
        DateFrom: str,
        DateTo: str,
        TenantCode: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.YardiPropertyId = YardiPropertyId
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.DateFrom = DateFrom
        self.DateTo = DateTo
        self.TenantCode = TenantCode


class GetTenantLeaseDocuments:
    """Interface: Common Data."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        YardiPropertyId: str,
        InterfaceEntity: str,
        InterfaceLicense: str,
        TenantCode: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.YardiPropertyId = YardiPropertyId
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.TenantCode = TenantCode


class GetTenantDocument:
    """Interface: Common Data."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        YardiPropertyId: str,
        InterfaceEntity: str,
        InterfaceLicense: str,
        TenantCode: str = None,
        FileName: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.YardiPropertyId = YardiPropertyId
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.TenantCode = TenantCode
        self.FileName = FileName


class GetAttachmentTypes:
    """Interface: Common Data."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        InterfaceEntity: str,
        InterfaceLicense: str
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
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        InterfaceEntity: str,
        InterfaceLicense: str
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
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        InterfaceEntity: str,
        InterfaceLicense: str,
        YardiPropertyId: str,
        UnitId: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.YardiPropertyId = YardiPropertyId
        self.UnitId = UnitId


class GetUserPropertyAccess:
    """Interface: Common Data."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        InterfaceEntity: str,
        InterfaceLicense: str
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
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        InterfaceEntity: str,
        InterfaceLicense: str,
        YardiPropertyId: str,
        UnitId: str = None,
        MoveIn: str = None,
        MoveOut: str = None,
        LeaseChgFrom: str = None,
        LeaseChgTo: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.YardiPropertyId = YardiPropertyId
        self.UnitId = UnitId
        self.MoveIn = MoveIn
        self.MoveOut = MoveOut
        self.LeaseChgFrom = LeaseChgFrom
        self.LeaseChgTo = LeaseChgTo


class GetTenantStatus:
    """Interface: Common Data."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        InterfaceEntity: str,
        InterfaceLicense: str,
        YardiPropertyId: str
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.YardiPropertyId = YardiPropertyId


class GetUnitInformation:
    """Interface: Common Data."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        YardiPropertyId: str,
        InterfaceEntity: str,
        InterfaceLicense: str
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.YardiPropertyId = YardiPropertyId
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetCurrentUnitInformation:
    """Interface: Common Data."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        YardiPropertyId: str,
        InterfaceEntity: str,
        InterfaceLicense: str
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.YardiPropertyId = YardiPropertyId
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetContacts:
    """Interface: Common Data."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        InterfaceEntity: str,
        InterfaceLicense: str,
        YardiPropertyId: str,
        TenantCode: str = None,
        ContactRoleType: str = None,
        ContactRoleDescription: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.YardiPropertyId = YardiPropertyId
        self.TenantCode = TenantCode
        self.ContactRoleType = ContactRoleType
        self.ContactRoleDescription = ContactRoleDescription


class GetContactRoles:
    """Interface: Common Data."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        InterfaceEntity: str,
        InterfaceLicense: str,
        ContactRoleType: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.ContactRoleType = ContactRoleType


class GetUnitTransferData:
    """Interface: Common Data."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        YardiPropertyId: str,
        InterfaceEntity: str,
        InterfaceLicense: str
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.YardiPropertyId = YardiPropertyId
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetUnitTransferData_DateRange:
    """Interface: Common Data."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        YardiPropertyId: str,
        InterfaceEntity: str,
        InterfaceLicense: str,
        FromDate: str,
        ToDate: str
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.YardiPropertyId = YardiPropertyId
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.FromDate = FromDate
        self.ToDate = ToDate


class GetSchedulers:
    """Interface: Common Data."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        InterfaceEntity: str,
        InterfaceLicense: str,
        UpdatedDate: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.UpdatedDate = UpdatedDate


class GetRoommatePromotions:
    """Interface: Common Data."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        YardiPropertyId: str,
        InterfaceEntity: str,
        InterfaceLicense: str,
        MoveOutFrom: str,
        MoveOutTo: str
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.YardiPropertyId = YardiPropertyId
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.MoveOutFrom = MoveOutFrom
        self.MoveOutTo = MoveOutTo


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


