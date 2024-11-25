import os


class GetInvoiceRegister:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        YardiPropertyId: str,
        InvoicePostMonthFrom: str,
        InvoicePostMonthTo: str,
        InvoiceFromDate: str,
        InvoiceToDate: str,
        InvoiceCreationFromDate: str,
        InvoiceCreationToDate: str,
        InvoiceLastModifiedFromDate: str,
        InvoiceLastModifiedToDate: str,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
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
        self.VendorId = VendorId
        self.InvoiceRegisterId = InvoiceRegisterId
        self.InvoiceNumber = InvoiceNumber
        self.ExpenseType = ExpenseType
        self.JobId = JobId
        self.ContractId = ContractId
        self.BatchId = BatchId
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class CancelInvoiceRegisterBatch:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        BatchId: str,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
        InvoiceNumber: str = None
    ):
        self.BatchId = BatchId
        self.InvoiceNumber = InvoiceNumber
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetPropertyConfigurations:
    """Interface: Vendor Invoicing."""
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


class GetVendor_Login:
    """Interface: Vendor Invoicing."""
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
    """Interface: Vendor Invoicing."""
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


class GetVendorsSync:
    """Interface: Vendor Invoicing."""
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


class GetBudgets:
    """Interface: Vendor Invoicing."""
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
        BudgetYear: str = None,
        Book: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.BudgetYear = BudgetYear
        self.Book = Book
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetBudgets_Month:
    """Interface: Vendor Invoicing."""
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
        BudgetYear: str = None,
        Book: str = None,
        Month: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.BudgetYear = BudgetYear
        self.Book = Book
        self.Month = Month
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetPayables:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        YardiPropertyId: str,
        InvoicePostMonthFrom: str,
        InvoicePostMonthTo: str,
        InvoiceFromDate: str,
        InvoiceToDate: str,
        UnpaidOnly: bool,
        CheckFromDate: str,
        CheckToDate: str,
        InvoiceCreationFromDate: str,
        InvoiceCreationToDate: str,
        No3rdPartyInv: bool,
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
        self.CheckFromDate = CheckFromDate
        self.CheckToDate = CheckToDate
        self.InvoiceCreationFromDate = InvoiceCreationFromDate
        self.InvoiceCreationToDate = InvoiceCreationToDate
        self.No3rdPartyInv = No3rdPartyInv
        self.VendorId = VendorId
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetPayables2:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        YardiPropertyId: str,
        InvoicePostMonthFrom: str,
        InvoicePostMonthTo: str,
        InvoiceFromDate: str,
        InvoiceToDate: str,
        UnpaidOnly: bool,
        InvoiceCreationFromDate: str,
        InvoiceCreationToDate: str,
        No3rdPartyInv: bool,
        CheckPostMonthFrom: str,
        CheckPostMonthTo: str,
        CheckClearedFromDate: str,
        CheckClearedToDate: str,
        CheckCreationFromDate: str,
        CheckCreationToDate: str,
        CheckFromDate: str,
        CheckToDate: str,
        UnpostedInvoicesOnly: bool,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
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
        self.VendorId = VendorId
        self.PayableId = PayableId
        self.InvoiceNumber = InvoiceNumber
        self.ExpenseType = ExpenseType
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetPayableByBatchId:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        BatchId: str,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE")
    ):
        self.BatchId = BatchId
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetPayableByLastModifiedDate:
    """Interface: Vendor Invoicing."""
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


class GetVendorInvoicingConfiguration:
    """Interface: Vendor Invoicing."""
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


