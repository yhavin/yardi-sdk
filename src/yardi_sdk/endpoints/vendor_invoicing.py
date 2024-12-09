import os


class GetInvoiceRegister:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        YardiPropertyId: str = None,
        InvoicePostMonthFrom: str = None,
        InvoicePostMonthTo: str = None,
        InvoiceFromDate: str = None,
        InvoiceToDate: str = None,
        InvoiceCreationFromDate: str = None,
        InvoiceCreationToDate: str = None,
        InvoiceLastModifiedFromDate: str = None,
        InvoiceLastModifiedToDate: str = None,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        VendorId: str = None,
        InvoiceRegisterId: str = None,
        InvoiceNumber: str = None,
        ExpenseType: str = None,
        JobId: str = None,
        ContractId: str = None,
        BatchId: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.InvoicePostMonthFrom = InvoicePostMonthFrom
        self.InvoicePostMonthTo = InvoicePostMonthTo
        self.InvoiceFromDate = InvoiceFromDate
        self.InvoiceToDate = InvoiceToDate
        self.InvoiceCreationFromDate = InvoiceCreationFromDate
        self.InvoiceCreationToDate = InvoiceCreationToDate
        self.InvoiceLastModifiedFromDate = InvoiceLastModifiedFromDate
        self.InvoiceLastModifiedToDate = InvoiceLastModifiedToDate
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.VendorId = VendorId
        self.InvoiceRegisterId = InvoiceRegisterId
        self.InvoiceNumber = InvoiceNumber
        self.ExpenseType = ExpenseType
        self.JobId = JobId
        self.ContractId = ContractId
        self.BatchId = BatchId


class CancelInvoiceRegisterBatch:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        BatchId: str = None,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        InvoiceNumber: str = None
    ):
        self.BatchId = BatchId
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.InvoiceNumber = InvoiceNumber


class GetPropertyConfigurations:
    """Interface: Vendor Invoicing."""
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


class GetVendor_Login:
    """Interface: Vendor Invoicing."""
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
    """Interface: Vendor Invoicing."""
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


class GetVendorsSync:
    """Interface: Vendor Invoicing."""
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


class GetBudgets:
    """Interface: Vendor Invoicing."""
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
        BudgetYear: str = None,
        Book: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.BudgetYear = BudgetYear
        self.Book = Book


class GetBudgets_Month:
    """Interface: Vendor Invoicing."""
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
        BudgetYear: str = None,
        Book: str = None,
        Month: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.BudgetYear = BudgetYear
        self.Book = Book
        self.Month = Month


class GetPayables:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        YardiPropertyId: str = None,
        InvoicePostMonthFrom: str = None,
        InvoicePostMonthTo: str = None,
        InvoiceFromDate: str = None,
        InvoiceToDate: str = None,
        UnpaidOnly: bool = None,
        CheckFromDate: str = None,
        CheckToDate: str = None,
        InvoiceCreationFromDate: str = None,
        InvoiceCreationToDate: str = None,
        No3rdPartyInv: bool = None,
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
        self.CheckFromDate = CheckFromDate
        self.CheckToDate = CheckToDate
        self.InvoiceCreationFromDate = InvoiceCreationFromDate
        self.InvoiceCreationToDate = InvoiceCreationToDate
        self.No3rdPartyInv = No3rdPartyInv
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.VendorId = VendorId


