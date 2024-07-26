from .providers import HTTPProvider
from .responses import StatusResponse
from typing import Literal


def get_transaction(token: str = None, type:Literal["payin", "client_payout", "merchant_payout"]="payin") -> StatusResponse:
    """
    Récupère une transaction à partir d'un jeton.

    Parameters
    ----------
    token : (str, optional)
        Le jeton de la transaction. Defaults à None.
    type : Literal["payin", "client_payout", "merchant_payout"]

    Returns
    -------
    ligdicash.responses.StatusResponse
        Une instance de StatusResponse représentant la transaction.

    Raises
    ------
    ligdicash.errors.InvalidTokenError
        Si le jeton est invalide ou n'est pas fourni.
    """

    from . import InvalidTokenError

    if not token or token == "":
        raise InvalidTokenError()
    provider = HTTPProvider()
    response = provider.get(
        f"redirect/checkout-invoice/confirm/?invoiceToken={token}" if type == "payin" else f"withdrawal/confirm/?withdrawalToken={token}" if type == "client_payout" else f"straight/payout/confirm/?payoutToken={token}",
        feature="status"
    )
    response_data = StatusResponse.from_dict(response)
    return response_data
