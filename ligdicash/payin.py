from typing import Dict, List

from .decorators import is_not_testable
from .providers import HTTPProvider
from .responses import BaseResponse


class InvoiceItem:
    """
    Représente un article dans une facture.

    Attributes
    ----------
    name : str
        Le nom de l'article.
    description : str
        La description de l'article.
    _quantity : int
        La quantité de l'article.
    _unit_price : float
        Le prix unitaire de l'article.
    total_price : float
        Le prix total de l'article.
    """

    def __init__(self, name: str, description: str, quantity: int, unit_price: float):
        """
        Initialise une instance de InvoiceItem.

        Parameters:
        -----------
        name : str
            Le nom de l'article.
        description : str
            La description de l'article.
        quantity : int
            La quantité de l'article.
        unit_price : float
            Le prix unitaire de l'article.
        """
        self.name = name
        self.description = description
        self._quantity = quantity
        self._unit_price = unit_price
        self.total_price = unit_price * quantity

    @property
    def quantity(self) -> int:
        """
        Retourne la quantité de l'article.

        Return:
        -------
        int:
            Quantité de l'article
        """
        return self._quantity

    @property
    def unit_price(self) -> int:
        """
        Retourne le prix unitaire de l'article.

        Return:
        -------
        int:
            Prix unitaire de l'article
        """
        return self._unit_price

    @quantity.setter
    def quantity(self, new_quantity: int) -> int:
        """
        Définit la quantité de l'article.

        Parameters:
        -----------
        new_quantity : int
            La nouvelle quantité de l'article.
        """
        self._quantity = new_quantity
        self.total_price = self._unit_price * new_quantity

    @unit_price.setter
    def unit_price(self, new_unit_price: float) -> int:
        """
        Définit le prix unitaire de l'article.

        Parameters:
        -----------
        new_unit_price : float
            Le nouveau prix unitaire de l'article.
        """
        self._unit_price = new_unit_price
        self.total_price = new_unit_price * self._quantity

    def to_dict(self) -> Dict[str, str | int]:
        """
        Retourne une représentation dictionnaire de l'article.

        Return:
        -------
        dict:
            Dictionnaire réprésentant l'article.
        """
        return {
            "name": self.name,
            "description": self.description,
            "quantity": self._quantity,
            "unit_price": self._unit_price,
            "total_price": self.total_price,
        }


