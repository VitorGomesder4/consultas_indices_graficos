CREATE DATABASE IF NOT EXISTS consultas_indices_graficos;
USE consultas_indices_graficos;

    -- Exportacoes brasileiras (Comex Stat / MDIC): uma linha por combinacao de
    -- ano, mes, NCM, pais de destino, UF de origem, via e URF
    -- CO_NCM    -> liga com ncm_sh, ncm_cuci, ncm_cgce, ncm_isic etc. (co_ncm)
    -- CO_UNID   -> liga com ncm_unidade (co_unid); QT_ESTAT esta nessa unidade
    -- CO_PAIS   -> liga com pais (co_pais) e pais_bloco (co_pais)
    -- SG_UF_NCM -> liga com uf (sg_uf)
    -- CO_VIA    -> liga com via (co_via)
    -- CO_URF    -> liga com urf (co_urf)
    -- QT_ESTAT  = quantidade na unidade estatistica do NCM; KG_LIQUIDO sempre em kg; VL_FOB em US$
    CREATE TABLE IF NOT EXISTS exportacoes (
    id_exportacao INT(11) NOT NULL AUTO_INCREMENT,
    CO_ANO VARCHAR(15) NULL,
    CO_MES VARCHAR(15) NULL,
    CO_NCM VARCHAR(15) NULL,
    CO_UNID VARCHAR(15) NULL,
    CO_PAIS VARCHAR(15) NULL,
    SG_UF_NCM CHAR(2) NULL,
    CO_VIA VARCHAR(15) NULL,
    CO_URF VARCHAR(15) NULL,
    QT_ESTAT VARCHAR(15) NULL,
    KG_LIQUIDO VARCHAR(15) NULL,
    VL_FOB VARCHAR(15) NULL,
    PRIMARY KEY (id_exportacao)
    );

-- Tabelas auxiliares Comex Stat (MDIC) - apenas CREATE TABLE IF NOT EXISTS -- Codigos sao VARCHAR para preservar zeros a esquerda (ex.: NCM 01011010, pais 013)

-- Indice: lista as 16 abas do arquivo, com descricao e chave de cruzamento
-- 16 linhas na planilha
CREATE TABLE IF NOT EXISTS indice_tabelas (
  numero_da_aba VARCHAR(2) NOT NULL,
  nome VARCHAR(80) NULL,
  descricao TEXT NULL,
  arquivo_referencia VARCHAR(20) NULL,
  chave_de_cruzamento VARCHAR(30) NULL,
  PRIMARY KEY (numero_da_aba)
);

-- Aba 1: SH - Sistema Harmonizado
-- Códigos e descrições do Sistema Harmonizado (Seções, Capítulos-SH2, Posições-SH4 e Subposições-SH6).
-- Arquivo de referencia: NCM_SH.csv | Chave de cruzamento: CO_SH6
-- 13741 linhas na planilha
CREATE TABLE IF NOT EXISTS ncm_sh (
  co_ncm VARCHAR(8) NOT NULL,
  no_ncm_por VARCHAR(1000) NULL,
  co_sh6 VARCHAR(6) NULL,
  no_sh6_por VARCHAR(1000) NULL,
  no_sh6_esp VARCHAR(1000) NULL,
  no_sh6_ing VARCHAR(500) NULL,
  co_sh4 VARCHAR(4) NULL,
  no_sh4_por VARCHAR(255) NULL,
  no_sh4_esp VARCHAR(255) NULL,
  no_sh4_ing VARCHAR(255) NULL,
  co_sh2 VARCHAR(2) NULL,
  no_sh2_por VARCHAR(255) NULL,
  no_sh2_esp VARCHAR(100) NULL,
  no_sh2_ing VARCHAR(100) NULL,
  co_ncm_secrom VARCHAR(5) NULL,
  no_sec_por VARCHAR(255) NULL,
  no_sec_esp VARCHAR(255) NULL,
  no_sec_ing VARCHAR(255) NULL,
  PRIMARY KEY (co_ncm)
);

