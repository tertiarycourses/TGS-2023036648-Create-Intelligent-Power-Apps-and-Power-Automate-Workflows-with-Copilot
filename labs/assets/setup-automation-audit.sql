/*
  C903 synthetic training table.
  Run only in the trainer-approved C903 SQL Server or Azure SQL database.
  The script is idempotent: it creates the table only when it does not exist.
*/

SET NOCOUNT ON;
SET XACT_ABORT ON;

IF OBJECT_ID(N'dbo.C903AutomationAudit', N'U') IS NULL
BEGIN
    CREATE TABLE dbo.C903AutomationAudit
    (
        AuditID         bigint IDENTITY(1,1) NOT NULL
            CONSTRAINT PK_C903AutomationAudit PRIMARY KEY,
        RequestID       nvarchar(30) NOT NULL,
        DataverseRowID  nvarchar(80) NOT NULL,
        EventType       nvarchar(40) NOT NULL,
        EventTimeUTC    datetime2(0) NOT NULL,
        FlowRunNote     nvarchar(200) NULL,
        CreatedUTC      datetime2(0) NOT NULL
            CONSTRAINT DF_C903AutomationAudit_CreatedUTC DEFAULT SYSUTCDATETIME()
    );

END;

IF NOT EXISTS
(
    SELECT 1
    FROM sys.indexes
    WHERE object_id = OBJECT_ID(N'dbo.C903AutomationAudit')
      AND name = N'UX_C903AutomationAudit_Request_Event'
      AND is_unique = 1
)
BEGIN
    CREATE UNIQUE INDEX UX_C903AutomationAudit_Request_Event
        ON dbo.C903AutomationAudit(RequestID, EventType);
END;

IF NOT EXISTS
(
    SELECT 1
    FROM sys.indexes
    WHERE object_id = OBJECT_ID(N'dbo.C903AutomationAudit')
      AND name = N'UX_C903AutomationAudit_Request_Event'
      AND is_unique = 1
)
    THROW 51003, 'C903 unique RequestID/EventType index is missing.', 1;

SELECT
    AuditID,
    RequestID,
    DataverseRowID,
    EventType,
    EventTimeUTC,
    FlowRunNote,
    CreatedUTC
FROM dbo.C903AutomationAudit
WHERE RequestID LIKE N'NW-%'
ORDER BY AuditID;

SELECT
    i.name AS IndexName,
    i.is_unique AS IsUnique
FROM sys.indexes AS i
WHERE i.object_id = OBJECT_ID(N'dbo.C903AutomationAudit')
  AND i.name = N'UX_C903AutomationAudit_Request_Event';