class Invoice:
    """
    Une classe qui représente une facture

    Attributes
    ----------
    items : List[InvoiceItem]
        Liste des items associés à la facture.
    currency : str
        La devise utilisée pour la facture.
    description : str
        Description de la facture.
    customer_firstname : str
        Prénom du client.
    customer_lastname : str
        Nom de famille du client.
    customer_email : str
        Adresse e-mail du client.
    store_name : str
        Nom du magasin.
    store_website_url : str
        URL du site web du magasin.
    external_id : str
        ID externe de la facture.
    otp : str
        Code otp du paiement.
    provider : ligdicash.providers.HTTPProvider
        Le client HTTP.
    total_amount : float
        Le montant total de la facture.
    """

    def __init__(
        self,
        currency: str = "xof",
        description: str = "",
        customer_firstname: str = "",
        customer_lastname: str = "",
        customer_email: str = "",
        store_name: str = "",
        store_website_url: str = "",
    ):
        """
        Initialise une instance de Invoice.

        Parameters
        ----------
        currency : str, optional
            La devise utilisée pour la facture (par défaut "xof").
        description : str, optional
            La description de la facture (par défaut "").
        customer_firstname : str, optional
            Le prénom du client (par défaut "").
        customer_lastname : str, optional
            Le nom du client (par défaut "").
        customer_email : str, optional
            L'adresse email du client (par défaut "").
        store_name : str, optional
            Le nom de la boutique (par défaut "").
        store_website_url : str, optional
            L'URL du site web de la boutique (par défaut "").
        """
        self.items: List[InvoiceItem] = []
        self.currency = currency
        self.description = description
        self.customer_firstname = customer_firstname
        self.customer_lastname = customer_lastname
        self.customer_email = customer_email
        self.store_name = store_name
        self.store_website_url = store_website_url
        self.external_id = ""
        self.otp = ""

        self.provider = HTTPProvider()

    def to_dict(self, customer: str = "") -> Dict[str, any]:
        """
        Convertit l'objet Invoice en un dictionnaire.

        Parameters
        ----------
        customer : str, facultatif
            Le numéro à utiliser pour la transaction. Par défaut, "".

        Returns
        -------
        Dict[str, any]
            Un dictionnaire représentant l'objet Invoice.
        """
        items = [item.to_dict() for item in self.items]
        return {
            "items": items,
            "total_amount": self.total_amount,
            "devise": self.currency,
            "description": self.description,
            "customer": customer,
            "customer_firstname": self.customer_firstname,
            "customer_lastname": self.customer_lastname,
            "customer_email": self.customer_email,
            "external_id": self.external_id,
            "otp": self.otp,
        }

    def set_items_total(self):
        """
        Met à jour le montant total de la facture en fonction des articles présents.
        """
        self.total_amount = sum(item.total_price for item in self.items)

    def add_item(self, name: str, description: str, quantity: int, unit_price: float):
        """
        Ajoute un article à la facture.

        Parameters
        ----------
        name : str
            Le nom de l'article.
        description : str
            La description de l'article.
        quantity : int
            La quantité de l'article.
        unit_price : float
            Le prix unitaire de l'article.
        """
        new_item = InvoiceItem(name, description, quantity, unit_price)
        self.items.append(new_item)
        self.set_items_total()

    def pay_with_redirection(
        self,
        cancel_url: str = "",
        return_url: str = "",
        callback_url: str = "",
        custom_data: Dict[str, any] = {},
    ) -> BaseResponse:
        """
        Génère un lien de paiement.

        Parameters:
        -----------
        cancel_url : str, optional
            L'URL de redirection en cas d'annulation du paiement.
            Default est une chaîne vide.
        return_url : str, optional
            L'URL de redirection en cas de succès du paiement.
            Default est une chaîne vide.
        callback_url : str, optional
            L'URL de callback.
            Default est une chaîne vide.
        custom_data : dict[str, any], optional
            Données personnalisées à inclure dans la requête de paiement.
            Default est un dictionnaire vide.

        Returns:
        --------
        ligdicash.responses.BaseResponse
            Une réponse contenant les informations de la transaction.
        """
        payload = {
            "commande": {
                "invoice": self.to_dict(),
                "store": {
                    "name": self.store_name,
                    "website_url": self.store_website_url,
                },
                "actions": {
                    "cancel_url": cancel_url,
                    "return_url": return_url,
                    "callback_url": callback_url,
                },
                "custom_data": custom_data,
            }
        }
        response = self.provider.post(
            "redirect/checkout-invoice/create", payload, feature="payin"
        )
        response_data = BaseResponse.from_dict(response)
        return response_data

    def pay_without_redirection(
        self,
        otp: str = "",
        customer: str = "",
        callback_url: str = "",
        custom_data: Dict[str, any] = {},
    ) -> BaseResponse:
        """
        Effectue un paiement sans redirection.

        Parameters:
        -----------
        otp : str, optional
            Le code à usage unique (OTP) fourni par le client pour confirmer le paiement.
            Default est une chaîne vide.
        customer : str, optional
            Identifiant unique du client effectuant le paiement.
            Default est une chaîne vide.
        callback_url : str, optional
            L'URL de rappel appelée par le fournisseur de paiement pour confirmer la transaction.
            Default est une chaîne vide.
        custom_data : dict[str, any], optional
            Données personnalisées à inclure dans la requête de paiement.
            Default est un dictionnaire vide.

        Returns:
        --------
        ligdicash.responses.BaseResponse or None
            Si un OTP valide est fourni, une réponse contenant les informations de la transaction est renvoyée.
            Sinon, la méthode ne retourne rien.
        """
        self.otp = otp
        payload = {
            "commande": {
                "invoice": self.to_dict(customer),
                "store": {
                    "name": self.store_name,
                    "website_url": self.store_website_url,
                },
                "actions": {
                    "callback_url": callback_url,
                },
                "custom_data": custom_data,
            }
        }
        response = self.provider.post(
            "straight/checkout-invoice/create", payload, feature="payin"
        )
        response_data = BaseResponse.from_dict(response)
        return response_data