-- Aba 2: CUCI - Classificação Uniforme para Comércio Internacional
-- Códigos e descrições dos níveis da classificação CUCI (Revisão 4). Pode ser utilizada conjuntamente com ISIC.
-- Arquivo de referencia: NCM_CUCI.csv | Chave de cruzamento: CO_CUCI
-- 13746 linhas na planilha
CREATE TABLE IF NOT EXISTS ncm_cuci (
  co_ncm VARCHAR(8) NOT NULL,
  no_ncm_por VARCHAR(1000) NULL,
  co_cuci_item VARCHAR(5) NULL,
  no_cuci_item VARCHAR(255) NULL,
  co_cuci_sub VARCHAR(4) NULL,
  no_cuci_sub VARCHAR(255) NULL,
  co_cuci_grupo VARCHAR(5) NULL,
  no_cuci_grupo VARCHAR(255) NULL,
  co_cuci_divisao VARCHAR(2) NULL,
  no_cuci_divisao VARCHAR(100) NULL,
  co_cuci_sec VARCHAR(1) NULL,
  no_cuci_sec VARCHAR(80) NULL,
  PRIMARY KEY (co_ncm)
);

-- Aba 3: CGCE - Classificação por Grandes Categorias Econômicas
-- Códigos e descrições dos níveis da classificação CGCE.
-- Arquivo de referencia: NCM_CGCE.csv | Chave de cruzamento: CO_CGCE_N3
-- 13746 linhas na planilha
CREATE TABLE IF NOT EXISTS ncm_cgce (
  co_ncm VARCHAR(8) NOT NULL,
  no_ncm_por VARCHAR(1000) NULL,
  co_cgce_n3 VARCHAR(3) NULL,
  no_cgce_n3 VARCHAR(100) NULL,
  no_cgce_n3_ing VARCHAR(80) NULL,
  no_cgce_n3_esp VARCHAR(100) NULL,
  co_cgce_n2 VARCHAR(2) NULL,
  no_cgce_n2 VARCHAR(80) NULL,
  no_cgce_n2_ing VARCHAR(80) NULL,
  no_cgce_n2_esp VARCHAR(80) NULL,
  co_cgce_n1 VARCHAR(1) NULL,
  no_cgce_n1 VARCHAR(50) NULL,
  no_cgce_n1_ing VARCHAR(30) NULL,
  no_cgce_n1_esp VARCHAR(50) NULL,
  PRIMARY KEY (co_ncm)
);

-- Aba 4: ISIC - International Standard Industrial Classification (Setores Industriais)
-- Códigos e descrições da classificação ISIC (Revisão 4).
-- Arquivo de referencia: NCM_ISIC.csv | Chave de cruzamento: CO_ISIC_CLASSE
-- 13746 linhas na planilha
CREATE TABLE IF NOT EXISTS ncm_isic (
  co_ncm VARCHAR(8) NOT NULL,
  no_ncm_por VARCHAR(1000) NULL,
  co_isic_classe VARCHAR(4) NULL,
  no_isic_classe VARCHAR(150) NULL,
  no_isic_classe_ing VARCHAR(150) NULL,
  no_isic_classe_esp VARCHAR(150) NULL,
  co_isic_grupo VARCHAR(3) NULL,
  no_isic_grupo VARCHAR(150) NULL,
  no_isic_grupo_ing VARCHAR(150) NULL,
  no_isic_grupo_esp VARCHAR(150) NULL,
  co_isic_divisao VARCHAR(2) NULL,
  no_isic_divisao VARCHAR(150) NULL,
  no_isic_divisao_ing VARCHAR(150) NULL,
  no_isic_divisao_esp VARCHAR(150) NULL,
  co_isic_secao VARCHAR(1) NULL,
  no_isic_secao VARCHAR(30) NULL,
  no_isic_secao_ing VARCHAR(50) NULL,
  no_isic_secao_esp VARCHAR(30) NULL,
  PRIMARY KEY (co_ncm)
);

