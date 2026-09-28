# Day 79 - Translation Service

from googletrans import Translator

translator = Translator()

def translate_text(text, target_lang):
    """Translate text into the selected target language."""
    if not text or not text.strip():
        raise ValueError("Text cannot be empty.")

    if not target_lang:
        raise ValueError("Target language is required.")

    result = translator.translate(text.strip(), dest=target_lang)

    return {
        "translated_text": result.text,
        "source_language": result.src,
        "target_language": target_lang
    }
    
# Done