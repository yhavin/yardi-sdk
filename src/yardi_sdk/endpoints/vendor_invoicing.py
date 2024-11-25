class GetInvoiceRegister:
    """Interface: Vendor Invoicing."""
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
        InvoiceCreationFromDate: str,
        InvoiceCreationToDate: str,
        InvoiceLastModifiedFromDate: str,
        InvoiceLastModifiedToDate: str,
        VendorId: str = None,
        InvoiceRegisterId: str = None,
        InvoiceNumber: str = None,
        ExpenseType: str = None,
        JobId: str = None,
        ContractId: str = None,
        BatchId: str = None
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


class CancelInvoiceRegisterBatch:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        InterfaceEntity: str,
        InterfaceLicense: str,
        BatchId: str,
        InvoiceNumber: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.BatchId = BatchId
        self.InvoiceNumber = InvoiceNumber


class GetPropertyConfigurations:
    """Interface: Vendor Invoicing."""
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


class GetVendor_Login:
    """Interface: Vendor Invoicing."""
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
    """Interface: Vendor Invoicing."""
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


class GetVendorsSync:
    """Interface: Vendor Invoicing."""
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


class GetBudgets:
    """Interface: Vendor Invoicing."""
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
        BudgetYear: str = None,
        Book: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.YardiPropertyId = YardiPropertyId
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.BudgetYear = BudgetYear
        self.Book = Book


class GetBudgets_Month:
    """Interface: Vendor Invoicing."""
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
        BudgetYear: str = None,
        Book: str = None,
        Month: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.YardiPropertyId = YardiPropertyId
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.BudgetYear = BudgetYear
        self.Book = Book
        self.Month = Month


class GetPayables:
    """Interface: Vendor Invoicing."""
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
        CheckFromDate: str,
        CheckToDate: str,
        InvoiceCreationFromDate: str,
        InvoiceCreationToDate: str,
        No3rdPartyInv: bool,
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
        self.CheckFromDate = CheckFromDate
        self.CheckToDate = CheckToDate
        self.InvoiceCreationFromDate = InvoiceCreationFromDate
        self.InvoiceCreationToDate = InvoiceCreationToDate
        self.No3rdPartyInv = No3rdPartyInv
        self.VendorId = VendorId


class GetPayables2:
    """Interface: Vendor Invoicing."""
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
        VendorId: str = None,
        PayableId: str = None,
        InvoiceNumber: str = None,
        ExpenseType: str = None
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


class GetPayableByBatchId:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        InterfaceEntity: str,
        InterfaceLicense: str,
        BatchId: str
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.BatchId = BatchId


class GetPayableByLastModifiedDate:
    """Interface: Vendor Invoicing."""
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
        FromDate: str,
        ToDate: str
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.YardiPropertyId = YardiPropertyId
        self.FromDate = FromDate
        self.ToDate = ToDate


class GetVendorInvoicingConfiguration:
    """Interface: Vendor Invoicing."""
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


class GetPurchaseOrders:
    """Interface: Vendor Invoicing."""
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
        POCreationFromDate: str,
        POCreationToDate: str,
        OpenOnly: bool,
        PONum: str = None,
        ThirdPartyPONum: str = None,
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
        self.POCreationFromDate = POCreationFromDate
        self.POCreationToDate = POCreationToDate
        self.OpenOnly = OpenOnly
        self.PONum = PONum
        self.ThirdPartyPONum = ThirdPartyPONum
        self.VendorId = VendorId


class GetPOFromModifiedDate:
    """Interface: Vendor Invoicing."""
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
        POModifiedFromDate: str,
        POModifiedToDate: str
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.YardiPropertyId = YardiPropertyId
        self.POModifiedFromDate = POModifiedFromDate
        self.POModifiedToDate = POModifiedToDate


class GetPOChangeOrders:
    """Interface: Vendor Invoicing."""
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
        COCreationFromDate: str,
        COCreationToDate: str,
        OpenOnly: bool,
        IncludeParentPO: bool,
        PONum: str = None,
        ThirdPartyPONum: str = None,
        ChangeOrderNum: str = None,
        ThirdPartyCONum: str = None,
        ExpenseType: str = None,
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


