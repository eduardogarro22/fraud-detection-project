--CREATE DATABASE BankFraudDB;
--GO

USE BankFraudDB;
GO

--CREATE TABLE Fraud_Transactions_Raw (
--    transaccion_id INT IDENTITY(1,1) PRIMARY KEY,
--    time_seconds INT NOT NULL,
    
--    v1 FLOAT,
--    v2 FLOAT,
--    v3 FLOAT,
--    v4 FLOAT,
--    v5 FLOAT,
--    v6 FLOAT,
--    v7 FLOAT,
--    v8 FLOAT,
--    v9 FLOAT,
--    v10 FLOAT,
--    v11 FLOAT,
--    v12 FLOAT,
--    v13 FLOAT,
--    v14 FLOAT,
--    v15 FLOAT,
--    v16 FLOAT,
--    v17 FLOAT,
--    v18 FLOAT,
--    v19 FLOAT,
--    v20 FLOAT,
--    v21 FLOAT,
--    v22 FLOAT,
--    v23 FLOAT,
--    v24 FLOAT,
--    v25 FLOAT,
--    v26 FLOAT,
--    v27 FLOAT,
--    v28 FLOAT,

--    amount DECIMAL(12,2) NOT NULL,
--    is_fraud BIT NOT NULL
--);

--CREATE INDEX idx_fraud_flag
--ON Fraud_Transactions_Raw (is_fraud);

--CREATE INDEX idx_amount
--ON Fraud_Transactions_Raw (amount);

--CREATE TABLE clientes (
--    cliente_id INT IDENTITY(1,1) PRIMARY KEY,
--    nombre VARCHAR(50) NOT NULL,
--    apellido VARCHAR(50) NOT NULL,
--    dni VARCHAR(20) UNIQUE NOT NULL,
--    fecha_alta DATE NOT NULL DEFAULT GETDATE(),
--    riesgo_base VARCHAR(10) CHECK (riesgo_base IN ('bajo', 'medio', 'alto'))
--);

--CREATE TABLE cuentas (
--    cuenta_id INT IDENTITY(1,1) PRIMARY KEY,
--    cliente_id INT NOT NULL,
--    tipo_cuenta VARCHAR(30) NOT NULL,
--    saldo DECIMAL(18,2) NOT NULL DEFAULT 0,
--    fecha_apertura DATE NOT NULL DEFAULT GETDATE(),
--    estado VARCHAR(15) CHECK (estado IN ('activa', 'bloqueada', 'cerrada')),

--    CONSTRAINT fk_cuentas_clientes
--        FOREIGN KEY (cliente_id)
--        REFERENCES clientes(cliente_id)
--);

--CREATE TABLE transacciones (
--    transaccion_id BIGINT IDENTITY(1,1) PRIMARY KEY,
--    cuenta_id INT NOT NULL,
--    fecha DATETIME NOT NULL,
--    monto DECIMAL(18,2) NOT NULL,
--    tipo_transaccion VARCHAR(30) NOT NULL,
--    canal VARCHAR(20),
--    es_fraude BIT DEFAULT 0,

--    CONSTRAINT fk_transacciones_cuentas
--        FOREIGN KEY (cuenta_id)

--        REFERENCES cuentas(cuenta_id)
--);

--CREATE TABLE Fraud_Detected (
--    transaccion_id INT PRIMARY KEY,
--    time_seconds FLOAT,
--    amount DECIMAL(18,2),
--    is_fraud BIT,
--    riesgo VARCHAR(10),
--    fecha_procesado DATETIME DEFAULT GETDATE()
--);

--CREATE TABLE Fraud_Scored (
--    transaccion_id INT PRIMARY KEY,
--    fraud_probability FLOAT,
--    fraud_prediction BIT,
--    fecha_score DATETIME DEFAULT GETDATE()
--);

--CREATE VIEW vw_transacciones_sospechosas AS
--SELECT *
--FROM Fraud_Transactions_Raw
--WHERE amount > 1500 OR is_fraud = 1;

--CREATE VIEW vw_transacciones_con_riesgo AS
--SELECT
--    transaccion_id,
--    time_seconds,
--    amount,
--    is_fraud,
--    CASE
--        WHEN is_fraud = 1 OR amount >= 2500 THEN 'HIGH'
--        WHEN amount BETWEEN 1000 AND 2499 THEN 'MEDIUM'
--        ELSE 'LOW'
--    END AS riesgo
--FROM Fraud_Transactions_Raw;


--INSERT INTO clientes (nombre, apellido, dni, riesgo_base)
--VALUES
--('Juan', 'Pérez', '30123456', 'bajo'),
--('María', 'Gómez', '28987654', 'medio'),
--('Carlos', 'López', '31222333', 'alto');

--INSERT INTO cuentas (cliente_id, tipo_cuenta, saldo, estado)
--VALUES
--(1, 'Caja de Ahorro', 150000, 'activa'),
--(2, 'Caja de Ahorro', 90000, 'activa'),
--(3, 'Cuenta Corriente', 500000, 'activa');

--INSERT INTO Fraud_Detected (
--    transaccion_id,
--    time_seconds,
--    amount,
--    is_fraud,
--    riesgo
--)
--SELECT
--    transaccion_id,
--    time_seconds,
--    amount,
--    is_fraud,
--    riesgo
--FROM vw_transacciones_con_riesgo;

--INSERT INTO Fraud_Transactions_Raw (
--    time_seconds,
--    v1, v2, v3, v4, v5, v6, v7, v8, v9, v10,
--    v11, v12, v13, v14, v15, v16, v17, v18, v19, v20,
--    v21, v22, v23, v24, v25, v26, v27, v28,
--    amount,
--    is_fraud
--)
--SELECT
--    [Time],
--    V1, V2, V3, V4, V5, V6, V7, V8, V9, V10,
--    V11, V12, V13, V14, V15, V16, V17, V18, V19, V20,
--    V21, V22, V23, V24, V25, V26, V27, V28,
--    Amount,
--    Class
--FROM dbo.transactions;

--indices para python--
--CREATE INDEX idx_fraud_riesgo ON Fraud_Detected(riesgo);
--CREATE INDEX idx_fraud_amount ON Fraud_Detected(amount);
--CREATE INDEX idx_fraud_isfraud ON Fraud_Detected(is_fraud);

