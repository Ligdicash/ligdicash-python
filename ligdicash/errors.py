class LigdicashError(Exception):
    """
    Exception de base pour les erreurs liées à l'API Ligdicash.

    Attributes
    ----------
    code : str
        Le code d'erreur associé à l'exception.
    message : str
        Le message d'erreur associé à l'exception.
    """

    def __init__(self, code: str, message: str):
        """
        Constructeur de la classe LigdicashError.

        Parameters
        ----------
        code : str
            Le code d'erreur associé à l'exception.
        message : str
            Le message d'erreur associé à l'exception.
        """
        self.code = code
        self.message = message
        super(LigdicashError, self).__init__(message)

    def get_code(self):
        """
        Retourne le code d'erreur associé à l'exception.

        Return
        ------
        str
            Le code d'erreur associé à l'exception.
        """
        return self.code

    def get_message(self):
        """
        Retourne le message d'erreur associé à l'exception.

        Return
        ------
        str
            Le message d'erreur associé à l'exception.
        """
        return self.message

    def __str__(self):
        """
        Retourne le message d'erreur associé à l'exception.

        Return
        ------
        str
            Le message d'erreur associé à l'exception.
        """
        return self.message

    def __repr__(self):
        """
        Retourne une représentation en chaîne de caractères de l'exception.

        Return
        ------
        str
            Une représentation en chaîne de caractères de l'exception.
        """
        return f"{self.code}: {self.message}"


class AuthenticationError(LigdicashError):
    """Classe d'erreur pour les erreurs d'authentification Ligdicash."""

    def __init__(self, code: str):
        """
        Initialise une nouvelle instance de AuthenticationError.

        Parameters
        ----------
        code : str
            Le code d'erreur de Ligdicash.
        """
        super(AuthenticationError, self).__init__(
            code, "api_key or auth_token is invalid"
        )


class ApplicationAuthenticationError(LigdicashError):
    """Classe d'erreur pour les erreurs d'authentification d'application Ligdicash."""

    def __init__(self, code: str):
        super(ApplicationAuthenticationError, self).__init__(
            code, "Unable to authenticate your application"
        )


class MerchantBalanceLowError(LigdicashError):
    """Classe d'erreur si le solde du commerçant est insuffisant."""

    def __init__(self, code: str):
        super(MerchantBalanceLowError, self).__init__(code, "Merchant balance low")


class MerchantPayoutDisabledError(LigdicashError):
    """Classe d'erreur si le retrait est désactivé pour ce commerçant."""

    def __init__(self, code: str):
        super(MerchantPayoutDisabledError, self).__init__(
            code, "Payout is disabled for this Merchant"
        )


class MerchantPayinDisabledError(LigdicashError):
    """Classe d'erreur si la fonctionnalité de paiement n'est pas activée pour ce commerçant"""

    def __init__(self, code: str):
        super(MerchantPayinDisabledError, self).__init__(
            code, "Merchant Payin feature is not activated"
        )


class CustomerDoesNotExistError(LigdicashError):
    """Classe d'erreur si le client n'est pas enregistré sur la plateforme."""

    def __init__(self, code: str):
        super(CustomerDoesNotExistError, self).__init__(
            code, "This customer is not registered on the platform"
        )


class TransactionAlreadyExistError(LigdicashError):
    """Classe d'erreur si la transaction existe déjà."""

    def __init__(self, code: str):
        super(TransactionAlreadyExistError, self).__init__(
            code, "Transaction already exists"
        )


class InvoiceNotFoundError(LigdicashError):
    """Classe d'erreur si la facture n'a pas été trouvée."""

    def __init__(self, code: str):
        super(InvoiceNotFoundError, self).__init__(code, "Invoice not found")


class InvalidAmountError(LigdicashError):
    """Classe d'erreur si le montant est invalide. Il doit être compris entre 20 et 1 000 000."""

    def __init__(self, code: str):
        super(InvalidAmountError, self).__init__(
            code, "Invalid amount. It should fall within the range of 20 to 1000000."
        )


class InvalidTokenError(LigdicashError):
    """Classe d'erreur si le Token est invalide."""

    def __init__(self, code: str):
        super(InvalidTokenError, self).__init__(code, "Invalid token")


class MerchantAccountDoesNotExistError(LigdicashError):
    """Classe d'erreur si aucun compte marchand sur le réseau spécifié."""

    def __init__(self, code: str):
        super(MerchantAccountDoesNotExistError, self).__init__(
            code, "No merchant account on the specified network"
        )


