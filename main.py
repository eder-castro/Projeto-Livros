from google.cloud import vision

def detect_text(path, api_key):
    """Detects text in the image file using an API key."""
    client = vision.ImageAnnotatorClient() # Remove credentials=None para usar o cabeçalho da API Key

    with open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image, request_kwargs={'headers': {'X-Goog-Api-Key': api_key}})
    texts = response.text_annotations
    print('Texts:')
    for text in texts:
        print(f'"{text.description}"')
        vertices = (['({},{})\n'.format(v.x, v.y) for v in text.bounding_poly.vertices])
        print('bounds: {}'.format(''.join(vertices)))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

if __name__ == '__main__':
    image_path = 'caminho/para/sua/imagem.jpg'
    your_api_key =   # Substitua pela sua chave real
    detect_text(image_path, your_api_key)