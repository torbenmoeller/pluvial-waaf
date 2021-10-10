"""
You can deploy this code by running this command:
gcloud functions deploy waaf --runtime python39 --trigger-http --allow-unauthenticated --entry-point gcp_entry_point
"""
from flask import Flask, Request

# This serves static content
app = Flask(__name__, static_folder='static', static_url_path='/')


@app.route('/api')
def api():
    # Backend code can be written normally
    return "Hello from the api!"


def gcp_entry_point(request: Request):
    """
    This method is only used as the entrypoint for Google Cloud Functions
    The code comes from this Stackoverflow question:
    https://stackoverflow.com/questions/53488766/using-flask-routing-in-gcp-function
    The answer was provides by Martin: https://stackoverflow.com/users/4443309/martin
    """
    with app.request_context(request.environ):
        try:
            rv = app.preprocess_request()
            if rv is None:
                rv = app.dispatch_request()
        except Exception as e:
            rv = app.handle_user_exception(e)
        response = app.make_response(rv)
        return app.process_response(response)


if __name__ == '__main__':
    app.run()
