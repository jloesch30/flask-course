from myapp import create_app

# initialize app, blueprints and DB
app = create_app()

if __name__ == '__main__':
    # app config and run
    app.run(host='127.0.0.1', port=8080, debug=True)
    # fc indicates what db we will be accessing
    app.config['MONGODB_SETTINGS'] = {'db':'fc', 'alias':'default'}