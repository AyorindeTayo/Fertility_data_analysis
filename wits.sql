CREATE TABLE individuals (
    IndividualId INT PRIMARY KEY,
    DoB DATE,
    Gender CHAR(1),
    ObsStartDate DATE,
    ObsEndDate DATE
);

CREATE TABLE pregnancies_and_births (
    MotherId INT,
    OutcomeDate DATE,
    Outcome CHAR(1),
    ChildId INT,
    Birthweight NUMERIC(4, 1),
    FOREIGN KEY (MotherId) REFERENCES individuals (IndividualId),
    FOREIGN KEY (ChildId) REFERENCES individuals (IndividualId)
);

CREATE TABLE codebook (
    Table_Name VARCHAR(50),
    Column_Name VARCHAR(50),
    Description TEXT,
    Domain_values TEXT
);
