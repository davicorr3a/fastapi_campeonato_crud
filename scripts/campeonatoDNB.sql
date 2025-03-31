CREATE DATABASE CampeonatoDB;
\c CampeonatoDB;
-- Criar schema
CREATE SCHEMA campeonato;
-- Tabela Arbitro
CREATE TABLE campeonato.Arbitro (
id SERIAL PRIMARY KEY,


nome VARCHAR(100) NOT NULL UNIQUE,
especializacao VARCHAR(50) NOT NULL
);
-- Tabela Partidas
CREATE TABLE campeonato.Partidas (
id SERIAL PRIMARY KEY,
codigo VARCHAR(20) NOT NULL,
data DATE NOT NULL,
horario TIME NOT NULL,
estadio_id INT,
time_casa_id INT,
time_visitante_id INT,
FOREIGN KEY (estadio_id) REFERENCES campeonato.Estadio(id),
FOREIGN KEY (time_casa_id) REFERENCES campeonato.Time(id),
FOREIGN KEY (time_visitante_id) REFERENCES campeonato.Time(id)
);
-- Tabela Arbitro_Partida
CREATE TABLE campeonato.Arbitro_Partida (
arbitro_id INT,
partida_id INT,
funcao VARCHAR(50) NOT NULL,
PRIMARY KEY (arbitro_id, partida_id),
FOREIGN KEY (arbitro_id) REFERENCES campeonato.Arbitro(id),
FOREIGN KEY (partida_id) REFERENCES campeonato.Partidas(id)
);
-- Tabela Estadio
CREATE TABLE campeonato.Estadio (
id SERIAL PRIMARY KEY,
nome VARCHAR(100) NOT NULL,
localizacao VARCHAR(100) NOT NULL,
capacidade INT NOT NULL,
tipo_de_gramado VARCHAR(50) NOT NULL,
patrocinadores TEXT
);
-- Tabela Time
CREATE TABLE campeonato.Time (
id SERIAL PRIMARY KEY,
nome VARCHAR(100) NOT NULL,
nome_time VARCHAR(100) NOT NULL,


temporada VARCHAR(20) NOT NULL,
categoria VARCHAR(50) NOT NULL,
total_jogadores INT NOT NULL,
liga_id INT,
FOREIGN KEY (liga_id) REFERENCES campeonato.Liga(id)
);
-- Tabela Plantel
CREATE TABLE campeonato.Plantel (
id SERIAL PRIMARY KEY,
total_jogadores INT NOT NULL,
temporada VARCHAR(20) NOT NULL,
categoria VARCHAR(50) NOT NULL,
time_id INT,
FOREIGN KEY (time_id) REFERENCES campeonato.Time(id)
);
-- Tabela Jogador
CREATE TABLE campeonato.Jogador (
id SERIAL PRIMARY KEY,
nome VARCHAR(100) NOT NULL,
tipo VARCHAR(50) NOT NULL,
idade INT NOT NULL,
data_entrada DATE NOT NULL,
data_saida DATE,
plantel_id INT,
FOREIGN KEY (plantel_id) REFERENCES campeonato.Plantel(id)
);
-- Tabela Estatisticas_Jogador
CREATE TABLE campeonato.Estatisticas_Jogador (
estatistica_id SERIAL PRIMARY KEY,
jogador_id INT,
gols INT NOT NULL,
assistencias INT NOT NULL,
cartao_amarelo INT NOT NULL,
cartao_vermelho INT NOT NULL,
FOREIGN KEY (jogador_id) REFERENCES campeonato.Jogador(id)
);
-- Tabela Treinador
CREATE TABLE campeonato.Treinador (
id SERIAL PRIMARY KEY,


nome VARCHAR(100) NOT NULL,
categoria VARCHAR(50) NOT NULL,
time_id INT,
FOREIGN KEY (time_id) REFERENCES campeonato.Time(id)
);
-- Tabela Contrato
CREATE TABLE campeonato.Contrato (
id SERIAL PRIMARY KEY,
jogador_id INT,
data_inicio DATE NOT NULL,
data_fim DATE NOT NULL,
salario DECIMAL(10,2) NOT NULL,
FOREIGN KEY (jogador_id) REFERENCES campeonato.Jogador(id)
);
-- Tabela Contrato_Treinador
CREATE TABLE campeonato.Contrato_Treinador (
id SERIAL PRIMARY KEY,
treinador_id INT,
data_inicio DATE NOT NULL,
data_fim DATE NOT NULL,
salario DECIMAL(10,2) NOT NULL,
bonus_desempenho DECIMAL(10,2),
FOREIGN KEY (treinador_id) REFERENCES campeonato.Treinador(id)
);
-- Tabela Funcionario
CREATE TABLE campeonato.Funcionario (
id SERIAL PRIMARY KEY,
nome VARCHAR(100) NOT NULL,
idade INT NOT NULL,
salario DECIMAL(10,2) NOT NULL,
tipo VARCHAR(50) NOT NULL,
time_id INT,
FOREIGN KEY (time_id) REFERENCES campeonato.Time(id)
);
-- Tabela Porteiro
CREATE TABLE campeonato.Porteiro (
funcionario_id INT PRIMARY KEY,
turno VARCHAR(20) NOT NULL,
portaria VARCHAR(50) NOT NULL,
area VARCHAR(50) NOT NULL,
FOREIGN KEY (funcionario_id) REFERENCES campeonato.Funcionario(id)
);
-- Tabela Especialista_Saude
CREATE TABLE campeonato.Especialista_Saude (
funcionario_id INT PRIMARY KEY,
certificados TEXT,
horario_atendimento VARCHAR(100),
FOREIGN KEY (funcionario_id) REFERENCES campeonato.Funcionario(id)
);
-- Tabela Liga
CREATE TABLE campeonato.Liga (
id SERIAL PRIMARY KEY,
nome VARCHAR(100) NOT NULL,
divisao VARCHAR(50) NOT NULL
);