class GetPOChangeOrdersFromModifiedDate:
    """Interface: Vendor Invoicing."""
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
        COModifiedFromDate: str,
        COModifiedToDate: str,
        IncludeParentPO: bool,
        PONum: str = None,
        ThirdPartyPONum: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.YardiPropertyId = YardiPropertyId
        self.COModifiedFromDate = COModifiedFromDate
        self.COModifiedToDate = COModifiedToDate
        self.IncludeParentPO = IncludeParentPO
        self.PONum = PONum
        self.ThirdPartyPONum = ThirdPartyPONum


class ImportVendors_Login:
    """Interface: Vendor Invoicing."""
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
        XmlDoc: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.YardiPropertyId = YardiPropertyId
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.XmlDoc = XmlDoc


class ImportPayable_Login:
    """Interface: Vendor Invoicing."""
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


class ImportPurchaseOrder:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        InterfaceEntity: str,
        InterfaceLicense: str,
        PurchaseOrder: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.PurchaseOrder = PurchaseOrder


class ImportPOChangeOrders:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        InterfaceEntity: str,
        InterfaceLicense: str,
        PurchaseChangeOrderXML: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.PurchaseChangeOrderXML = PurchaseChangeOrderXML


class ImportCheck_Login:
    """Interface: Vendor Invoicing."""
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


class ImportJournalEntries:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        InterfaceEntity: str,
        InterfaceLicense: str,
        JournalDoc: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.JournalDoc = JournalDoc


class ExportChartOfAccounts:
    """Interface: Vendor Invoicing."""
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


class GetBookNames:
    """Interface: Vendor Invoicing."""
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


class GetJournalEntries:
    """Interface: Vendor Invoicing."""
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
        BatchId: str,
        JournalEntryPostMonthFrom: str,
        JournalEntryPostMonthTo: str,
        JournalEntryFromDate: str,
        JournalEntryToDate: str,
        JournalCreationFromDate: str,
        JournalCreationToDate: str,
        Book: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.YardiPropertyId = YardiPropertyId
        self.BatchId = BatchId
        self.JournalEntryPostMonthFrom = JournalEntryPostMonthFrom
        self.JournalEntryPostMonthTo = JournalEntryPostMonthTo
        self.JournalEntryFromDate = JournalEntryFromDate
        self.JournalEntryToDate = JournalEntryToDate
        self.JournalCreationFromDate = JournalCreationFromDate
        self.JournalCreationToDate = JournalCreationToDate
        self.Book = Book


class GetJournalEntries2:
    """Interface: Vendor Invoicing."""
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
        BatchId: str,
        JournalEntryPostMonthFrom: str,
        JournalEntryPostMonthTo: str,
        JournalEntryFromDate: str,
        JournalEntryToDate: str,
        JournalCreationFromDate: str,
        JournalCreationToDate: str,
        Book: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.YardiPropertyId = YardiPropertyId
        self.BatchId = BatchId
        self.JournalEntryPostMonthFrom = JournalEntryPostMonthFrom
        self.JournalEntryPostMonthTo = JournalEntryPostMonthTo
        self.JournalEntryFromDate = JournalEntryFromDate
        self.JournalEntryToDate = JournalEntryToDate
        self.JournalCreationFromDate = JournalCreationFromDate
        self.JournalCreationToDate = JournalCreationToDate
        self.Book = Book


class GetPurchaseOrderSupport:
    """Interface: Vendor Invoicing."""
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


class OpenPayableBatch:
    """Interface: Vendor Invoicing."""
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
        BatchDescription: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.YardiPropertyId = YardiPropertyId
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.BatchDescription = BatchDescription


class AddPayablesToBatch:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        InterfaceEntity: str,
        InterfaceLicense: str,
        BatchId: str,
        TransactionXml: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.BatchId = BatchId
        self.TransactionXml = TransactionXml


class ReviewPayableBatch:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        InterfaceEntity: str,
        InterfaceLicense: str,
        BatchId: str
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.BatchId = BatchId


class PostPayableBatch:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        InterfaceEntity: str,
        InterfaceLicense: str,
        BatchId: str
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.BatchId = BatchId


class ReturnOpenPayableBatches:
    """Interface: Vendor Invoicing."""
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


