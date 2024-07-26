from typing import Dict, Literal
from .providers import HTTPProvider
from .responses import BaseResponse
from .decorators import is_not_testable


class Withdrawal:
    """
    Permet de créer une demande de retrait d'argent.

    Parameters
    ----------
    description : str, optional
        Description de la transaction, par défaut "".
    amount : float, optional
        Montant de la transaction, par défaut 100.
    customer : str, optional
        Identifiant du client effectuant la transaction, par défaut "".

    Attributes
    ----------
    amount : float
        Montant de la transaction.
    description : str
        Description de la transaction.
    customer : str
        Numéro du destinataire.
    provider : ligdicash.providers.HTTPProvider
        Client HTTP permettant de communiquer avec l'API de Ligdicash.
    """

    def __init__(self, description: str = "", amount: float = 100, customer: str = ""):
        """
        Initialise une instance de Withdrawal

        Parameters
        ----------
        description : str, optional
            Description de la transaction, par défaut "".
        amount : float, optional
            Montant de la transaction, par défaut 100.
        customer : str, optional
            Numéro du destinataire, par défaut "".
        """
        self.amount = amount
        self.description = description
        self.customer = customer
        self.provider = HTTPProvider()

    def send(
        self,
        type: Literal["client", "merchant"] = "client",
        to_wallet=False,
        callback_url: str = "",
        custom_data: Dict[str, any] = {},
    ) -> BaseResponse:
        """
        Envoie une demande de retrait d'argent.

        Parameters
        ----------
        type : Literal["client", "merchant"], optional
            Indique si le montant doit d'abord passer par le portefeuille Ligdicash du client.
        to_wallet : bool, optional
            Indique si le montant doit être transféré sur un portefeuille Ligdicash, par défaut False. Unique à type="client".
        callback_url : str, optional
            URL de rappel pour recevoir des notifications sur le statut de la transaction, par défaut "".
        custom_data : Dict[str, any], optional
            Données personnalisées à envoyer avec la demande de retrait, par défaut {}.

        Returns
        -------
        ligdicash.responses.BaseResponse
            Objet représentant la réponse de l'API de Ligdicash.

        Raises
        ------
        ligdicash.errors.FeatureNotTestableError
            Si la fonction est utilisée en mode "test".
        """
        command = {
            "amount": self.amount,
            "description": self.description,
            "customer": self.customer,
            "custom_data": custom_data,
            "callback_url": callback_url,
        }
        if type == "client":
            command["top_up_wallet"] = 1 if to_wallet else 0
        payload = {
            "commande": command
        }
        response = self.provider.post("withdrawal/create" if type == "client" else "straight/payout", payload, feature="client_payout" if type == "client" else "merchant_payout")
        response_data = BaseResponse.from_dict(response)
        return response_data
