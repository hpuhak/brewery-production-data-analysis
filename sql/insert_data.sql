-- Tuotanto (2 linjaa, 3 tuotetta: Lager, Ale, Porter)
INSERT INTO production (date, line_id, product_name, units_produced, shift) VALUES
('2025-07-01', 1, 'Lager', 5200, 'A'),
('2025-07-01', 1, 'Lager', 5100, 'B'),
('2025-07-01', 2, 'Ale', 4800, 'A'),
('2025-07-01', 2, 'Ale', 4700, 'B'),

('2025-07-02', 1, 'Porter', 5300, 'A'),
('2025-07-02', 1, 'Porter', 5150, 'B'),
('2025-07-02', 2, 'Lager', 4900, 'A'),
('2025-07-02', 2, 'Lager', 4750, 'B'),

('2025-07-03', 1, 'Ale', 5000, 'A'),
('2025-07-03', 1, 'Ale', 4950, 'B'),
('2025-07-03', 2, 'Porter', 4600, 'A'),
('2025-07-03', 2, 'Porter', 4500, 'B'),

('2025-07-04', 1, 'Lager', 5400, 'A'),
('2025-07-04', 1, 'Lager', 5300, 'B'),
('2025-07-04', 2, 'Ale', 5000, 'A'),
('2025-07-04', 2, 'Ale', 4900, 'B'),

('2025-07-05', 1, 'Porter', 5500, 'A'),
('2025-07-05', 1, 'Porter', 5450, 'B'),
('2025-07-05', 2, 'Lager', 5100, 'A'),
('2025-07-05', 2, 'Lager', 5000, 'B');

-- Laatupoikkeamat
INSERT INTO quality_checks (date, line_id, defect_type, defect_count) VALUES
('2025-07-01', 1, 'Vaahtoisuus liikaa', 5),
('2025-07-01', 1, 'Etikettivirhe', 3),
('2025-07-01', 2, 'Sameus', 4),

('2025-07-02', 1, 'Sameus', 6),
('2025-07-02', 2, 'Etikettivirhe', 2),

('2025-07-03', 1, 'Etikettivirhe', 5),
('2025-07-03', 2, 'Vaahtoisuus liikaa', 3),
('2025-07-03', 2, 'Korkkivika', 2),

('2025-07-04', 1, 'Sameus', 7),
('2025-07-04', 2, 'Etikettivirhe', 4),

('2025-07-05', 1, 'Etikettivirhe', 6),
('2025-07-05', 2, 'Vaahtoisuus liikaa', 5);

-- Seisokit
INSERT INTO downtime (date, line_id, reason, minutes_lost) VALUES
('2025-07-01', 1, 'Huolto', 30),
('2025-07-01', 2, 'Raaka-ainepula', 45),

('2025-07-02', 1, 'Konerikko', 60),
('2025-07-02', 2, 'Huolto', 20),

('2025-07-03', 1, 'Sähkökatko', 15),
('2025-07-03', 2, 'Raaka-ainepula', 40),

('2025-07-04', 1, 'Huolto', 35),
('2025-07-04', 2, 'Käyttövirhe', 10),

('2025-07-05', 1, 'Konerikko', 50),
('2025-07-05', 2, 'Raaka-ainepula', 30);