class GetPayables2:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        YardiPropertyId: str = None,
        InvoicePostMonthFrom: str = None,
        InvoicePostMonthTo: str = None,
        InvoiceFromDate: str = None,
        InvoiceToDate: str = None,
        UnpaidOnly: bool = None,
        InvoiceCreationFromDate: str = None,
        InvoiceCreationToDate: str = None,
        No3rdPartyInv: bool = None,
        CheckPostMonthFrom: str = None,
        CheckPostMonthTo: str = None,
        CheckClearedFromDate: str = None,
        CheckClearedToDate: str = None,
        CheckCreationFromDate: str = None,
        CheckCreationToDate: str = None,
        CheckFromDate: str = None,
        CheckToDate: str = None,
        UnpostedInvoicesOnly: bool = None,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        VendorId: str = None,
        PayableId: str = None,
        InvoiceNumber: str = None,
        ExpenseType: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.InvoicePostMonthFrom = InvoicePostMonthFrom
        self.InvoicePostMonthTo = InvoicePostMonthTo
        self.InvoiceFromDate = InvoiceFromDate
        self.InvoiceToDate = InvoiceToDate
        self.UnpaidOnly = UnpaidOnly
        self.InvoiceCreationFromDate = InvoiceCreationFromDate
        self.InvoiceCreationToDate = InvoiceCreationToDate
        self.No3rdPartyInv = No3rdPartyInv
        self.CheckPostMonthFrom = CheckPostMonthFrom
        self.CheckPostMonthTo = CheckPostMonthTo
        self.CheckClearedFromDate = CheckClearedFromDate
        self.CheckClearedToDate = CheckClearedToDate
        self.CheckCreationFromDate = CheckCreationFromDate
        self.CheckCreationToDate = CheckCreationToDate
        self.CheckFromDate = CheckFromDate
        self.CheckToDate = CheckToDate
        self.UnpostedInvoicesOnly = UnpostedInvoicesOnly
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.VendorId = VendorId
        self.PayableId = PayableId
        self.InvoiceNumber = InvoiceNumber
        self.ExpenseType = ExpenseType


class GetPayableByBatchId:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        BatchId: str = None,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None
    ):
        self.BatchId = BatchId
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")


class GetPayableByLastModifiedDate:
    """Interface: Vendor Invoicing."""
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


class GetVendorInvoicingConfiguration:
    """Interface: Vendor Invoicing."""
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


class GetPurchaseOrders:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        YardiPropertyId: str = None,
        POCreationFromDate: str = None,
        POCreationToDate: str = None,
        OpenOnly: bool = None,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        PONum: str = None,
        ThirdPartyPONum: str = None,
        VendorId: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.POCreationFromDate = POCreationFromDate
        self.POCreationToDate = POCreationToDate
        self.OpenOnly = OpenOnly
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.PONum = PONum
        self.ThirdPartyPONum = ThirdPartyPONum
        self.VendorId = VendorId


class GetPOFromModifiedDate:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        YardiPropertyId: str = None,
        POModifiedFromDate: str = None,
        POModifiedToDate: str = None,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.POModifiedFromDate = POModifiedFromDate
        self.POModifiedToDate = POModifiedToDate
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")


class GetPOChangeOrders:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        YardiPropertyId: str = None,
        COCreationFromDate: str = None,
        COCreationToDate: str = None,
        OpenOnly: bool = None,
        IncludeParentPO: bool = None,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        PONum: str = None,
        ThirdPartyPONum: str = None,
        ChangeOrderNum: str = None,
        ThirdPartyCONum: str = None,
        ExpenseType: str = None,
        VendorId: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.COCreationFromDate = COCreationFromDate
        self.COCreationToDate = COCreationToDate
        self.OpenOnly = OpenOnly
        self.IncludeParentPO = IncludeParentPO
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.PONum = PONum
        self.ThirdPartyPONum = ThirdPartyPONum
        self.ChangeOrderNum = ChangeOrderNum
        self.ThirdPartyCONum = ThirdPartyCONum
        self.ExpenseType = ExpenseType
        self.VendorId = VendorId


class GetPOChangeOrdersFromModifiedDate:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        YardiPropertyId: str = None,
        COModifiedFromDate: str = None,
        COModifiedToDate: str = None,
        IncludeParentPO: bool = None,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        PONum: str = None,
        ThirdPartyPONum: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.COModifiedFromDate = COModifiedFromDate
        self.COModifiedToDate = COModifiedToDate
        self.IncludeParentPO = IncludeParentPO
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.PONum = PONum
        self.ThirdPartyPONum = ThirdPartyPONum


class ImportVendors_Login:
    """Interface: Vendor Invoicing."""
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
        XmlDoc: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.XmlDoc = XmlDoc


class ImportPayable_Login:
    """Interface: Vendor Invoicing."""
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


class ImportPurchaseOrder:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        PurchaseOrder: str = None
    ):
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.PurchaseOrder = PurchaseOrder


class ImportPOChangeOrders:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        PurchaseChangeOrderXML: str = None
    ):
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.PurchaseChangeOrderXML = PurchaseChangeOrderXML


class ImportCheck_Login:
    """Interface: Vendor Invoicing."""
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


class ImportJournalEntries:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        JournalDoc: str = None
    ):
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.JournalDoc = JournalDoc


