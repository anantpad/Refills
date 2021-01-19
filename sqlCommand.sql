select distinct r.RcopiaIdentifier,p.PTID,m.MID,u.FIRSTNAME,u.LASTNAME,u.NPI,l.ADDRESS1,l.CITY,l.STATE,l.ZIP,l.PRIMPHONE,l.FAXPHONE,
        pp.First,pp.last,pp.Sex,pp.Birthdate,pp.Address1,pp.City,pp.State,pp.Zip,pp.Phone1,
        m.DESCRIPTION,CONCAT(m.NDCLABPROD,m.NDCPACKAGE) as NDCID,
        p.QUANTITY,m.INSTRUCTIONS from RcopiaMapPrescription r
        JOIN PRESCRIB p on p.PTID = r.CentricityIdentifier
        JOIN MEDICATE m on m.MID = p.MID
        JOIN DDID_RXNORM rx on rx.DDID = m.DDID
        JOIN NDCTODDID ndc on ndc.DDID = m.DDID
        JOIN PatientProfile pp on pp.PId = p.PID
        JOIN USR u on u.PVID = p.PUBUSER
        JOIN DOCUMENT d on d.SDID = p.SDID
        JOIN LOCREG l on l.LOCID = d.LOCOFCARE
        WHERE r.IsDeleted != 'Y';