select distinct concat(pp.First,' ',pp.last) as pname,pp.patientId, pp.Sex,pp.Birthdate,pp.Address1,pp.City,pp.State,pp.Zip,pp.Phone1,pp.First,pp.last
        from RcopiaMapPrescription r
        JOIN PRESCRIB p on p.PTID = r.CentricityIdentifier
        JOIN PatientProfile pp on pp.PId = p.PID
        WHERE r.IsDeleted != 'Y';