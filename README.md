# Painel para Londres

Painel em Streamlit para planejar uma viagem a Londres. Tem quatro abas:

- **Por pontos famosos**: 35 atrações com busca e filtro por região. Ao tocar numa delas, abre a região inteira, com o que ver, estações de metrô e dicas práticas.
- **Rotas temáticas**: Rock, Pubs, Esporte, Premium, Harry Potter e Kids. As paradas vêm em ordem, e um link abre a rota completa no Google Maps.
- **Estimativa de gastos**: escolha duração, perfil e número de pessoas e veja o total em libras, separado por categoria.
- **Segurança & Heathrow**: mapa esquemático por área, dicas e o guia da Piccadilly Line até o aeroporto.

## Rodar no computador

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Onde mexer

Todo o conteúdo está em `dados.py`: regiões, atrações, rotas, valores da estimativa e preços de referência. O `app.py` só monta a tela. Para corrigir um horário ou incluir um pub, edite `dados.py` e recarregue a página. Não há banco de dados.

Os preços foram conferidos em outubro de 2026. A TfL reajusta as tarifas todo março e os ingressos mudam conforme a data, então confira no site oficial antes de comprar.

## Publicar

No [Streamlit Community Cloud](https://share.streamlit.io), conecte este repositório e indique `app.py` como arquivo principal.
