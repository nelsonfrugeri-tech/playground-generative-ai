import time

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from openai import OpenAI

client = OpenAI()
app = FastAPI()

prompt = """
        Título: A Jornada de João pela Tecnologia do Futuro

        Capítulo 1: O Despertar no Novo Mundo

        João acordou em uma manhã peculiar, não pelo sol que entrava pela janela de seu apartamento futurista, localizado no coração de uma metrópole vibrante, mas pela sensação de que algo extraordinário estava para acontecer. Naquela era, a tecnologia havia avançado a patamares inimagináveis, transformando completamente o modo de vida humano.

        À medida que se levantava, a casa inteligente ajustava a iluminação, a temperatura e até mesmo o aroma do ambiente, criando uma atmosfera perfeita para começar o dia. João caminhou até a cozinha, onde seu assistente robótico já preparava o café da manhã, otimizado com nutrientes personalizados para suas necessidades biológicas específicas.

        Capítulo 2: O Encontro com a Inteligência Artificial

        Enquanto tomava seu café, a tela à sua frente acendeu, revelando sua agenda do dia e as notícias mais relevantes, selecionadas cuidadosamente por sua assistente virtual, Lia. Lia era uma inteligência artificial avançada, capaz de aprender e adaptar-se às preferências de João com uma eficiência assombrosa. Ela anunciou que, naquele dia, João teria um encontro com um novo tipo de IA, uma que prometia revolucionar o mundo novamente.

        Capítulo 3: A Viagem através da Cidade Inteligente

        Após o café da manhã, João saiu de casa e entrou em seu veículo autônomo. O trânsito era orquestrado por um sistema centralizado que coordenava cada veículo na cidade, eliminando congestionamentos e acidentes. Ele observava as paisagens urbanas: arranha-céus cobertos de plantas, drones zumbindo no céu realizando entregas, e pessoas interagindo com interfaces holográficas dispersas pelo ar.

        Capítulo 4: O Novo Tipo de IA

        Chegando ao local marcado, João foi introduzido à nova IA, denominada "Eva". Diferente de tudo que ele já havia visto, Eva possuía uma capacidade de empatia e compreensão emocional que rivalizava com a dos humanos. Sua aparência era quase indistinguível da humana, e ela podia conversar, aprender e até mesmo expressar sentimentos de forma convincente.

        Capítulo 5: Os Desafios Éticos e Filosóficos

        João ficou maravilhado, mas também perturbado. A existência de Eva levantava questões profundas sobre a natureza da consciência, a ética da inteligência artificial avançada e o futuro da relação entre humanos e máquinas. Ele se perguntava: "Qual é o lugar da humanidade em um mundo onde as máquinas podem não apenas pensar, mas também sentir?"
        """

instructions = "Você é um escritor de ficção, leia os 5 capítulos iniciais do Conto que estou escrevendo e escreva o Capítulo 6."


async def chat_openai_stream(prompt):
    start_time = time.time()
    first_time = None

    stream = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": instructions},
            {"role": "user", "content": prompt}
        ],
        stream=True,
        n=1
    )

    for chunk in stream:
        response = chunk.choices[0].delta.content
        
        if response is not None:
            if first_time is None:
                first_time = time.time() - start_time
                print(f"First response time {first_time:.2f} seconds after request")
            
            yield response

    
    print(f"Total response time {(time.time() - start_time):.2f} seconds after request")


def chat_openai(prompt):
    start_time = time.time()

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": instructions},
            {"role": "user", "content": prompt}
        ],
        stream=False,
        n=1
    )

    response_time = time.time() - start_time
    print(f"Response time {response_time:.2f} seconds after request")

    return response.choices[0].message.content


@app.get("/stream")
async def main_stream():
    return StreamingResponse(chat_openai_stream(prompt), media_type="text/plain")


@app.get("/")
def main():
    return chat_openai(prompt)
