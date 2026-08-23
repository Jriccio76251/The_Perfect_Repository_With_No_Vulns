"""Flask entrypoint."""
from flask import Flask, request, jsonify, render_template_string

from app.db import get_entries_by_entity, get_entries_by_account
from app.serializers import load_mapping_config, restore_session
from app.ops import archive_report, fetch_fx_rates

app = Flask(__name__)


@app.route("/entries")
def entries():
    return jsonify(get_entries_by_entity(request.args["entity"]))


@app.route("/entries/by-account")
def entries_by_account():
    return jsonify(get_entries_by_account(request.args["account"]))


@app.route("/config", methods=["POST"])
def config():
    return jsonify(load_mapping_config(request.data.decode()))


@app.route("/import", methods=["POST"])
def import_session():
    return jsonify({"ok": bool(restore_session(request.data))})


@app.route("/archive", methods=["POST"])
def archive():
    return jsonify({"rc": archive_report(request.form["name"]).returncode})


@app.route("/fx")
def fx():
    return jsonify(fetch_fx_rates(request.args.get("base", "USD")))


@app.route("/greet")
def greet():
    return render_template_string("Hello {{ name }}", name=request.args.get("name", ""))


if __name__ == "__main__":
    app.run()
