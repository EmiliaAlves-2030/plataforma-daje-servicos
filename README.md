# DAJE Serviços - Apoio em Campo

Projeto prático da disciplina de Projeto de Software focado no ODS 8 (Trabalho Decente e Crescimento Econômico).

## Sobre o Projeto

Aplicação web responsiva desenvolvida para ajudar os ajudantes da DAJE Serviços a realizarem vistorias técnicas e cálculo de materiais para instalação de piso vinílico direto na obra. O sistema conta com:

- Checklist de avaliação do contrapiso (desnível e umidade)
- Calculadora de caixas de piso vinílico e argamassa de regularização
- Módulos rápidos de orientação técnica

## Acessibilidade

A interface foi pensada para uso em celular durante a obra:

- Cores de alto contraste para facilitar a leitura sob o sol
- Botões grandes para toque na tela
- Avisos com texto, cor e ícone juntos
- Campo de medida já abre o teclado numérico com vírgula e ponto

## Tecnologias Utilizadas

- **Front-end:** HTML5, CSS3 (Tailwind CSS) e JavaScript Vanilla
- **Back-end:** Python 3.12 com FastAPI e Pydantic
- **Testes:** Pytest
- **CI/CD:** GitHub Actions

## Como Rodar Localmente

1. Clone o repositório e acesse a pasta:
```bash
git clone <URL-DO-SEU-REPOSITORIO>
cd daje-servicos-mvp
