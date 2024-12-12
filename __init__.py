from flask import Flask, render_template
from flask_graphql import GraphQLView
import graphene

# Definición del esquema GraphQL
class Query(graphene.ObjectType):
    hello = graphene.String(description="Retorna un mensaje de bienvenida")
    greet = graphene.String(name=graphene.String(default_value="mundo"), description="Saluda a un nombre dado")

    def resolve_hello(self, info):
        return "¡Hola desde GraphQL!"

    def resolve_greet(self, info, name):
        return f"¡Hola, {name}!"

schema = graphene.Schema(query=Query)

# Configuración de la aplicación Flask
def create_app():
    app = Flask(__name__)

    # Ruta para el explorador GraphiQL
    app.add_url_rule(
        "/graphql",
        view_func=GraphQLView.as_view(
            "graphql",
            schema=schema,
            graphiql=False  # Desactivamos el explorador integrado
        )
    )

    @app.route('/')
    def home():
        return render_template('index.html')

    return app
