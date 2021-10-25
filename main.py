from website import create_app

app = create_app()
app.app_context().push()

if __name__ == "__main__":
    # add_plants() # was use for seeding the database
    app.run(debug=True)
