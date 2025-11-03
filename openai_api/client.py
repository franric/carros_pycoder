import openai
from openai import OpenAI

def get_car_ai_bio(model, brand, year):
  openai.api_key = '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'
  input = '''
  Crie uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. Fale sobre a parte tecnica e beneficios ao comprar esse veiculo.
  '''
  input = input.format(model, brand, year)
  response = openai.completions.create(
    model='gpt-3.5-turbo-instruct',
    prompt=input,
    max_tokens=180,
    temperature=0.7,
  )
  texto = response.choices[0].text.strip()
  return texto
  # return response['choices'][0]['text']

def get_car_ai_bio_new(model, brand, year):
    openai.api_key = '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'
    prompt = (
        f"Crie uma descrição de venda para o carro {model} {brand} {year} "
        f"em até 250 caracteres. Fale brevemente da parte técnica e dos benefícios."
    )

    resp = openai.chat.completions.create(
        model="gpt-4o-mini",  # ou outro modelo de sua preferência
        messages=[
            {"role": "system", "content": "Você é um redator de anúncios automotivos objetivo e persuasivo."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=180,
        temperature=0.7,
    )
    texto = resp.choices[0].message.content.strip()
    # (Opcional) garantir o limite de 250 caracteres:
    if len(texto) > 250:
        texto = texto[:247].rstrip() + "..."
    return texto
