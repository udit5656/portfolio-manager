from groww import GrowwTransaction
from dataClass import GoogleSheetTransaction


def groww_to_google_sheet(groww_transaction: GrowwTransaction):
    return GoogleSheetTransaction(
        groww_transaction.date,
        groww_transaction.type,
        groww_transaction.symbol,
        groww_transaction.quantity,
        groww_transaction.price,
    )
