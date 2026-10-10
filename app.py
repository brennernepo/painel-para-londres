import unicodedata
from html import escape
from urllib.parse import quote

import streamlit as st

from dados import (
    CATEGORIAS,
    DICAS_SEGURANCA,
    HEATHROW,
    INGRESSOS,
    LINHAS,
    MAPA_SEGURANCA,
    MARCOS,
    NIVEIS_SEGURANCA,
    PERFIS,
    REGIOES,
    ROTAS,
    TARIFA_HEATHROW,
)

st.set_page_config(page_title="Painel para Londres", page_icon="🗺", layout="wide")

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600&family=DM+Sans:wght@400;500;600&display=swap');
:root {
  --bg: #FBF5EF; --card: #FFFFFF; --bg3: #F6E7DA;
  --border: rgba(160,52,28,0.13); --border2: rgba(160,52,28,0.26);
  --red: #C8312B; --orange: #E8772E; --tint: rgba(232,119,46,0.09);
  --text: #2B1E1A; --text2: rgba(43,30,26,0.74); --text3: rgba(43,30,26,0.50);
  --ok: #157A55; --ok-bg: #E3F3EB;
  --warn: #9A5306; --warn-bg: #FCEBD3;
  --bad: #B42318; --bad-bg: #FDE4E1;
}
html, body, .stApp, .stMarkdown, button, input, textarea, label, p { font-family: 'DM Sans', sans-serif; }
.stApp { background: var(--bg); }
[data-testid="stHeader"] { background: transparent; }
[data-testid="stMainBlockContainer"] { max-width: 940px; padding-top: 2rem; padding-bottom: 4rem; }

