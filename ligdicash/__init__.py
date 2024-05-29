from typing import Literal

from .errors import (
    AmountOutOfRangeError,
    ApiError,
    ApplicationAuthenticationError,
    AuthenticationError,
    CustomerDoesNotExistError,
    DataInputError,
    FeatureNotTestableError,
    InvalidAmountError,
    InvalidHashError,
    InvalidMethodError,
    InvalidTokenError,
    InvoiceNotFoundError,
    IpDeniedError,
    LigdicashError,
    MerchantAccountDoesNotExistError,
    MerchantBalanceLowError,
    MerchantPayinDisabledError,
    MerchantPayoutDisabledError,
    NoDeposit3MError,
    NoDeposit24HError,
    RecipientOperatorNotIdentifiedError,
    UnauthorizedCurrencyConversionError,
    NoHashError,
    NoNetworkAccessConfigurationError,
    NoPendProcPayout24HError,
    ProcessingError,
    SendingError,
    TransactionAlreadyExistError,
    UnauthorizedMethodError,
)
from .payin import Invoice, InvoiceItem
from .payout import Withdrawal
from .transaction import get_transaction

api_key: str = None
auth_token: str = None
platform: Literal["test", "live"] = "live"
