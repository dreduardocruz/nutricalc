# 🧬 NutriCalc Brasil — Instituto Python

Calculadora interativa de refeições diárias, metabolismo basal (Mifflin-St Jeor & Katch-McArdle via Bioimpedância) e distribuição de macronutrientes baseada na Tabela Brasileira de Composição de Alimentos (TACO).

Idealizado e disponibilizado por **Dr. Eduardo Pereira Cruz** — **Instituto Python**.
CRM-GO 6527 · Ginecologia e Obstetrícia — RQE 2394 · Acupuntura — RQE 13650.

---

## ✨ Funcionalidades Principais
- **100% Compatível com iOS (iPhone/iPad), Android e Desktop:** Web App responsivo com suporte a *Add to Home Screen* (PWA Apple Meta Tags) e inputs otimizados (`16px`) que evitam zoom indesejado no Safari do iOS.
- **Integração Direta com Pipeline de Bioimpedância:**
  - Suporta cálculo automático pela equação de **Katch-McArdle** ao informar a **Massa Magra (kg)** ou **% de Gordura Corporal (BF)**, ou uso direto da **TMB Medida** no laudo da bioimpedância.
  - **Injeção via URL Query Params:** Gere links personalizados no seu backend em Python/Flask para enviar diretamente ao WhatsApp do paciente:
    ```
    https://seu-usuario.github.io/nutricalc-instituto-python/?nome=Maria+Silva&sexo=F&idade=38&peso=68.5&altura=164&bf=22.4&massa_magra=53.1&tmb=1490
    ```
  - **Importação via JSON:** Modal dedicado para colar o JSON extraído do laudo de bioimpedância.
- **Logo Personalizável:** Basta colocar o arquivo `logo.png` na raiz do projeto que o cabeçalho substitui automaticamente o ícone padrão pela logomarca do **Instituto Python**.

---

## 🚀 Como Publicar no GitHub Pages (no seu PC)

```bash
git init
git add .
git commit -m "feat: release inicial NutriCalc Instituto Python"
git branch -M main
git remote add origin git@github.com:dreduardocruz/nutricalc.git
git push -u origin main
```

---

## 🤖 Créditos de Desenvolvimento
Código-fonte desenvolvido com o auxílio da inteligência artificial **Google Gemini 4.0**, sob arquitetura, integração clínica e curadoria do **Dr. Eduardo Pereira Cruz — Instituto Python**.

## 📜 Licença
Distribuído sob a licença **MIT**. Veja o arquivo `LICENSE` para mais detalhes.
