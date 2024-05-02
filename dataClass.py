import enum
from dataclasses import dataclass


class TransactionType(enum.Enum):
    BUY = "Buy"
    SELL = "Sell"
    DIV = "Div"
    SPLIT = "Split"
    Fee = "Fee"


@dataclass
class DataEquityPortfolio:
    data: str
    type: TransactionType
    stock: str
    units: int
    price: float
    fees: float = 0.0
    stock_split_ratio: float = 1.0