class NoPendProcPayout24HError(LigdicashError):
    """Classe d'erreur si aucun paiement en attente ou traité au cours des dernières 24 heures."""

    def __init__(self, code: str):
        super(NoPendProcPayout24HError, self).__init__(
            code, "No pending or processed payout within the last 24hours"
        )


class NoDeposit3MError(LigdicashError):
    """Classe d'erreur si aucun paiement en attente ou traité au cours des 3 derniers mois"""

    def __init__(self, code: str):
        super(NoDeposit3MError, self).__init__(
            code, "No deposit withing the last 3 months"
        )


class RecipientOperatorNotIdentifiedError(LigdicashError):
    """Classe d'erreur si l'opérateur du destinataire n'a pas été identifié"""

    def __init__(self, code: str):
        super(RecipientOperatorNotIdentifiedError, self).__init__(
            code, "Recipient operator not identified"
        )


class UnauthorizedCurrencyConversionError(LigdicashError):
    """Classe d'erreur si la conversion de devise n'est pas autorisée."""

    def __init__(self, code: str):
        super(UnauthorizedCurrencyConversionError, self).__init__(
            code, "Unauthorized currency conversion"
        )


class NoDeposit24HError(LigdicashError):
    """Classe d'erreur si aucun dépôt au cours des dernières 24 heures."""

    def __init__(self, code: str):
        super(NoDeposit24HError, self).__init__(
            code, "No deposit withing the last 24 hours"
        )


class AmountOutOfRangeError(LigdicashError):
    """Classe d'erreur si le montant demandé est hors de l'interval [20;1000000]."""

    def __init__(self, code: str):
        super(AmountOutOfRangeError, self).__init__(
            code, "Request amount is out of range [20;1000000]"
        )


class IpDeniedError(LigdicashError):
    """Classe d'erreur si l'adresse IP est refusée."""

    def __init__(self, code: str):
        super(IpDeniedError, self).__init__(code, "IP denied")


class ProcessingError(LigdicashError):
    """Classe d'erreur si une erreur s'est produite pendant le traitement."""

    def __init__(self, code: str):
        super(ProcessingError, self).__init__(
            code, "An error occurred while processing"
        )


class SendingError(LigdicashError):
    """Classe d'erreur si une erreur s'est produite lors de l'envoi."""

    def __init__(self, code: str):
        super(SendingError, self).__init__(code, "An error occurred while processing")


class DataInputError(LigdicashError):
    """Classe d'erreur s'il y'a une erreur de saisie de données."""

    def __init__(self, code: str):
        super(DataInputError, self).__init__(code, "Data Input error")


class ApiError(LigdicashError):
    """Classe d'erreur s'il y'a une erreur d'API."""

    def __init__(self, code: str):
        super(ApiError, self).__init__(code, "Api error")


class NoHashError(LigdicashError):
    """Classe d'erreur si aucun hash n'a été fourni."""

    def __init__(self, code: str):
        super(NoHashError, self).__init__(code, "No hash provided")


class InvalidHashError(LigdicashError):
    """Classe d'erreur si le hash est invalide."""

    def __init__(self, code: str):
        super(InvalidHashError, self).__init__(code, "Invalid hash")


class NoNetworkAccessConfigurationError(LigdicashError):
    """Classe d'erreur si aucun accès réseau n'est configuré."""

    def __init__(self, code: str):
        super(NoNetworkAccessConfigurationError, self).__init__(
            code, "No network access configured"
        )


class UnauthorizedMethodError(LigdicashError):
    """Classe d'erreur si la méthode HTTP n'est pas autorisée."""

    def __init__(self, code: str):
        super(UnauthorizedMethodError, self).__init__(code, "Unauthorised method")


class InvalidMethodError(LigdicashError):
    """Classe d'erreur si la méthode HTTP est invalide."""

    def __init__(self, code: str):
        super(InvalidMethodError, self).__init__(code, "Invalid method")


class FeatureNotTestableError(LigdicashError):
    """Classe d'erreur si la fonctionnalité ne peut pas être utilisée sur la plateforme de test."""

    def __init__(self, feature_name: str):
        super(FeatureNotTestableError, self).__init__(
            "featurenottestable",
            f"{feature_name} feature can't be used on test platform",
        )
