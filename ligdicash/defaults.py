CONF_BASE_URL = {
    "test": "https://test.ligdicash.com/pay/v01/",
    "live": "https://app.ligdicash.com/pay/v01/",
}
""" Définition de l'url de test et de live """


def get_platform_url(name: str) -> str | None:
    """
    Retourne l'URL de base de la plateforme en fonction de son nom.

    Args
    ----
    name : str
        Le nom de la plateforme ("test" ou "live").

    Returns
    -------
    Union : [str, None]
        L'URL de base correspondante, ou None si le nom de la plateforme est invalide.

    Examples
    --------
    >>> get_platform_url("test")
    "https://test.ligdicash.com/pay/v01/"

    >>> get_platform_url("invalid")
    None
    """
    return CONF_BASE_URL.get(name, None)