.topo { display: flex; align-items: center; gap: 10px; padding-bottom: 16px; border-bottom: 1px solid var(--border); margin-bottom: 26px; }
.marca-icone { width: 36px; height: 36px; border-radius: 10px; display: flex; align-items: center; justify-content: center;
  background: linear-gradient(135deg, var(--red), var(--orange)); color: #fff; font-size: 17px; }
.marca-nome { font-family: 'Cormorant Garamond', serif; font-size: 24px; font-weight: 600; color: var(--text); }
.titulo { font-family: 'Cormorant Garamond', serif; font-size: 40px; font-weight: 500; line-height: 1.1; color: var(--text); margin: 0 0 8px; }
.titulo span { color: var(--red); }
.descricao { font-size: 14px; color: var(--text2); max-width: 580px; margin-bottom: 6px; }
.rotulo { font-size: 11px; font-weight: 500; letter-spacing: .08em; text-transform: uppercase; color: var(--text3); margin: 22px 0 10px; }
.aviso { font-size: 12px; color: var(--text3); font-style: italic; margin: 8px 0 0; }

/* abas */
[data-testid="stTabs"] [role="tab"] p { font-size: 14px; }
[data-testid="stTabs"] [role="tab"][aria-selected="true"] p { color: var(--red); font-weight: 600; }

/* busca, filtro de região e seletor de seção */
.st-key-busca [data-baseweb="input"], .st-key-busca [data-baseweb="input"] > div, .st-key-busca input { background: #fff !important; }
.st-key-busca [data-baseweb="input"] { border: 1px solid var(--border2); border-radius: 12px; }
[data-testid="stButtonGroup"] button[aria-checked="true"] { background: linear-gradient(135deg, var(--red), var(--orange));
  border-color: transparent; color: #fff; }
[data-testid="stButtonGroup"] button[aria-checked="true"] p { color: #fff; }

/* cartões clicáveis: pontos famosos e rotas */
.st-key-grade button, .st-key-rotas button {
  width: 100%; min-height: 104px; padding: 12px 14px; border-radius: 14px; box-shadow: none;
  background: var(--card); border: 1px solid var(--border); color: var(--text);
  justify-content: flex-start; align-items: flex-start; text-align: left; transition: border-color .15s, transform .15s;
}
.st-key-grade button:hover, .st-key-rotas button:hover { border-color: var(--orange); color: var(--text); transform: translateY(-1px); }
.st-key-grade button:hover, .st-key-rotas button[kind="secondary"]:hover { background: var(--card); }
.st-key-grade button > div, .st-key-rotas button > div,
.st-key-grade button > div > span, .st-key-rotas button > div > span { width: 100%; justify-content: flex-start; text-align: left; }
.st-key-grade button [data-testid="stMarkdownContainer"], .st-key-rotas button [data-testid="stMarkdownContainer"] { width: 100%; white-space: normal; }
.st-key-grade button p, .st-key-rotas button p { display: block; text-align: left; font-size: 12px; line-height: 1.35; margin: 0;
  white-space: normal; overflow: visible; text-overflow: clip; }
.st-key-grade button p:first-child, .st-key-rotas button p:first-child { font-size: 20px; margin-bottom: 6px; }
.st-key-grade button strong, .st-key-rotas button strong { font-size: 14px; font-weight: 600; color: var(--text); }
.st-key-grade .stMarkdownColoredText, .st-key-rotas .stMarkdownColoredText { color: var(--text3) !important; }
.st-key-rotas button { min-height: 96px; }
.st-key-grade { gap: 10px !important; }
.st-key-grade > .stElementContainer { flex: 0 0 calc(20% - 8px) !important; width: calc(20% - 8px) !important; max-width: none !important; }
@media (max-width: 760px) { .st-key-grade > .stElementContainer { flex-basis: calc(33.333% - 7px) !important; width: calc(33.333% - 7px) !important; } }
@media (max-width: 520px) { .st-key-grade > .stElementContainer { flex-basis: calc(50% - 5px) !important; width: calc(50% - 5px) !important; } }
.st-key-rotas button[kind="primary"] { background: var(--tint); border: 1.5px solid var(--orange); color: var(--text); }
.st-key-outros button, .st-key-voltar button { border-radius: 99px; font-size: 13px; padding: 4px 14px; min-height: 0; }

/* região */
.regiao { background: var(--card); border: 1px solid var(--border); border-radius: 16px; overflow: hidden; }
.faixa { height: 5px; background: linear-gradient(90deg, var(--red), var(--orange)); }
.regiao-corpo { padding: 18px 22px 20px; }
.regiao-nome { font-family: 'Cormorant Garamond', serif; font-size: 30px; font-weight: 600; color: var(--text); line-height: 1.15; }
.regiao-desc { font-size: 14px; color: var(--text2); margin: 6px 0 12px; max-width: 640px; }
.selo { display: inline-flex; align-items: center; gap: 6px; font-size: 12px; font-weight: 500; padding: 3px 10px; border-radius: 99px; }
.selo::before { content: ""; width: 7px; height: 7px; border-radius: 50%; background: currentColor; }
.selo.verde { background: var(--ok-bg); color: var(--ok); }
.selo.atencao { background: var(--warn-bg); color: var(--warn); }
.selo.evitar { background: var(--bad-bg); color: var(--bad); }

.pontos { display: grid; grid-template-columns: repeat(auto-fill, minmax(255px, 1fr)); gap: 10px; }
.ponto { background: var(--card); border: 1px solid var(--border); border-radius: 14px; padding: 14px 16px;
  display: flex; flex-direction: column; gap: 7px; }
.ponto-topo { display: flex; align-items: center; gap: 9px; }
.ponto-emoji { font-size: 20px; }
.ponto-nome { font-weight: 600; font-size: 15px; color: var(--text); line-height: 1.25; }
.ponto-texto { font-size: 13px; color: var(--text2); line-height: 1.5; }
.tags { display: flex; flex-wrap: wrap; gap: 5px; }
.tag { font-size: 11px; padding: 2px 9px; border-radius: 99px; background: var(--bg3); color: var(--text2); }
.tag.gratis { background: var(--ok-bg); color: var(--ok); }
.tag.pago { background: #FDE9DA; color: #A84616; }
a.maps { margin-top: auto; padding-top: 4px; font-size: 12px; font-weight: 600; color: var(--red) !important; text-decoration: none; }
a.maps:hover { text-decoration: underline; }

.duas-col { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
.bloco { background: var(--card); border: 1px solid var(--border); border-radius: 14px; padding: 6px 16px; }
.bloco .rotulo { margin: 10px 0 4px; }
.linha { display: flex; justify-content: space-between; align-items: center; gap: 14px; padding: 9px 0; border-bottom: 1px solid var(--border); }
.linha:last-child { border-bottom: none; }
.linha-r { flex: 1 1 45%; font-size: 13px; color: var(--text2); }
.linha-v { flex: 1 1 55%; font-size: 13px; font-weight: 500; color: var(--text); text-align: right; }
.estacao { font-size: 13px; font-weight: 500; color: var(--text); }
.linhas-metro { display: flex; flex-wrap: wrap; justify-content: flex-end; gap: 4px 8px; }
.lm { display: inline-flex; align-items: center; gap: 4px; font-size: 11px; color: var(--text3); white-space: nowrap; }
.lm i { width: 9px; height: 9px; border-radius: 50%; display: inline-block; box-shadow: 0 0 0 1px rgba(0,0,0,.08); }

/* rotas */
.rota { background: var(--card); border: 1px solid var(--border); border-radius: 16px; overflow: hidden; margin-top: 6px; }
.rota-nome { font-family: 'Cormorant Garamond', serif; font-size: 28px; font-weight: 600; color: var(--text); }
.chip { display: inline-block; font-size: 12px; padding: 3px 10px; border-radius: 99px; background: var(--tint); color: #A84616; font-weight: 500; }
.parada { display: grid; grid-template-columns: 30px 1fr; gap: 12px; padding: 14px 22px; border-top: 1px solid var(--border); }
.num { width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center;
  background: linear-gradient(135deg, var(--red), var(--orange)); color: #fff; font-size: 13px; font-weight: 600; }
.parada-nome { font-weight: 600; font-size: 15px; color: var(--text); }
.parada-end { font-size: 12px; color: var(--text3); margin: 1px 0 4px; }
.parada-texto { font-size: 13px; color: var(--text2); line-height: 1.5; margin-bottom: 4px; }

/* gastos */
.tiles { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin-top: 4px; }
.tile { background: var(--card); border: 1px solid var(--border); border-radius: 14px; padding: 16px; text-align: center; }
.tile.forte { background: linear-gradient(135deg, var(--red), var(--orange)); border-color: transparent; }
.tile-valor { font-size: 28px; font-weight: 600; color: var(--text); line-height: 1.2; font-variant-numeric: tabular-nums; }
.tile-rot { font-size: 12px; color: var(--text2); }
.tile.forte .tile-valor, .tile.forte .tile-rot { color: #fff; }
.cat { padding: 10px 0; border-bottom: 1px solid var(--border); }
.cat:last-child { border-bottom: none; }
.cat-topo { display: flex; justify-content: space-between; align-items: baseline; }
.cat-nome { font-size: 14px; color: var(--text); }
.cat-sub { font-size: 11px; color: var(--text3); }
.cat-valor { font-size: 15px; font-weight: 600; color: var(--text); font-variant-numeric: tabular-nums; }
.barra { height: 4px; border-radius: 4px; background: var(--bg3); margin-top: 7px; }
.barra i { display: block; height: 100%; border-radius: 4px; background: var(--orange); }

/* segurança */
.mapa { background: var(--card); border: 1px solid var(--border); border-radius: 16px; padding: 14px 16px; }
.mapa-rolagem { overflow-x: auto; }
.mapa-rolagem svg { min-width: 600px; }
.heathrow-linha { display: flex; align-items: center; gap: 12px; padding: 14px 16px; }
.heathrow-cor { width: 6px; align-self: stretch; border-radius: 4px; background: #003688; }
.ramais { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 10px; }
.ramal { background: var(--card); border: 1px solid var(--border); border-radius: 14px; padding: 12px 14px; }
.ramal-nome { font-weight: 600; font-size: 14px; color: var(--text); }
.ramal-sim { font-size: 13px; color: var(--ok); margin-top: 4px; }
.ramal-nao { font-size: 13px; color: var(--bad); }
.alerta { border-radius: 12px; padding: 10px 14px; font-size: 13px; margin-top: 10px; }
.alerta.laranja { background: var(--warn-bg); color: var(--warn); }
.alerta.vermelho { background: var(--bad-bg); color: var(--bad); }

@media (max-width: 640px) {
  .titulo { font-size: 32px; }
  .duas-col, .tiles, .ramais { grid-template-columns: 1fr; }
  .parada { padding: 12px 16px; }
  .regiao-corpo { padding: 16px; }
}
</style>
"""


# ---------------------------------------------------------------------------
# Utilitários
# ---------------------------------------------------------------------------
def normalizar(texto: str) -> str:
    sem_acento = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    return sem_acento.lower()


def url_maps(busca: str) -> str:
    return f"https://www.google.com/maps/search/?api=1&query={quote(busca)}"


def url_rota(enderecos: list[str]) -> str:
    origem, *meio, destino = enderecos
    url = f"https://www.google.com/maps/dir/?api=1&origin={quote(origem)}&destination={quote(destino)}"
    if meio:
        url += "&waypoints=" + quote("|".join(meio))
    return url


def libras(valor: float) -> str:
    return "£" + f"{valor:,.0f}".replace(",", ".")


def html(trecho: str) -> None:
    st.markdown(trecho, unsafe_allow_html=True)


def classe_tag(tag: str) -> str:
    t = normalizar(tag)
    if "gratis" in t:
        return "tag gratis"
    if "pag" in t or "£" in tag:
        return "tag pago"
    return "tag"


def rolar_ate(chave: str) -> None:
    script = f"""<script>
    setTimeout(function () {{
      var doc = window.parent && window.parent.document ? window.parent.document : document;
      var alvo = doc.querySelector('.st-key-{chave}') || document.querySelector('.st-key-{chave}');
      if (alvo) alvo.scrollIntoView({{behavior: 'smooth', block: 'start'}});
    }}, 250);
    </script>"""
    st.html(script, unsafe_allow_javascript=True)


def selo(nivel: str) -> str:
    return f'<span class="selo {nivel}">{escape(NIVEIS_SEGURANCA[nivel])}</span>'


# ---------------------------------------------------------------------------
# Estado
# ---------------------------------------------------------------------------
st.session_state.setdefault("ponto", None)
st.session_state.setdefault("rota", None)
st.session_state.setdefault("rolar", None)

MARCOS_POR_ID = {m[0]: m for m in MARCOS}


def escolher_ponto(id_marco: str) -> None:
    st.session_state.ponto = id_marco
    st.session_state.rolar = "painel_regiao"


def trocar_ponto() -> None:
    st.session_state.ponto = None
    st.session_state.rolar = "busca_topo"


def escolher_rota(id_rota: str) -> None:
    st.session_state.rota = id_rota
    st.session_state.rolar = "detalhe_rota"


# ---------------------------------------------------------------------------
# Cabeçalho
# ---------------------------------------------------------------------------
st.html(CSS)
html(
    '<div class="topo"><div class="marca-icone">🗺</div><div class="marca-nome">Brenner</div></div>'
    '<div class="titulo">Painel para <span>Londres</span></div>'
    '<div class="descricao">Toque num ponto famoso para ver tudo o que há na região, ou escolha uma rota '
    "temática e monte o dia. Cada parada abre direto no Google Maps.</div>"
)

aba_pontos, aba_rotas, aba_gastos, aba_seguranca = st.tabs(
    ["Por pontos famosos", "Rotas temáticas", "Estimativa de gastos", "Segurança & Heathrow"], key="aba"
)


# ---------------------------------------------------------------------------
# Aba 1: pontos famosos
# ---------------------------------------------------------------------------
def texto_busca_regiao(chave: str) -> str:
    r = REGIOES[chave]
    partes = [r["nome"], r["filtro"], r["descricao"]]
    for p in r["pontos"]:
        partes += [p[1], p[2], " ".join(p[3])]
    return normalizar(" ".join(partes))


def mostrar_grade() -> None:
    with st.container(key="busca_topo"):
        busca = st.text_input(
            "Buscar", placeholder="🔍  Buscar ponto famoso (ex: Tower, Camden, museu…)",
            label_visibility="collapsed", key="busca",
        )
        filtros = ["Todos"] + [r["filtro"] for r in REGIOES.values()]
        filtro = st.pills("Filtrar por região", filtros, default="Todos", key="filtro")

    termo = normalizar(busca.strip())
    marcos = []
    for id_marco, emoji, nome, chave in MARCOS:
        regiao = REGIOES[chave]
        if filtro not in (None, "Todos") and regiao["filtro"] != filtro:
            continue
        if termo and termo not in normalizar(nome) and termo not in texto_busca_regiao(chave):
            continue
        marcos.append((id_marco, emoji, nome, regiao["filtro"]))

    if not marcos:
        st.info("Nenhum ponto encontrado. Tente outro nome ou volte o filtro para Todos.")
        return

    with st.container(key="grade", horizontal=True, wrap=True, gap="small"):
        for id_marco, emoji, nome, rotulo in marcos:
            st.button(
                f"{emoji}\n\n**{nome}**\n\n:gray[{rotulo}]",
                key=f"m_{id_marco}", on_click=escolher_ponto, args=(id_marco,), width="stretch",
            )


def mostrar_regiao(id_marco: str) -> None:
    _, emoji_sel, nome_sel, chave = MARCOS_POR_ID[id_marco]
    r = REGIOES[chave]

    with st.container(key="painel_regiao"):
        with st.container(key="voltar"):
            st.button("← Trocar de ponto", on_click=trocar_ponto)

        html(
            f'<div class="regiao"><div class="faixa"></div><div class="regiao-corpo">'
            f'<div class="regiao-nome">{escape(r["nome"])}</div>'
            f'<div class="regiao-desc">{escape(r["descricao"])}</div>{selo(r["seguranca"])}'
            f"</div></div>"
        )

        outros = [m for m in MARCOS if m[3] == chave and m[0] != id_marco]
        if outros:
            html('<div class="rotulo">Outros pontos desta região</div>')
            with st.container(key="outros", horizontal=True, gap="small"):
                for id_outro, emoji, nome, _ in outros:
                    st.button(f"{emoji} {nome}", key=f"o_{id_outro}", on_click=escolher_ponto, args=(id_outro,))

        cartoes = []
        for ponto in r["pontos"]:
            emoji, nome, texto, tags = ponto[:4]
            busca = ponto[4] if len(ponto) > 4 else nome
            tags_html = "".join(f'<span class="{classe_tag(t)}">{escape(t)}</span>' for t in tags)
            cartoes.append(
                f'<div class="ponto"><div class="ponto-topo"><span class="ponto-emoji">{emoji}</span>'
                f'<span class="ponto-nome">{escape(nome)}</span></div>'
                f'<div class="ponto-texto">{escape(texto)}</div><div class="tags">{tags_html}</div>'
                f'<a class="maps" href="{url_maps(busca + ", London")}" target="_blank">📍 Abrir no Google Maps</a></div>'
            )
        html(f'<div class="rotulo">Tudo o que tem para explorar aqui</div><div class="pontos">{"".join(cartoes)}</div>')

        estacoes = "".join(
            f'<div class="linha"><span class="estacao">{escape(nome)}</span><span class="linhas-metro">'
            + "".join(f'<span class="lm"><i style="background:{LINHAS[l]}"></i>{escape(l)}</span>' for l in linhas)
            + "</span></div>"
            for nome, linhas in r["metro"]
        )
        dicas = "".join(
            f'<div class="linha"><span class="linha-r">{escape(rot)}</span><span class="linha-v">{escape(val)}</span></div>'
            for rot, val in r["dicas"]
        )
        html(
            '<div class="duas-col" style="margin-top:12px">'
            f'<div class="bloco"><div class="rotulo">Como chegar</div>{estacoes}</div>'
            f'<div class="bloco"><div class="rotulo">Dicas práticas</div>{dicas}</div></div>'
        )


with aba_pontos:
    if st.session_state.ponto:
        mostrar_regiao(st.session_state.ponto)
    else:
        mostrar_grade()


# ---------------------------------------------------------------------------
# Aba 2: rotas temáticas
# ---------------------------------------------------------------------------
with aba_rotas:
    with st.container(key="rotas"):
        for inicio in range(0, len(ROTAS), 2):
            colunas = st.columns(2, gap="small")
            for col, rota in zip(colunas, ROTAS[inicio:inicio + 2]):
                with col:
                    st.button(
                        f"{rota['emoji']}\n\n**{rota['nome']}**\n\n:gray[{rota['chamada']}]",
                        key=f"r_{rota['id']}", on_click=escolher_rota, args=(rota["id"],), width="stretch",
                        type="primary" if st.session_state.rota == rota["id"] else "secondary",
                    )

    rota = next((r for r in ROTAS if r["id"] == st.session_state.rota), None)
    if rota:
        with st.container(key="detalhe_rota"):
            buscas = [f"{nome}, {endereco}" for nome, endereco, _, _ in rota["paradas"]]
            paradas = "".join(
                f'<div class="parada"><div class="num">{i}</div><div>'
                f'<div class="parada-nome">{escape(nome)}</div>'
                f'<div class="parada-end">{escape(endereco)} · {escape(estacao)}</div>'
                f'<div class="parada-texto">{escape(texto)}</div>'
                f'<a class="maps" href="{url_maps(busca)}" target="_blank">📍 Abrir no Google Maps</a></div></div>'
                for i, ((nome, endereco, estacao, texto), busca) in enumerate(zip(rota["paradas"], buscas), start=1)
            )
            html(
                f'<div class="rota"><div class="faixa"></div><div class="regiao-corpo">'
                f'<div class="rota-nome">{rota["emoji"]} {escape(rota["nome"])}</div>'
                f'<div class="regiao-desc">{escape(rota["descricao"])}</div>'
                f'<span class="chip">{escape(rota["duracao"])}</span></div></div>'
            )
            st.link_button("🗺 Abrir a rota completa no Google Maps", url_rota(buscas), type="primary")
            html(f'<div class="rotulo">Paradas, em ordem</div><div class="rota">{paradas}</div>')


# ---------------------------------------------------------------------------
# Aba 3: estimativa de gastos
# ---------------------------------------------------------------------------
with aba_gastos:
    html('<div class="descricao" style="margin-top:4px">Configure a viagem e veja quanto custa cada parte, em libras.</div>')
    with st.container(border=True):
        c1, c2, c3 = st.columns(3)
        dias = c1.selectbox("Duração", [3, 5, 7, 10], index=1, format_func=lambda d: f"{d} dias")
        perfil = c2.selectbox("Perfil de gasto", list(PERFIS), index=1)
        pessoas = c3.selectbox("Pessoas", [1, 2, 3, 4, 5, 6], index=1,
                               format_func=lambda p: "1 pessoa" if p == 1 else f"{p} pessoas")

    gastos = PERFIS[perfil]
    dia_pessoa = sum(gastos.values())
    aeroporto = 2 * TARIFA_HEATHROW  # ida e volta pela Piccadilly Line
    total = (dia_pessoa * dias + aeroporto) * pessoas
    transporte = (gastos["Transporte"] * dias + aeroporto) * pessoas

    html(
        '<div class="tiles">'
        f'<div class="tile forte"><div class="tile-valor">{libras(total)}</div><div class="tile-rot">Total estimado</div></div>'
        f'<div class="tile"><div class="tile-valor">{libras(dia_pessoa)}</div><div class="tile-rot">Por dia, por pessoa</div></div>'
        f'<div class="tile"><div class="tile-valor">{libras(transporte)}</div><div class="tile-rot">Transporte, com ida e volta a Heathrow</div></div>'
        "</div>"
        '<div class="aviso">Estimativa de referência. O gasto real muda com a época, o câmbio e as escolhas de cada um. '
        "Hospedagem e passagem aérea ficam de fora.</div>"
    )

    maior = max(gastos.values())
    categorias = "".join(
        f'<div class="cat"><div class="cat-topo"><div><div class="cat-nome">{escape(cat)}</div>'
        f'<div class="cat-sub">{escape(CATEGORIAS[cat])}</div></div>'
        f'<div class="cat-valor">{libras(valor)}</div></div>'
        f'<div class="barra"><i style="width:{valor / maior * 100:.0f}%"></i></div></div>'
        for cat, valor in gastos.items()
    )
    html(f'<div class="rotulo">Por categoria, por pessoa, por dia</div><div class="bloco">{categorias}</div>')

    referencia = "".join(
        f'<div class="linha"><span class="linha-r">{escape(item)}</span><span class="linha-v">{escape(preco)}</span></div>'
        for item, preco in INGRESSOS
    )
    html(
        f'<div class="rotulo">Preços de referência · outubro de 2026</div><div class="bloco">{referencia}</div>'
        '<div class="aviso">Ingressos mudam conforme a data e a TfL reajusta tarifas todo março. Confira no site oficial antes de comprar.</div>'
    )


# ---------------------------------------------------------------------------
# Aba 4: segurança e Heathrow
# ---------------------------------------------------------------------------
CORES_MAPA = {
    "verde": ("#E3F3EB", "#157A55", None),
    "atencao": ("#FCEBD3", "#9A5306", "noite: atenção"),
    "evitar": ("#FDE4E1", "#B42318", "evitar à noite"),
}


def svg_mapa() -> str:
    caixas = []
    for nome, nivel, x, y in MAPA_SEGURANCA:
        fundo, cor, sub = CORES_MAPA[nivel]
        meio = y + (20 if sub else 29)
        caixas.append(
            f'<rect x="{x}" y="{y}" width="120" height="50" rx="10" fill="{fundo}"/>'
            f'<text x="{x + 60}" y="{meio}" text-anchor="middle" font-size="13" font-weight="600" fill="{cor}">{escape(nome)}</text>'
        )
        if sub:
            caixas.append(
                f'<text x="{x + 60}" y="{y + 37}" text-anchor="middle" font-size="11" fill="{cor}">{sub}</text>'
            )
    rio = (
        '<path d="M0,365 C120,370 200,360 250,330 S320,285 380,284 L560,284 C600,284 610,300 640,300 S720,285 760,290" '
        'fill="none" stroke="#BFD6EA" stroke-width="9" stroke-linecap="round"/>'
        '<text x="14" y="396" font-size="11" font-style="italic" fill="#6F8FAE">Rio Tâmisa</text>'
    )
    return (
        '<svg viewBox="0 0 760 410" role="img" aria-label="Mapa esquemático de segurança de Londres por área" '
        'style="width:100%;height:auto;font-family:\'DM Sans\',sans-serif">'
        + rio + "".join(caixas) + "</svg>"
    )


with aba_seguranca:
    secao = st.segmented_control(
        "Seção", ["🗺 Mapa", "🛡 Dicas", "✈️ Heathrow"], default="🗺 Mapa", required=True,
        label_visibility="collapsed", key="secao",
    )

    if secao == "🗺 Mapa":
        niveis_usados = [n for n in NIVEIS_SEGURANCA if any(nv == n for _, nv, _, _ in MAPA_SEGURANCA)]
        html(
            '<div class="rotulo">Mapa de segurança por área</div>'
            '<div class="descricao">Orientação geral para turistas, pensando sobretudo na volta para o hotel à noite. '
            "O mapa é esquemático, sem escala.</div>"
        )
        resumo = "".join(
            f'<div class="cat">{selo(n)}<div class="linha-r" style="margin-top:6px">'
            + escape(", ".join(nome for nome, nv, _, _ in MAPA_SEGURANCA if nv == n)) + "</div></div>"
            for n in niveis_usados
        )
        html(f'<div class="mapa"><div class="mapa-rolagem">{svg_mapa()}</div></div>')
        html(
            f'<div class="bloco" style="margin-top:10px">{resumo}</div>'
            '<div class="aviso">Furto é o risco mais comum, e acontece justamente nas áreas tranquilas e cheias de '
            "turistas: Oxford Street, Westminster, mercados e metrô lotado.</div>"
        )

    elif secao == "🛡 Dicas":
        linhas = "".join(
            f'<div class="linha"><span class="linha-r">{escape(r)}</span><span class="linha-v">{escape(v)}</span></div>'
            for r, v in DICAS_SEGURANCA
        )
        html(f'<div class="rotulo">Dicas de segurança</div><div class="bloco">{linhas}</div>')

    else:
        h = HEATHROW
        sentidos = "".join(
            f'<div class="linha"><span class="linha-r">{escape(r)}</span><span class="linha-v">{escape(v)}</span></div>'
            for r, v in h["sentidos"]
        )
        ramais = "".join(
            f'<div class="ramal"><div class="ramal-nome">{escape(n)}</div>'
            f'<div class="ramal-sim">✓ {escape(sim)}</div><div class="ramal-nao">✗ {escape(nao)}</div></div>'
            for n, sim, nao in h["ramais"]
        )
        fatos = "".join(
            f'<div class="linha"><span class="linha-r">{escape(r)}</span><span class="linha-v">{escape(v)}</span></div>'
            for r, v in h["fatos"]
        )
        html(
            '<div class="rotulo">Do centro para Heathrow</div>'
            f'<div class="descricao">{escape(h["intro"])}</div>'
            '<div class="bloco" style="padding:0"><div class="heathrow-linha"><div class="heathrow-cor"></div><div>'
            f'<div class="ramal-nome">{escape(h["linha"])}</div><div class="cat-sub">{escape(h["resumo"])}</div>'
            f"</div></div></div>"
            f'<div class="bloco" style="margin-top:10px">{sentidos}</div>'
            f'<div class="ramais">{ramais}</div>'
            f'<div class="alerta vermelho">⚠️ {escape(h["uxbridge"])}</div>'
            f'<div class="alerta laranja">💡 Pegou o trem errado? {escape(h["trem_errado"])}</div>'
            f'<div class="rotulo">Horários e alternativas</div><div class="bloco">{fatos}</div>'
        )


# Rolagem até o conteúdo que acabou de abrir
if st.session_state.rolar:
    rolar_ate(st.session_state.rolar)
    st.session_state.rolar = None
