from restapi import app
import os
import secrets
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    Response,
    session,
)
from restapi.resources import get_bucket, get_buckets_list


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        bucket = request.form["bucket"]
        session["bucket"] = bucket
        return redirect(url_for("files"))
    else:
        buckets = get_buckets_list()
        return render_template("index.html", buckets=buckets)


@app.route("/files", methods=["GET"])
def files():
    my_bucket = get_bucket()
    summaries = my_bucket.objects.all()

    return render_template("files.html", my_bucket=my_bucket, files=summaries)


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    user = request.form["user"]
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(file.filename)
    file.filename = f"{user}.{random_hex}{f_ext}"

    my_bucket = get_bucket()
    my_bucket.Object(file.filename).put(Body=file)

    flash("File uploaded successfully")
    return redirect(url_for("files"))


@app.route("/delete", methods=["POST"])
def delete():
    key = request.form["key"]

    my_bucket = get_bucket()
    my_bucket.Object(key).delete()

    flash("File deleted successfully")
    return redirect(url_for("files"))


@app.route("/download", methods=["POST"])
def download():
    key = request.form["key"]

    my_bucket = get_bucket()
    file_obj = my_bucket.Object(key).get()

    return Response(
        file_obj["Body"].read(),
        mimetype="text/plain",
        headers={"Content-Disposition": "attachment;filename={}".format(key)},
    )


@app.route("/storage", methods=["GET", "POST"])
def storage():
    if request.method == "POST":
        user = request.form["username"]
        my_bucket = get_bucket()
        all_files = my_bucket.objects.filter(Prefix=user)
        return render_template("storage.html", my_bucket=my_bucket, files=all_files)
    else:
        return render_template("storage.html")
