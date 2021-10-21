from website import create_app, add_plants

app = create_app()
app.app_context().push()

if __name__ == "__main__":
    add_plants()
    app.run(debug=True)
