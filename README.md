# 🧮 Calculadora de Milhas

Um pequeno programa em **Python** feito para resolver uma dúvida bem prática: **vale mais a pena pagar uma passagem aérea com dinheiro ou com milhas?**

A ferramenta calcula o **valor real de cada milha (em centavos)** com base no preço da passagem, na quantidade de milhas exigidas e na taxa de embarque, e devolve uma recomendação automática sobre a melhor forma de pagamento.

---

## 📋 Sobre o projeto

Toda vez que eu ia comprar uma passagem, surgia a mesma dúvida: usar as milhas acumuladas ou pagar em dinheiro? Fazer essa conta manualmente — considerando a taxa de embarque — era chato e pouco preciso.

Para resolver isso (e praticar lógica de programação), criei esse script em Python que automatiza todo o cálculo e ainda sugere a melhor decisão.

---

## ⚙️ Funcionalidades

- ✅ Cálculo automático do valor de cada 1.000 milhas em reais (R$)
- ✅ Validação de entradas (impede valores negativos, zerados ou inválidos)
- ✅ Tratamento de erros com `try/except`
- ✅ Recomendação automática sobre usar milhas ou dinheiro
- ✅ Limpeza de tela compatível com Windows, Linux e macOS

---

## 🚀 Como executar

1. Certifique-se de ter o **Python 3** instalado.
2. Clone este repositório:
   ```bash
   git clone https://github.com/Diigz/calculadora-de-milhas.git
   cd calculadora-de-milhas
   ```
3. Execute o script:
   ```bash
   python calculadora_milhas.py
   ```

---

## 🖥️ Exemplo de uso

```
=== CALCULADORA DE MILHAS ===

Me diga o valor da passagem: 1200
Muito bem, agora me diga o valor em milhas: 50000
Por fim, me diga a taxa de embarque com as milhas: 80

Realizando o cálculo, o valor de cada milha está R$22.40
Por esse valor de R$22.40 está aceitável.
```

---

## 📌 Critérios de recomendação

| Valor de cada 1.000 milhas (R$) | Recomendação                                  |
|----------------------------------|-----------------------------------------------|
| até 20,00                        | 🟢 Vale muito a pena usar as milhas            |
| de 20,01 a 24,99                 | 🟡 Está aceitável                              |
| de 25,00 a 29,99                 | 🟠 Está bom, mas considere usar dinheiro       |
| 30,00 ou mais                     | 🔴 Opte por usar dinheiro                      |

---

## 🧠 Conceitos aplicados

- Estruturas de repetição (`while`)
- Controle de fluxo (`continue`, `break`)
- Tratamento de exceções (`try/except ValueError`)
- Formatação de strings (`f-strings`)
- Funções (`def`)
- Compatibilidade entre sistemas operacionais (`os.system`)

---

## 🛠️ Tecnologias

- Python 3

---

## 🤝 Contribuições

Sugestões e melhorias são bem-vindas! Sinta-se livre para abrir uma *issue* ou enviar um *pull request*.

---

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar, estudar e modificar.
