from TTS.utils.manage import ModelManager

def list_models():
    model_manager = ModelManager()
    models = model_manager.list_models()
    return models

if __name__ == "__main__":
    models = list_models()
    print("Available models:", models)