class GetPurchaseOrders:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        YardiPropertyId: str,
        POCreationFromDate: str,
        POCreationToDate: str,
        OpenOnly: bool,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
        PONum: str = None,
        ThirdPartyPONum: str = None,
        VendorId: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.POCreationFromDate = POCreationFromDate
        self.POCreationToDate = POCreationToDate
        self.OpenOnly = OpenOnly
        self.PONum = PONum
        self.ThirdPartyPONum = ThirdPartyPONum
        self.VendorId = VendorId
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetPOFromModifiedDate:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        YardiPropertyId: str,
        POModifiedFromDate: str,
        POModifiedToDate: str,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE")
    ):
        self.YardiPropertyId = YardiPropertyId
        self.POModifiedFromDate = POModifiedFromDate
        self.POModifiedToDate = POModifiedToDate
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetPOChangeOrders:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        YardiPropertyId: str,
        COCreationFromDate: str,
        COCreationToDate: str,
        OpenOnly: bool,
        IncludeParentPO: bool,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
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
        self.PONum = PONum
        self.ThirdPartyPONum = ThirdPartyPONum
        self.ChangeOrderNum = ChangeOrderNum
        self.ThirdPartyCONum = ThirdPartyCONum
        self.ExpenseType = ExpenseType
        self.VendorId = VendorId
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetPOChangeOrdersFromModifiedDate:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        YardiPropertyId: str,
        COModifiedFromDate: str,
        COModifiedToDate: str,
        IncludeParentPO: bool,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
        PONum: str = None,
        ThirdPartyPONum: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.COModifiedFromDate = COModifiedFromDate
        self.COModifiedToDate = COModifiedToDate
        self.IncludeParentPO = IncludeParentPO
        self.PONum = PONum
        self.ThirdPartyPONum = ThirdPartyPONum
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class ImportVendors_Login:
    """Interface: Vendor Invoicing."""
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
        XmlDoc: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.XmlDoc = XmlDoc
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class ImportPayable_Login:
    """Interface: Vendor Invoicing."""
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


class ImportPurchaseOrder:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
        PurchaseOrder: str = None
    ):
        self.PurchaseOrder = PurchaseOrder
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class ImportPOChangeOrders:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
        PurchaseChangeOrderXML: str = None
    ):
        self.PurchaseChangeOrderXML = PurchaseChangeOrderXML
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class ImportCheck_Login:
    """Interface: Vendor Invoicing."""
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


class ImportJournalEntries:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
        JournalDoc: str = None
    ):
        self.JournalDoc = JournalDoc
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class ExportChartOfAccounts:
    """Interface: Vendor Invoicing."""
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


class GetBookNames:
    """Interface: Vendor Invoicing."""
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


class GetJournalEntries:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        YardiPropertyId: str,
        BatchId: str,
        JournalEntryPostMonthFrom: str,
        JournalEntryPostMonthTo: str,
        JournalEntryFromDate: str,
        JournalEntryToDate: str,
        JournalCreationFromDate: str,
        JournalCreationToDate: str,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
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
        self.Book = Book
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetJournalEntries2:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        YardiPropertyId: str,
        BatchId: str,
        JournalEntryPostMonthFrom: str,
        JournalEntryPostMonthTo: str,
        JournalEntryFromDate: str,
        JournalEntryToDate: str,
        JournalCreationFromDate: str,
        JournalCreationToDate: str,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
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
        self.Book = Book
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetPurchaseOrderSupport:
    """Interface: Vendor Invoicing."""
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


class OpenPayableBatch:
    """Interface: Vendor Invoicing."""
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
        BatchDescription: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.BatchDescription = BatchDescription
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class AddPayablesToBatch:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        BatchId: str,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
        TransactionXml: str = None
    ):
        self.BatchId = BatchId
        self.TransactionXml = TransactionXml
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class ReviewPayableBatch:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        BatchId: str,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE")
    ):
        self.BatchId = BatchId
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class PostPayableBatch:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        BatchId: str,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE")
    ):
        self.BatchId = BatchId
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class ReturnOpenPayableBatches:
    """Interface: Vendor Invoicing."""
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


