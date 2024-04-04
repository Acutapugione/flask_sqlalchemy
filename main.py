from routes import app


app.template_folder = "../my_inner_draw_system"
app.run(port=3000, debug=True)