-- Aba 5: SIIT - Setores Industriais por Intensidade Tecnológica
-- Códigos e descrições da classificação SIIT.
-- Arquivo de referencia: NCM_SIIT.csv | Chave de cruzamento: CO_SIIT
-- 13440 linhas na planilha
CREATE TABLE IF NOT EXISTS ncm_siit (
  co_ncm VARCHAR(8) NOT NULL,
  no_ncm_por VARCHAR(1000) NULL,
  co_siit VARCHAR(4) NULL,
  no_siit VARCHAR(80) NULL,
  PRIMARY KEY (co_ncm)
);

-- Aba 6: Unidade Estatística da NCM
-- Códigos e descrições das unidades estatísticas das NCMs.
-- Arquivo de referencia: NCM_UNIDADE.csv | Chave de cruzamento: CO_UNID
-- 13746 linhas na planilha
CREATE TABLE IF NOT EXISTS ncm_unidade (
  co_ncm VARCHAR(8) NOT NULL,
  no_ncm_por VARCHAR(1000) NULL,
  co_unid VARCHAR(2) NULL,
  no_unid VARCHAR(30) NULL,
  sg_unid VARCHAR(5) NULL,
  PRIMARY KEY (co_ncm)
);

-- Aba 7: Fator Agregado da NCM - Classificação própria da SECEX
-- Códigos e descrições de Fator Agregado das NCMs. Pode ser utilizada conjuntamente com a tabela de PPI ou PPE.
-- Arquivo de referencia: NCM_FAT_AGREG.csv | Chave de cruzamento: CO_FAT_AGREG
-- 13724 linhas na planilha
CREATE TABLE IF NOT EXISTS ncm_fat_agreg (
  co_ncm VARCHAR(8) NOT NULL,
  no_ncm_por VARCHAR(1000) NULL,
  co_fat_agreg VARCHAR(2) NULL,
  no_fat_agreg VARCHAR(30) NULL,
  no_fat_agreg_gp VARCHAR(30) NULL,
  PRIMARY KEY (co_ncm)
);

-- Aba 8: Pauta de Produtos Importados - Classificação própria da SECEX
-- Códigos e descrições da Pauta de Produtos Importados. DEVE SER UTILIZADA APENAS PARA IMPORTAÇÃO.
-- Arquivo de referencia: NCM_PPI.csv | Chave de cruzamento: CO_PPI
-- 13440 linhas na planilha
CREATE TABLE IF NOT EXISTS ncm_ppi (
  co_ncm VARCHAR(8) NOT NULL,
  no_ncm_por VARCHAR(1000) NULL,
  co_ppi VARCHAR(4) NULL,
  no_ppi VARCHAR(80) NULL,
  no_ppi_min VARCHAR(80) NULL,
  no_ppi_ing VARCHAR(80) NULL,
  PRIMARY KEY (co_ncm)
);

-- Aba 9: Pauta de Produtos Exportados - Classificação própria da SECEX
-- Códigos e descrições da Pauta de Produtos Exportados. DEVE SER UTILIZADA APENAS PARA EXPORTAÇÃO.
-- Arquivo de referencia: NCM_PPE.csv | Chave de cruzamento: CO_PPE
-- 13440 linhas na planilha
CREATE TABLE IF NOT EXISTS ncm_ppe (
  co_ncm VARCHAR(8) NOT NULL,
  no_ncm_por VARCHAR(1000) NULL,
  co_ppe VARCHAR(4) NULL,
  no_ppe VARCHAR(80) NULL,
  no_ppe_min VARCHAR(80) NULL,
  no_ppe_ing VARCHAR(80) NULL,
  PRIMARY KEY (co_ncm)
);

-- Aba 10: Países
-- Códigos e descrições de países.
-- Arquivo de referencia: PAIS.csv | Chave de cruzamento: CO_PAIS
-- 281 linhas na planilha
CREATE TABLE IF NOT EXISTS pais (
  co_pais VARCHAR(3) NOT NULL,
  co_pais_ison3 VARCHAR(3) NULL,
  co_pais_isoa3 VARCHAR(3) NULL,
  no_pais VARCHAR(50) NULL,
  no_pais_ing VARCHAR(80) NULL,
  no_pais_esp VARCHAR(80) NULL,
  PRIMARY KEY (co_pais)
);