class CancelPayableBatch:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        BatchId: str,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE")
    ):
        self.BatchId = BatchId
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetJobCost:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        IncludeChangeOrderOnly: bool,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
        JobId: str = None,
        ContractId: str = None
    ):
        self.IncludeChangeOrderOnly = IncludeChangeOrderOnly
        self.JobId = JobId
        self.ContractId = ContractId
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetJobCostByProperty:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        IncludeChangeOrderOnly: bool,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
        PropertyId: str = None,
        JobId: str = None,
        ContractId: str = None
    ):
        self.IncludeChangeOrderOnly = IncludeChangeOrderOnly
        self.PropertyId = PropertyId
        self.JobId = JobId
        self.ContractId = ContractId
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetRetentionAmounts:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
        JobId: str = None,
        ContractId: str = None,
        VendorId: str = None
    ):
        self.JobId = JobId
        self.ContractId = ContractId
        self.VendorId = VendorId
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class ReversePayable:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        PostMonth: str,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
        InvoiceNumber: str = None,
        InvoiceID: str = None
    ):
        self.PostMonth = PostMonth
        self.InvoiceNumber = InvoiceNumber
        self.InvoiceID = InvoiceID
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetSegmentInformation:
    """Interface: Vendor Invoicing."""
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


class GetInvoiceRegisterImage:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        YardiPropertyId: str,
        PageNo: str,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
        InvoiceID: str = None,
        InvoiceNumber: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.PageNo = PageNo
        self.InvoiceID = InvoiceID
        self.InvoiceNumber = InvoiceNumber
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetInvoiceImage:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        YardiPropertyId: str,
        PageNo: str,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
        PayableID: str = None,
        InvoiceNumber: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.PageNo = PageNo
        self.PayableID = PayableID
        self.InvoiceNumber = InvoiceNumber
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class ImportInvoiceRegisterImage:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        YardiPropertyId: str,
        InvoiceDate: str,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
        InvoiceRegisterID: str = None,
        InvoiceNumber: str = None,
        VendorId: str = None,
        XMLDoc: str = None
    ):
        self.YardiPropertyId = YardiPropertyId
        self.InvoiceDate = InvoiceDate
        self.InvoiceRegisterID = InvoiceRegisterID
        self.InvoiceNumber = InvoiceNumber
        self.VendorId = VendorId
        self.XMLDoc = XMLDoc
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetBankInformation:
    """Interface: Vendor Invoicing."""
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


class GetCheckInvoice:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        CheckPostMonthFrom: str,
        CheckPostMonthTo: str,
        CheckClearedFromDate: str,
        CheckClearedToDate: str,
        CheckCreationFromDate: str,
        CheckCreationToDate: str,
        CheckFromDate: str,
        CheckToDate: str,
        JoinCheckFiltersWithOr: bool,
        UnprintedChecksOnly: bool,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
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
        self.CheckBatchId = CheckBatchId
        self.MarkedFor = MarkedFor
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetCheckBatchInvoices:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        CheckPostMonthFrom: str,
        CheckPostMonthTo: str,
        CheckClearedFromDate: str,
        CheckClearedToDate: str,
        CheckCreationFromDate: str,
        CheckCreationToDate: str,
        CheckFromDate: str,
        CheckToDate: str,
        JoinCheckFiltersWithOr: bool,
        UnprintedChecksOnly: bool,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
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
        self.CheckBatchId = CheckBatchId
        self.MarkedFor = MarkedFor
        self.ExpenseType = ExpenseType
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class SetCheckInvoiceAsPrinted:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
        CheckBatchId: str = None
    ):
        self.CheckBatchId = CheckBatchId
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class ImportInvoiceRegister:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        UserName: str = os.getenv("USERNAME"),
        Password: str = os.getenv("PASSWORD"),
        ServerName: str = os.getenv("SERVER_NAME"),
        Database: str = os.getenv("DATABASE"),
        Platform: str = os.getenv("PLATFORM"),
        InterfaceEntity: str = os.getenv("INTERFACE_ENTITY"),
        InterfaceLicense: str = os.getenv("INTERFACE_LICENSE"),
        InvoicRegisterDoc: str = None
    ):
        self.InvoicRegisterDoc = InvoicRegisterDoc
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense


class GetVersionNumber:
    """Interface: Vendor Invoicing."""
    def __init__(self):
        pass


class Ping:
    """Interface: Vendor Invoicing."""
    def __init__(self):
        pass


