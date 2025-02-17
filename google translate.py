import asyncio
from googletrans import Translator

# Function to translate text to English (asynchronous)
async def translate_to_english(text):
    try:
        # Initialize the Translator
        translator = Translator()

        # Perform the translation to English (target language is 'en')
        translation = await translator.translate(text, dest='en')

        # Return the translated text
        return translation.text

    except Exception as e:
        print(f"Translation error: {e}")
        return None

# Main program
if __name__ == "__main__":
    # Get user input
    text_to_translate = input("Enter the text to translate to English: ")

    # Run the asynchronous function and get the result
    translated_text = asyncio.run(translate_to_english(text_to_translate))

    if translated_text:
        print("Translated text:", translated_text)
    else:
        print("Failed to translate the text.")
