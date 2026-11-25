import ollama

def preguntar_a_ollama(prompt: str, model: str = "llama3.2"):
    try:
        # Envia la petició a la instància local d'Ollama
        response = ollama.generate(
            model=model,
            prompt=prompt
        )
        # Retorna el text generat
        return response['response']
    except Exception as e:
        return f"Error en connectar amb Ollama: {e}"

def preguntar_amb_stream(prompt: str, model: str = "llama3.2"):
    try:
        # S'activa el paràmetre stream=True
        stream = ollama.generate(
            model=model,
            prompt=prompt,
            stream=True
        )
        
        print("Resposta d'Ollama: ", end="", flush=True)
        for chunk in stream:
            # Imprimeix cada fragment directament a la consola sense salt de línia
            print(chunk['response'], end="", flush=True)
        print() # Salt de línia final
        
    except Exception as e:
        print(f"\nError de connexió: {e}")

if __name__ == "__main__":
    #pregunta = "Explica breument què és una API REST."
    #print(f"Pregunta: {pregunta}\n")
    

    pregunta = "Dona'm 3 idees per a un esmorzar saludable."
    preguntar_amb_stream(pregunta)
