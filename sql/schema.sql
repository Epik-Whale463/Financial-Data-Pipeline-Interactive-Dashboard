CREATE TABLE IF NOT EXISTS financial_reports (
    Date DATE PRIMARY KEY,
    Revenue DECIMAL(15,2) NOT NULL,
    Expenses DECIMAL(15,2) NOT NULL,
    Profit DECIMAL(15,2) GENERATED ALWAYS AS (Revenue - Expenses) STORED,
    ROI DECIMAL(5,2),
    EBITDA DECIMAL(15,2),
    Region VARCHAR(50)
);

CREATE INDEX idx_date ON financial_reports (Date);
CREATE INDEX idx_region ON financial_reports (Region);