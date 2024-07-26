# Librairie Python LigdiCash

Ce projet est un SDK Python qui permet de manipuler l'API de LigdiCash.
Vous pourrez éffectuer des Payins, Payouts, des vérifications de transactions et des retraits.

Vous retrouverez la documentation de l'API de LigdiCash sur [https://developers.ligdicash.com/](https://developers.ligdicash.com/).

## Installation

```bash
pip install ligdicash
```

## Initialisation

L'initialisation de la librairie LigdiCash nécessite une clé API et un jeton d'authentification.
Vous pouvez obtenir ces informations en créant un projet API sur la plateforme LigdiCash.

```python
import ligdicash

ligdicash.api_key = "RE6J...4I4O"
ligdicash.auth_token = "eyJ0eXAiOiJ...Zm5kNp6BJuAY"
ligdicash.platform = "live"
```

## Payin

Le Payin est une transaction qui permet à un client de payer pour un produit ou un service.
Il existe deux types de Payin : avec rédirection et sans rédirection.

### Remplir la facture

```python
// Décrire la facture et le client
invoice = ligdicash.Invoice(
    currency="xof",
    description="Facture pour l'achat de vêtements sur MaSuperBoutique.com",
    customer_firstname="Cheik",
    customer_lastname="Cissé",
    customer_email="cheikcisse@gmail.com",
    store_name="MaSuperBoutique",
    store_website_url="masuperboutique.com",
)

# Ajouter des éléments(produit, service, etc) à la facture
invoice.add_item(
    name="Premier produit",
    description="__description_du_produit__",
    quantity=3,
    unit_price=3500,
)

invoice.add_item(
    name="Deuxieme produit",
    description="__description_du_produit__",
    quantity=1,
    unit_price=5000,
)

invoice.add_item(
    name="TVA",
    description="__description_du_produit__",
    quantity=1,
    unit_price=1000,
)
```

### Payin avec rédirection

Le Payin avec rédirection permet de rediriger le client vers une page de paiement sécurisée, conçue par LigdiCash.

```python
response = invoice.pay_with_redirection(
    return_url="https://masuperboutique.com/success",
    callback_url="https://masuperboutique.com/cancel",
    callback_url="https://backend.masuperboutique.com/callback",
    custom_data={
        "order_id": "ORD-1234567890",
        "customer_id": "CUST-1234567890",
    },
) 

payment_url = response.response_text;
redirect_user(payment_url);
```

### Payin sans rédirection

Le Payin sans rédirection permet de payer directement sur la page de la boutique, sans être redirigé vers une page de paiement.

```python
response = invoice.pay_without_redirection(
    otp="XXXXXX,
    customer="226XXXXXXXX", # Numéro utilisé précédé du préfix du pays
    callback_url="https://backend.masuperboutique.com/callback",
    custom_data={
        "product_id": "PR025632545",
    },
)

const token = response.token;
check_payment_status(token);
```

## Payout

Le Payout est une transaction qui permet à un marchand de rembourser un client ou de lui envoyer de l'argent.

```python
invoice = ligdicash.Withdrawal(
    amount=100,
    description="Remboursement de la commande ORD-123456",
    customer="226XXXXXXXX"
)
response = invoice.send(
    type="client",
    to_wallet=True, #true si l'argent doit rester dans le wallet du client, false si l'argent doit être envoyé sur son compte mobile money
    callback_url="https://backend.masuperboutique.com/callback-payout",
)

token = response.token;
check_payment_status(token);
```

## Vérification de transaction

La vérification de transaction permet de vérifier l'état d'une transaction.
Vous devez toujours vérifier l'état d'une transaction avant de livrer un produit ou de valider une commande.

Pour obtenir une transaction, vous devez fournir le token de la transaction.

```python
transaction_token = "eyJ0eXAiOiJ...pZCI6IjY"
transaction = ligdicash.get_transaction(transaction_token, "client_payout") # "payin" ou "client_payout" ou "merchant_payout"
status = transaction.status;
if status === "completed":
    // La transaction a été effectuée avec succès
elif status === "pending":
    // La transaction est en cours de traitement
else:
    // La transaction a échouée
```