from typing import Dict, Any, Optional


class BaseResponse:
    """
    Cette classe définit un objet BaseResponse qui représente une réponse de base de l'API.

    Attributes
    ----------
    response_code : str
        Code de réponse de la requête, "00" ou "01".
    token : str
        Token de la requête.
    response_text : str
        Texte de réponse de la requête.
    description : str
        Description de la réponse.
    wiki : list[str]
        Liste des liens wiki liés à la réponse.
    custom_data : Dict[str, Any], optional
        Données personnalisées de la réponse, par défaut {}.
    customdata : Dict[str, Any], optional
        Autre version de custom_data, par défaut {}.
    """

    def __init__(
        self,
        response_code: str,
        token: str,
        response_text: str,
        description: str,
        wiki: list[str],
        customdata: Dict[str, Any] = {},
        custom_data: Dict[str, Any] = {},
        *args,
        **kwargs
    ):
        """
        Initialise une instance de BaseResponse avec les données fournies.

        Parameters
        ----------
        response_code : str
            Code de réponse de la requête, "00" ou "01".
        token : str
            Token de la requête.
        response_text : str
            Texte de réponse de la requête.
        description : str
            Description de la réponse.
        wiki : list[str]
            Dictionnaire d'erreur ou Lien menant vers le dictionnaire d'erreur.
        custom_data : Dict[str, Any], optional
            Données personnalisées de la réponse, par défaut {}.
        customdata : Dict[str, Any], optional
            Autre version de custom_data, par défaut {}.
        """
        self.response_code = response_code
        self.token = token
        self.response_text = response_text
        self.description = description
        self.custom_data = custom_data or customdata
        self.wiki = wiki

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "BaseResponse":
        """
        Crée une instance de BaseResponse à partir d'un dictionnaire de données.

        Parameters
        ----------
        data : Dict[str, Any]
            Le dictionnaire de données pour créer l'instance.

        Returns
        -------
        ligdicash.responses.BaseResponse
            Une instance de ligdicash.responses.BaseResponse avec les données fournies.
        """
        return cls(**data)


class StatusResponse(BaseResponse):
    """
    Classe représentant une réponse de statut pour une transaction.
    Hérite de la classe ligdicash.responses.BaseResponse

    Attributes
    ----------
    response_code : str
        Code de réponse de la demande de paiement, "00" ou "01".
    token : str
        token de la transaction.
    response_text : str
        Texte de réponse de la transaction.
    description : str
        Description de la demande de paiement.
    custom_data : dict[str, any], optionnel
        Données associées à la transaction.
    wiki : list[str]
        Dictionnaire d'erreur ou Lien menant vers le dictionnaire d'erreur.
    montant : str
        Montant de la transaction.
    amount : str
        Montant de la transaction.
    status : str
        Statut de la transaction.
    operator_id : str
        ID de l'opérateur de la transaction.
    operator_name : str
        Nom de l'opérateur de la transaction.
    external_id : str
        ID externe de la transaction.
    customer : str
        Numéro utilisé pour la transaction.
    """

    def __init__(
        self,
        response_code: str,
        token: str,
        response_text: str,
        description: str,
        custom_data: Dict[str, Any],
        wiki: list[str],
        amount: int,
        montant: int,
        status: str,
        operator_id: str,
        operator_name: str,
        external_id: str,
        transaction_id: str,
        date: Optional[str] = None,
        customer: Optional[str] = None,
        request_id: Optional[str] = None,
    ):
        """
        Initialise une instance de StatusResponse

        Parameters
        ----------
        response_code : str
            Code de réponse de la demande de paiement, "00" ou "01".
        token : str
            token de la transaction.
        response_text : str
            Texte de réponse de la transaction.
        description : str
            Description de la demande de paiement.
        custom_data : dict[str, any], optionnel
            Données associées à la transaction.
        wiki : list[str]
            Dictionnaire d'erreur ou Lien menant vers le dictionnaire d'erreur.
        montant : str
            Montant de la transaction.
        status : str
            Statut de la transaction.
        operator_id : str
            ID de l'opérateur de la transaction.
        operator_name : str
            Nom de l'opérateur de la transaction.
        external_id : str
            ID externe de la transaction.
        customer : str
            Numéro utilisé pour la transaction.
        """
        super().__init__(
            response_code, token, response_text, description, custom_data, wiki
        )
        self.montant = montant
        self.amount = amount
        self.status = status
        self.operator_id = operator_id
        self.operator_name = operator_name
        self.external_id = external_id
        self.request_id = request_id
        self.transaction_id = transaction_id
        self.customer = customer
        self.date = date

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "StatusResponse":
        """
        Construit une instance de la classe StatusResponse à partir d'un dictionnaire.

        Parameters
        ----------
        data : dict[str, any]
            Dictionnaire contenant les données pour construire l'instance.

        Returns
        -------
        ligdicash.responses.StatusResponse
            L'instance construite à partir des données.

        """
        return cls(**data)
