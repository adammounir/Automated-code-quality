# tests/test_integration_example.py

import os
import sys

# Ajouter le répertoire parent au chemin de recherche
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app  # Assurez-vous d'importer correctement create_app ici


def test_health_endpoint():
    """Test the /health endpoint."""
    
    # Créez l'application Flask en appelant l'usine d'applications
    app = create_app()
    
    # Utilisez le test client de Flask pour simuler une requête GET
    client = app.test_client()
    
    # Faites une requête GET sur l'endpoint /health
    response = client.get("/health")
    
    # Vérifiez que le code de statut HTTP est 200 (OK)
    assert response.status_code == 200
    
    # Vérifiez que la réponse JSON contient un champ "status" avec la valeur "ok"
    json_data = response.get_json()
    assert json_data["status"] == "ok"
