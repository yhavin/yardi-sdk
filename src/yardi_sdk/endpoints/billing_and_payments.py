import os


class GetResidentTransaction_Login:
    """Interface: Billing and Payments."""
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
        TenantId: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.TenantId = TenantId


class GetResidentTransactions_Login:
    """Interface: Billing and Payments."""
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


class GetResidentTransactions_ByChargeDate_Login:
    """Interface: Billing and Payments."""
    def __init__(
        self,
        YardiPropertyId: str,
        FromDate: str,
        ToDate: str,
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


class GetResidentTransactions_ByApplicationDate_Login:
    """Interface: Billing and Payments."""
    def __init__(
        self,
        YardiPropertyId: str,
        FromDate: str,
        ToDate: str,
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


class GetResidentCharges_Login:
    """Interface: Billing and Payments."""
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


class GetResidentCharges_ByDate_Login:
    """Interface: Billing and Payments."""
    def __init__(
        self,
        YardiPropertyId: str,
        FromDate: str,
        ToDate: str,
        FilterByAppDate: bool,
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
        self.FilterByAppDate = FilterByAppDate
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")


class GetResidentPrepays_Login:
    """Interface: Billing and Payments."""
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


class GetResidentPrepays_ByDate_Login:
    """Interface: Billing and Payments."""
    def __init__(
        self,
        YardiPropertyId: str,
        FromDate: str,
        ToDate: str,
        FilterByAppDate: bool,
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
        self.FilterByAppDate = FilterByAppDate
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")


class GetResidents_Login:
    """Interface: Billing and Payments."""
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


class GetResidentLeaseCharges_Login:
    """Interface: Billing and Payments."""
    def __init__(
        self,
        YardiPropertyId: str,
        PostMonth: str,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        TenantId: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.PostMonth = PostMonth
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.TenantId = TenantId


class GetResidentsLeaseCharges_Login:
    """Interface: Billing and Payments."""
    def __init__(
        self,
        YardiPropertyId: str,
        PostMonth: str,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.PostMonth = PostMonth
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")


class GetOwnerTransactions_Login:
    """Interface: Billing and Payments."""
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


class GetUnitInformation_Login:
    """Interface: Billing and Payments."""
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


class GetResidentBalances:
    """Interface: Billing and Payments."""
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


class GetCondoUnitInformation_Login:
    """Interface: Billing and Payments."""
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


class GetPropertyConfigurations:
    """Interface: Billing and Payments."""
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


class ImportResidentTransactions_Login:
    """Interface: Billing and Payments."""
    def __init__(
        self,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        TransactionXml: str = None
    ):
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.TransactionXml = TransactionXml


class ImportResidentTransactions_DepositDate:
    """Interface: Billing and Payments."""
    def __init__(
        self,
        DepositDate: str,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        TransactionXml: str = None,
        DepositMemo: str = None
    ):
        self.DepositDate = DepositDate
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.TransactionXml = TransactionXml
        self.DepositMemo = DepositMemo


class ImportReceipt_Login:
    """Interface: Billing and Payments."""
    def __init__(
        self,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        TransactionXml: str = None
    ):
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.TransactionXml = TransactionXml


class ImportCharge_Login:
    """Interface: Billing and Payments."""
    def __init__(
        self,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        TransactionXml: str = None
    ):
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.TransactionXml = TransactionXml


class ImportPayable_Login:
    """Interface: Billing and Payments."""
    def __init__(
        self,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        PayableDoc: str = None
    ):
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.PayableDoc = PayableDoc


class ImportCheck_Login:
    """Interface: Billing and Payments."""
    def __init__(
        self,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        CheckDoc: str = None
    ):
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.CheckDoc = CheckDoc


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
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        VendorId: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.InvoicePostMonthFrom = InvoicePostMonthFrom
        self.InvoicePostMonthTo = InvoicePostMonthTo
        self.InvoiceFromDate = InvoiceFromDate
        self.InvoiceToDate = InvoiceToDate
        self.UnpaidOnly = UnpaidOnly
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.VendorId = VendorId


class GetVendor_Login:
    """Interface: Billing and Payments."""
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
        VendorId: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.VendorId = VendorId


class GetVendors_Login:
    """Interface: Billing and Payments."""
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


class ExportChartOfAccounts:
    """Interface: Billing and Payments."""
    def __init__(
        self,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        PropertyId: str = None
    ):
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.PropertyId = PropertyId


class GetChargeTypes_Login:
    """Interface: Billing and Payments."""
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


class GetVendorOptions_Login:
    """Interface: Billing and Payments."""
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


class GetSegmentInformation:
    """Interface: Billing and Payments."""
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


