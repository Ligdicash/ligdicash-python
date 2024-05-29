import ligdicash

PAYOUT_CLIENT_WIKI = {
    "test": {
        "00": ligdicash.AuthenticationError,
        "01": ligdicash.MerchantPayoutDisabledError,
        "02": ligdicash.CustomerDoesNotExistError,
        "03": ligdicash.MerchantAccountDoesNotExistError,
        "03a": ligdicash.NoPendProcPayout24HError,
        "03b": ligdicash.NoDeposit3MError,
        "04": ligdicash.MerchantBalanceLowError,
        "05": ligdicash.AmountOutOfRangeError,
        "06": ligdicash.IpDeniedError,
        "07": ligdicash.TransactionAlreadyExistError,
        "08": ligdicash.ProcessingError,
        "09": ligdicash.DataInputError,
        "10": ligdicash.ApiError,
        "13": ligdicash.NoHashError,
        "14": ligdicash.InvalidHashError,
    },
    "live": {
        "00": ligdicash.AuthenticationError,
        "01": ligdicash.MerchantPayoutDisabledError,
        "02": ligdicash.CustomerDoesNotExistError,
        "03": ligdicash.MerchantAccountDoesNotExistError,
        "03a": ligdicash.NoPendProcPayout24HError,
        "03b": ligdicash.NoDeposit3MError,
        "04": ligdicash.MerchantBalanceLowError,
        "05": ligdicash.AmountOutOfRangeError,
        "06": ligdicash.IpDeniedError,
        "07": ligdicash.TransactionAlreadyExistError,
        "08": ligdicash.ProcessingError,
        "09": ligdicash.DataInputError,
        "10": ligdicash.ApiError,
        "13": ligdicash.NoHashError,
        "14": ligdicash.InvalidHashError,
    },
}

PAYOUT_MARCHAND_WIKI = {
    "test": {
        "00": ligdicash.AuthenticationError,
        "01": ligdicash.ApplicationAuthenticationError,
        "02": ligdicash.AmountOutOfRangeError,
        "03": ligdicash.MerchantAccountDoesNotExistError,
        "04": ligdicash.NoPendProcPayout24HError,
        "05": ligdicash.RecipientOperatorNotIdentifiedError,
        "06": ligdicash.MerchantAccountDoesNotExistError,
        "07": ligdicash.MerchantAccountDoesNotExistError,
        "08": ligdicash.MerchantBalanceLowError,
        "09": ligdicash.ProcessingError,
        "10": ligdicash.ApiError,
        "11": ligdicash.NoHashError,
        "12": ligdicash.InvalidHashError,
        "13": ligdicash.UnauthorizedCurrencyConversionError,
        "14": ligdicash.IpDeniedError,
    },
    "live": {
        "00": ligdicash.AuthenticationError,
        "01": ligdicash.ApplicationAuthenticationError,
        "02": ligdicash.AmountOutOfRangeError,
        "03": ligdicash.MerchantAccountDoesNotExistError,
        "04": ligdicash.NoPendProcPayout24HError,
        "05": ligdicash.RecipientOperatorNotIdentifiedError,
        "06": ligdicash.MerchantAccountDoesNotExistError,
        "07": ligdicash.MerchantAccountDoesNotExistError,
        "08": ligdicash.MerchantBalanceLowError,
        "09": ligdicash.ProcessingError,
        "10": ligdicash.ApiError,
        "11": ligdicash.NoHashError,
        "12": ligdicash.InvalidHashError,
        "13": ligdicash.UnauthorizedCurrencyConversionError,
        "14": ligdicash.IpDeniedError,
    },
}
""" Wiki des erreurs possibles pour le Payout en test ou en live """


PAYIN_WIKI = {
    "test": {
        "00": ligdicash.AuthenticationError,
        "01": ligdicash.ApplicationAuthenticationError,
        "02": ligdicash.InvalidAmountError,
        "03": ligdicash.IpDeniedError,
        "04": ligdicash.ProcessingError,
    },
    "live": {
        "00": ligdicash.AuthenticationError,
        "01": ligdicash.MerchantPayinDisabledError,
        "02": ligdicash.InvalidAmountError,
        "03": ligdicash.IpDeniedError,
        "04": ligdicash.ProcessingError,
        "05": ligdicash.SendingError,
        "06": ligdicash.SendingError,
        "07": ligdicash.NoNetworkAccessConfigurationError,
        "08": ligdicash.DataInputError,
        "09": ligdicash.ApiError,
        "10": ligdicash.NoHashError,
        "11": ligdicash.InvalidHashError,
        "12": ligdicash.InvalidMethodError,
        "13": ligdicash.UnauthorizedMethodError,
    },
}
""" Wiki des erreurs possibles pour le Payin en test ou en live """


STATUS_WIKI = {
    "test": {
        "00": ligdicash.AuthenticationError,
        "01": ligdicash.ApplicationAuthenticationError,
        "02": ligdicash.InvoiceNotFoundError,
        "03": ligdicash.ProcessingError,
    },
    "live": {
        "00": ligdicash.AuthenticationError,
        "01": ligdicash.MerchantPayinDisabledError,
        "02": ligdicash.InvoiceNotFoundError,
        "03": ligdicash.ProcessingError,
        "04": ligdicash.DataInputError,
    },
}
""" Wiki des erreurs possibles pour le statut d'une transaction en test ou en live """


WIKI = {
    "payin": PAYIN_WIKI,
    "client_payout": PAYOUT_CLIENT_WIKI,
    "merchant_payout": PAYOUT_MARCHAND_WIKI,
    "status": STATUS_WIKI,
}
""" Définission des wiki Payin, Payout et Status """


def get_wiki_error(wiki_name: str, error_code: str):
    """
    Fonction qui retourne L'erreur correspondant au nom de wiki et au code d'erreur donnés et à la plateforme actuelle

    Parameters
    ----------
    wiki_name : str
        Nom du wiki.
    error_code : str
        Code d'erreur.

    Returns
    -------
    Exception
        Erreur correspondant.
    """
    if WIKI.get(wiki_name) and WIKI.get(wiki_name).get(ligdicash.platform) and WIKI.get(wiki_name).get(ligdicash.platform).get(error_code):
        print (WIKI.get(wiki_name).get(ligdicash.platform).get(error_code))
        return WIKI.get(wiki_name).get(ligdicash.platform).get(error_code)
    return ligdicash.ApiError
