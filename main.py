import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

dftotal=pd.read_csv('https://raw.githubusercontent.com/jorgemalber/app_tpadII/main/evasao_ano_grupo.csv')
dfcurso=pd.read_csv('https://raw.githubusercontent.com/jorgemalber/app_tpadII/main/evasao_ano_curso_grupo.csv')
dfarea=pd.read_csv('https://raw.githubusercontent.com/jorgemalber/app_tpadII/main/evasao_ano_area_grupo.csv')

st.set_page_config(page_title='Evasão UFPB ' , page_icon='🗿', layout="wide", initial_sidebar_state="collapsed", menu_items=None)
st.title("Evasão UFPB :rocket: ")
st.markdown('Um pequeno dashboard que exibe os dados de evasão da **UFPB** por segmento de ingressants,curso e área')

def figura_total():

    fig = px.line(dftotal, x="ANO", y=['EVASAO','_MASC','_FEM','_17_29','_30_MAIS','_BRANCA','_N_BRANCA','_DIURNO', '_NOTURNO', '_17_29', '_30_MAIS', '_BRANCA', '_N_BRANCA',
       '_RESERVA_VAGA', '_RVREDEPUBLICA', '_RVETNICO',
       '_RVSOCIAL_RF', '_PROCESCPUBLICA', '_PROCESCPRIVADA'],markers=True,color_discrete_sequence=px.colors.qualitative.Antique)

    fig.update_layout(template='simple_white',
    yaxis_title='% Evasão',
    title='Evasão total vs evasão por segmento',
    hovermode="x",
    width=1200,height=600
    )
    fig.add_annotation(x=2020, y=100,
            text="boom",
            showarrow=False,
            yshift=5)
    st.plotly_chart(fig)

def evasao_area():
    fig = px.bar(ev_area_media, x=['EVASAO','_MASC','_FEM','_17_29','_30_MAIS','_BRANCA','_N_BRANCA','_DIURNO', '_NOTURNO', '_17_29', '_30_MAIS', '_BRANCA', '_N_BRANCA',
       '_RESERVA_VAGA', '_RVREDEPUBLICA', '_RVETNICO',
       '_RVSOCIAL_RF', '_PROCESCPUBLICA', '_PROCESCPRIVADA'],
        y="NO_CINE_AREA_GERAL",
     orientation='h', width=1200, height=600,
        title='Evasão média por área ',color_discrete_sequence=px.colors.qualitative.Antique)
    st.plotly_chart(fig)
def evasao_curso_maior():
    fig = px.bar(ev_curso_media_top_maior, x=['EVASAO','_MASC','_FEM','_17_29','_30_MAIS','_BRANCA','_N_BRANCA','_DIURNO', '_NOTURNO', '_17_29', '_30_MAIS', '_BRANCA', '_N_BRANCA',
       '_RESERVA_VAGA', '_RVREDEPUBLICA', '_RVETNICO',
       '_RVSOCIAL_RF', '_PROCESCPUBLICA', '_PROCESCPRIVADA'],
        y="NO_CINE_ROTULO",
     orientation='h', width=1200, height=600,
        title='Top 10 maior evasão média ',color_discrete_sequence=px.colors.qualitative.Antique)
    st.plotly_chart(fig)
def evasao_curso_menor():
    fig = px.histogram(ev_curso_media_top_menor, x=['EVASAO','_MASC','_FEM','_17_29','_30_MAIS','_BRANCA','_N_BRANCA','_DIURNO', '_NOTURNO', '_17_29', '_30_MAIS', '_BRANCA', '_N_BRANCA',
       '_RESERVA_VAGA', '_RVREDEPUBLICA', '_RVETNICO',
       '_RVSOCIAL_RF', '_PROCESCPUBLICA', '_PROCESCPRIVADA'],
        y="NO_CINE_ROTULO",
     orientation='h', width=1100, height=600,
        title='Top 10 menor evasão média ',color_discrete_sequence=px.colors.qualitative.Antique)
    st.plotly_chart(fig)
ev_area_media=dfarea.groupby('NO_CINE_AREA_GERAL').agg('mean').reset_index().sort_values(by=['EVASAO'])
ev_curso_media_top_maior=(
    dfcurso.groupby('NO_CINE_ROTULO')
    .agg('mean').reset_index()
    .sort_values(by=['EVASAO'],ascending=True)
    .tail(10).query('NO_CINE_ROTULO!="Ciências naturais formação de professor" & NO_CINE_ROTULO!= "Letras outras línguas estrangeiras modernas formação de professor"')
)
ev_curso_media_top_menor=(
    dfcurso.groupby('NO_CINE_ROTULO')
    .agg('mean').reset_index()
    .sort_values(by=['EVASAO'],ascending=True)
    .query('NO_CINE_ROTULO!="Educação do campo formação de professor"')
    .head(10)
    )
    
figura_total()
evasao_area()
evasao_curso_maior()
evasao_curso_menor()