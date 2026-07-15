from flask_restx import Resource, Namespace
from .models import Account


api = Namespace(
    "accounts",
    description="Account operations"
)


@api.route("")
class AccountList(Resource):

    def get(self):
        """
        List all accounts
        """
        return [
            account.to_dict()
            for account in Account.accounts
        ]

    def post(self):
        """
        Create an account
        """
        data = api.payload

        account = Account(
            data["name"],
            data["email"]
        )

        Account.accounts.append(account)

        return account.to_dict(), 201


@api.route("/<int:id>")
class AccountResource(Resource):

    def get(self, id):
        """
        Read an account
        """
        for account in Account.accounts:
            if account.id == id:
                return account.to_dict()

        return {"message": "Account not found"}, 404

    def put(self, id):
        """
        Update an account
        """
        data = api.payload

        for account in Account.accounts:
            if account.id == id:
                account.name = data["name"]
                account.email = data["email"]

                return account.to_dict()

        return {"message": "Account not found"}, 404

    def delete(self, id):
        """
        Delete an account
        """
        for account in Account.accounts:
            if account.id == id:
                Account.accounts.remove(account)
                return {"message": "Account deleted"}

        return {"message": "Account not found"}, 404
