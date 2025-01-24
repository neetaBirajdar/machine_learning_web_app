from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from PIL import Image
import numpy as np
import io
import base64
from ml.detect_number_ml import detect_number

router = APIRouter()

class ImageData(BaseModel):
    image: str  # Base64-encoded image data

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")

@router.get("/draw_number", response_class=HTMLResponse)
async def draw_number(request: Request):
    return templates.TemplateResponse("draw_number.html",
                                      {"request": request})


@router.post("/drawn_number_detection")
async def drawn_number_detection(data: ImageData):
    """
    Preprocess the base64-encoded image:
    - Decode the base64 image
    - Resize to 28x28 pixels
    - Convert to grayscale
    - Flatten into a 1D array of type float32
    """
    try:
        # Decode the base64 image
        image_data = data.image.split(",")[1]  # Remove "data:image/png;base64,"
        decoded_image = base64.b64decode(image_data)
        image = Image.open(io.BytesIO(decoded_image))

        # Convert image to grayscale
        image = image.convert("L")

        # Resize to 28x28 pixels
        image = image.resize((28, 28))

        # Convert to NumPy array and normalize pixel values to [0, 1]
        image_array = np.asarray(image, dtype=np.float32) / 255.0
        print("Image shape:", image_array.shape)

        # Flatten the array to 1D
        flattened_array = image_array.flatten()

        # Predict the number using the model
        predicted_number = detect_number(flattened_array)
        print("Predicted number:", predicted_number)

        return JSONResponse(content={"result": str(predicted_number)}, status_code=200)

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing image: {str(e)}")
