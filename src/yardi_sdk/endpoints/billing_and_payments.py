class GetResidentTransaction_Login:
    """Interface: Billing and Payments."""
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
        TenantId: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.YardiPropertyId = YardiPropertyId
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.TenantId = TenantId


class GetResidentTransactions_Login:
    """Interface: Billing and Payments."""
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


class GetResidentTransactions_ByChargeDate_Login:
    """Interface: Billing and Payments."""
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


class GetResidentTransactions_ByApplicationDate_Login:
    """Interface: Billing and Payments."""
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


class GetResidentCharges_Login:
    """Interface: Billing and Payments."""
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


class GetResidentCharges_ByDate_Login:
    """Interface: Billing and Payments."""
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
        ToDate: str,
        FilterByAppDate: bool
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
        self.FilterByAppDate = FilterByAppDate


class GetResidentPrepays_Login:
    """Interface: Billing and Payments."""
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


class GetResidentPrepays_ByDate_Login:
    """Interface: Billing and Payments."""
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
        ToDate: str,
        FilterByAppDate: bool
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
        self.FilterByAppDate = FilterByAppDate


class GetResidents_Login:
    """Interface: Billing and Payments."""
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


class GetResidentLeaseCharges_Login:
    """Interface: Billing and Payments."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        YardiPropertyId: str,
        PostMonth: str,
        InterfaceEntity: str,
        InterfaceLicense: str,
        TenantId: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.YardiPropertyId = YardiPropertyId
        self.PostMonth = PostMonth
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.TenantId = TenantId


class GetResidentsLeaseCharges_Login:
    """Interface: Billing and Payments."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        YardiPropertyId: str,
        PostMonth: str,
        InterfaceEntity: str,
        InterfaceLicense: str
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.YardiPropertyId = YardiPropertyId
        self.PostMonth = PostMonth
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetOwnerTransactions_Login:
    """Interface: Billing and Payments."""
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


class GetUnitInformation_Login:
    """Interface: Billing and Payments."""
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


class GetResidentBalances:
    """Interface: Billing and Payments."""
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


class GetCondoUnitInformation_Login:
    """Interface: Billing and Payments."""
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


class GetPropertyConfigurations:
    """Interface: Billing and Payments."""
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


class ImportResidentTransactions_Login:
    """Interface: Billing and Payments."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        InterfaceEntity: str,
        InterfaceLicense: str,
        TransactionXml: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.TransactionXml = TransactionXml


class ImportResidentTransactions_DepositDate:
    """Interface: Billing and Payments."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        InterfaceEntity: str,
        InterfaceLicense: str,
        DepositDate: str,
        TransactionXml: str = None,
        DepositMemo: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.DepositDate = DepositDate
        self.TransactionXml = TransactionXml
        self.DepositMemo = DepositMemo


class ImportReceipt_Login:
    """Interface: Billing and Payments."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        InterfaceEntity: str,
        InterfaceLicense: str,
        TransactionXml: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.TransactionXml = TransactionXml


class ImportCharge_Login:
    """Interface: Billing and Payments."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        InterfaceEntity: str,
        InterfaceLicense: str,
        TransactionXml: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.TransactionXml = TransactionXml


class ImportPayable_Login:
    """Interface: Billing and Payments."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        InterfaceEntity: str,
        InterfaceLicense: str,
        PayableDoc: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.PayableDoc = PayableDoc


class ImportCheck_Login:
    """Interface: Billing and Payments."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        InterfaceEntity: str,
        InterfaceLicense: str,
        CheckDoc: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.CheckDoc = CheckDoc


class GetPayables:
    """Interface: Billing and Payments."""
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
        InvoicePostMonthFrom: str,
        InvoicePostMonthTo: str,
        InvoiceFromDate: str,
        InvoiceToDate: str,
        UnpaidOnly: bool,
        VendorId: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.YardiPropertyId = YardiPropertyId
        self.InvoicePostMonthFrom = InvoicePostMonthFrom
        self.InvoicePostMonthTo = InvoicePostMonthTo
        self.InvoiceFromDate = InvoiceFromDate
        self.InvoiceToDate = InvoiceToDate
        self.UnpaidOnly = UnpaidOnly
        self.VendorId = VendorId


class GetVendor_Login:
    """Interface: Billing and Payments."""
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
        VendorId: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.YardiPropertyId = YardiPropertyId
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.VendorId = VendorId


class GetVendors_Login:
    """Interface: Billing and Payments."""
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


class ExportChartOfAccounts:
    """Interface: Billing and Payments."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        InterfaceEntity: str,
        InterfaceLicense: str,
        PropertyId: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.PropertyId = PropertyId


class GetChargeTypes_Login:
    """Interface: Billing and Payments."""
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


class GetVendorOptions_Login:
    """Interface: Billing and Payments."""
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


class GetSegmentInformation:
    """Interface: Billing and Payments."""
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


