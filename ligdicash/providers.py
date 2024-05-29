import json
import requests
import ligdicash
from .defaults import get_platform_url
from .wiki import get_wiki_error
from typing import Literal
import re


class HTTPProvider:
    """
    Une classe pour fournir une interface pour les requêtes HTTP à une API.

    Attributes
    ----------
    api_key : str
        La clé API pour l'authentification.
    auth_token : str
        Le jeton d'authentification pour l'API.
    base_url : str
        L'URL de base de l'API.
    session : requests.Session
        La session utilisée pour envoyer des requêtes HTTP.

    """

    def __init__(
        self, api_key: str = None, auth_token: str = None, base_url: str = None
    ):
        """
        Initialise une instance de HTTPProvider

        Parameters
        ----------
        api_key : str
            La clé API pour l'authentification.
        auth_token str
            Le jeton d'authentification pour l'API.
        base_url : str
            L'URL de base de l'API.
        """
        self.api_key = api_key or ligdicash.api_key
        self.auth_token = auth_token or ligdicash.auth_token
        self.base_url = base_url
        if not self.base_url:
            self.base_url = get_platform_url(ligdicash.platform)
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Apikey": self.api_key,
                "Authorization": f"Bearer {self.auth_token}",
                "Accept": "application/json",
                "Content-Type": "application/json",
            }
        )

    def build_url(self, url: str):
        """
        Construit l'URL complète à partir de l'URL de base et de l'URL relative.

        Parameters
        ----------
        url : str
            L'URL relative.

        Returns
        -------
        str
            L'URL complète construite.
        """
        return self.base_url + url

    def get_data_or_raise_error(
        self, response: requests.Response, feature: Literal["payin", "client_payout", "merchant_payout", "status"]
    ) -> dict:
        """
        Récupère les données de réponse JSON si la réponse HTTP est OK. Sinon, lève une exception.

        Parameters
        ----------
        response : requests.Response
            La réponse HTTP à traiter.
        feature : Literal["payin", "client_payout", "merchant_payout", "status"]
            La fonctionnalité appelée.

        Returns
        -------
        dict
            Les données de réponse JSON.

        Raises
        ------
        ligdicash.errors.WikiError
            Si la réponse n'est pas OK, lève une exception personnalisée en fonction de l'erreur renvoyée.
        """
        if not response.ok:
            response.raise_for_status()
        else:
            response_data = response.json()
            res_code = response_data["response_code"]
            res_text = response_data["response_text"]
            if res_code == "00":
                return response_data
            else:
                error_code = re.search(r"\d{2,3}[a-z]?", res_text, re.IGNORECASE)
                if error_code:
                    error_code = error_code.group()
                error = get_wiki_error(wiki_name=feature, error_code=error_code)
                raise error(error_code)

    def post(
        self, url: str, payload: dict, feature: Literal["payin", "client_payout", "merchant_payout", "status"]
    ) -> dict:
        """
        Envoie une requête POST à l'API et récupère les données de la réponse.

        Parameters
        ----------
        url : str
            L'URL à laquelle envoyer la requête.
        payload : dict
            Le corps de la requête HTTP.
        feature : Literal["payin", "client_payout", "merchant_payout", "status"]
            La fonctionnalité utilisée.

        Return
        ------
        dict
            Les données de réponse de la requête HTTP.

        Raises
        ------
        HTTPError or ligdicash.errors.WikiError
            Si la réponse n'est pas OK.
        """
        response = self.session.post(self.build_url(url), data=json.dumps(payload))
        response_data = self.get_data_or_raise_error(response, feature)
        return response_data

    def get(self, url: str, feature: Literal["payin", "client_payout", "merchant_payout", "status"]) -> dict:
        """
        Envoie une requête GET à l'API et récupère les données de la réponse.

        Parameters
        ----------
        url : str
            L'URL à laquelle envoyer la requête.
        feature : Literal["payin", "client_payout", "merchant_payout", "status"]
            La fonctionnalité utilisée.

        Return
        ------
        dict
            Les données de réponse de la requête HTTP.

        Raises
        ------
        HTTPError or ligdicash.errors.WikiError
            Si la réponse n'est pas OK.
        """
        response = self.session.get(self.build_url(url))
        response_data = self.get_data_or_raise_error(response, feature)
        return response_data
