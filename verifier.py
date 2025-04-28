import pyautogui as pag

while True:
    # Get the current mouse position
    x, y = pag.position()
    
    # Get the RGB value of the pixel at the current mouse position
    rgb = pag.screenshot().getpixel((x, y))
    
    # Print the current mouse position and RGB value
    print(f"Mouse position: ({x}, {y}), RGB: {rgb}")
    if pag.pixelMatchesColor(x, y, (251, 65, 73), tolerance=5):
        print("Pixel matches the target color!")
        print(pag.pixelMatchesColor(x, y, (251, 65, 73), tolerance=5))
    
    # Wait for a short period before checking again
    pag.sleep(0.5)