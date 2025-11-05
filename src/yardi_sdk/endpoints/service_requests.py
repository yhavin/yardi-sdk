import os


class GetPropertyConfigurations:
    """Interface: Service Requests."""
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


class GetResident_SearchPlus:
    """Interface: Service Requests."""
    def __init__(
        self,
        YardiPropertyId: str,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        UnitCode: str = None,
        ResidentCode: str = None,
        Name: str = None,
        PhoneNumber: str = None,
        Address: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.UnitCode = UnitCode
        self.ResidentCode = ResidentCode
        self.Name = Name
        self.PhoneNumber = PhoneNumber
        self.Address = Address


class GetResident_Search:
    """Interface: Service Requests."""
    def __init__(
        self,
        YardiPropertyId: str,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        UnitCode: str = None,
        ResidentCode: str = None,
        Name: str = None,
        PhoneNumber: str = None,
        Address: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.UnitCode = UnitCode
        self.ResidentCode = ResidentCode
        self.Name = Name
        self.PhoneNumber = PhoneNumber
        self.Address = Address


class GetServiceRequest_Search:
    """Interface: Service Requests."""
    def __init__(
        self,
        YardiPropertyId: str,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        UnitCode: str = None,
        ResidentCode: str = None,
        Name: str = None,
        Address: str = None,
        PhoneNumber: str = None,
        Status: str = None,
        OpenOrClosed: str = None,
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
        self.UnitCode = UnitCode
        self.ResidentCode = ResidentCode
        self.Name = Name
        self.Address = Address
        self.PhoneNumber = PhoneNumber
        self.Status = Status
        self.OpenOrClosed = OpenOrClosed
        self.FromDate = FromDate
        self.ToDate = ToDate


class GetServiceRequest_AttachmentSearch:
    """Interface: Service Requests."""
    def __init__(
        self,
        YardiPropertyId: str,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        UnitCode: str = None,
        ResidentCode: str = None,
        Name: str = None,
        Address: str = None,
        PhoneNumber: str = None,
        Status: str = None,
        OpenOrClosed: str = None,
        FromDate: str = None,
        ToDate: str = None,
        AttachmentFromDate: str = None,
        AttachmentToDate: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.UnitCode = UnitCode
        self.ResidentCode = ResidentCode
        self.Name = Name
        self.Address = Address
        self.PhoneNumber = PhoneNumber
        self.Status = Status
        self.OpenOrClosed = OpenOrClosed
        self.FromDate = FromDate
        self.ToDate = ToDate
        self.AttachmentFromDate = AttachmentFromDate
        self.AttachmentToDate = AttachmentToDate


class GetServiceRequest_ByDateRange:
    """Interface: Service Requests."""
    def __init__(
        self,
        YardiPropertyId: str,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        UnitCode: str = None,
        ResidentCode: str = None,
        Name: str = None,
        Address: str = None,
        PhoneNumber: str = None,
        Status: str = None,
        OpenOrClosed: str = None,
        FromDate: str = None,
        ToDate: str = None,
        VendorCode: str = None,
        Origin: str = None,
        CreatedFromDate: str = None,
        CreatedToDate: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.UnitCode = UnitCode
        self.ResidentCode = ResidentCode
        self.Name = Name
        self.Address = Address
        self.PhoneNumber = PhoneNumber
        self.Status = Status
        self.OpenOrClosed = OpenOrClosed
        self.FromDate = FromDate
        self.ToDate = ToDate
        self.VendorCode = VendorCode
        self.Origin = Origin
        self.CreatedFromDate = CreatedFromDate
        self.CreatedToDate = CreatedToDate


class CreateOrEditServiceRequests:
    """Interface: Service Requests."""
    def __init__(
        self,
        YardiPropertyId: str,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        ServiceRequestXml: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.ServiceRequestXml = ServiceRequestXml


class GetCustomValues:
    """Interface: Service Requests."""
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


class GetCustomValues2:
    """Interface: Service Requests."""
    def __init__(
        self,
        ExportCustomValues: bool,
        ExportEmployees: bool,
        ExportPropertyListCode: bool,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None
    ):
        self.ExportCustomValues = ExportCustomValues
        self.ExportEmployees = ExportEmployees
        self.ExportPropertyListCode = ExportPropertyListCode
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")


class GetServiceRequests:
    """Interface: Service Requests."""
    def __init__(
        self,
        YardiPropertyId: str,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        ServiceRequestIdArray: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.ServiceRequestIdArray = ServiceRequestIdArray


class ImportWorkOrderDocumentExt:
    """Interface: Service Requests."""
    def __init__(
        self,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        DataBase: str = None,
        WorkOrderId: str = None,
        PropertyCode: str = None,
        AttachmentType: str = None,
        Description: str = None,
        Attachment: str = None,
        Extension: str = None
    ):
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.DataBase = DataBase
        self.WorkOrderId = WorkOrderId
        self.PropertyCode = PropertyCode
        self.AttachmentType = AttachmentType
        self.Description = Description
        self.Attachment = Attachment
        self.Extension = Extension


class ImportWorkOrderDocumentPDF:
    """Interface: Service Requests."""
    def __init__(
        self,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        DataBase: str = None,
        WorkOrderId: str = None,
        PropertyCode: str = None,
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
        self.WorkOrderId = WorkOrderId
        self.PropertyCode = PropertyCode
        self.AttachmentType = AttachmentType
        self.Description = Description
        self.Attachment = Attachment


class GetAttachmentTypes:
    """Interface: Service Requests."""
    def __init__(
        self,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        PropertyID: str = None
    ):
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.PropertyID = PropertyID


class GetAttachments:
    """Interface: Service Requests."""
    def __init__(
        self,
        ServiceRequestId: str,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        PropertyID: str = None
    ):
        self.ServiceRequestId = ServiceRequestId
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.PropertyID = PropertyID


class GetAttachments_DateRange:
    """Interface: Service Requests."""
    def __init__(
        self,
        ServiceRequestId: str,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        PropertyID: str = None,
        FromDate: str = None,
        ToDate: str = None
    ):
        self.ServiceRequestId = ServiceRequestId
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.PropertyID = PropertyID
        self.FromDate = FromDate
        self.ToDate = ToDate


class GetVendorConfiguration:
    """Interface: Service Requests."""
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


class GetVersionNumber:
    """Interface: Service Requests."""
    def __init__(self):
        pass


class Ping:
    """Interface: Service Requests."""
    def __init__(self):
        pass


