from flask import Flask, request

firstName = request.form.get("first_name")
lastName = request.form.get("last_name")
email = request.form.get("email")
password = request.form.get("password")