from openai import OpenAI

client = OpenAI(
    api_key="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"
)

#arreglo para mensajes
messages = [
    {"role": "system", "content": "Eres un asistente cordial y prestativo."}
  ]
#inpur del usuario de solicitud
input_mess = input("Esperando msj: ")

#adicionando el input del usuario a la variables messag
messages.append({"role": "user", "content":input_mess})


while input_mess != "fin":
    response = client.chat.completions.create(
        model="gpt-3.5-turbo", messages=messages, temperature=1, max_tokens=200)

    #obtengo respuesta de chatgpt
    content = response.choices[0].message.content

    #adicional al final del message
    messages.append({"role": "user", "content": content})
    print(content)

    #nuevo ingreso
    input_mess = input("Esperando msj: ")
    messages.append({"role": "user", "content": input_mess})


