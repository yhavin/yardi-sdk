import os


class GetResidentTransaction_Login:
    """Interface: Billing and Payments."""
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
        TenantId: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.TenantId = TenantId
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetResidentTransactions_Login:
    """Interface: Billing and Payments."""
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


class GetResidentTransactions_ByChargeDate_Login:
    """Interface: Billing and Payments."""
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


class GetResidentTransactions_ByApplicationDate_Login:
    """Interface: Billing and Payments."""
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


class GetResidentCharges_Login:
    """Interface: Billing and Payments."""
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


class GetResidentCharges_ByDate_Login:
    """Interface: Billing and Payments."""
    def __init__(
        self,
        YardiPropertyId: str,
        FromDate: str,
        ToDate: str,
        FilterByAppDate: bool,
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
        self.FilterByAppDate = FilterByAppDate
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetResidentPrepays_Login:
    """Interface: Billing and Payments."""
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


class GetResidentPrepays_ByDate_Login:
    """Interface: Billing and Payments."""
    def __init__(
        self,
        YardiPropertyId: str,
        FromDate: str,
        ToDate: str,
        FilterByAppDate: bool,
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
        self.FilterByAppDate = FilterByAppDate
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetResidents_Login:
    """Interface: Billing and Payments."""
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


class GetResidentLeaseCharges_Login:
    """Interface: Billing and Payments."""
    def __init__(
        self,
        YardiPropertyId: str,
        PostMonth: str,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
        TenantId: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.PostMonth = PostMonth
        self.TenantId = TenantId
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetResidentsLeaseCharges_Login:
    """Interface: Billing and Payments."""
    def __init__(
        self,
        YardiPropertyId: str,
        PostMonth: str,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE")
    ):
        self.YardiPropertyId = YardiPropertyId
        self.PostMonth = PostMonth
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetOwnerTransactions_Login:
    """Interface: Billing and Payments."""
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


class GetUnitInformation_Login:
    """Interface: Billing and Payments."""
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


class GetResidentBalances:
    """Interface: Billing and Payments."""
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


class GetCondoUnitInformation_Login:
    """Interface: Billing and Payments."""
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


class GetPropertyConfigurations:
    """Interface: Billing and Payments."""
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


class ImportResidentTransactions_Login:
    """Interface: Billing and Payments."""
    def __init__(
        self,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
        TransactionXml: str = None
    ):
        self.TransactionXml = TransactionXml
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class ImportResidentTransactions_DepositDate:
    """Interface: Billing and Payments."""
    def __init__(
        self,
        DepositDate: str,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
        TransactionXml: str = None,
        DepositMemo: str = None
    ):
        self.DepositDate = DepositDate
        self.TransactionXml = TransactionXml
        self.DepositMemo = DepositMemo
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class ImportReceipt_Login:
    """Interface: Billing and Payments."""
    def __init__(
        self,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
        TransactionXml: str = None
    ):
        self.TransactionXml = TransactionXml
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class ImportCharge_Login:
    """Interface: Billing and Payments."""
    def __init__(
        self,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
        TransactionXml: str = None
    ):
        self.TransactionXml = TransactionXml
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class ImportPayable_Login:
    """Interface: Billing and Payments."""
    def __init__(
        self,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
        PayableDoc: str = None
    ):
        self.PayableDoc = PayableDoc
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class ImportCheck_Login:
    """Interface: Billing and Payments."""
    def __init__(
        self,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
        CheckDoc: str = None
    ):
        self.CheckDoc = CheckDoc
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetPayables:
    """Interface: Billing and Payments."""
    def __init__(
        self,
        YardiPropertyId: str,
        InvoicePostMonthFrom: str,
        InvoicePostMonthTo: str,
        InvoiceFromDate: str,
        InvoiceToDate: str,
        UnpaidOnly: bool,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
        VendorId: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.InvoicePostMonthFrom = InvoicePostMonthFrom
        self.InvoicePostMonthTo = InvoicePostMonthTo
        self.InvoiceFromDate = InvoiceFromDate
        self.InvoiceToDate = InvoiceToDate
        self.UnpaidOnly = UnpaidOnly
        self.VendorId = VendorId
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetVendor_Login:
    """Interface: Billing and Payments."""
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
        VendorId: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.VendorId = VendorId
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetVendors_Login:
    """Interface: Billing and Payments."""
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


class ExportChartOfAccounts:
    """Interface: Billing and Payments."""
    def __init__(
        self,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
        PropertyId: str = None
    ):
        self.PropertyId = PropertyId
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetChargeTypes_Login:
    """Interface: Billing and Payments."""
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


class GetVendorOptions_Login:
    """Interface: Billing and Payments."""
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


class GetSegmentInformation:
    """Interface: Billing and Payments."""
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


class GetVersionNumber_Str:
    """Interface: Billing and Payments."""
    def __init__(self):
        pass


class GetVersionNumber:
    """Interface: Billing and Payments."""
    def __init__(self):
        pass


class Ping:
    """Interface: Billing and Payments."""
    def __init__(self):
        pass


