import json
import logging
import azure.functions as func

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Create the Function App using v2 model
app = func.FunctionApp()


# route parameter is changed: api/{functionname} to api/message
@app.function_name(name="HttpTrigger-api")
@app.route(route="message", auth_level=func.AuthLevel.ANONYMOUS)
def get_basic(req: func.HttpRequest) -> str:
    logger.info("AZ-FUNC API message.")

    # return "Hello, from the stocks API!"
    return json.dumps({"text": "Ciao, from the stocks API!"})