class ExportChartOfAccounts:
    """Interface: Vendor Invoicing."""
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


class GetBookNames:
    """Interface: Vendor Invoicing."""
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


class GetJournalEntries:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        YardiPropertyId: str = None,
        BatchId: str = None,
        JournalEntryPostMonthFrom: str = None,
        JournalEntryPostMonthTo: str = None,
        JournalEntryFromDate: str = None,
        JournalEntryToDate: str = None,
        JournalCreationFromDate: str = None,
        JournalCreationToDate: str = None,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        Book: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.BatchId = BatchId
        self.JournalEntryPostMonthFrom = JournalEntryPostMonthFrom
        self.JournalEntryPostMonthTo = JournalEntryPostMonthTo
        self.JournalEntryFromDate = JournalEntryFromDate
        self.JournalEntryToDate = JournalEntryToDate
        self.JournalCreationFromDate = JournalCreationFromDate
        self.JournalCreationToDate = JournalCreationToDate
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.Book = Book


class GetJournalEntries2:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        YardiPropertyId: str = None,
        BatchId: str = None,
        JournalEntryPostMonthFrom: str = None,
        JournalEntryPostMonthTo: str = None,
        JournalEntryFromDate: str = None,
        JournalEntryToDate: str = None,
        JournalCreationFromDate: str = None,
        JournalCreationToDate: str = None,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        Book: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.BatchId = BatchId
        self.JournalEntryPostMonthFrom = JournalEntryPostMonthFrom
        self.JournalEntryPostMonthTo = JournalEntryPostMonthTo
        self.JournalEntryFromDate = JournalEntryFromDate
        self.JournalEntryToDate = JournalEntryToDate
        self.JournalCreationFromDate = JournalCreationFromDate
        self.JournalCreationToDate = JournalCreationToDate
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.Book = Book


class GetPurchaseOrderSupport:
    """Interface: Vendor Invoicing."""
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


class OpenPayableBatch:
    """Interface: Vendor Invoicing."""
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
        BatchDescription: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.BatchDescription = BatchDescription


class AddPayablesToBatch:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        BatchId: str = None,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        TransactionXml: str = None
    ):
        self.BatchId = BatchId
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.TransactionXml = TransactionXml


class ReviewPayableBatch:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        BatchId: str = None,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None
    ):
        self.BatchId = BatchId
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")


class PostPayableBatch:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        BatchId: str = None,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None
    ):
        self.BatchId = BatchId
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")


class ReturnOpenPayableBatches:
    """Interface: Vendor Invoicing."""
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


class CancelPayableBatch:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        BatchId: str = None,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None
    ):
        self.BatchId = BatchId
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")


class GetJobCost:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        IncludeChangeOrderOnly: bool = None,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        JobId: str = None,
        ContractId: str = None
    ):
        self.IncludeChangeOrderOnly = IncludeChangeOrderOnly
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.JobId = JobId
        self.ContractId = ContractId


class GetJobCostByProperty:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        IncludeChangeOrderOnly: bool = None,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        PropertyId: str = None,
        JobId: str = None,
        ContractId: str = None
    ):
        self.IncludeChangeOrderOnly = IncludeChangeOrderOnly
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.PropertyId = PropertyId
        self.JobId = JobId
        self.ContractId = ContractId


class GetRetentionAmounts:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        JobId: str = None,
        ContractId: str = None,
        VendorId: str = None
    ):
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.JobId = JobId
        self.ContractId = ContractId
        self.VendorId = VendorId


class ReversePayable:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        PostMonth: str = None,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        InvoiceNumber: str = None,
        InvoiceID: str = None
    ):
        self.PostMonth = PostMonth
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.InvoiceNumber = InvoiceNumber
        self.InvoiceID = InvoiceID


class GetSegmentInformation:
    """Interface: Vendor Invoicing."""
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


class GetInvoiceRegisterImage:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        YardiPropertyId: str = None,
        PageNo: str = None,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        InvoiceID: str = None,
        InvoiceNumber: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.PageNo = PageNo
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.InvoiceID = InvoiceID
        self.InvoiceNumber = InvoiceNumber


class GetInvoiceImage:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        YardiPropertyId: str = None,
        PageNo: str = None,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        PayableID: str = None,
        InvoiceNumber: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.PageNo = PageNo
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.PayableID = PayableID
        self.InvoiceNumber = InvoiceNumber


