import pandas as pd  
import numpy as np   
import matplotlib.pyplot as plt  
from io import StringIO
from flask import Flask, render_template, request
# Insert the file path for genetic data here:
## The file should be in CSV format and should have at least two columns. One of them should be named "rsid," and the other should be named "genotype."
df = pd.read_csv("", sep=';')


gen_expr_df = pd.DataFrame({
    'SNP': ["rs429358", "rs7412", "rs1801133", "rs1801131", "rs12934922", "rs80357406", "rs80359065", "rs80358911", "rs80359065", "rs80359537"],
    'Expr': ["" for _ in range(10)] 
})

for index, row in gen_expr_df.iterrows():
    snp = row['SNP']
    
    matching_row = df[df['rsid'] == snp]
    
    if not matching_row.empty:
        genotype = matching_row.iloc[0]['genotype']
        
        gen_expr_df.at[index, 'Expr'] = genotype

res_ApoE2 = "You carry the APOE-ε2 variante which implies a low risk for Alzheimer's disease."
res_ApoE3 = "You carry the APOE-ε3 variante which implies a normal risk for Alzheimer's disease."
res_ApoE4 = "You carry the APOE-ε4 variante which implies an elevated for Alzheimer's disease."
res_MTHFR1 = "You carry a heterozygous C677T polymorphism which implies a slightly elevated risk for high homocystein."
res_MTHFR_homo1 = "You carry a homozygous C677T polymorphism which implies a strongly elevated risk for high homocystein."
res_MTHFR2 = "You carry a heterozygous A1298C polymorphism which implies a slightly elevated risk for high homocystein."
res_MTHFR_homo2 = "You carry a homozygous A1298C polymorphism which implies a strongly elevated risk for high homocystein."
BCMO1 = "You carry a heterozygous BCMO1 polymorphism which implies a slightly reduced ability to convert beta-carotene into retinol."
BCMO1_homo = "You carry a heterozygous BCMO1 polymorphism which implies a strongly reduced ability to convert beta-carotene into retinol."
if gen_expr_df.Expr[0] == "GG":
    print(res_ApoE2)
if gen_expr_df.Expr[0] == "GT":
    print(res_ApoE3)
if gen_expr_df.Expr[0] == "TT":
    print(res_ApoE4)
if gen_expr_df.Expr[2] == "TT":
    print(res_MTHFR_homo1)
if gen_expr_df.Expr[2] == "GT":
    print(res_MTHFR1)
if gen_expr_df.Expr[3] == "GG":
    print(res_MTHFR_homo2)
if gen_expr_df.Expr[3] == "GT":
    print(res_MTHFR2)

print(gen_expr_df)