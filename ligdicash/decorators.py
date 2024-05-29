from typing import Callable


def is_not_testable(func: Callable) -> Callable:
    """
    Décorateur qui lève une exception FeatureNotTestableError si la plateforme est en mode test.

    Args
    ----
    func : Callable
        Fonction à décorer.

    Returns
    -------
    Callable
        Fonction décorée.

    Raises
    ------
    ligdicash.errors.FeatureNotTestableError
        Si la plateforme est en mode test.
    """

    def inner(*args, **kwargs):
        from . import platform, FeatureNotTestableError

        if platform == "test":
            raise FeatureNotTestableError("Payin-without-redirection")
        return func(*args, **kwargs)

    return inner