-- Tabela Federacao
CREATE TABLE campeonato.Federacao (
id SERIAL PRIMARY KEY NOT NULL,
nome VARCHAR(100) NOT NULL,
localizacao VARCHAR(100) NOT NULL,
especializacao VARCHAR(100) NOT NULL,
liga_id INT NOT NULL,
FOREIGN KEY (liga_id) REFERENCES campeonato.Liga (id)
);
-- Tabela Patrocinador
CREATE TABLE campeonato.Patrocinador (
id SERIAL PRIMARY KEY,
nome VARCHAR(100) NOT NULL,
categoria VARCHAR(50) NOT NULL,
valor DECIMAL(10,2) NOT NULL
);


-- Tabela Liga_Patrocinador
CREATE TABLE campeonato.Liga_Patrocinador (
liga_id INT,
patrocinador_id INT,
PRIMARY KEY (liga_id, patrocinador_id),
FOREIGN KEY (liga_id) REFERENCES campeonato.Liga(id),
FOREIGN KEY (patrocinador_id) REFERENCES
campeonato.Patrocinador(id)
);
-- Tabela Time_Estadio
CREATE TABLE campeonato.Time_Estadio (
time_id INT,
estadio_id INT,
PRIMARY KEY (time_id, estadio_id),
FOREIGN KEY (time_id) REFERENCES campeonato.Time(id),
FOREIGN KEY (estadio_id) REFERENCES campeonato.Estadio(id)
);
-- Tabela Time_Patrocinador
CREATE TABLE campeonato.Time_Patrocinador (
time_id INT,
patrocinador_id INT,
PRIMARY KEY (time_id, patrocinador_id),
FOREIGN KEY (time_id) REFERENCES campeonato.Time(id),
FOREIGN KEY (patrocinador_id) REFERENCES
campeonato.Patrocinador(id)
);