class ImportInvoiceRegisterImage:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        YardiPropertyId: str = None,
        InvoiceDate: str = None,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        InvoiceRegisterID: str = None,
        InvoiceNumber: str = None,
        VendorId: str = None,
        XMLDoc: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.InvoiceDate = InvoiceDate
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.InvoiceRegisterID = InvoiceRegisterID
        self.InvoiceNumber = InvoiceNumber
        self.VendorId = VendorId
        self.XMLDoc = XMLDoc


class GetBankInformation:
    """Interface: Vendor Invoicing."""
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


class GetCheckInvoice:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        CheckPostMonthFrom: str = None,
        CheckPostMonthTo: str = None,
        CheckClearedFromDate: str = None,
        CheckClearedToDate: str = None,
        CheckCreationFromDate: str = None,
        CheckCreationToDate: str = None,
        CheckFromDate: str = None,
        CheckToDate: str = None,
        JoinCheckFiltersWithOr: bool = None,
        UnprintedChecksOnly: bool = None,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        CheckBatchId: str = None,
        MarkedFor: str = None
    ):
        self.CheckPostMonthFrom = CheckPostMonthFrom
        self.CheckPostMonthTo = CheckPostMonthTo
        self.CheckClearedFromDate = CheckClearedFromDate
        self.CheckClearedToDate = CheckClearedToDate
        self.CheckCreationFromDate = CheckCreationFromDate
        self.CheckCreationToDate = CheckCreationToDate
        self.CheckFromDate = CheckFromDate
        self.CheckToDate = CheckToDate
        self.JoinCheckFiltersWithOr = JoinCheckFiltersWithOr
        self.UnprintedChecksOnly = UnprintedChecksOnly
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.CheckBatchId = CheckBatchId
        self.MarkedFor = MarkedFor


class GetCheckBatchInvoices:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        CheckPostMonthFrom: str = None,
        CheckPostMonthTo: str = None,
        CheckClearedFromDate: str = None,
        CheckClearedToDate: str = None,
        CheckCreationFromDate: str = None,
        CheckCreationToDate: str = None,
        CheckFromDate: str = None,
        CheckToDate: str = None,
        JoinCheckFiltersWithOr: bool = None,
        UnprintedChecksOnly: bool = None,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        CheckBatchId: str = None,
        MarkedFor: str = None,
        ExpenseType: str = None
    ):
        self.CheckPostMonthFrom = CheckPostMonthFrom
        self.CheckPostMonthTo = CheckPostMonthTo
        self.CheckClearedFromDate = CheckClearedFromDate
        self.CheckClearedToDate = CheckClearedToDate
        self.CheckCreationFromDate = CheckCreationFromDate
        self.CheckCreationToDate = CheckCreationToDate
        self.CheckFromDate = CheckFromDate
        self.CheckToDate = CheckToDate
        self.JoinCheckFiltersWithOr = JoinCheckFiltersWithOr
        self.UnprintedChecksOnly = UnprintedChecksOnly
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.CheckBatchId = CheckBatchId
        self.MarkedFor = MarkedFor
        self.ExpenseType = ExpenseType


class SetCheckInvoiceAsPrinted:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        CheckBatchId: str = None
    ):
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.CheckBatchId = CheckBatchId


class ImportInvoiceRegister:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        UserName: str = None,
        Password: str = None,
        ServerName: str = None,
        Database: str = None,
        Platform: str = None,
        InterfaceEntity: str = None,
        InterfaceLicense: str = None,
        InvoicRegisterDoc: str = None
    ):
        self.UserName = UserName or os.getenv("USERNAME")
        self.Password = Password or os.getenv("PASSWORD")
        self.ServerName = ServerName or os.getenv("SERVER_NAME")
        self.Database = Database or os.getenv("DATABASE")
        self.Platform = Platform or os.getenv("PLATFORM")
        self.InterfaceEntity = InterfaceEntity or os.getenv("INTERFACE_ENTITY")
        self.InterfaceLicense = InterfaceLicense or os.getenv("INTERFACE_LICENSE")
        self.InvoicRegisterDoc = InvoicRegisterDoc


class GetVersionNumber:
    """Interface: Vendor Invoicing."""
    def __init__(self):
        pass


class Ping:
    """Interface: Vendor Invoicing."""
    def __init__(self):
        pass


