from zeep.xsd.types.builtins import (
    String,
    Boolean,
    Decimal,
    Float,
    Double,
    DateTime,
    Date,
    Integer 
)


type_map = {
    String: "str",
    Boolean: "bool",
    Decimal: "float",
    Float: "float",
    Double: "float",
    DateTime: "str",
    Date: "str",
    Integer: "int"
}