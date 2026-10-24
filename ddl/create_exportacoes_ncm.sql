-- Exportacoes brasileiras (Comex Stat / MDIC): uma linha por combinacao de
-- ano, mes, NCM, pais de destino, UF de origem, via e URF
-- CO_NCM    -> liga com ncm_sh, ncm_cuci, ncm_cgce, ncm_isic etc. (co_ncm)
-- CO_UNID   -> liga com ncm_unidade (co_unid); QT_ESTAT esta nessa unidade
-- CO_PAIS   -> liga com pais (co_pais) e pais_bloco (co_pais)
-- SG_UF_NCM -> liga com uf (sg_uf)
-- CO_VIA    -> liga com via (co_via)
-- CO_URF    -> liga com urf (co_urf)
-- QT_ESTAT  = quantidade na unidade estatistica do NCM; KG_LIQUIDO sempre em kg; VL_FOB em US$
CREATE TABLE exportacoes (
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