class CancelPayableBatch:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        InterfaceEntity: str,
        InterfaceLicense: str,
        BatchId: str
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.BatchId = BatchId


class GetJobCost:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        InterfaceEntity: str,
        InterfaceLicense: str,
        IncludeChangeOrderOnly: bool,
        JobId: str = None,
        ContractId: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.IncludeChangeOrderOnly = IncludeChangeOrderOnly
        self.JobId = JobId
        self.ContractId = ContractId


class GetJobCostByProperty:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        InterfaceEntity: str,
        InterfaceLicense: str,
        IncludeChangeOrderOnly: bool,
        PropertyId: str = None,
        JobId: str = None,
        ContractId: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.IncludeChangeOrderOnly = IncludeChangeOrderOnly
        self.PropertyId = PropertyId
        self.JobId = JobId
        self.ContractId = ContractId


class GetRetentionAmounts:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        InterfaceEntity: str,
        InterfaceLicense: str,
        JobId: str = None,
        ContractId: str = None,
        VendorId: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.JobId = JobId
        self.ContractId = ContractId
        self.VendorId = VendorId


class ReversePayable:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        InterfaceEntity: str,
        InterfaceLicense: str,
        PostMonth: str,
        InvoiceNumber: str = None,
        InvoiceID: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.PostMonth = PostMonth
        self.InvoiceNumber = InvoiceNumber
        self.InvoiceID = InvoiceID


class GetSegmentInformation:
    """Interface: Vendor Invoicing."""
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


class GetInvoiceRegisterImage:
    """Interface: Vendor Invoicing."""
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
        PageNo: str,
        InvoiceID: str = None,
        InvoiceNumber: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.YardiPropertyId = YardiPropertyId
        self.PageNo = PageNo
        self.InvoiceID = InvoiceID
        self.InvoiceNumber = InvoiceNumber


class GetInvoiceImage:
    """Interface: Vendor Invoicing."""
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
        PageNo: str,
        PayableID: str = None,
        InvoiceNumber: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.YardiPropertyId = YardiPropertyId
        self.PageNo = PageNo
        self.PayableID = PayableID
        self.InvoiceNumber = InvoiceNumber


class ImportInvoiceRegisterImage:
    """Interface: Vendor Invoicing."""
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
        InvoiceDate: str,
        InvoiceRegisterID: str = None,
        InvoiceNumber: str = None,
        VendorId: str = None,
        XMLDoc: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.YardiPropertyId = YardiPropertyId
        self.InvoiceDate = InvoiceDate
        self.InvoiceRegisterID = InvoiceRegisterID
        self.InvoiceNumber = InvoiceNumber
        self.VendorId = VendorId
        self.XMLDoc = XMLDoc


class GetBankInformation:
    """Interface: Vendor Invoicing."""
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


class GetCheckInvoice:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        InterfaceEntity: str,
        InterfaceLicense: str,
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
        CheckBatchId: str = None,
        MarkedFor: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
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


class GetCheckBatchInvoices:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        InterfaceEntity: str,
        InterfaceLicense: str,
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
        CheckBatchId: str = None,
        MarkedFor: str = None,
        ExpenseType: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
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


class SetCheckInvoiceAsPrinted:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        InterfaceEntity: str,
        InterfaceLicense: str,
        CheckBatchId: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.CheckBatchId = CheckBatchId


class ImportInvoiceRegister:
    """Interface: Vendor Invoicing."""
    def __init__(
        self,
        UserName: str,
        Password: str,
        ServerName: str,
        Database: str,
        Platform: str,
        InterfaceEntity: str,
        InterfaceLicense: str,
        InvoicRegisterDoc: str = None
    ):
        self.UserName = UserName
        self.Password = Password
        self.ServerName = ServerName
        self.Database = Database
        self.Platform = Platform
        self.InterfaceEntity = InterfaceEntity
        self.InterfaceLicense = InterfaceLicense
        self.InvoicRegisterDoc = InvoicRegisterDoc


class GetVersionNumber:
    """Interface: Vendor Invoicing."""
    def __init__(self):
        pass


class Ping:
    """Interface: Vendor Invoicing."""
    def __init__(self):
        pass


