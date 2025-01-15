from fastapi import HTTPException, APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import UploadFile, File
from fastapi.responses import JSONResponse
from PIL import Image
import numpy as np
import io

from ml.detect_number_ml import detect_number



# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Create the router instance
router = APIRouter(tags=["number_detector"])


                                    
@router.get("/display_number", response_class=HTMLResponse)
async def display_number(request: Request):
    return templates.TemplateResponse("display_number.html",
                                      {"request": request})


@router.post("/number_detection")
async def preprocess_image(file: UploadFile = File(...)):
    """
    Preprocess the uploaded image:
    - Resize to 28x28 pixels
    - Convert to grayscale
    - Flatten into a 1D array of type float32
    """
    try:
        # Load the uploaded image
        image_data = await file.read()
        image = Image.open(io.BytesIO(image_data))

        # Convert image to grayscale
        image = image.convert("L")

        # Resize to 28x28 pixels
        image = image.resize((28, 28))

        # Convert to NumPy array and normalize pixel values to [0, 1]
        image_array = np.asarray(image, dtype=np.float32) / 255.0
        print("****Shape*****", image_array.shape)
        # # Flatten the array to 1D
        flattened_array = image_array.flatten()

        # print("Array", flattened_array)
        print("****Shape*****", flattened_array.shape)
        print("Size", flattened_array.size)
     
        predicted_number = detect_number(flattened_array)
        print("predicted_number", {"result": str(predicted_number)})
        
       
        return JSONResponse(content={"result": str(predicted_number)}, status_code=200)
      
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing image: {str(e)}")


