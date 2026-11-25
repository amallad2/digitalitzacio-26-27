import gradio as gr
import ollama

def respondre_ollama(prompt):
    try:
        response = ollama.generate(
            model="llama3.2",
            prompt=prompt
        )
        return response['response']
    except Exception as e:
        return f"Error de connexió amb Ollama: {e}"

# Definim la interfície gràfica amb Gradio
demo = gr.Interface(
    fn=respondre_ollama,             # Funció de Python que s'executa
    inputs=gr.Textbox(lines=2, placeholder="Escriu la teva pregunta..."), # Camp d'entrada
    outputs="text",                  # On es mostra la resposta
    title="Asistent Ollama amb Gradio",
    description="Escriu una pregunta per enviar-la al teu model local d'Ollama."
)

# Inicia el servidor web local
if __name__ == "__main__":
    demo.launch()