-- Aba 11: Blocos de Países
-- Códigos e descrições das principais agregações de países em blocos. Deve ser usada em cojunto com a tabela de países.
-- Arquivo de referencia: PAIS_BLOCO.csv | Chave de cruzamento: CO_BLOCO
-- 324 linhas na planilha
CREATE TABLE IF NOT EXISTS pais_bloco (
  co_pais VARCHAR(3) NOT NULL,
  co_bloco VARCHAR(3) NOT NULL,
  no_bloco VARCHAR(50) NULL,
  no_bloco_ing VARCHAR(50) NULL,
  no_bloco_esp VARCHAR(50) NULL,
  PRIMARY KEY (co_pais, co_bloco)
);

-- Aba 12: Unidades da Federação
-- Códigos e nome das unidades da federação (estados) do Brasil.
-- Arquivo de referencia: UF.csv | Chave de cruzamento: CO_UF ou SG_UF
-- 34 linhas na planilha
CREATE TABLE IF NOT EXISTS uf (
  co_uf VARCHAR(2) NOT NULL,
  sg_uf VARCHAR(2) NULL,
  no_uf VARCHAR(30) NULL,
  no_regiao VARCHAR(30) NULL,
  PRIMARY KEY (co_uf)
);

-- Aba 13: Municípios
-- Códigos e nome dos municípios brasileiros. Pode ser utilizada em conjunto com a tabela de UF. Fundamental para utilização junto com o arquivo de dados brutos por municípios domicílio fiscal das empresas
-- Arquivo de referencia: UF_MUN.csv | Chave de cruzamento: CO_MUN_GEO
-- 5570 linhas na planilha
CREATE TABLE IF NOT EXISTS uf_mun (
  co_mun_geo VARCHAR(7) NOT NULL,
  no_mun VARCHAR(50) NULL,
  no_mun_min VARCHAR(50) NULL,
  sg_uf VARCHAR(2) NULL,
  PRIMARY KEY (co_mun_geo)
);

-- Aba 14: Via
-- Código e descrição da via (modal) de transporte
-- Arquivo de referencia: VIA.csv | Chave de cruzamento: CO_VIA
-- 17 linhas na planilha
CREATE TABLE IF NOT EXISTS via (
  co_via VARCHAR(2) NOT NULL,
  no_via VARCHAR(30) NULL,
  PRIMARY KEY (co_via)
);

-- Aba 15: Urf
-- Código e descrição da Unidade da Receita Federal (embarque/despacho) mais detalhes em: http://idg.receita.fazenda.gov.br/orientacao/aduaneira/importacao-e-exportacao/recinto-alfandegados
-- Arquivo de referencia: URF.csv | Chave de cruzamento: CO_URF
-- 281 linhas na planilha
CREATE TABLE IF NOT EXISTS urf (
  co_urf VARCHAR(7) NOT NULL,
  no_urf VARCHAR(80) NULL,
  PRIMARY KEY (co_urf)
);

-- Aba 16: ISIC Seção x CUCI Grupo
-- Códigos e descrições dos níveis ISIC e CUCI usados na coletiva de apresentação da balança comercial brasileira.
-- Arquivo de referencia: ISIC_CUCI.csv | Chave de cruzamento: CO_CUCI_GRUPO e CO_ISIC_SECAO
-- 13746 linhas na planilha
CREATE TABLE IF NOT EXISTS isic_cuci (
  co_ncm VARCHAR(8) NOT NULL,
  no_ncm_por VARCHAR(1000) NULL,
  co_isic_secao VARCHAR(1) NULL,
  no_isic_secao VARCHAR(30) NULL,
  co_cuci_grupo VARCHAR(5) NULL,
  no_cuci_grupo VARCHAR(255) NULL,
  PRIMARY KEY (co_ncm)
);
