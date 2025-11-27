from flask import Flask, jsonify
from .db import get_product_by_id
from .cache import get_cached_product, set_cached_product

def create_app():
    app = Flask(__name__)

    @app.route("/health")
    def health():
        return jsonify({"status": "ok"})

    @app.route("/products/<int:product_id>")
    def get_product(product_id: int):
        # 1. Try cache
        cached = get_cached_product(product_id)
        if cached:
            response = jsonify({"source": "cache", "product": cached})
            response.headers["X-Cache"] = "HIT"
            return response, 200

        # 2. Fallback to DB
        product = get_product_by_id(product_id)
        if not product:
            return jsonify({"error": "Product not found"}), 404

        # 3. Store in cache
        set_cached_product(product_id, product)

        response = jsonify({"source": "database", "product": product})
        response.headers["X-Cache"] = "MISS"
        return response, 200

    return app

if __name__ == "__main__":
    # for local dev
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
